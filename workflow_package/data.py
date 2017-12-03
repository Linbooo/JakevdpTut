

from urllib.request import urlretrieve
import os
import pandas as pd

FREMONT_URL = 'http://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data                                                                  
                                                                                                            
    Parameters                                                                                              
    --------------                                                                                          
    filename : string(optional)                                                                             
             location to save the data                                                                      
    url: string(optional)                                                                                   
         web location of the data                                                                           
    force_download : bool (optional)                                                                        
         If True, force download the data                                                                   
                                                                                                            
    Returns                                                                                                 
    --------------                                                                                          
    datßa : Pandas Dataframe                                                                                
         the Fremont bridge data                                                                            
    """
    if force_download or not os.path.exists('Fremont.csv'):
        urlretrieve(url, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ['West','East']
    data['Total'] = data['West'] + data['East']

    return data