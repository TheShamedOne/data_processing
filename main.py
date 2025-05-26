import pandas as pd

import HelperFunctions as hf


# file path goes here
file_path = ""

df = pd.read_csv(file_path)

print(hf.get_info(df))