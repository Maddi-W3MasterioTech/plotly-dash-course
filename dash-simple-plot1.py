import dash
import dash_html_components as html 
import dash_core_components as dcc 
import plotly.express as px 

df = px.data.iris()
fig = px.scatter(df,x="sepal_width",y="sepal_length",size="petal_length",color="species")

fig.update_layout(
    plot_bgcolor="#252262",
    font_color="rgb(122,3,120)"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("hello from dash app with styling",style=   {"color":"#29B1D3",
        "textAlign":"center",
    }
    
    ),
    dcc.Graph(figure=fig,style={"height":400}
    ),
],
className="dash-first-div"
)

if __name__ == "__main__":
    app.run_server(debug=True)