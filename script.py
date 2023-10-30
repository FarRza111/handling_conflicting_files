"""
Author: FarizRzayev
Purpose: Handling conflicting files

"""

import pandas as pd
import numpy as np
import os
import re
import shutil
from datetime import date
import warnings
warnings.filterwarnings("ignore")

latest_path = "./latest/"
if not os.path.exists(latest_path):
    os.makedirs(latest_path)

this_month = date.today().strftime("%Y%m")
latest_filename = "Batch_alert_" + this_month + ".xlsx"
esas_file = "data_details"
destination_folder = "Dashboard_Data"


destination_to_move = os.path.join(os.getcwd(), destination_folder)
mainpath = os.getcwd()
print("destination to move", destination_to_move)
print("main path", mainpath)


matching_file = [file for file in os.listdir(latest_path) if re.search(".xlsx", file)]
df = pd.read_excel(latest_path + matching_file[0], skiprows = 2)

if len(matching_file) > 2:
    print(f"there should appear only 2 files and these are {matching_file}")
elif len(matching_file)>1 and matching_file != esas_file:
    df_latest = pd.read_excel(latest_path + latest_filename, skiprows = 2)
    data = df.append(df_latest)    
    data.to_excel("Data.xlsx")
else:
    data = pd.read_excel(latest_path + "data_details.xlsx", skiprows = 2)
    data.to_excel("Data.xlsx")    
