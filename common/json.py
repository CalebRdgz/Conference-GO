from json import JSONEncoder


class ModelEncoder(JSONEncoder):
    properties = []

    def default(self, o):
        if isinstance(o, self.model):
            d = []
            for property in self.properties:
                d[property] = "foobar"
            return d
        return super().default(o)