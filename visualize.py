#!/usr/bin/env python:w


from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.read_csv('data/mes_idf_horaire_no2.csv', index_col='id')

# qualif_value = {'Mauvais': 0,
#                'Médiocre': 1,
#                'Moyen': 2,
#                'Bon': 3,
#                'Très bon': 4}

# df['qualif_value'] = df['qualif'].map(qualif_value)
print(df.columns)
all_dims = df.columns

# App layout
app.layout = html.Div([

    html.H1("Air Paris Data Visualization", style={'text-align': 'center'}),

    dcc.Dropdown(id="dropdown",
                 options=[{"label": x, "value": x}
                          for x in all_dims],
                 value=all_dims[[-5, -8]],
                 multi=True,
                 style={'width': "40%"}
                 ),

    dcc.Graph(id='AirParif', style={'height': "90vh"})

])


# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='AirParif', component_property='figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_bar_chart(dim):
    # Plotly Express
    fig = px.scatter_matrix(
        data_frame=df,
        dimensions=dim,
        color='nom_com',
        template='plotly_dark'
    )
    return fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
