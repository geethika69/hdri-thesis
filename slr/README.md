# SLR starter kit
1. Run the searches in queries.md (once per database), export CSV with columns title, authors, year, doi, abstract; name each file after the database (scopus.csv ...).
2. `python dedupe.py exports/*.csv` -> screening.csv.
3. Fill ta_decision (include/exclude) and reasons; then ft_decision for included records; the second reader fills second_reader_ta / second_reader_ft for a random 20%.
4. `python counts.py <total identified>` -> numbers for Fig. 1.4 and kappa for Section 1.6.2.
5. Extract included studies into extraction.csv; the four gap_c* columns apply the Section 1.6.4 test (all four = gap rejected; three = near miss).
Record the run date in queries.md and in Section 1.6.1.
