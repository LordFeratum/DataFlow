class Promise:
    @staticmethod
    def resolve(data):
        return data

    @staticmethod
    def as_list(data):
        return list(data)

    @staticmethod
    def as_int(data):
        return int(data)

    @staticmethod
    def as_float(data):
        return float(data)

    @staticmethod
    def for_each(callback):
        def _for_each(data):
            for datum in data:
                callback(datum)
        return _for_each
