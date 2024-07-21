# Import packages
from dash import html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import requests

# Incorporate data
url = "https://www.datos.gov.co/resource/u37r-hjmu.json?$limit=2000"
headers = {"Accept": "application/header"}
response = requests.get(url, headers=headers)
df = pd.DataFrame.from_dict(response.json())
df = df.sort_values('periodo', ascending=True)

# Data
description = {
    "count": "Número de estudiantes",
    "periodo": "Periodo de los resultados",
    "estu_consecutivo": "Identificador del examinando",
    "estu_tipodocumento": "Tipo de documento",
    "estu_pais_reside": "País de residencia del examinando",
    "estu_cod_reside_depto": "Código Departamento de residencia del examinando",
    "estu_depto_reside": "Departamento de residencia del examinando",
    "estu_cod_reside_mcpio": "Código del municipio donde reside",
    "estu_mcpio_reside": "Municipio donde reside el examinando",
    "estu_coddane_cole_termino": "Código Dane del Colegio donde se graduó",
    "estu_cod_cole_mcpio_termino": "Municipio donde termino bachillerato",
    "estu_cod_depto_presentacion": "Código Departamento de Presentación del examen",
    "inst_cod_institucion" : "Código de la institución educación Superior",
    "inst_nombre_institucion": "Nombre Instutición de Educación Superior",
    "inst_caracter_academico" : "Carácter Académico Institución",
    "estu_nucleo_pregrado": "Núcleo asociado al pregrado que estudia",
    "estu_inst_departamento": "Departamento de la Institución Educación Superior",
    "estu_inst_codmunicipio": "Código del municipio de la Institución Educación Superior",
    "estu_inst_municipio" :"Municipio de la Institución Educación Superior",
    "estu_prgm_academico": "Programa académico al que pertenece",
    "estu_prgm_departamento": "Departamento del programa académico.",
    "estu_prgm_codmunicipio": "Código del municipio del programa académico",
    "estu_prgm_municipio" : "Municipio del programa académico.",
    "estu_nivel_prgm_academico": "Nivel del programa académico",
    "estu_metodo_prgm" : "Metodología del programa académico",
    "estu_valormatriculauniversidad" : "Valor matricula de la universidad",
    "estu_depto_presentacion": "Departamento de Presentación del examen.",
    "estu_cod_mcpio_presentacion": "Código de Municipio de Presentación del examen.",
    "estu_mcpio_presentacion": "Municipio de Presentación del examen.",
    "estu_pagomatriculabeca" : "¿Paga usted mismo su matricula?",
    "estu_pagomatriculacredito": "¿Tiene crédito para pagar su matricula?",
    "estu_horassemanatrabaja": "¿Cuántas horas a las semana trabaja?",
    "estu_snies_prgmacademico" : "Código Snies del Programa Académico",
    "estu_privado_libertad": "¿Es privado de la libertad?",
    "estu_nacionalidad": "Nacionalidad del examinando",
    "estu_estudiante": "S si es estudiante o N si es individual",
    "estu_genero": "Genero del examinando",
    "estu_cole_termino": "Colegio donde termino bachillerato",
    "estu_pagomatriculapadres": "¿Sus padres pagan su matricula?",
    "estu_estadoinvestigacion": "¿Permite publicar la investigación?",
    "estu_fechanacimiento": "Fecha de nacimiento del examinando",
    "estu_pagomatriculapropio" : "¿Paga usted mismo su matricula?",
    "estu_tipodocumentosb11" : "Tipo de documento con el que presento Saber 11",
    "fami_educacionpadre": "Nivel de estudios del padre",
    "fami_tieneautomovil" : "¿Tiene automóvil?",
    "fami_tienelavadora" : "¿Tiene lavadora?",
    "fami_estratovivienda" : "Estrato del examinando",
    "fami_tienecomputador": "¿Tiene computador?",
    "fami_tieneinternet" : "¿Tiene internet?",
    "fami_educacionmadre" : "Nivel de estudios de la madre",
    "inst_origen": "Tipo de Institución en la que Estudia",
    "mod_razona_cuantitat_punt": "Promedio del Puntaje Modulo Razonamiento Cuantitativo",
    "mod_comuni_escrita_punt": "Promedio del Puntaje Modulo Comunicación Escrita",
    "mod_comuni_escrita_desem" : "Desempeño Modulo comunicación escrita",
    "mod_ingles_desem": "Desempeño modulo de Inglés",
    "mod_lectura_critica_punt": "Promedio del Puntaje Modulo Lectura Crítica",
    "mod_ingles_punt": "Promedio del Puntaje Modulo Inglés",
    "mod_competen_ciudada_punt": "Promedio del Puntaje Modulo Competencias Ciudadanas"
}

