# Run this app with `python leco08/03_app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Dash
# https://dash.plotly.com
import dash
import dash_core_components as dcc
import dash_html_components as html

# Inputs und Outputs für Callbacks
from dash.dependencies import Input, Output

# Dash Bootstrap Comonents
# https://dash-bootstrap-components.opensource.faculty.ai
import dash_bootstrap_components as dbc

# Grafiken mit Plotly Express
# https://plotly.com/python/plotly-express/
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Import Data Frame
df = pd.read_pickle("lec07/data.pickle.gzip", compression="gzip")

# Helper Functions
def relative_cases_age(df):
    """
    Calculate relative share of age groups of total share.
    """
    df["AnteilAlter"] = df["AnzahlFall"] / df["AnzahlFall"].sum()
    return df


def filter_geography(bundeslaender, landkreis):
    """
    Filter Data Frame for given Bundeslaender (List) and a Landkreis.
    """
    if landkreis is None:
        landkreis = ""
    df_temp = df
    if len(bundeslaender) > 0:
        df_temp = df[df["Bundesland"].isin(bundeslaender)]
    if len(landkreis) > 0:
        df_temp = df_temp[df["Landkreis"] == landkreis]
    return df_temp


# Menu, extracted from app layout
menu = dbc.FormGroup(
    [
        html.H3("Bundesländer"),
        dbc.Checklist(
            id="bundesland",
            options=[
                {"label": item, "value": item}
                for item in df["Bundesland"].unique().sort_values()
            ],
            value=[],
            switch=True,
        ),
        html.H3("Landkreis"),
        html.P("Wähle einen Landkreis aus."),
        dbc.Select(
            id="landkreis",
            options=[
                {"label": item, "value": item}
                for item in pd.Index([""]).append(
                    df["Landkreis"].unique().categories.sort_values()
                )
            ],
        ),
    ]
)

# App layout, must be defined for any Dash app
app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(children=html.H1("Corona-Dashboard")),
                        dbc.Row(
                            children=html.P(
                                """
        Beispielapp STADS / Uni Mannheim
    """
                            )
                        ),
                        dbc.Row(menu),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Row(dcc.Graph(id="graph1")),
                        dbc.Row(dcc.Graph(id="graph2")),
                        dbc.Row(dcc.Graph(id="graph3")),
                    ],
                ),
            ]
        )
    ],
    fluid=False,
)


# App Callbacks, werden immer in diesem Format definiert
# fuer einen Output darf maximal eine Funktion definiert werden
# Funktionsnamen voellig irrelevant
@app.callback(Output("landkreis", "options"), [Input("bundesland", "value")])
def update_landkreise(bundeslaender):
    df_temp = filter_geography(bundeslaender, [])
    return [
        {"label": item, "value": item}
        for item in pd.Index([""]).append(
            df_temp["Landkreis"].unique().categories.sort_values()
        )
    ]


@app.callback(
    Output("graph1", "figure"),
    [Input("bundesland", "value"), Input("landkreis", "value")],
)
def update_graph1(bundeslaender, landkreis):
    df_temp = filter_geography(bundeslaender, landkreis)
    return px.line(
        df_temp.groupby("Meldedatum").agg("sum")["AnzahlFall"].reset_index(),
        x="Meldedatum",
        y="AnzahlFall",
    )


@app.callback(
    Output("graph2", "figure"),
    [Input("bundesland", "value"), Input("landkreis", "value")],
)
def update_graph2(bundeslaender, landkreis):
    df_temp = filter_geography(bundeslaender, landkreis)
    return px.line(
        df_temp.groupby(["Meldedatum", "Altersgruppe"]).agg("sum").reset_index(),
        x="Meldedatum",
        y="AnzahlFall",
        color="Altersgruppe",
    )


@app.callback(
    Output("graph3", "figure"),
    [Input("bundesland", "value"), Input("landkreis", "value")],
)
def update_graph3(bundeslaender, landkreis):
    df_temp = filter_geography(bundeslaender, landkreis)
    df_temp = (
        df_temp.groupby(["Meldedatum", "Altersgruppe"])
        .sum()
        .reset_index()
        .groupby("Meldedatum")
        .apply(relative_cases_age)
        .reset_index()[["Meldedatum", "Altersgruppe", "AnteilAlter"]]
    )
    return px.line(
        df_temp,
        x="Meldedatum",
        y="AnteilAlter",
        color="Altersgruppe",
    )


if __name__ == "__main__":
    app.run_server(debug=True)
