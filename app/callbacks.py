import dash
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np


def update_pie_chart_count(selected_data: dict, df: pd.DataFrame):

    df = df.drop_duplicates(subset=['Subject', 'Session'])

    if selected_data is not None:
        selected_points = [point['x'] for point in selected_data['points']]
        filtered_df = df[df['Output QC'].isin(selected_points)]
    else:
        filtered_df = df

    # Create a new column 'QC Status' with values "Success" for 1, "Failed" for others
    filtered_df['QC Status'] = np.where(
        filtered_df['Output QC'] == 1, "Success", "Failed")

    # Count the number of "Success" and "Failed"
    qc_status_counts = filtered_df['QC Status'].value_counts()

    # Create a Pie Chart
    fig = px.pie(
        qc_status_counts,
        values=qc_status_counts.values,
        names=qc_status_counts.index,
        title='Success/Fail Distribution'
    )

    fig.update_layout(
        plot_bgcolor='#ffffff',  # Set the background color inside the pie chart
        paper_bgcolor='#ffffff',  # Set the background color outside the pie chart
    )

    return fig


def total_subjects_pie_chart_count(selected_data: dict, df: pd.DataFrame):
    df = df.drop_duplicates(subset=['Subject'])
    if selected_data is not None:
        selected_points = [point['x'] for point in selected_data['points']]
        filtered_df = df[df['Output QC'].isin(selected_points)]
    else:
        filtered_df = df
    filtered_df['QC Status'] = np.where(
        filtered_df['Output QC'] == 1, "Success", "Failed")
    qc_status_counts = filtered_df['QC Status'].value_counts()
    outer_pie = go.Pie(
        values=[qc_status_counts[0], qc_status_counts[1]],
        hole=1,
        textinfo='none'
    )
    inner_pie = go.Pie(
        values=[qc_status_counts[0], qc_status_counts[1]],
        hole=0.8,
        textinfo='none'
    )
    layout = go.Layout(
        showlegend=False,
    )
    fig = go.Figure(data=[outer_pie, inner_pie], layout=layout)
    fig.update_layout(
        width=125,  # Minimum width
        height=125,  # Minimum height
        margin=dict(l=10, r=10, t=10, b=10),  # Adjust margins for spacing
        autosize=False,  # Disable autosizing
    )
    return fig


def total_sessions_pie_chart_count(selected_data: dict, df: pd.DataFrame):
    df = df.drop_duplicates(subset=['Subject', 'Session'])
    if selected_data is not None:
        selected_points = [point['x'] for point in selected_data['points']]
        filtered_df = df[df['Output QC'].isin(selected_points)]
    else:
        filtered_df = df
    filtered_df['QC Status'] = np.where(
        filtered_df['Output QC'] == 1, "Success", "Failed")
    qc_status_counts = filtered_df['QC Status'].value_counts()
    outer_pie = go.Pie(
        values=[qc_status_counts[0], qc_status_counts[1]],
        hole=1,
        textinfo='none'
    )
    inner_pie = go.Pie(
        values=[qc_status_counts[0], qc_status_counts[1]],
        hole=0.8,
        textinfo='none'
    )
    layout = go.Layout(
        showlegend=False,
    )
    fig = go.Figure(data=[outer_pie, inner_pie], layout=layout)
    fig.update_layout(
        width=125,  # Minimum width
        height=125,  # Minimum height
        margin=dict(l=10, r=10, t=10, b=10),  # Adjust margins for spacing
        autosize=False,  # Disable autosizing
    )
    return fig


def total_images_pie_chart_count(selected_data: dict, df: pd.DataFrame):
    if selected_data is not None:
        selected_points = [point['x'] for point in selected_data['points']]
        filtered_df = df[df['Output QC'].isin(selected_points)]
    else:
        filtered_df = df
    filtered_df['QC Status'] = np.where(
        filtered_df['Output QC'] == 1, "Success", "Failed")
    qc_status_counts = filtered_df['QC Status'].value_counts()
    outer_pie = go.Pie(
        values=[qc_status_counts[0], qc_status_counts[1]],
        hole=1,
        textinfo='none'
    )
    inner_pie = go.Pie(
        values=[qc_status_counts[0], qc_status_counts[1]],
        hole=0.8,
        textinfo='none'
    )
    layout = go.Layout(
        showlegend=False,
    )
    fig = go.Figure(data=[outer_pie, inner_pie], layout=layout)
    fig.update_layout(
        width=125,  # Minimum width
        height=125,  # Minimum height
        margin=dict(l=10, r=10, t=10, b=10),  # Adjust margins for spacing
        autosize=False,  # Disable autosizing
    )
    return fig


