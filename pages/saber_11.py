# Import packages
from dash import html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import requests

# Incorporate data
url = "https://www.datos.gov.co/resource/kgxf-xxbe.json?$limit=2000"
headers = {"Accept": "application/header"}
response = requests.get(url, headers=headers)
df = pd.DataFrame.from_dict(response.json())
df = df.sort_values('periodo', ascending=True)

# Data
description = {
    "count": "Número de estudiantes",
    "periodo": "Periodo de los resultados",
    "estu_tipodocumento": "Tipo de documento",
    "estu_consecutivo": "Identificador",
    "cole_area_ubicacion": "Ubicación de la sede",
    "cole_bilingue": "¿Es colegio bilingüe?",
    "cole_calendario": "Calendario del establecimiento",
    "cole_caracter": "Carácter del establecimiento",
    "cole_cod_dane_establecimiento": "Código DANE del establecimiento",
    "cole_cod_dane_sede": "Código DANE de la sede",
    "cole_cod_depto_ubicacion": "Departamento de la sede",
    "cole_cod_mcpio_ubicacion": "Código municipio de la sede",
    "cole_codigo_icfes": "Código ICFES del establecimiento",
    "cole_depto_ubicacion": "Departamento de la sede",
    "cole_genero": "Genero del establecimiento",
    "cole_jornada": "Jornada de la sede",
    "cole_mcpio_ubicacion": "Municipio de la sede",
    "cole_naturaleza": "Naturaleza del establecimiento",
    "cole_nombre_establecimiento": "Nombre del establecimiento",
    "cole_nombre_sede": "Nombre de la sede",
    "cole_sede_principal": "¿Es la sede principal?",
    "estu_cod_depto_presentacion": "Código del departamento de presentación del examen.",
    "estu_cod_mcpio_presentacion": "Código del municipio de presentación del examen.",
    "estu_cod_reside_depto": "Código del departamento de residencia del examinando",
    "estu_cod_reside_mcpio": "Código del municipio de residencia del examinando",
    "estu_depto_presentacion": "Departamento de presentación del examen.",
    "estu_depto_reside": "Departamento de residencia del examinando",
    "estu_estadoinvestigacion": "¿Permite usar sus datos para investigaciones?",
    "estu_estudiante": "S si es estudiante o N si es individual",
    "estu_fechanacimiento": "Fecha de nacimiento del examinando",
    "estu_genero": "Genero del examinando",
    "estu_mcpio_presentacion": "Municipio de presentación del examen.",
    "estu_mcpio_reside": "Municipio de residencia del examinando",
    "estu_nacionalidad": "Nacionalidad del examinando",
    "estu_pais_reside": "País de residencia del examinando",
    "estu_privado_libertad": "¿Es privado de la libertad?",
    "fami_cuartoshogar": "¿Cuántos cuartos tiene su hogar?",
    "fami_educacionmadre": "Nivel de estudios de la madre",
    "fami_educacionpadre": "Nivel de estudios de la padre",
    "fami_estratovivienda": "Estrato del examinando",
    "fami_personashogar": "¿Con cuantas personas vive?",
    "fami_tieneautomovil": "¿Tiene automóvil?",
    "fami_tienecomputador": "¿Tiene computador?",
    "fami_tieneinternet": "¿Tiene internet?",
    "fami_tienelavadora": "¿Tiene lavadora?",
    "desemp_ingles": "Desempeño inglés",
    "punt_ingles": "Promedio del puntaje de inglés",
    "punt_matematicas": "Promedio del puntaje de matemáticas",
    "punt_sociales_ciudadanas": "Promedio del puntaje de sociales y ciudadanas",
    "punt_c_naturales": "Promedio del puntaje ciencias naturales",
    "punt_lectura_critica": "Promedio del puntaje de lectura crítica",
    "punt_global": "Promedio del puntaje global",
}

# Initialize the app
register_page(__name__)

# Options
data_type_option_values = ['count', 'punt_global', 'punt_ingles', 'punt_matematicas', 'punt_sociales_ciudadanas', 'punt_c_naturales', 'punt_lectura_critica']
data_type_options = [{'label': description[i], 'value': i} for i in data_type_option_values]
all_options_values = [i for i in df.columns if i not in data_type_option_values]
all_options = [{'label': description[i], 'value': i} for i in all_options_values]
graph_type_options = ['Gráfico de barras', 'Gráfico de columnas', 'Gráfico circular', 'Diagrama de dispersión']

