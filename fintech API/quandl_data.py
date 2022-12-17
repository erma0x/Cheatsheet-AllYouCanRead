
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quandl

API_KEY = "oWFh-gJABvyzZzzsyfTy" # EXAMPLE
API_KEY = "oWFh-gJABvyzZUNsyfTy"
quandl.ApiConfig.apy_key = API_KEY


df = quandl.get("WIKI/AAPL",
		 rows = 5 ,
		 start_date="2017-12-10", 
		 end_date="2018-12-31",paginate=True)

print(df,"\n\n")


# EXAMPLES

#mydata = quandl.get(["NSE/OIL.1", "WIKI/AAPL.4"])
#print(mydata,"\n\n")


#daily_changes = mydata2.pct_change(periods=1)
#daily_changes.plot()

#mydata = quandl.get("EIA/PET_RWTC_D", collapse="monthly")

#mydata = quandl.get_table('ZACKS/FC', ticker='AAPL')

#data = quandl.get_table('ZACKS/FC', paginate=True) # avoid exidiing call limits

#mydata = quandl.get("FRED/GDP", transformation="rdiff")

