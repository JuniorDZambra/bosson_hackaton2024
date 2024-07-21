# Import the required libraries
from dash import register_page, html, dcc

# Register the page
register_page(__name__, path='/')

# Define the layout
layout = html.Div(
  children=[
    html.Tbody(
      children=[
        html.Header(
          children=[
            html.Img(src=r"../assets/LogoB.png", alt="Logo de Boson", className="logo"),
            html.H1("Visualización de Bosson"),
          ]
        ),
        html.Div(className="sub", children=[html.H2("Visualización interactiva para análisis de desempeño escolar en Colombia")]),
        html.Div(
          className="button-container",
          children=[
            html.Div(
              className="button",
              children=[
                html.H2("Saber 11°"),
                html.H4(
                  "Es una evaluación estandarizada administrada por el Instituto Colombiano para la Evaluación de la Educación (ICFES). Este examen tiene como objetivo medir la calidad de la educación impartida a los estudiantes que culminan el nivel de educación media en Colombia. La prueba evalúa cinco áreas fundamentales del conocimiento: Lectura Crítica, Matemáticas, Sociales y Ciudadanas, Ciencias Naturales, e Inglés."
                ),
                dcc.Link(html.Button("Visualizar Datos"), href=r"saber-11", refresh=True),
              ],
            ),
            html.Div(
              className="button",
              children=[
                html.H2("Saber Pro"),
                html.H4(
                  "Es una evaluación estandarizada dirigida a los estudiantes que están próximos a culminar sus programas de educación superior en Colombia. Administrado por el ICFES, este examen tiene como propósito medir las competencias genéricas y específicas adquiridas durante la formación universitaria. Las competencias evaluadas incluyen habilidades de comunicación, razonamiento cuantitativo, lectura crítica, competencias ciudadanas, e inglés, además de competencias específicas relacionadas con el campo de estudio del estudiante."
                ),
                dcc.Link(html.Button("Visualizar Datos"), href=r"saber-pro", refresh=True),
              ],
            ),
          ],
        ),
        html.Footer(
          children=[
            html.Div(
              children=[
                html.H2("Patrocinadores"),
                html.Img(src=r"../assets/IMG_4141.PNG", alt="Patrocinador 1"),
                html.Img(src=r"../assets/IMG_4142.PNG", alt="Patrocinador 2"),
                html.Img(src=r"../assets/IMG_4143.PNG", alt="Patrocinador 3"),
                html.Img(src=r"../assets/IMG_4144.PNG", alt="Patrocinador 4"),
                html.Img(src=r"../assets/IMG_4145.PNG", alt="Patrocinador 5"),
                html.Img(src=r"../assets/IMG_4146.PNG", alt="Patrocinador 6"),
                html.Img(src=r"../assets/IMG_4147.PNG", alt="Patrocinador 7")
              ], className="sponsors"
            )
          ]
        ),
      ]
    ),
  ]
)
