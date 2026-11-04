// vision.swift: Apple Vision measurements for the composition skill.
// Usage: vision <image> [--mask-dir DIR] [--saliency-only]   -> one JSON object on stdout.
// Coordinates: x,y in 0-1 from the TOP-LEFT of the (EXIF-oriented) image.
// Build: swiftc -O -swift-version 5 vision.swift -o vision   (look.py does this for you)
import Foundation
import Vision
import CoreImage
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers

func r4(_ v: Double) -> Double { (v * 10000).rounded() / 10000 }
func r4(_ v: CGFloat) -> Double { r4(Double(v)) }

var errors: [String] = []
func note(_ s: String) { errors.append(s) }

// ---- args
let args = CommandLine.arguments
guard args.count >= 2 else {
    FileHandle.standardError.write("usage: vision <image> [--mask-dir DIR]\n".data(using: .utf8)!)
    exit(2)
}
let path = args[1]
var maskDir: String? = nil
if let i = args.firstIndex(of: "--mask-dir"), i + 1 < args.count { maskDir = args[i + 1] }

// ---- load
guard let src = CGImageSourceCreateWithURL(URL(fileURLWithPath: path) as CFURL, nil),
      let cg = CGImageSourceCreateImageAtIndex(src, 0, nil) else {
    print("{\"ok\":false,\"error\":\"cannot read image\"}")
    exit(1)
}
var orientation = CGImagePropertyOrientation.up
if let props = CGImageSourceCopyPropertiesAtIndex(src, 0, nil) as? [CFString: Any],
   let o = props[kCGImagePropertyOrientation] as? UInt32,
   let oo = CGImagePropertyOrientation(rawValue: o) { orientation = oo }
let swapWH = [.left, .right, .leftMirrored, .rightMirrored].contains(orientation)
let imgW = swapWH ? cg.height : cg.width
let imgH = swapWH ? cg.width : cg.height

var out: [String: Any] = [
    "ok": true,
    "image": ["width": imgW, "height": imgH, "orientation": Int(orientation.rawValue)],
]

func handler() -> VNImageRequestHandler { VNImageRequestHandler(cgImage: cg, orientation: orientation, options: [:]) }

// ---- helpers
struct Grid { var w: Int; var h: Int; var v: [Float] }

func readFloatBuffer(_ pb: CVPixelBuffer) -> Grid? {
    CVPixelBufferLockBaseAddress(pb, .readOnly)
    defer { CVPixelBufferUnlockBaseAddress(pb, .readOnly) }
    let w = CVPixelBufferGetWidth(pb), h = CVPixelBufferGetHeight(pb)
    guard let base = CVPixelBufferGetBaseAddress(pb) else { return nil }
    let bpr = CVPixelBufferGetBytesPerRow(pb)
    var v = [Float](repeating: 0, count: w * h)
    for y in 0..<h {
        let row = base.advanced(by: y * bpr).assumingMemoryBound(to: Float.self)
        for x in 0..<w { v[y * w + x] = row[x] }
    }
    return Grid(w: w, h: h, v: v)
}

/// Local maxima with minimum separation; strength normalised by the map max.
func peaks(_ g: Grid, count: Int, minDist: Double = 0.12) -> [[String: Double]] {
    let mx = g.v.max() ?? 0
    guard mx > 0 else { return [] }
    // 3x3 box smooth
    var sm = g.v
    for y in 0..<g.h { for x in 0..<g.w {
        var s: Float = 0, n: Float = 0
        for dy in -1...1 { for dx in -1...1 {
            let xx = x + dx, yy = y + dy
            if xx >= 0, yy >= 0, xx < g.w, yy < g.h { s += g.v[yy * g.w + xx]; n += 1 }
        } }
        sm[y * g.w + x] = s / n
    } }
    var cands: [(Int, Int, Float)] = []
    for y in 0..<g.h { for x in 0..<g.w {
        let c = sm[y * g.w + x]
        var isMax = true
        for dy in -1...1 { for dx in -1...1 where !(dx == 0 && dy == 0) {
            let xx = x + dx, yy = y + dy
            if xx >= 0, yy >= 0, xx < g.w, yy < g.h, sm[yy * g.w + xx] > c { isMax = false }
        } }
        if isMax && c > 0 { cands.append((x, y, c)) }
    } }
    cands.sort { $0.2 > $1.2 }
    var chosen: [(Int, Int, Float)] = []
    for c in cands {
        let cx = (Double(c.0) + 0.5) / Double(g.w), cy = (Double(c.1) + 0.5) / Double(g.h)
        if chosen.allSatisfy({ o in
            let ox = (Double(o.0) + 0.5) / Double(g.w), oy = (Double(o.1) + 0.5) / Double(g.h)
            return hypot(cx - ox, cy - oy) >= minDist }) { chosen.append(c) }
        if chosen.count >= count { break }
    }
    return chosen.map { ["x": r4((Double($0.0) + 0.5) / Double(g.w)), "y": r4((Double($0.1) + 0.5) / Double(g.h)),
                         "strength": r4(Double($0.2 / mx)), "raw": r4(Double($0.2))] }
}

