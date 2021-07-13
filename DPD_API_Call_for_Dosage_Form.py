import requests
import json
import pandas as pd
import csv
import os

link = 'form?lang=en&type=json'
csv_file = 'form.csv'

response_API = requests.get(f'https://health-products.canada.ca/api/drug/{link}')
print(f'The API has responded: {response_API.status_code}')
data = response_API.text
data_list = json.loads(data)

for i in range(len(data_list)):
    write_dict = data_list[i]
    
    #write the dictionary entry to the CSV
    df = pd.DataFrame.from_dict(write_dict, orient='index')
    final_df = df.transpose()
    if i != 0:
        final_df.to_csv(csv_file, mode = 'a', index = False, header = not os.path.exists(csv_file))
    else:
        final_df.to_csv(csv_file, mode = 'a', index = False)