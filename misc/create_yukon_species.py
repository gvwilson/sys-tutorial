"""Create Yukon birds observations as CSV and SQLite DB.

Raw: https://clo-pfw-prod.s3.us-west-2.amazonaws.com/data/202306/PFW_spp_translation_table_May2023.zip
Source: Project FeederWatch <https://feederwatch.org/>
Obtained: 2024-02-21
"""

import pandas as pd
import sqlite3
import sys

COLUMNS = {
    "species_code": "species_id",
    "scientific_name": "sci_name",
    "american_english_name": "en_us",
}

infile, csvfile, dbfile = sys.argv[1], sys.argv[2], sys.argv[3]

df = pd.read_csv(infile)
df = df[list(COLUMNS.keys())].rename(columns=COLUMNS)

df.to_csv(csvfile, index=False)

connection = sqlite3.connect(dbfile)
df.to_sql("species", connection, if_exists="replace", index=False)
