import dash
import dash_html_components as html 
import dash_core_components as dcc 
import plotly.express as px 

df = px.data.iris()
fig = px.scatter(df,x="sepal_width",y="sepal_length",size="petal_length",color="species")

app = dash.Dash()

app.layout = html.Div([
    html.H1("hello from dash app"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server()