import numpy as np
import pandas as pd
import sys

# Nome file input ed output da cambiare
from names import input_file_name, output_file_name

def preprocessing():

    path_csv = sys.path[0] # prendi il path della cartella
    output_path = sys.path[0] + output_file_name # nome del nuovo file
   
    df = pd.read_csv(path_csv+input_file_name) 
    # prendi il CSV in input e lo trasformi in un dataframe 
    
    # PIPELINE 
    (df    
    .pipe(correct_error_type1)         # ERROR CORRECTION
    .pipe(normalize_df)                  # NORMALIZE
    .pipe(date_time_formatting)
    )
    
    df.to_csv(output_path)              # Save into CSV



# CORREZIONE DATI 
    # ERRORE TIPO 1
def correct_error_type1(df):
    columns = df.columns # prendi tutte le colonne del CSV
    new_df = df.copy() # crea un dataframe vuoto

    for col in columns: # passa ogni colonna del dataframe
        if col in ['low','high','open','close']:
            for i in range(len(df[col])):
                if df[col][i] > 5: # found error <5 only for EURUSD
                    new_df[col][i] = np.mean(new_df[col][i+1],new_df[col][i-1])
    return new_df             
    
 
# NORMALIZZAZIONE 
def min_max(nparray): 
    """ Metodo min_max per la normalizzazione
     ( elemento_i - Min ) / (Max - Min) """
    return (nparray - np.min(nparray)) / (np.max(nparray) - np.min(nparray))

def normalize_df(df):
    " normalizza ogni colonna tranne 'date_time' "
    columns = df.columns # prendi tutte le colonne del CSV
    new_df = pd.DataFrame() # crea un dataframe vuoto
    new_df["date_time"] = df["date_time"]
    for col in columns: # passa ogni colonna del dataframe
        if col != "date_time":
            new_col_array = min_max(df[col]) # normalizza colonna
            new_df[col] = new_col_array
      
    return new_df

def date_time_formatting(df):
    #df['date_time'] = pd.to_datetime(df['date_time']) # convert column to datetime object
    df.set_index('date_time', inplace=True) # set column 'date' to index
    return df

if __name__=="__main__":
  preprocessing() # generate output cs
