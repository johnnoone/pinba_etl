from collections import defaultdict, OrderedDict

GAUGES = defaultdict(list)
COLLECTORS = OrderedDict()


class Gauge:

    def __init__(self,
                 provider,
                 name=None,
                 values=None,
                 cardinality=None):
        self.provider = provider
        self.name = name
        self.cardinality = cardinality
        self.values = values
        GAUGES.setdefault(provider, []).append(self)


class Collector:

    def __init__(self, name, query, gauges=None):
        self.query = query
        self.name = name
        gauges = gauges or []
        for gauge in gauges:
            GAUGES[self.name].append(gauge)
        COLLECTORS[name] = self

    @property
    def stmt(self):
        obj = self.query.stmt
        obj = ' '.join(line.strip().strip() for line in obj.split('\n'))
        return obj.rstrip(';')

    __str__ = stmt

    @property
    def gauges(self):
        for gauge in GAUGES[self.name]:
            yield gauge

    __iter__ = gauges

    def has_gauges(self):
        for g in self.gauges:
            return True
        return False
