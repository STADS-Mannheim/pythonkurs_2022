import dash
from dash.dependencies import Output
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# schönere Designs
import dash_bootstrap_components as dbc

# Datenpaket
import pandas as pd

# Graphen
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.YETI])

# importiere Datensatz
df = pd.read_pickle("lec07/data.pickle.gzip", compression="gzip")

menu = dbc.FormGroup(
    [
        html.H3("Bundeslaender"),
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
        html.P("Wähle einen Landkreis aus"),
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

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(html.H1("Corona-Dashboard")),
                        dbc.Row(html.P("Beispielapp STADS / Uni Mannheim")),
                        dbc.Row(menu),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        html.H1("Pythonkurs"),
                        html.P("Hallo, hier steht ein Text"),
                        dcc.Graph(id="graph1"),
                        dcc.Graph(id="graph2"),
                        dcc.Graph(id="stads"),
                    ]
                ),
            ]
        ),
    ],
    fluid=False,
)


def filter_geo(bundesland, landkreis):
    """
    Filtere Datensatz nach Bundesland(Liste) und einem Lankreis, falls übergeben.
    """
    df_temp = df
    if landkreis is None:
        landkreis = ""
    if len(bundesland) > 0:
        df_temp = df[df["Bundesland"].isin(bundesland)]
    if len(landkreis) > 0:
        df_temp = df_temp[df_temp["Landkreis"] == landkreis]
    return df_temp


@app.callback(
    Output("graph1", "figure"),
    [Input("bundesland", "value"), Input("landkreis", "value")],
)
def update_graph1(bundesland, landkreis):
    df_temp = filter_geo(bundesland, landkreis)
    df_temp = df_temp.groupby("Meldedatum").agg("sum")["AnzahlFall"].reset_index()
    return px.line(df_temp, x="Meldedatum", y="AnzahlFall")


@app.callback(
    Output("graph2", "figure"),  # wichtig: nur mit einer Funktion ein Objekt als Output
    [Input("bundesland", "value"), Input("landkreis", "value")],
)
def update_graph2(bundesland, landkreis):
    df_temp = filter_geo(bundesland, landkreis)
    df_temp = df_temp.groupby(["Meldedatum", "Altersgruppe"]).agg("sum").reset_index()
    return px.line(df_temp, x="Meldedatum", y="AnzahlFall", color="Altersgruppe")


@app.callback(
    Output("stads", "figure"),  # wichtig: nur mit einer Funktion ein Objekt als Output
    [Input("bundesland", "value"), Input("landkreis", "value")],
)
def update_graph_stads(bundesland, landkreis):
    def relative_cases_age(df):
        df["AnteilAlter"] = df["AnzahlFall"] / df["AnzahlFall"].sum()
        return df

    df_temp = filter_geo(bundesland, landkreis)
    df_temp = (
        df_temp.groupby(["Meldedatum", "Altersgruppe"])
        .agg("sum")
        .reset_index()
        .groupby("Meldedatum")
        .apply(relative_cases_age)
        .reset_index()
    )
    return px.line(df_temp, x="Meldedatum", y="AnteilAlter", color="Altersgruppe")


if __name__ == "__main__":
    app.run_server(debug=True)