def update_site_distribution(selected_data: dict, df: pd.DataFrame):

    median_age_by_site = df.groupby('Site')['Age'].median().reset_index()
    sorted_sites = median_age_by_site.sort_values(by='Age')["Site"].tolist()

    # Sort the DataFrame by the sorted site order
    df['Site'] = pd.Categorical(
        df['Site'], categories=sorted_sites, ordered=True)
    df.sort_values('Site', inplace=True)

    fig = px.box(
        df,
        x='Site',
        y='Age',
        category_orders={"Site": sorted_sites}
    )

    return fig


def update_sex_plot(selected_data: dict, df: pd.DataFrame):

    if selected_data is not None:
        selected_points = [point['x'] for point in selected_data['points']]
        filtered_df = df[df['Output QC'].isin(selected_points)]
    else:
        filtered_df = df

    filtered_df = filtered_df[filtered_df['Sex'].isin(['F', 'M'])]
    filtered_df = filtered_df.drop_duplicates(subset=['Subject', 'Session'])
    sex_counts = filtered_df['Sex'].value_counts()

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=sex_counts.index,
        y=sex_counts.values,
        marker_color=['#1f77b4', '#ff0000'],  # Blue for M, Red for F
        text=sex_counts.values,
        textposition='auto',
        hoverinfo='x+y+text',  # Show both x and y values in hover text
    ))

    return fig


def update_site_failed_qc(selected_data: dict, df: pd.DataFrame):
    df = df.drop_duplicates(subset=['Subject', 'Session'])
    # Filter the data based on the selected points (if any)
    if selected_data is not None:
        selected_points = [point['x'] for point in selected_data['points']]
        filtered_df = df[df['Output QC'].isin(selected_points)]
    else:
        filtered_df = df

    # Create a pivot table to count the QC statuses for each site
    pivot_df = pd.pivot_table(filtered_df, values='Session', index='Site',
                              columns='QC Status', aggfunc='count', fill_value=0)

    return {
        'data': [
            go.Bar(
                x=pivot_df.index,
                y=pivot_df['Success'],
                name='Success',
                marker=dict(color='blue')
            ),
            go.Bar(
                x=pivot_df.index,
                y=pivot_df['Failed'],
                name='Failed',
                marker=dict(color='red')
            )
        ],
        'layout': go.Layout(
            title='QC Sessions by Site',
            xaxis=dict(title='Site'),
            yaxis=dict(title='Count'),
            barmode='group'
        )
    }


def update_subject_dropdown(selected_site, df: pd.DataFrame):
    subjects_for_site = df[df['Site'] == selected_site]['Subject'].unique()
    subject_options = [{'label': subject, 'value': subject}
                       for subject in subjects_for_site]
    return subject_options


def update_displayed_image(selected_site, selected_subject, df: pd.DataFrame):
    link = 'https://drive.google.com/uc?export=view&id=1369Huyga6V4DJBRonleQKxfsSUmLe3PK'

    img = html.Img(src=link, style={'width': '95%', 'height': 'auto'})
    return img


def register_callbacks(app: dash.Dash, df: pd.DataFrame):

    app.callback(
        Output('pie_chart_count', 'figure'),
        [Input('pie_chart_count', 'selectedData')]
    )(lambda selected_data: update_pie_chart_count(selected_data, df))

    app.callback(
        Output('total_subjects_pie', 'figure'),
        [Input('total_subjects_pie', 'selectedData')]
    )(lambda selected_data: total_subjects_pie_chart_count(selected_data, df))

    app.callback(
        Output('total_sessions_pie', 'figure'),
        [Input('total_sessions_pie', 'selectedData')]
    )(lambda selected_data: total_sessions_pie_chart_count(selected_data, df))

    app.callback(
        Output('total_images_pie', 'figure'),
        [Input('total_images_pie', 'selectedData')]
    )(lambda selected_data: total_images_pie_chart_count(selected_data, df))

    app.callback(
        Output('site_distribution', 'figure'),
        [Input('site_distribution', 'selectedData')]
    )(lambda selected_data: update_site_distribution(selected_data, df))

    app.callback(
        Output('sex_bar_plot', 'figure'),
        [Input('sex_bar_plot', 'selectedData')]
    )(lambda selected_data: update_sex_plot(selected_data, df))

    app.callback(
        Output('site_failed_qc', 'figure'),
        [Input('site_failed_qc', 'selectedData')]
    )(lambda selected_data: update_site_failed_qc(selected_data, df))

    app.callback(
        Output('subject-dropdown', 'options'),
        Input('site-dropdown', 'value')
    )(lambda value: update_subject_dropdown(value, df))

    app.callback(
        Output('image-container', 'children'),
        [Input('site-dropdown', 'value'), Input('subject-dropdown', 'value')]
    )(lambda selected_site, selected_subject: update_displayed_image(selected_site, selected_subject, df))

    return
