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


def main():
    """Main execution entry point"""
    args = read_arguments()
    df, projects = dataframe_from_json(args.datafile)
    plot_project_bar(df)
    plot_timeseries_bar(projects, 'D')


def fix_times(df):
    """Converts start and end columns to datetime format and adds an 'Hours_Worked' column
    containing a Timedelta of each session."""
    df = df.assign(
        start = pd.to_datetime(df['start'], dayfirst=True),
        end = pd.to_datetime(df['end'], dayfirst=True),
        Hours_Worked = lambda x: (x.end - x.start) / pd.Timedelta(hours=1)
        )
    return df


def dataframe_from_json(filepath):
    """Loads a time-tracker app data json file and generates a DataFrame where each row is a session."""
    with open(filepath) as file:
        data = json.load(file)
    projects = []
    for index, project in enumerate(data['projects']):
        temp_df = (
            pd.DataFrame(project['sessions'])
            .assign(Project = project['project_name'])
        )
        projects.append(temp_df)
    df = (
        pd.concat(projects)
        .pipe(fix_times)
    )
    return df, projects


def plot_project_bar(df):
    """Generates a bar chart which shows the Hours spent working for each project."""
    project_view_df = df[['Project', 'Hours_Worked']].groupby(['Project']).sum().reset_index()
    fig = (
        px.bar(project_view_df, x='Hours_Worked', y='Project', orientation='h', title="Work done per Project")
        .update_yaxes(categoryorder = "total ascending")
        .update_traces(texttemplate='%{value:.1f}', textposition = 'outside')
        .show()
    )


def plot_timeseries_bar(projects, frequency):
    """Generates a bar chart which shows a breakdown of daily work done."""
    resampled_projects = []
    for project in projects:
        temp_df = (
            project.pipe(fix_times)
            .resample(frequency, on='start').sum().reset_index()
            .rename(columns={'start':"Date"})
            .assign(Project = project['Project'][0])
        )
        resampled_projects.append(temp_df)
    resampled_df = pd.concat(resampled_projects)
    fig = (
        px.bar(resampled_df, x='Date', y='Hours_Worked', color="Project", title='Daily Work')
        .show()
    )
    

def read_arguments():
    """Defines the command-line arguments for this script and fetches those arguments"""
    parser = argparse.ArgumentParser(description='Generates a dashboard for exploring time-tracker app data')
    parser.add_argument("-f", "--file", dest="datafile", help="filepath of time-tracker app data file")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()