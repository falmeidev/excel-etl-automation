# Libraries
import pandas as pd
import numpy as np
from faker import Faker

def generate_data():

    fake = Faker()

    # Define time period
    dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")

    # Define production lines
    prod_lines = ["L01","L02"]

    # Create a list with the data and line combinations
    combinations = [(date, line) for date in dates for line in prod_lines]

    #########################
    ##### Production ########
    #########################

    # Create the dataframe
    production_data = pd.DataFrame(combinations, columns=["date", "line"])

    # Generate production data
    production_data["produced_tons"] = np.random.uniform(100, 500, len(production_data))  # Production between 100 and 500 tons
    production_data["efficiency"] = np.random.uniform(75, 98, len(production_data))  # Efficiency between 75% and 98%

    production_data.to_excel("./data_source/paper_production.xlsx", index=False)

    #########################
    ###### Materials ########
    #########################

    # Generate raw materials data
    materials_data = pd.DataFrame(combinations, columns=["date", "line"])

    materials_data["cellulose_kg"] = np.random.uniform(5000, 20000, len(materials_data))  # Cellulose between 5000 ND 20000 kg
    materials_data["chemicals_kg"] = np.random.uniform(100, 1000, len(materials_data))  # Chemical products usage, between 100 and 1000 kg
    materials_data["water_liters"] = np.random.uniform(20000, 100000, len(materials_data))  # Water usage between 20000 and 100000 liters

    materials_data.to_excel("./data_source/pmaterials_used.xlsx", index=False)

    #########################
    ###### Downtime #########
    #########################

    # Generate downtime data 
    downtime_reasons = ["Maintenance", "Mechanical Failure", "Raw Material Shortage", "Power Outage", "No Downtime"]

    downtime_data = pd.DataFrame(combinations, columns=["date", "line"])

    downtime_data["downtime_hours"] = np.random.choice([0, 1, 2, 3, 4, 5], len(downtime_data), p=[0.7, 0.1, 0.08, 0.06, 0.04, 0.02])  # Most of days without downtime
    downtime_data["reason"] = np.random.choice(downtime_reasons, len(downtime_data), p=[0.2, 0.2, 0.15, 0.05, 0.4])  # Downtime reason

    # Correct downtime info
    downtime_data["downtime_hours"] = np.where(downtime_data["reason"] == "No Downtime", 0, downtime_data["downtime_hours"])
    downtime_data["reason"] = np.where(downtime_data["downtime_hours"] == 0, "No Downtime", downtime_data["reason"])

    downtime_data.to_excel("./data_source/pdowntime.xlsx", index=False)

    # Print Success Message
    print("CSV files generated with success!")

if __name__ == "__main__":
    generate_data()
