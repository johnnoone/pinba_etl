
class Gauge:

    def __init__(self, name=None, cardinality=None, values=None):
        self.name = name
        self.cardinality = cardinality
        self.values = values


class Collector:

    def __init__(self, name, query, gauges=None):
        self.query = query
        self.name = name
        self.gauges = gauges or []

    @property
    def stmt(self):
        obj = self.query.stmt
        obj = ' '.join(line.strip().strip() for line in obj.split('\n'))
        return obj.rstrip(';')

    __str__ = stmt

    __iter__ = lambda x: iter(x.gauges)

    def has_gauges(self):
        for g in self.gauges:
            return True
        return False
