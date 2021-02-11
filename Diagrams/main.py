from plotly import graph_objs as go


def build_histogram():
    names = ['Bob', 'Alex', 'Alan', 'Alyona', 'Katia']
    marks = [9, 4, 11, 10, 9]
    diag = go.Bar(x=names, y=marks)
    fig = go.Figure(data=[diag])
    fig.write_html(file='diag.html', auto_open=True)


def build_pie():
    names = ['Bob', 'Alex', 'Alan', 'Alyona', 'Katia']
    marks = [9, 4, 11, 10, 9]
    diag = go.Pie(labels=names, values=marks)
    fig = go.Figure(data=[diag])
    fig.write_html('pie_diag.html', auto_open=True)


def y(x):
    return x ** 2


def build_line_graphic():
    x_list = []
    y_list = []
    x = -10
    while x < 10:
        x_list.append(x)
        y_list.append(y(x))
        x += 1

    diag = go.Scatter(x=x_list, y=y_list)
    fig = go.Figure(data=[diag])
    fig.write_html('function.html', auto_open=True)


build_line_graphic()
