import pandas as pd
from google.cloud import bigquery
import os
import pandas_gbq
from google.oauth2 import service_account

#CONSTANTS
filepath = "data/Historical Product Demand.csv"
#os.environ["GOOGLE_CREDENTIALS"]='/d/projekty_z_programowania/dataengineering_batch/terraform_gcp/terraform/keys/key.json'
credentials = service_account.Credentials.from_service_account_file(
    'D:\\projekty_z_programowania\\dataengineering_batch\\terraform_gcp\\terraform\\keys\\key.json',
)
dataset_id = "dwh_warehouse_dataset"
project_id = "dwh-terraform-gcp"
def load_data(filepath):
    raw_data = pd.read_csv(filepath)
    return raw_data



def transform_to_tables(raw_data):
    fact_product = raw_data

    dim_product = raw_data[['Product_Code', 'Product_Category']].drop_duplicates()

    dim_warehouse = pd.DataFrame(raw_data.Warehouse.unique(), columns=['Warehouse'])
    
    dim_product_category = pd.DataFrame(raw_data.Product_Category.unique(), columns=['Product_Category'])
    
    dim_date = pd.DataFrame(raw_data.Date.unique(), columns=['Order_Date'])

    return fact_product, dim_product, dim_warehouse, dim_product_category, dim_date

def upload_to_bigquery(tables, table_names):
    pandas_gbq.context.credentials = credentials
    for table, table_name in zip(tables, table_names):
        pandas_gbq.to_gbq(table, f"{dataset_id}.{table_name}", project_id=project_id, if_exists='replace')


if __name__ == "__main__":
    raw_data = load_data(filepath)
    fact_product, dim_product, dim_warehouse, dim_product_category, dim_date = transform_to_tables(raw_data)
    tables = [fact_product, dim_product, dim_warehouse, dim_product_category, dim_date]
    table_names = ["fact_product", "dim_product", "dim_warehouse", "dim_product_category", "dim_date"]
    upload_to_bigquery(tables, table_names)
    # print(fact_product)
    # print(dim_product)
    # print(dim_warehouse)
    # print(dim_product_category)
    # print(dim_date)