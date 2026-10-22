"""Merge database exports into screening.csv, removing duplicates (DOI, then normalised title).
Usage: python dedupe.py exports/*.csv   (each CSV needs columns: title, authors, year, doi, abstract; file name = source)
"""
import sys, re, csv, os
import pandas as pd

def norm(t): return re.sub(r'[^a-z0-9]', '', str(t).lower())

frames = []
for f in sys.argv[1:]:
    d = pd.read_csv(f).fillna('')
    d['source'] = os.path.splitext(os.path.basename(f))[0]
    frames.append(d)
df = pd.concat(frames, ignore_index=True)
n_identified = len(df)
df['doi'] = df['doi'].astype(str).str.lower().str.replace('https://doi.org/', '', regex=False).str.strip()
df['tkey'] = df['title'].map(norm)
has = df['doi'] != ''
dup_doi = df[has].duplicated('doi', keep='first')
df = pd.concat([df[has][~dup_doi], df[~has]]).sort_index()
df = df.drop_duplicates('tkey', keep='first')
df.insert(0, 'id', range(1, len(df) + 1))
for c in ['ta_decision','ta_reason','ft_decision','ft_reason','second_reader_ta','second_reader_ft','quality_score']:
    df[c] = ''
df.drop(columns=['tkey']).to_csv('screening.csv', index=False)
print(f'identified={n_identified} after_dedupe={len(df)} removed={n_identified-len(df)}')
