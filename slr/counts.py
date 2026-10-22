"""PRISMA counts for Fig. 1.4 and Cohen's kappa from screening.csv.
Decisions: include / exclude (ta_decision, ft_decision). Second reader fills second_reader_ta / second_reader_ft for the 20% sample.
Usage: python counts.py [identified_total]
"""
import sys, pandas as pd

d = pd.read_csv('screening.csv').fillna('')
identified = int(sys.argv[1]) if len(sys.argv) > 1 else None

def kappa(a, b):
    m = (a != '') & (b != '')
    a, b = a[m], b[m]
    n = len(a)
    if n == 0: return None, 0
    po = (a == b).mean()
    pe = sum((a == c).mean() * (b == c).mean() for c in set(a) | set(b))
    return (1.0 if pe == 1 else (po - pe) / (1 - pe)), n

ta_ex = (d.ta_decision == 'exclude').sum()
ft = d[d.ta_decision == 'include']
ft_ex = (ft.ft_decision == 'exclude').sum()
inc = (ft.ft_decision == 'include').sum()
print('identified (before dedupe):', identified)
print('after duplicates removed  :', len(d))
print('excluded on title/abstract:', ta_ex)
print('full texts assessed       :', len(ft))
print('excluded at full text     :', ft_ex)
print('  reasons:', ft[ft.ft_decision == 'exclude'].ft_reason.value_counts().to_dict())
print('included in synthesis     :', inc)
for name, a, b in [('title/abstract', 'ta_decision', 'second_reader_ta'), ('full text', 'ft_decision', 'second_reader_ft')]:
    k, n = kappa(d[a].astype(str), d[b].astype(str))
    print(f'kappa {name}:', None if k is None else round(k, 3), f'(n={n})')
