# Layout will accept a pandas dataframe

import pandas as pd
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px


class Layout:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def create_layout(self) -> html.Div:
        '''
        Returns a list of html.Divs to create the layout (in form of html.Div)
        '''
        layout = html.Div([
            self.title(),
            self.summary_subject_count(),
            self.summary_session_count(),
            self.summary_image_count(),
            self.count_histogram()
        ], style={'position': 'relative'})
        return layout

    def title(self) -> html.Div:
        div = html.Div([
            html.H1("PRIME-DE QC Structural", style={'font-weight': 'bold'})],
            style={'position': 'absolute',
                   'top': '5px', 'left': '10px'}
        )
        return div

    def summary_subject_count(self) -> html.Div:
        unique_subject_count = len(self.df['Subject'].unique())
        div = html.Div([
            html.H2(f"Total Subjects: {unique_subject_count}")
        ], style={'position': 'absolute', 'top': '50px', 'left': '10px'})
        return div

    def summary_session_count(self) -> html.Div:
        df_unique = self.df.drop_duplicates(subset=['Subject', 'Session'])
        unique_subject_session_count = df_unique.shape[0]
        div = html.Div([
            html.H2(f"Total Sessions: {unique_subject_session_count}")
        ], style={'position': 'absolute', 'top': '80px', 'left': '10px'})
        return div

    def summary_image_count(self) -> html.Div:
        df_length = len(self.df)
        div = html.Div([
            html.H2(f"Total Images: {df_length}")
        ], style={'position': 'absolute', 'top': '110px', 'left': '10px'})
        return div

    def count_histogram(self) -> html.Div:
        div = html.Div([
            dcc.Graph(
                id='histogram_count',
                config={'displayModeBar': False}
            )
        ], style={'position': 'absolute', 'top': '100px', 'right': '10px'})
        return div
