# Has its own class in case I want to load in multiple CSV and do some data wrangling later

import pandas as pd
import subprocess


class Loader:

    def __init__(self):
        # self.update_data()
        self.df = self.load_data(
            'data/QC_data.csv')

    def load_data(self, path: str) -> pd.DataFrame:
        '''
        Load the data 'QC_data.csv' as pd dataframe
        '''
        df = pd.read_csv(path, dtype={'Subject': str, 'Session': str})
        return df

    def get_data(self) -> pd.DataFrame:
        return self.df