# App layout
layout = dbc.Container([
    html.Div([
            html.Div([
                html.H1([
                    html.Span("Dashboard de Saber 11°"),
                ]),
                html.P("Este dashboard permite visualizar los resultados de las pruebas Saber 11°."),
                ],
                style={
                    "vertical-alignment": "top",
                    "height": 200
            }),
            html.Div([
                html.Div([
                    html.H6('Dimensión:'),
                    dcc.Dropdown(
                        options=all_options,
                        value='periodo',
                        id='dropdown1',
                        clearable=False,
                        optionHeight=60
                    )
                ], style={'height': '7.5vh'}),
                html.Div([
                    html.H6('Datos de salida:'),
                    dcc.Dropdown(
                        options=data_type_options,
                        value='count',
                        id='dropdown3',
                        clearable=False,
                        optionHeight=60
                    )
                ], style={'height': '7.5vh'}),
                html.Div([
                    html.H6('Agrupación:'),
                    dcc.Dropdown(
                        id='dropdown2',
                        optionHeight=60
                    )
                ], style={'height': '7.5vh'}),
                html.Div([
                    html.H6('Filtro:'),
                    dcc.Dropdown(
                        id='filter_column',
                        multi=True,
                    )
                ], style={'height': '7.5vh'})
            ],
                style={
                    'margin-left': 15,
                    'margin-right': 15,
                    'margin-top': 30
                }
            ),
            html.Div([
                html.Div([
                    html.H6('Tipo de gráfica:'),
                    dbc.RadioItems(
                        id='graph_type',
                        inline=True,
                        value=graph_type_options[1],
                    )
                ],
                style={'width': 206}),
                html.Div(style={'width': 104})
              ],
              style={
                  'margin-left': 15,
                  'margin-right': 15,
                  'display': 'flex'
            }),
            html.Div(
              dcc.Link(html.Button("Regresar al Home"), href=r"/", refresh=True),
              style={
                  'marginLeft': 70,
                  'margin-bottom': 30,
                  'position': 'absolute',
                  'bottom': 0
              }
            )
        ],
        style={
            'position': 'fixed',
            'width': 375,
            'left': 0,
            'top': 0,
            'bottom': 0,
            'padding': '2rem 1rem',
            'border': '3px solid #ff901b',
    }),
    html.Div(
        children = [
            html.Div([
                    html.H2('Gráfica:'),
                    dcc.Graph(figure={}, responsive=True, id='graph', style={'height': '65vh'}),
                ],
                style={
                    "width": "120vh",
                    "height": "70vh",
                    'marginLeft': 'auto',
                    'marginRight': 'auto'
                },
            ),
            html.Div([
                    html.H2('Tabla:'),
                    dash_table.DataTable(data=df.to_dict('records'),
                                        sort_action='native',
                                        sort_mode='multi',
                                        virtualization=True,
                                        page_size=20
                    ),
                ],
                style={
                    "width": "120vh",
                    'marginLeft': 'auto',
                    'marginRight': 'auto'
                },
            )
        ],
        style={
            'width': '100%',
            'margin-top': 35,
            'margin-right': 35,
            'margin-left': 375,
            'margin-bottom': 35,
        })
    ],
    fluid=True,
    style={'display': 'flex'},
    className='lead'
)

# Callback to set the group options
@callback(
    Output('dropdown2', 'options'),
    Input('dropdown1', 'value'))
def set_options(selected_option):
    return [{'label': description[i], 'value': i} for i in all_options_values if i != selected_option]

# Callback to set the filter options
@callback(
    Output('filter_column', 'options'),
    Input('dropdown1', 'value'))
def set_filter_options(selected_option):
    return df[selected_option].unique()

# Callback to set the graph options
@callback(
    Output('graph_type', 'options'),
    Input('dropdown3', 'value'))
def set_graph_options(selected_column):
    if selected_column == 'count':
      return [{'label': html.Span([html.Img(src=f"../assets/{i}.png", height=20), html.Span(i, style={'font_size': 15, 'padding-left': 10})], style={'align-items': 'center', 'justify-content': 'center'}), 'value': i} for i in graph_type_options if i != 'Diagrama de dispersión']
    else:
      return [{'label': html.Span([html.Img(src=f"../assets/{i}.png", height=20), html.Span(i, style={'font_size': 15, 'padding-left': 10})], style={'align-items': 'center', 'justify-content': 'center'}), 'value': i} for i in graph_type_options]

# Callback to build the graph
@callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='dropdown1', component_property='value'),
    Input(component_id='dropdown2', component_property='value'),
    Input(component_id='filter_column', component_property='value'),
    Input(component_id='dropdown3', component_property='value'),
    Input(component_id='graph_type', component_property='value')
)
def build_graph(selected_option, group_option, filter_option, selected_column, selected_graph):
    if selected_column == 'count':
        selected_column = None
        histfunc = None
    else:
        histfunc = 'avg'
    if not filter_option:
        filter_option = df[selected_option].unique()
    if group_option is not None:
        color = group_option
        barmode = 'group'
    else:
        color = None
        barmode = None
    if selected_graph == 'Gráfico de barras':
        fig = px.histogram(df[df[selected_option].isin(filter_option)], y=selected_option, x=selected_column, orientation='h', histfunc=histfunc, color=color, barmode=barmode)
    elif selected_graph == 'Gráfico de columnas':
        fig = px.histogram(df[df[selected_option].isin(filter_option)], x=selected_option, y=selected_column, histfunc=histfunc, color=color, barmode=barmode)
    elif selected_graph == 'Gráfico circular':
        fig = px.pie(df[df[selected_option].isin(filter_option)], names=selected_option, values=selected_column)
    elif selected_graph == 'Diagrama de dispersión':
        fig = px.scatter(df[df[selected_option].isin(filter_option)], x=selected_option, y=selected_column)
    return fig
