from json import dumps
import plotly.graph_objs as go


def get_kidnappers(filename='kidnappers.csv'):
    """
    :param filename: str
    :return: [{},{},{},{}]    (список із словників-викрадачів)
    """
    kidnappers_list = []
    file = open(filename, 'rt', encoding='utf-8')
    headers = file.readline()
    for line in file:
        line_list = line.rstrip().split(', ')  # ['Боб', 'Булька', 'Бобові', '27', 'літаюча тарілка; засмоктувач; люлька']
        kidnapper_dict = {
            'ім`я': line_list[0],
            'планета': line_list[1],
            'раса': line_list[2],
            'викрадення': int(line_list[3]),
            'девайси': line_list[4].split('; ')
        }
        kidnappers_list.append(kidnapper_dict)
    return kidnappers_list


def build_diagram_with_planets():
    kidnappers = get_kidnappers()
    planets_dict = {}
    for kidnapper in kidnappers:
        if kidnapper['планета'] in planets_dict:
            planets_dict[kidnapper['планета']] += kidnapper['викрадення']
        else:
            planets_dict[kidnapper['планета']] = kidnapper['викрадення']

    x = []
    y = []
    for planet in planets_dict:
        x.append(planet)
        y.append(planets_dict[planet])

    diag = go.Bar(x=x, y=y)
    fig = go.Figure(data=[diag])
    fig.write_html('planets.html', auto_open=True)


def build_devices_diagram():
    kidnappers = get_kidnappers()
    # print(dumps(kidnappers, indent=4, ensure_ascii=False))
    devices_counts = {}

    for kidnapper in kidnappers:
        for device in kidnapper['девайси']:
            if device in devices_counts:
                devices_counts[device] += 1
            else:
                devices_counts[device] = 1

    x = []
    y = []
    for device in devices_counts:
        x.append(device)
        y.append(devices_counts[device])

    # diag = go.Pie(labels=x, values=y)
    parallel_sort(y, x)
    diag = go.Bar(x=x, y=y)
    fig = go.Figure(data=[diag])
    fig.write_html('devices.html', auto_open=True)


def parallel_sort(lst1, lst2):
    ogr = len(lst1) - 1
    while ogr > 0:
        i = 0
        while i < ogr:
            if lst1[i] < lst1[i+1]:
                lst1[i], lst1[i + 1] = lst1[i + 1], lst1[i]
                lst2[i], lst2[i + 1] = lst2[i + 1], lst2[i]
            i += 1
        ogr -= 1


build_devices_diagram()
