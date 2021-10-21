import plotly_express as px

gapminder = px.data.gapminder()

fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp",
                 size="pop", color="country", size_max=70, 
                 log_x=True, animation_frame="year", title="Gapminder",
                 range_x =[100, 100000], range_y=[25,90])
fig.show()
