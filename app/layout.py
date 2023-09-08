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
            self.count_pie_chart(),
            self.site_distribution(),
            self.create_summary(),
            self.sex_bar_plot(),
            self.site_failed_qc(),
            self.input_checker()
        ], style={'position': 'relative'})
        return layout

    def title(self) -> html.Div:
        div = html.Div([
            html.H1("PRIME-DE QC Structural", style={'font-weight': 'bold', 'font-family': 'Avenir Next'})],
            style={'display': 'flex',
                   'justify-content': 'center'}
        )
        return div

    def line_sep(self) -> html.Div:
        div = html.Div([
            html.Hr(
                style={'border-color': '#1d4b73',
                       'display': 'flex',
                       'justify-content': 'center'}
            )
        ])
        return div

    def count_pie_chart(self) -> html.Div:
        div = html.Div([
            dcc.Graph(
                id='pie_chart_count',
                config={'displayModeBar': False},
                style={
                    'height': '28vw',
                    'width': '28vw',
                    'margin': '2px',
                    'border': '2px solid',
                    'border-color': '#333'
                }
            )
        ], style={
            'position': 'absolute',
            'top': '15vh',
            'left': '2vw'
        })
        return div

    def site_distribution(self) -> html.Div:
        div = html.Div([
            dcc.Graph(
                id='site_distribution',
                config={'displayModeBar': False},
                style={
                    'height': '28vw',
                    'width': '65vw',
                    'margin': '2px',
                    'border': '2px solid',
                    'border-color': '#333'
                }
            )
        ], style={'position': 'absolute',
                  'top': '15vh',
                  'right': '2vw'
                  })
        return div

    def create_summary(self) -> html.Div:
        div = html.Div(
            children=[
                html.P(f"Subjects:",
                       style={
                           'font-family': 'Avenir Next',
                           'color': '#1d4b73',
                           'position': 'absolute',
                           'top': '0vh',
                           'left': '4vw',
                           'font-weight': 'bold',
                           'font-size': '20px'}),
                dcc.Graph(
                    id='total_subjects_pie',
                    config={'displayModeBar': False},
                    style={
                        'position': 'absolute',
                        'top': '7vh',
                        'left': '6vw'
                    }
                ),
                html.P(f"Sessions:",
                       style={
                           'font-family': 'Avenir Next',
                           'color': '#1d4b73',
                           'position': 'relative',
                           'top': '0vh',
                           'left': '22vw',
                           'font-weight': 'bold',
                           'font-size': '20px'}),
                dcc.Graph(
                    id='total_sessions_pie',
                    config={'displayModeBar': False},
                    style={
                        'position': 'absolute',
                        'top': '7vh',
                        'left': '24vw'
                    }
                ),
                html.P(f"Images:",
                       style={
                           'font-family': 'Avenir Next',
                           'color': '#1d4b73',
                           'position': 'absolute',
                           'top': '0vh',
                           'left': '40vw',
                           'font-weight': 'bold',
                           'font-size': '20px'}),
                dcc.Graph(
                    id='total_images_pie',
                    config={'displayModeBar': False},
                    style={
                        'position': 'absolute',
                        'top': '7vh',
                        'left': '40vw'
                    }
                )
            ],
            style={
                'height': '26vh',
                'width': '55vw',
                'margin': '2px',
                'border': '2px solid',
                'border-color': '#333',
                'position': 'absolute',
                'top': '80vh',
                'left': '2vw',
                'backgroundColor': '#ffffff'
            }
        )
        return div

    def sex_bar_plot(self) -> html.Div:
        div = html.Div([
            dcc.Graph(
                id='sex_bar_plot',
                config={'displayModeBar': False},
                style={
                    'height': '31.5vw',  # Set initial height using viewport width units
                    'width': '35vw',   # Set initial width using viewport width units
                    'margin': '2px',
                    'border': '2px solid',
                    'border-color': '#333'
                }
            )
        ], style={
            'position': 'absolute',
            'top': '80vh',   # Set initial top position using viewport height units
            'right': '2vw'   # Set initial right position using viewport width units
        })

        return div

    def site_failed_qc(self) -> html.Div:
        div = html.Div([
            dcc.Graph(
                id='site_failed_qc',
                config={'displayModeBar': False},
                style={
                    'height': '28vh',
                    'width': '55vw',
                    'margin': '2px',
                    'border': '2px solid',
                    'border-color': '#333'
                }
            )
        ], style={'position': 'absolute',
                  'top': '115vh',
                  'left': '2vw'
                  })

        return div

    def input_checker(self) -> html.Div:

        div = html.Div([
            html.H3('DCAN_in_denoised Input Checker', style={
                    'position': 'absolute', 'top': '2vh', 'left': '2vw'}),

            html.Div([
                html.Label('Select a site:'),
                dcc.Dropdown(
                    id='site-dropdown',
                    options=[{'label': site, 'value': site}
                             for site in list(self.df['Site'].dropna().unique())],
                    value=self.df['Site'].iloc[0],
                    style={'width': '150px'}
                )
            ], style={'position': 'absolute',
                      'top': '2vh',
                      'left': '35vw'}),
            html.Div([
                html.Label('Select a subject:'),
                dcc.Dropdown(
                    id='subject-dropdown'
                )
            ], style={'position': 'absolute',
                      'top': '2vh',
                      'left': '45vw'}),

            html.Div(id='image-container', style={'position': 'absolute',
                                                  'top': '10vh',
                                                  'left': '2vw'})
        ], style={
            'position': 'absolute',
            'top': '150vh',  # Adjust the top position as needed
            'left': '2vw',
            'height': '65vh',  # Adjust the height as needed
            'width': '95vw',   # Adjust the width as needed
            'border': '2px solid',
            'border-color': '#333',
            'backgroundColor': '#ffffff'
        })

        return div
