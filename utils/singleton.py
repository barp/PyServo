
def singleton(_class):
    instances = {}
    def getInstance(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)
        return instances[_class]
    return getInstance
