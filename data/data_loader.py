# Has its own class in case I want to load in multiple CSV and do some data wrangling later

import pandas as pd
import subprocess


class Loader:

    def __init__(self):
        self.update_data()
        df_QC = self.load_data(
            'data/QC_data.csv')
        demographic_df = self.load_data(
            'data/demographic_data.csv')
        self.merge_data(df_QC, demographic_df)
    
    def update_data(self):
        subprocess.run(['bash', r'C:\Users\Sam\Documents\projects\QCDash\data'], shell=True)

    def load_data(self, path: str) -> pd.DataFrame:
        '''
        Load the data 'QC_data.csv' as pd dataframe
        '''
        df = pd.read_csv(path)
        return df

    def merge_data(self, qc_df: pd.DataFrame, demographic_df: pd.DataFrame) -> pd.DataFrame:
        '''
        Merging the demographic and QC dataframes to make one dataframe
        '''

        # Subset the demographic data first
        demographic_df = demographic_df[['Site', 'BIDS_subID',
                                        'BIDS_session', 'Sex', 'Age(Years)', 'Species']]
        demographic_df['BIDS_session'] = demographic_df['BIDS_session'].astype(
            'object')

        merge_on_columns = {
            'qc_df': ['Subject', 'Session'],
            'demographic_df': ['BIDS_subID', 'BIDS_session']
        }
        
        print(qc_df.dtypes)
        print(demographic_df.dtypes)

        self.merged_df = qc_df.merge(
            demographic_df, left_on=merge_on_columns['qc_df'], right_on=merge_on_columns['demographic_df'], how='inner')

    def get_data(self) -> pd.DataFrame:
        return self.merged_df
