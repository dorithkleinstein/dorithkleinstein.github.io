"""Draw the faint data lines behind the share cards.

Average birth weight by state, 2016 to 2024, from the birth outcomes dbt project's seed file.
The average for each state and year is weighted by births. States far from the middle are drawn
darker, the rest fainter, so the lines stay quiet behind the text.

Run with: python3 make-lines.py
Writes lines.svg next to this file.
"""
import csv, os
from collections import defaultdict

SEED = os.path.expanduser('~/dbt_projects/birth_outcomes/seeds/births_by_state_race_year.csv')
W, H = 1200, 630
PAD_Y = -40          # let the outermost lines run off the top and bottom, as on the GitHub card

total = defaultdict(float); births = defaultdict(float)
with open(SEED) as f:
    for r in csv.DictReader(f):
        try:
            n = float(r['births']); w = float(r['avg_birth_weight_grams'])
        except ValueError:
            continue    # suppressed cells
        key = (r['state'], int(r['year']))
        total[key] += n * w; births[key] += n

states = sorted({s for s, _ in total})
years = sorted({y for _, y in total})
avg = {k: total[k] / births[k] for k in total}
lo, hi = min(avg.values()), max(avg.values())
mid = sorted(avg.values())[len(avg) // 2]

def y_of(v):
    return PAD_Y + (hi - v) / (hi - lo) * (H - 2 * PAD_Y)

lines = []
for s in states:
    pts = [(i * W / (len(years) - 1), y_of(avg[(s, yr)])) for i, yr in enumerate(years) if (s, yr) in avg]
    if len(pts) < 2:
        continue
    spread = abs(sum(avg[(s, yr)] for yr in years if (s, yr) in avg) / len(pts) - mid) / (hi - lo)
    opacity = 0.10 + min((spread * 2) ** 1.6, 0.55)
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    lines.append(f'  <polyline points="{d}" stroke-opacity="{opacity:.2f}"/>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
       f'<g fill="none" stroke="#64858d" stroke-width="2" stroke-linejoin="round">\n'
       + '\n'.join(lines) + '\n</g>\n</svg>\n')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lines.svg'), 'w').write(svg)
print(f'{len(lines)} states, {years[0]} to {years[-1]}, {lo:.0f} to {hi:.0f} grams')
