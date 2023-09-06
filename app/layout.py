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
            html.Link(
                rel='stylesheet', href='/assets/styles.css'),
            self.title(),
            self.line_sep(),
            # self.summary_subject_count(),
            # self.summary_session_count(),
            # self.summary_image_count(),
            self.count_pie_chart(),
            self.site_distribution(),
            self.create_summary()
        ], style={'position': 'relative'})
        return layout

    def title(self) -> html.Div:
        div = html.Div([
            html.H1("PRIME-DE QC Structural", style={'font-weight': 'bold', 'font-family': 'Avenir Next'})],
            style={'position': 'absolute',
                   'top': '5px', 'left': '540px'}
        )
        return div

    def line_sep(self) -> html.Div:
        div = html.Div([
            html.Hr(
                style={'border-color': '#1d4b73',
                       'top': '80px',
                       'left': '5%',
                       'right': '5%',
                       'position': 'absolute'}
            )
        ])
        return div

    def summary_session_count(self) -> html.Div:
        df_unique = self.df.drop_duplicates(subset=['Subject', 'Session'])
        unique_subject_session_count = df_unique.shape[0]
        div = html.Div([
            html.H2(f"Total Sessions: {unique_subject_session_count}", style={
                    'font-family': 'Avenir Next'})
        ], style={'position': 'absolute', 'top': '80px', 'left': '10px'})
        return div

    def summary_image_count(self) -> html.Div:
        df_length = len(self.df)
        div = html.Div([
            html.H2(f"Total Images: {df_length}", style={
                    'font-family': 'Avenir Next'})
        ], style={'position': 'absolute', 'top': '110px', 'left': '10px'})
        return div

    def count_pie_chart(self) -> html.Div:
        div = html.Div([
            dcc.Graph(
                id='pie_chart_count',
                config={'displayModeBar': False},
                style={
                    'height': '400px',
                    'width': '400px',
                    'margin': '2px',
                    'border': '2px solid',
                    'border-color': '#333'
                }
            )
        ], style={'position': 'absolute', 'top': '150px', 'left': '20px'})
        return div

    def site_distribution(self) -> html.Div:
        div = html.Div([
            dcc.Graph(
                id='site_distribution',
                config={'displayModeBar': False},
                style={
                    'height': '400px',
                    'width': '950px',
                    'margin': '2px',
                    'border': '2px solid',
                    'border-color': '#333'
                }
            )
        ], style={'position': 'absolute', 'top': '150px', 'right': '20px'})
        return div

    def create_summary(self) -> html.Div:
        unique_subject_count = len(self.df['Subject'].unique())
        df_unique = self.df.drop_duplicates(subset=['Subject', 'Session'])
        unique_subject_session_count = df_unique.shape[0]
        df_length = len(self.df)
        div = html.Div(
            children=[
                html.P(f"Total Subjects:",
                       style={
                           'font-family': 'Avenir Next',
                           'color': '#1d4b73',
                           'position': 'absolute',
                           'top': '0%',
                           'left': '7%',
                           'font-weight': 'bold',
                           'font-size': '20px'}),
                dcc.Graph(
                    id='total_subjects_pie',
                    config={'displayModeBar': False},
                    style={
                        'height': '100px',
                        'width': '100px',
                        'position': 'absolute',
                        'top': '30%',
                        'left': '11%'
                    }
                ),
                html.P(f"Total Sessions:",
                       style={
                           'font-family': 'Avenir Next',
                           'color': '#1d4b73',
                           'position': 'absolute',
                           'top': '0%',
                           'left': '38%',
                           'font-weight': 'bold',
                           'font-size': '20px'}),
                dcc.Graph(
                    id='total_sessions_pie',
                    config={'displayModeBar': False},
                    style={
                        'height': '1000px',
                        'width': '1000px',
                        'position': 'absolute',
                        'top': '30%',
                        'left': '42%'
                    }
                ),
                html.P(f"Total Images:",
                       style={
                           'font-family': 'Avenir Next',
                           'color': '#1d4b73',
                           'position': 'absolute',
                           'top': '0',
                           'left': '70%',
                           'font-weight': 'bold',
                           'font-size': '20px'}),
                dcc.Graph(
                    id='total_images_pie',
                    config={'displayModeBar': False},
                    style={
                        'height': '1000px',
                        'width': '1000px',
                        'position': 'absolute',
                        'top': '30%',
                        'left': '73%'
                    }
                )
            ],
            style={
                'height': '150px',
                'width': '600px',
                'margin': '2px',
                'border': '2px solid',
                'border-color': '#333',
                'position': 'absolute',
                'top': '570px',
                'left': '20px',
                'backgroundColor': '#ffffff'
            }
        )
        return div
