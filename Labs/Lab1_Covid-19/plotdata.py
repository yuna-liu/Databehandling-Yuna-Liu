import plotly_express as px

def time_series_plot(df, y_variables):
    for y_variable in y_variables:
        fig = px.line(df, x="Vecka", y=y_variable, color='Region',
                    symbol="Region", title=y_variables[y_variable])
        fig.show()
        fig.write_html(
            f"Visualiseringar/Q3.{y_variables[y_variable]}.html", auto_open=True)

def scatter_plot(df, y_variables, x):
    for y_variable in y_variables:
        fig = px.scatter(df, x=x, y=y_variable,
                 color="Region", size="Befolkning", size_max=70,
                 log_x=False, animation_frame="Vecka", title=f"{y_variables[y_variable]} vs {x}",
                 range_y=[0,df[y_variable].quantile(0.95)])
        fig.show()
        fig.write_html(f'Visualiseringar/Q3.{y_variables[y_variable]} vs {x}.html', auto_open=True)