class MagicPen:
    colors = {
        'хз': '\033[95m',
        'блакитний': '\033[94m',
        'OKCYAN': '\033[36m',
        'зелений': '\033[92m',
        'жовтий': '\033[93m'
    }
    endcolor = '\033[0m'

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def get_color_code(self):
        if self.color in MagicPen.colors:
            return self.colors[self.color]
        else:
            return '??? color'

    def write(self, text):
        if self.type == 1:
            ready_text = text.upper()

        elif self.type == 2:
            ready_text = text

        elif self.type == 3:
            ready_text = text.lower()

        print(self.get_color_code() + ready_text + self.endcolor)


pen = MagicPen('Краснуша', 'жовтий', 3)
pen.write('этот текст был написан Краснушей')
pen2 = MagicPen('Блакуща', "блакитний", 1)
pen2.write('Я люблю php')
