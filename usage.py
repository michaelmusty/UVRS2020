import tabula
import pandas as pd

# user defined variables
path_to_roster = "/home/mjmusty/Downloads/LEBANON UVRC 2020 2020-02-24 080212.csv"
path_to_raceresults = "/home/mjmusty/Downloads/redzone20.pdf"

roster = pd.read_csv(path_to_roster, skiprows=[0,1])
# results = tabula.read_pdf(path_to_raceresults, pages="5-7", guess=False, stream=True)
tabula.convert_into(path_to_raceresults, "test.csv", "csv")
