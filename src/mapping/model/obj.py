    
class Obj(object):
    def __init__(self, d):
        for k, v in d.items():
            if isinstance(k, (list, tuple)):
                setattr(self, k, [Obj(x) if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, Obj(v) if isinstance(v, dict) else v)
