# tests/test_your_script.py
import pytest
import pandas as pd
from unittest import mock
from src.pipeline.etl import load_data, transform_to_tables, upload_to_bigquery

# Test load_data function
def test_load_data():
    # Test successful load
    with mock.patch('pandas.read_csv', return_value=pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})):
        data = load_data('some_file.csv')
        assert not data.empty
    
    # Test FileNotFoundError
    with mock.patch('pandas.read_csv', side_effect=FileNotFoundError):
        data = load_data('some_file.csv')
        assert data is None

# Test transform_to_tables function
def test_transform_to_tables():
    raw_data = pd.DataFrame({
        'Product_Code': ['P1', 'P2', 'P1'],
        'Product_Category': ['Cat1', 'Cat2', 'Cat1'],
        'Warehouse': ['W1', 'W2', 'W1'],
        'Date': ['2020-01-01', '2020-01-02', '2020-01-01']
    })
    
    fact_product, dim_product, dim_warehouse, dim_product_category, dim_date = transform_to_tables(raw_data)
    
    assert not fact_product.empty
    assert len(dim_product) == 2  # Unique products
    assert len(dim_warehouse) == 2  # Unique warehouses
    assert len(dim_product_category) == 2  # Unique product categories
    assert len(dim_date) == 2  # Unique dates

# Mock the credentials for BigQuery
mock_credentials = mock.Mock()

# Test upload_to_bigquery function
@mock.patch('src.pipeline.etl.pandas_gbq.to_gbq')
@mock.patch('src.pipeline.etl.credentials', mock_credentials)
def test_upload_to_bigquery(mock_to_gbq):
    tables = [
        pd.DataFrame({'col1': [1, 2]}),
        pd.DataFrame({'col2': [3, 4]}),
        pd.DataFrame({'col3': [5, 6]}),
        pd.DataFrame({'col4': [7, 8]}),
        pd.DataFrame({'col5': [9, 10]})
    ]
    table_names = ['fact_product', 'dim_product', 'dim_warehouse', 'dim_product_category', 'dim_date']
    
    upload_to_bigquery(tables, table_names)
    
    assert mock_to_gbq.call_count == len(tables)
    for i, call in enumerate(mock_to_gbq.call_args_list):
        args, kwargs = call
        assert args[1] == f"dwh_warehouse_dataset.{table_names[i]}"
