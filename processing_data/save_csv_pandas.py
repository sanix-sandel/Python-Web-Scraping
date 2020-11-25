import pandas as import pd
from get_planet_data import get_planet_data

planets=get_planet_data()
planets_df=pd.DataFrame(planets).set_index('Name')
planets_df.to_csv("./planets_pandas.csv")