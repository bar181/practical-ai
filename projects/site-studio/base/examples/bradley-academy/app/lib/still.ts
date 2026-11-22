// Animated captures (.webp and .gif) loop for as long as they are on screen. For a reader who asked for
// reduced motion, swap each one for a still of its first frame: drawing an animated image on a canvas
// paints its first frame. Works for pictures in hidden tabs and lazy pictures too, as each one loads.

const ANIMATED = 'img[src$=".webp"], img[src$=".gif"]';

function freeze(img: HTMLImageElement) {
  if (img.dataset.still || !img.naturalWidth) return;
  img.dataset.still = "";
  const canvas = document.createElement("canvas");
  canvas.width = img.naturalWidth;
  canvas.height = img.naturalHeight;
  try {
    canvas.getContext("2d")?.drawImage(img, 0, 0);
    canvas.toBlob((blob) => { if (blob) img.src = URL.createObjectURL(blob); }, "image/webp", 0.92);
  } catch {
    // A picture from another site cannot be read back; it stays as it is.
  }
}

/** Freezes every animated picture under `root`; returns a cleanup that stops waiting on pictures not yet loaded. */
export function freezeAnimatedImages(root: HTMLElement): () => void {
  const waiting: (() => void)[] = [];
  for (const img of root.querySelectorAll<HTMLImageElement>(ANIMATED)) {
    if (img.complete && img.naturalWidth) { freeze(img); continue; }
    const onLoad = () => freeze(img);
    img.addEventListener("load", onLoad, { once: true });
    waiting.push(() => img.removeEventListener("load", onLoad));
  }
  return () => waiting.forEach((stop) => stop());
}
