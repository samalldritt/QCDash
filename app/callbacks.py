import dash
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np


def update_histogram_count(selected_data: dict, df: pd.DataFrame):

    df = df.drop_duplicates(subset=['Subject', 'Session'])

    if selected_data is not None:
        selected_points = [point['x'] for point in selected_data['points']]
        filtered_df = df[df['Output QC'].isin(selected_points)]
    else:
        filtered_df = df

    # Create a new column 'QC Status' with values "Success" for 1, "Failed" for others
    filtered_df['QC Status'] = np.where(
        filtered_df['Output QC'] == 1, "Success", "Failed")

    fig = px.histogram(
        filtered_df,
        x='QC Status',
        labels={'QC Status': 'QC Status'},
        title='Success/Fail Distribution',
        category_orders={"QC Status": ["Failed", "Success"]}
    )

    # Update the title position and margin
    fig.update_layout(
        title_x=0.5,  # Center the title horizontally
        title_y=0.95,  # Position the title closer to the top
        margin=dict(t=40)  # Add top margin for the title
    )

    return fig


def register_callbacks(app: dash.Dash, df: pd.DataFrame):

    app.callback(
        Output('histogram_count', 'figure'),
        [Input('histogram_count', 'selectedData')]
    )(lambda selected_data: update_histogram_count(selected_data, df))

    return
