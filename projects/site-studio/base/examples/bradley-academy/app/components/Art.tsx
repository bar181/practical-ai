/** The Research opening: a field of points with a few paths lit through it. Drawn, not random,
 *  so it is the same on every visit: structure and light, not a photograph. */
export function Lattice() {
  const cols = 25, rows = 13, gx = 66, gy = 70, x0 = 8, y0 = 10;
  const dots: { x: number; y: number }[] = [];
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) dots.push({ x: x0 + c * gx, y: y0 + r * gy });
  const p = (c: number, r: number) => `${x0 + c * gx},${y0 + r * gy}`;
  const paths = [
    [[13, 1], [15, 2], [16, 4], [18, 5], [19, 7], [21, 8], [24, 8]],
    [[11, 3], [13, 4], [16, 4]],
    [[15, 9], [17, 8], [19, 7]],
    [[20, 2], [21, 4], [21, 8], [22, 10], [24, 11]],
  ];
  return (
    <svg className="lattice" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
      <g className="lattice-dots">
        {dots.map((d, i) => <circle key={i} cx={d.x} cy={d.y} r="2.2" />)}
      </g>
      <g className="lattice-paths">
        {paths.map((pts, i) => <polyline key={i} className={i === 0 ? "lattice-main" : undefined} points={pts.map(([c, r]) => p(c, r)).join(" ")} />)}
      </g>
      <g className="lattice-nodes">
        {[[13, 1], [16, 4], [19, 7], [24, 8], [21, 4], [24, 11]].map(([c, r]) => <circle key={`${c}-${r}`} cx={x0 + c * gx} cy={y0 + r * gy} r="7" />)}
      </g>
    </svg>
  );
}
