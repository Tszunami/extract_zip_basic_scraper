from os import listdir
from os.path import isfile, join
import pandas as pd

PATH_EXCEL = "./excel/"
PATH_CSV = "./csv/"

# finds files for conversion
excel = [f for f in listdir(PATH_EXCEL) if isfile(join(PATH_EXCEL, f))]

print("Files converted:")

# converts files found
for f in excel:
    excel_file = pd.DataFrame(pd.read_excel(PATH_EXCEL+f))
    file_path_csv = PATH_CSV+f[:f.find(".")]+".csv"
    excel_file.to_csv(file_path_csv, index=None, header=True)
    print(file_path_csv + "\n")

print("All excel files found in " + PATH_EXCEL + " have " + 
      "been converted to '.csv' and can be found in " + PATH_CSV)