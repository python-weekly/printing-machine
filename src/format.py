from data.data import FORMAT


class FormatItem:
    def __init__(self, name, ink, paper, price):
        self.name = name
        self.price = price
        self.ink = ink
        self.paper = paper


class Format:
    def __init__(self):
        self.formats = []
        self.format_names = FORMAT.keys()

        for format_name in self.format_names:
            self.formats.append(
                FormatItem(
                    name=format_name,
                    price=FORMAT[format_name]['price'],
                    ink=FORMAT[format_name]['materials']['ink'],
                    paper=FORMAT[format_name]['materials']['paper'],
                )
            )

    @property
    def print_format(self):
        return tuple(self.format_names)

    def find_format(self, format_name):
        for format in self.formats:
            if format.name == format_name:
                return format
        print(
            f'Invalid Format: The only available formats are {self.print_format}')