# Register the page
register_page(__name__)

# Options
data_type_option_values = ['count', 'mod_ingles_punt', 'mod_razona_cuantitat_punt', 'mod_competen_ciudada_punt', 'mod_comuni_escrita_punt', 'mod_lectura_critica_punt']
data_type_options = [{'label': description[i], 'value': i} for i in data_type_option_values]
all_options_values = [i for i in df.columns if i not in data_type_option_values]
all_options = [{'label': description[i], 'value': i} for i in all_options_values]
graph_type_options = ['Gráfico de barras', 'Gráfico de columnas', 'Gráfico circular', 'Diagrama de dispersión']

# App layout
layout = dbc.Container([
    html.Div([
            html.Div([
                html.H1([
                    html.Span("Dashboard de Saber Pro"),
                ]),
                html.P("Este dashboard permite visualizar los resultados de las pruebas Saber Pro."),
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
                        id='dropdown1_pro',
                        clearable=False,
                        optionHeight=60
                    )
                ], style={'height': '7.5vh'}),
                html.Div([
                    html.H6('Datos de salida:'),
                    dcc.Dropdown(
                        options=data_type_options,
                        value='count',
                        id='dropdown3_pro',
                        clearable=False,
                        optionHeight=60
                    )
                ], style={'height': '7.5vh'}),
                html.Div([
                    html.H6('Agrupación:'),
                    dcc.Dropdown(
                        id='dropdown2_pro',
                        optionHeight=60
                    )
                ], style={'height': '7.5vh'}),
                html.Div([
                    html.H6('Filtro:'),
                    dcc.Dropdown(
                        id='filter_column_pro',
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
                        id='graph_type_pro',
                        inline=True,
                        value=graph_type_options[1],
                    )
                ],
                style={'width': 206}),
              ],
              style={
                  'margin-left': 15,
                  'margin-right': 15,
                  'display': 'flex',
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
            'border': '3px solid #20e280',
    }),
    html.Div(
        children = [
            html.Div([
                    html.H2('Gráfica:'),
                    dcc.Graph(figure={}, responsive=True, id='graph_pro', style={'height': '65vh'}),
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
            "display": "inline-block"
        })
    ],
    fluid=True,
    style={'display': 'flex'},
    className='lead'
)

# Callback to set the group options
@callback(
    Output('dropdown2_pro', 'options'),
    Input('dropdown1_pro', 'value'))
def set_options(selected_option):
    return [{'label': description[i], 'value': i} for i in all_options_values if i != selected_option]

# Callback to set the filter options
@callback(
    Output('filter_column_pro', 'options'),
    Input('dropdown1_pro', 'value'))
def set_filter_options(selected_option):
    return df[selected_option].unique()

# Callback to set the graph options
@callback(
    Output('graph_type_pro', 'options'),
    Input('dropdown3_pro', 'value'))
def set_graph_options(selected_column):
    if selected_column == 'count':
      return [{'label': html.Span([html.Img(src=f"../assets/{i}.png", height=20), html.Span(i, style={'font_size': 15, 'padding-left': 10})], style={'align-items': 'center', 'justify-content': 'center'}), 'value': i} for i in graph_type_options if i != 'Diagrama de dispersión']
    else:
      return [{'label': html.Span([html.Img(src=f"../assets/{i}.png", height=20), html.Span(i, style={'font_size': 15, 'padding-left': 10})], style={'align-items': 'center', 'justify-content': 'center'}), 'value': i} for i in graph_type_options]

# Callback to build the graph
@callback(
    Output(component_id='graph_pro', component_property='figure'),
    Input(component_id='dropdown1_pro', component_property='value'),
    Input(component_id='dropdown2_pro', component_property='value'),
    Input(component_id='filter_column_pro', component_property='value'),
    Input(component_id='dropdown3_pro', component_property='value'),
    Input(component_id='graph_type_pro', component_property='value')
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