func gridJSON(_ g: Grid) -> [String: Any] {
    ["width": g.w, "height": g.h, "max": r4(Double(g.v.max() ?? 0)), "sum": r4(Double(g.v.reduce(0, +))),
     "values": g.v.map { r4(Double($0)) }]
}

func emit() -> Never {
    out["notes"] = errors
    let data = try! JSONSerialization.data(withJSONObject: out, options: [.sortedKeys])
    FileHandle.standardOutput.write(data)
    FileHandle.standardOutput.write("\n".data(using: .utf8)!)
    exit(0)
}
let saliencyOnly = args.contains("--saliency-only")

// ---- attention + objectness saliency
do {
    let req = VNGenerateAttentionBasedSaliencyImageRequest()
    try handler().perform([req])
    if let obs = req.results?.first, let g = readFloatBuffer(obs.pixelBuffer) {
        var a = gridJSON(g)
        a["peaks"] = peaks(g, count: 3)
        out["attention"] = a
    } else { out["attention"] = NSNull(); note("attention: no result") }
} catch { out["attention"] = NSNull(); note("attention: \(error.localizedDescription)") }

if saliencyOnly { emit() }

do {
    let req = VNGenerateObjectnessBasedSaliencyImageRequest()
    try handler().perform([req])
    if let obs = req.results?.first, let g = readFloatBuffer(obs.pixelBuffer) {
        var a = gridJSON(g)
        a["peaks"] = peaks(g, count: 3)
        // boxes are coarse; kept for reference only
        a["boxes_unreliable"] = (obs.salientObjects ?? []).map { o -> [String: Double] in
            let b = o.boundingBox
            return ["x": r4(b.minX), "y": r4(1 - b.maxY), "w": r4(b.width), "h": r4(b.height), "confidence": r4(Double(o.confidence))]
        }
        out["objectness"] = a
    } else { out["objectness"] = NSNull(); note("objectness: nothing found") }
} catch { out["objectness"] = NSNull(); note("objectness: \(error.localizedDescription)") }

// ---- horizon
do {
    let req = VNDetectHorizonRequest()
    try handler().perform([req])
    if let h = req.results?.first {
        out["horizon"] = ["angle_deg": r4(Double(h.angle) * 180 / Double.pi), "angle_rad": r4(Double(h.angle))]
    } else { out["horizon"] = NSNull(); note("horizon: no result") }
} catch { out["horizon"] = NSNull(); note("horizon: \(error.localizedDescription)") }

// ---- foreground instance masks
func writePNG(gray: [UInt8], w: Int, h: Int, to url: URL) -> Bool {
    var data = gray
    guard let ctx = CGContext(data: &data, width: w, height: h, bitsPerComponent: 8, bytesPerRow: w,
                              space: CGColorSpaceCreateDeviceGray(), bitmapInfo: CGImageAlphaInfo.none.rawValue),
          let im = ctx.makeImage(),
          let dest = CGImageDestinationCreateWithURL(url as CFURL, UTType.png.identifier as CFString, 1, nil) else { return false }
    CGImageDestinationAddImage(dest, im, nil)
    return CGImageDestinationFinalize(dest)
}

do {
    let req = VNGenerateForegroundInstanceMaskRequest()
    let hd = handler()
    try hd.perform([req])
    if let obs = req.results?.first, !obs.allInstances.isEmpty {
        let lab = obs.instanceMask
        CVPixelBufferLockBaseAddress(lab, .readOnly)
        let w = CVPixelBufferGetWidth(lab), h = CVPixelBufferGetHeight(lab)
        let bpr = CVPixelBufferGetBytesPerRow(lab)
        var labels = [UInt8](repeating: 0, count: w * h)
        if let base = CVPixelBufferGetBaseAddress(lab) {
            for y in 0..<h {
                let row = base.advanced(by: y * bpr).assumingMemoryBound(to: UInt8.self)
                for x in 0..<w { labels[y * w + x] = row[x] }
            }
        }
        CVPixelBufferUnlockBaseAddress(lab, .readOnly)
        var insts: [[String: Any]] = []
        var union = [UInt8](repeating: 0, count: w * h)
        for id in obs.allInstances.sorted() {
            var minx = w, miny = h, maxx = -1, maxy = -1, n = 0, sx = 0.0, sy = 0.0
            var m = [UInt8](repeating: 0, count: w * h)
            for y in 0..<h { for x in 0..<w where labels[y * w + x] == UInt8(id) {
                m[y * w + x] = 255; union[y * w + x] = 255
                n += 1; sx += Double(x); sy += Double(y)
                minx = min(minx, x); maxx = max(maxx, x); miny = min(miny, y); maxy = max(maxy, y)
            } }
            if n == 0 { continue }
            var d: [String: Any] = [
                "id": id,
                "bbox": ["x": r4(Double(minx) / Double(w)), "y": r4(Double(miny) / Double(h)),
                         "w": r4(Double(maxx - minx + 1) / Double(w)), "h": r4(Double(maxy - miny + 1) / Double(h))],
                "centroid": ["x": r4((sx / Double(n) + 0.5) / Double(w)), "y": r4((sy / Double(n) + 0.5) / Double(h))],
                "area_share": r4(Double(n) / Double(w * h)),
            ]
            if let dir = maskDir {
                try? FileManager.default.createDirectory(atPath: dir, withIntermediateDirectories: true)
                let p = URL(fileURLWithPath: dir).appendingPathComponent("mask_\(id).png")
                if writePNG(gray: m, w: w, h: h, to: p) { d["mask_png"] = p.path }
            }
            insts.append(d)
        }
        var fg: [String: Any] = ["count": insts.count, "mask_size": [w, h], "instances": insts]
        if let dir = maskDir {
            let p = URL(fileURLWithPath: dir).appendingPathComponent("mask_all.png")
            if writePNG(gray: union, w: w, h: h, to: p) { fg["mask_all_png"] = p.path }
        }
        out["foreground"] = fg
    } else { out["foreground"] = NSNull(); note("foreground: no instances found") }
} catch { out["foreground"] = NSNull(); note("foreground: \(error.localizedDescription)") }

