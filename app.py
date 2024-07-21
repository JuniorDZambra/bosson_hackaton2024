# Import the required libraries
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

# Import the pages
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Main
if __name__ == '__main__':
    app.run(debug=True)