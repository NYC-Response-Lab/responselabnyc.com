from airtable import Airtable
import json
from slugify import slugify
import os
import sys

base_key = 'appWWBnE4dVwQIn3n'
if 'AIRTABLE_API_KEY' not in os.environ:
    print('Missing AIRTABLE_API_KEY')
    sys.exit(-1)
AIRTABLE_API_KEY = os.environ['AIRTABLE_API_KEY'] 
TABLES = ['People', 'Projects', 'Partners']

for table_name in TABLES:
    airtable = Airtable(base_key, table_name, api_key=AIRTABLE_API_KEY)

    all_rows = airtable.get_all()
    JSON_DATA = []
    for row in all_rows:
        record = {'__id__': row['id']}
        for key, value in row['fields'].items():
            name = slugify(key, separator='_')
            record[name] = value
        JSON_DATA.append(record)

    with open("_data/%s.json" % table_name, 'w') as outfile:
        json.dump(JSON_DATA, outfile, indent=2, sort_keys=True)