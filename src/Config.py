'''
Named global variable space
To be treated like a global static object
'''

_config = {}

def setConfigVar(key, value):
    global _config
    if key in _config:
        assert False, f"Cannot override config vars ({key})"
        return

    try:
        value = float(value)
    except:
        pass
    _config[key] = value


def getConfigVar(key, default = None, required = False):
    global _config
    if key not in _config and required:
        raise Exception(f"Key ({key}) not found in config Dict")

    return _config.get(key, default)


def isConfigVar(key):
    global _config
    return key in _config


#Short names
def set(key, value):
    setConfigVar(key, value)
def get(key, default = None, required = False):
    return getConfigVar(key, default, required)
def contains(key):
    return isConfigVar(key)
