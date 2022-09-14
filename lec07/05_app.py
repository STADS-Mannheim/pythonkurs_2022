import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# schoeneres Design
import dash_bootstrap_components as dbc

# Datenpakete
import pandas as pd

# Graphen
import plotly.express as px

# importiere Datensatz
df = pd.read_pickle("lec07/data.pickle.gzip", compression="gzip")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])  # DARKLY

# 1.
# app.layout = dbc.Container(
#     children=[html.H1("Pythonkurs"), html.P("Hallo hier steht ein Text"),
#     dcc.Graph(figure=px.line(df,x="Meldedatum",y="AnzahlFall"))]
# )

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

# 2.
# app.layout = dbc.Container(
#     dbc.Row(
#         [
#             dbc.Col(
#                 [
#                     dbc.Row(html.H1("Corona-Dashboard")),
#                     dbc.Row(
#                         html.P(
#                             """
#         Beispielapp STADS / Uni Mannheim
#     """
#                         )
#                     ),
#                     dbc.Row(menu),
#                 ],
#                 width=3,
#             ),
#             dbc.Col(
#                 [
#                     html.H1("Pythonkurs"),
#                     html.P("Hallo hier steht ein Text"),
#                     dcc.Graph(figure=px.line(df, x="Meldedatum", y="AnzahlFall")),
#                 ]
#             ),
#         ]
#     )
# )

# 3.
# app.layout = dbc.Container(
#     dbc.Row(
#         [
#             dbc.Col(
#                 [
#                     dbc.Row(html.H1("Corona-Dashboard")),
#                     dbc.Row(
#                         html.P(
#                             """
#         Beispielapp STADS / Uni Mannheim
#     """
#                         )
#                     ),
#                     dbc.Row(menu),
#                 ],
#                 width=3,
#             ),
#             dbc.Col(
#                 [
#                     html.H1("Pythonkurs"),
#                     html.P("Hallo hier steht ein Text"),
#                     dcc.Graph(id="graph1"),
#                 ]
#             ),
#         ]
#     )
# )

# 5. 
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
                        dcc.Graph(id="graph1"),
                        dcc.Graph(id="graph2"),
                        dcc.Graph(id="abc"),
                    ],
                ),
            ]
        )
    ],
    fluid=True,
)

# 5.
def filter_geo(bundesland, landkreis):
    """
    Filtere Datensatz nach Bundeslaendern(Liste) und einem Landkreis, falls uebergeben.
    """
    df_temp = df
    if landkreis is None:
        landkreis = ""
    if len(bundesland) > 0:
        df_temp = df_temp[df_temp["Bundesland"].isin(bundesland)]
    if len(landkreis) > 0:
        df_temp = df_temp[df_temp["Landkreis"] == landkreis]
    return df_temp


# 4.
# def filter_geo(bundesland,landkreis):
#     df_temp = df[df["Bundesland"].isin(bundesland)]
#     df_temp = df_temp[df['Landkreis']==landkreis]
#     return df_temp

# 3.
# @app.callback(
#     Output("graph1", "figure"),
#     [Input("bundesland", "value"), Input("landkreis", "value")],
# )    # decorator
# def update_graph1(bundesland, landkreis):
#     df_temp = df  # Filter nah Bundseland und Landkreis
#     df_temp = df_temp.groupby("Meldedatum").agg("sum")["AnzahlFall"].reset_index()
#     return px.line(df_temp, x="Meldedatum", y="AnzahlFall")

# 4.
@app.callback(
    Output("graph1", "figure"),
    [Input("bundesland", "value"), Input("landkreis", "value")],
)  # decorator
def update_graph1(bundesland, landkreis):
    df_temp = filter_geo(bundesland, landkreis)
    df_temp = df_temp.groupby("Meldedatum").agg("sum")["AnzahlFall"].reset_index()
    return px.line(df_temp, x="Meldedatum", y="AnzahlFall")


@app.callback(
    Output(
        "graph2", "figure"
    ),  # wichtig: nur mit einer Funktion ein Objekt beschrieben als output
    [Input("bundesland", "value"), Input("landkreis", "value")],
)  # decorator
def update_graph2(bundesland, landkreis):
    df_temp = filter_geo(bundesland, landkreis)
    df_temp = df_temp.groupby(["Meldedatum", "Altersgruppe"]).agg("sum").reset_index()
    return px.line(df_temp, x="Meldedatum", y="AnzahlFall", color="Altersgruppe")


@app.callback(
    Output(
        "abc", "figure"
    ),  # wichtig: nur mit einer Funktion ein Objekt beschrieben als output
    [Input("bundesland", "value"), Input("landkreis", "value")],
)  # decorator
def update_graph_abc(bundesland, landkreis):
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
