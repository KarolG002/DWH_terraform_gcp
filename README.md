# Data Warehousing Project

This project involves setting up a data warehouse on Google Cloud Platform (GCP) using Terraform, pushing data to BigQuery with a Python script, and visualizing the data with Power BI. Data was acquired from kaggle.com

## Table of Contents

- [Project Overview](#project-overview)
- [Project Architecture](#project-architecture)
- [Power BI Dashboard](#power-bi-dashboard)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Testing](#testing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
## Project Overview

The goal of this project is to create a data warehouse that stores historical product demand data and provides insights through a Power BI dashboard. The infrastructure is provisioned using Terraform, data is loaded into BigQuery with a Python script, and Power BI is used for data visualization.

## Project Architecture

![Project architecture](images/Architecture.png "Architecture diagram")

## Power BI Dashboard

![Dashboard](images/Report.png "Power BI dashboard")

## Prerequisites

Before you begin, ensure you have the following installed:

- [Terraform](https://www.terraform.io/downloads.html) (v1.0+)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Python](https://www.python.org/downloads/) (v3.8+)
- [Pandas](https://pandas.pydata.org/)
- [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/)
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/)

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:
```bash
git clone https://github.com/KarolG002/DWH_terraform_gcp.git
cd DWH-terraform-gcp
```

### 2. Set up terraform
```bash
cd terraform
```
Supply your own project id and key and then:
```bash
terraform init

terraform apply
```

#### To tear down infrastracture
```bash
terraform destroy
```

### 3. Install Python Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install pandas pandas-gbq
pip install pytest
```

### 4. Run the Data Pipeline
```bash
python src/pipeline/etl.py
```
### 5. Set Up Power BI
Open Power BI Desktop.

Connect to your BigQuery dataset using the BigQuery Connector.

Create your visualizations based on the data available in the BigQuery tables.

## Testing
Navigate to the tests directory:

```bash
cd tests
```

Run the tests using pytest:
```bash
python -m pytest tests.py
```
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

The dataset used in this project was acquired from [Kaggle.com](https://www.kaggle.com/datasets/felixzhao/productdemandforecasting/data)

Thanks to the open-source community for the tools and libraries used in this project.