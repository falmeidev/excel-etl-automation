import pandas as pd

production = pd.read_excel("../data_source/paper_production.xlsx")
materials = pd.read_excel("../data_source/pmaterials_used.xlsx")
downtime = pd.read_excel("../data_source/pdowntime.xlsx")

consolidated_date = pd.merge(production, materials, on=["date","line"])
consolidated_date = pd.merge(consolidated_date, downtime, on=["date","line"])

consolidated_date.to_csv("../data_output/consolidated_date.csv", index=False)