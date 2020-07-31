from airtable import Airtable
import json
from slugify import slugify
import os
import sys
import requests

base_key = 'appWWBnE4dVwQIn3n'
if 'AIRTABLE_API_KEY' not in os.environ:
    print('Missing AIRTABLE_API_KEY')
    sys.exit(-1)
AIRTABLE_API_KEY = os.environ['AIRTABLE_API_KEY'] 
TABLES = ['People', 'Projects', 'Partners']
ATTACHMENTS = { 'People': 'Picture', 'Projects': 'Picture', 'Partners': 'Logo'}

for table_name in TABLES:
    print('Processing table `%s`' % table_name)
    airtable = Airtable(base_key, table_name, api_key=AIRTABLE_API_KEY)

    all_rows = airtable.get_all()
    JSON_DATA = []
    for row in all_rows:
        if len(row['fields']) == 0:
            print('Skipping empty record.')
            continue
        record = {'__id__': row['id']}
        for key, value in row['fields'].items():
            name = slugify(key, separator='_')
            record[name] = value
            if table_name in ATTACHMENTS and key in ATTACHMENTS[table_name]:
                attachment_folder = 'assets/img/%s' % table_name
                print(attachment_folder)
                if not os.path.exists(attachment_folder):
                    os.makedirs(attachment_folder)
                attachment = value[0]
                filename = attachment['filename']
                url = attachment['url']
                print('Need to download file %s from %s' % (filename, url))
                r = requests.get(url)  
                with open('%s/%s' % (attachment_folder, filename), 'wb') as f:
                    f.write(r.content)
        JSON_DATA.append(record)

    with open("_data/%s.json" % table_name, 'w') as outfile:
        json.dump(JSON_DATA, outfile, indent=2, sort_keys=True)