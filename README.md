# Daily Production Report Automation with Airflow

This project automates the daily production report update of a paper company by consolidating data from multiple Excel files into a single CSV file, by leveraging Python libraries and scheduling tools. 

# Overview

This project is a repplication of an improvement I did in a company data process. The daily routine involved gathering production data (production per line, raw material usage, machine breaks, etc.) from many separate Excel files every morning. With the leadership meeting scheduled at 8:20 AM and data available by 8:00 AM, the manual ETL process was often too slow, resulting in delayed reports. This project was initiated to automate the data consolidation and processing, ensuring the report is always delivered on time.

# Features

- Automated Data Extraction: Uses Python to read and consolidate data from multiple Excel files.
- Data Transformation: Applies necessary filters and transformations using Pandas.
- Unified Output: Saves the processed data into a single CSV file connected to the dashboard.
- Scheduling: Configured with Airflow to ensure the ETL process runs reliably in the desired period.
- Performance Improvement: Reduces the ETL process runtime substancially in comparison with the same process done manually, and also, improve data quality and reliability.

# Technologies

- Python: Core programming language.
- Pandas: Data manipulation and transformation (Python library).
- OpenPyXL: Excel file handling (Python library).
- Faker: Generate fake data (Python library).
- Airflow: Workflow orchestration and scheduling.

# Installation

## 1 - Clone the repository:

```bash
git clone https://github.com/falmeidev/excel-etl-automation.git
cd excel-etl-automation
```

## 2 - Install Docker (if you already have, SKIP THIS STEP)

Access the link and download the installer according with your OS.

[Docker] (https://www.docker.com/)

After the download, just double click the installer and proceed with installation.

**Note: In Linux, you can simply run:**

``` bash
sudo pacman -S docker
```

## 2 - Install Docker Compose (if you already have, SKIP THIS STEP)

Access the link and download the installer according with your OS.

[Docker Compose] (https://docs.docker.com/compose/install/)

After the download, just double click the installer and proceed with installation.

**Note: In Linux, you can simply run:**

``` bash
sudo pacman -S docker-compose
```

# Usage

In the project directory, initialize the Airflow container with the command below:

``` bash
docker compose up airflow-init
```

After the initialization, you can up the containers (note that there are many containers to run Airflow):

``` bash
docker compose up -d
```

To list the containers that are running, use the command ```docker ps```. Once the container 'webserver' is running with status 'healthy', open the browser and access the address ```http://localhost:8080/```.

The localhost in the port 8080 with open the Airflow UI. The credentials to access are: user=airflow/pass=airflow. 

Running the DAG in Airflow will execute the ETL process and provide the CSV file in the ```data_output``` folder.

# Scheduling & Orchestration

## Airflow Orchestration

    - DAG Configuration: An Airflow DAG is set up to orchestrate the ETL run.
    - Scheduling: The DAG is scheduled to run mannualy, but can be configured to run @Daily for exemplo, to ensure the report is always ready by the leadership meeting.

# Results 

- **Time Efficiency:** Reduced the ETL process from 15 minutes to 3.5 minutes.
- **Reliability:** Automated and validated the entire process, ensuring accurate and timely report delivery.
- **Operational Impact:** Enhanced the ability to deliver daily production reports before the management meeting.

# Contribution 🤝

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository, create a branch, and submit a pull request. We appreciate your feedback.

# License 📝

This project is licensed under the GNU v3.0 License - see the LICENSE file for details.