// ---- faces
func facePt(_ p: CGPoint, _ b: CGRect) -> [String: Double] {
    ["x": r4(b.minX + p.x * b.width), "y": r4(1 - (b.minY + p.y * b.height))]
}
func mean(_ pts: [CGPoint], _ b: CGRect) -> [String: Double]? {
    guard !pts.isEmpty else { return nil }
    let mx = pts.map { $0.x }.reduce(0, +) / CGFloat(pts.count)
    let my = pts.map { $0.y }.reduce(0, +) / CGFloat(pts.count)
    return facePt(CGPoint(x: mx, y: my), b)
}
do {
    let req = VNDetectFaceLandmarksRequest()
    try handler().perform([req])
    var faces: [[String: Any]] = []
    for f in req.results ?? [] {
        let b = f.boundingBox
        var d: [String: Any] = [
            "bbox": ["x": r4(b.minX), "y": r4(1 - b.maxY), "w": r4(b.width), "h": r4(b.height)],
            "confidence": r4(Double(f.confidence)),
        ]
        d["yaw_deg"] = f.yaw.map { r4(Double(truncating: $0) * 180 / Double.pi) } ?? NSNull()
        d["roll_deg"] = f.roll.map { r4(Double(truncating: $0) * 180 / Double.pi) } ?? NSNull()
        d["pitch_deg"] = f.pitch.map { r4(Double(truncating: $0) * 180 / Double.pi) } ?? NSNull()
        if let lm = f.landmarks {
            d["left_eye"] = lm.leftEye.flatMap { mean($0.normalizedPoints, b) } ?? NSNull()
            d["right_eye"] = lm.rightEye.flatMap { mean($0.normalizedPoints, b) } ?? NSNull()
            d["nose"] = lm.nose.flatMap { mean($0.normalizedPoints, b) } ?? NSNull()
        }
        faces.append(d)
    }
    out["faces"] = faces
    if faces.isEmpty { note("faces: none found") }
} catch { out["faces"] = []; note("faces: \(error.localizedDescription)") }

// ---- body pose
do {
    let req = VNDetectHumanBodyPoseRequest()
    try handler().perform([req])
    var poses: [[String: Any]] = []
    for o in req.results ?? [] {
        var joints: [String: Any] = [:]
        if let pts = try? o.recognizedPoints(.all) {
            for (k, p) in pts where p.confidence > 0 {
                joints[k.rawValue.rawValue] = ["x": r4(p.location.x), "y": r4(1 - p.location.y), "confidence": r4(Double(p.confidence))]
            }
        }
        poses.append(["confidence": r4(Double(o.confidence)), "joints": joints])
    }
    out["pose"] = poses
    if poses.isEmpty { note("pose: none found") }
} catch { out["pose"] = []; note("pose: \(error.localizedDescription)") }

// ---- text
do {
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    try handler().perform([req])
    var texts: [[String: Any]] = []
    for o in req.results ?? [] {
        guard let c = o.topCandidates(1).first else { continue }
        let b = o.boundingBox
        texts.append(["text": c.string, "confidence": r4(Double(c.confidence)),
                      "bbox": ["x": r4(b.minX), "y": r4(1 - b.maxY), "w": r4(b.width), "h": r4(b.height)]])
    }
    out["text"] = texts
    if texts.isEmpty { note("text: none found") }
} catch { out["text"] = []; note("text: \(error.localizedDescription)") }

// ---- aesthetics (macOS 15+)
out["aesthetics"] = NSNull()
if #available(macOS 15.0, *) {
    let sem = DispatchSemaphore(value: 0)
    Task {
        do {
            let req = CalculateImageAestheticsScoresRequest()
            let obs = try await req.perform(on: cg, orientation: orientation)
            out["aesthetics"] = ["overall_score": r4(Double(obs.overallScore)), "is_utility": obs.isUtility]
        } catch { note("aesthetics: \(error.localizedDescription)") }
        sem.signal()
    }
    sem.wait()
} else { note("aesthetics: needs macOS 15") }

emit()
