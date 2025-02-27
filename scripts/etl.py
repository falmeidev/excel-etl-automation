import pandas as pd

def run_etl():
    production = pd.read_excel("./data_source/paper_production.xlsx")
    materials = pd.read_excel("./data_source/pmaterials_used.xlsx")
    downtime = pd.read_excel("./data_source/pdowntime.xlsx")

    consolidated_data = pd.merge(production, materials, on=["date","line"])
    consolidated_data = pd.merge(consolidated_data, downtime, on=["date","line"])
    consolidated_data.to_csv("./data_output/consolidated_data.xlsx")

if __name__ == "__main__":
    run_etl()
