from json import dumps
import plotly.graph_objs as go


planets = ["Mars", "Bars", "Earth", "Wobby", "Planeta"]
satellits_counts = [0, 3, 1, 11, 5]

x = []
y = []
for planet in planets:
    x.append(planet)
for satellits_count in satellits_counts:
    y.append(satellits_count)

diag = go.Bar(x=x, y=y)
fig = go.Figure(data=[diag])
fig.write_html('planets.html', auto_open=True)