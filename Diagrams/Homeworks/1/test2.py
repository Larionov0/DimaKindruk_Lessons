from json import dumps
from plotly import graph_objs as go

buki = [
    {
        "тип": "казявка",
        "имя": "Бузявка",
        "кусючесть": 4
    },
    {
        "тип": "муравей",
        "имя": "Боровей",
        "кусючесть": 8
    },
    {
        "тип": "казявка",
        "имя": "Лизявка",
        "кусючесть": 3
    },
    {
        "тип": "казявка",
        "имя": "Жизявка",
        "кусючесть": 5
    },
    {
        "тип": "муравей",
        "имя": "Боверой",
        "кусючесть": 11
    },
    {
        "тип": "бабочка",
        "имя": "Аня",
        "кусючесть": 1
    },
    {
        "тип": "бабочка",
        "имя": "Ваня",
        "кусючесть": 0
    },
]


def build_diagram_with_buki(filename=buki):
    x = []
    y = []
    for buka in buki:
        x.append(buka['имя'])
        y.append(buka["кусючесть"])

    diag = go.Bar(x=x, y=y)
    fig = go.Figure(data=[diag])
    fig.write_html('planets.html', auto_open=True)


build_diagram_with_buki()
