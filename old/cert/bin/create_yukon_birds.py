"""Create Yukon birds observations as CSV and SQLite DB.

Raw: https://clo-pfw-prod.s3.us-west-2.amazonaws.com/data/202306/PFW_all_2021_2023_June2023_Public.zip
Source: Project FeederWatch <https://feederwatch.org/>
Obtained: 2024-02-21
"""

import pandas as pd
import sqlite3
import sys

COLUMNS = {
    "LOC_ID": "loc_id",
    "LATITUDE": "latitude",
    "LONGITUDE": "longitude",
    "SUBNATIONAL1_CODE": "region",
    "Year": "year",
    "Month": "month",
    "Day": "day",
    "SPECIES_CODE": "species_id",
    "HOW_MANY": "num",
}

infile, csvfile, dbfile = sys.argv[1], sys.argv[2], sys.argv[3]

df = pd.read_csv(infile)
df = df[list(COLUMNS.keys())].rename(columns=COLUMNS)
df = df[df["region"]=="CA-YT"]

df.to_csv(csvfile, index=False)

connection = sqlite3.connect(dbfile)
df.to_sql("birds", connection, if_exists="replace", index=False)
