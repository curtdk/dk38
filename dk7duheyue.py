from web3 import Web3, HTTPProvider
import ast
from google.cloud import bigquery


# addr='0x2807a5453DdFca0EF37C74554264B9689A1c498C';
# t16_0=web3.eth.get_storage_at(addr,0,);



client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
