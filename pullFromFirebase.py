import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from firebase import firebase
import requests
import sys

database_url = 'https://Photo-Flora-Size.firebaseio.com/'
TRACELIST = ['topMeasurements','sideMeasurements']
#database should have two collections: topCamera and sideCamera
#create a function to make sure these exist, if not should not continue with program and alert user


def get_database(DB_url):
    if requests.get(DB_url).status_code != 200:
        sys.exit("database not found")
    else:
        database = firebase.FirebaseApplication(DB_url, None)
        return database

database = get_database(database_url)
print(database.collections())


def get_FB_keys(doc_title, database):
    result_data = database.get(doc_title, None)
    return result_data, list(result_data)


def make_df(result_get, result_keys):
	# the return here should be a pd.DataFrame({date, value})
	# might need additional data cleaning functions see app.py in soft. eng. proj 1
	pass


def make_trace(traceName, dataframe):
    trace = go.Scatter(
        x=dataframe.day,
        y=dataframe.value,
        mode="lines+markers",
        name=traceName
    )
    return trace


# traces intended to be list: ["topCamera", "sideCamera"]
# width of plant and Height of plant respectively
def make_traces(traces, database):
    data = []
    for traceName in traces:
        result_data, result_keys = get_FB_keys(traceName, database)
        result_df = make_df(result_data, result_keys)
        trace = make_trace(traceName, result_df)
        data.append(trace)
    return data


def return_data_for_graph(database):
    data = make_traces(TRACELIST, database)
    return data


# def main():
#     app = dash.Dash()
#     database = get_database(database_url)
#     data = return_data_for_graph(database)
#     app.config.suppress_callback_exceptions = True
#     app.layout = html.Div([
#         dcc.Location(id='url', refresh=False),
#         html.Div(id='page-content')
#     ])

#     index_page = html.Div([
#         html.H1(children='Plant Measurement Data'),
#         html.Div(children='''By Andy Couto and Amanda Morrison'''),
#         html.Br(),
#         dcc.Link('Graph', href='/page-1'),
#         html.P('Graph of plant growth over time'),
#         html.Br()
#     ], style={
#                 'textAlign': 'center',
#                 'color': '#7FDBFF'
#             })

#     page_1_layout = html.Div(children=[
#         html.H1(children='Plant Growth Graph'),

#         html.Div(children='''
#             By Andy Couto and Amanda Morrison
#         '''),
#         dcc.Graph(
#             id='plant-growth-graph',
#             figure={
#                 'data': data,
#                 'layout': {
#                     'title': 'Plant Growth Over Time'
#                 }
#             }
#         ),
#         html.Div(id='page-1-content'),
#         html.Br(),
#         dcc.Link('Go back to home', href='/'),
#     ])


#     # Update the index
#     @app.callback(dash.dependencies.Output('page-content', 'children'),
#                   [dash.dependencies.Input('url', 'pathname')])
#     def display_page(pathname):
#         if pathname == '/page-1':
#             return page_1_layout
#         else:
#             return index_page


#     app.css.append_css({
#         'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
#     })

#     app.run_server(debug=True)


# if __name__ == '__main__':
#     main()