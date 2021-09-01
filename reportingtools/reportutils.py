"""
Functions for generating reports from app data.

Command-line Arguments:

    If run using the command-line, takes app data json file as an argument and generates plots.

Functions:

    fix_times(DataFrame) -> DataFrame
    dataframe_from_json(file) -> DataFrame, List of DataFrames
    plot_project_bar(DataFrame)
    plot_timeseries_bar(List of DataFrames, string)
    read_arguments() -> Namespace
"""


import json
import argparse

import pandas as pd
import plotly.express as px


def fix_times(df):
    """Converts start and end columns to datetime format and adds an 'Hours Worked' column
    containing a Timedelta of each session."""

    df['start'] = pd.to_datetime(df['start'], dayfirst=True)
    df['end'] = pd.to_datetime(df['end'], dayfirst=True)
    df['Hours Worked'] = (df['end'] - df['start']) / pd.Timedelta(hours=1)

    return df
    

def dataframe_from_json(filepath):
    """Loads a time-tracker app data json file and generates a DataFrame where each row is a session."""
    with open(filepath) as file:
        data = json.load(file)

    projects = []
    for index, project in enumerate(data['projects']):
        temp_df = pd.DataFrame(project['sessions'])
        temp_df['Project'] = project['project_name']
        projects.append(temp_df)

    df = pd.concat(projects)
    df = fix_times(df)
    
    return df, projects


def plot_project_bar(df):
    """Generates a bar chart which shows the Hours spent working for each project."""
    project_view_df = df[['Project', 'Hours Worked']]
    project_view_df = project_view_df.groupby(['Project']).sum().reset_index()
    fig = px.bar(project_view_df, x='Hours Worked', y='Project', orientation='h', title="Work done per Project")
    fig.update_yaxes(categoryorder = "total ascending")
    fig.update_traces(texttemplate='%{value:.1f}', textposition = 'outside')
    fig.show()

 
def plot_timeseries_bar(projects, frequency):
    """Generates a bar chart which shows a breakdown of daily work done."""

    resampled_projects = []
    for project in projects:
        temp_df = project
        temp_df = fix_times(temp_df)
        resampled_temp_df = temp_df.resample(frequency, on='start').sum().reset_index()
        resampled_temp_df['Project'] = temp_df['Project'][0]
        resampled_temp_df.rename(columns={'start':"Date"}, inplace=True)
        resampled_projects.append(resampled_temp_df)

    resampled_df = pd.concat(resampled_projects)
    fig = px.bar(resampled_df, x='Date', y='Hours Worked', color="Project", title='Daily Work')
    fig.show() 


def read_arguments():
    """Defines the command-line arguments for this script and fetches those arguments"""
    parser = argparse.ArgumentParser(description='Generates a dashboard for exploring time-tracker app data')
    parser.add_argument("-f", "--file", dest="datafile", help="filepath of time-tracker app data file")
    args = parser.parse_args()
    return args


def main():
    """Main execution entry point"""
    args = read_arguments()
    df, projects = dataframe_from_json(args.datafile)
    plot_project_bar(df)
    plot_timeseries_bar(projects, 'D')


if __name__ == "__main__":
    main()