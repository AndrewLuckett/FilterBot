'''
Named global variable space
To be treated like a global static object
'''

_config = {}

def setConfigVar(key, value):
    global _config
    try:
        value = float(value)
    except:
        pass
    _config[key] = value


def getConfigVar(key, default = None, required = False):
    global _config
    if key not in _config:
        if required:
            raise Exception(f"Key ({key}) not found in config Dict")
        return default
    return _config.get(key)


def isConfigVar(key):
    global _config
    return key in _config.keys()


#Short names
def set(key, value):
    setConfigVar(key, value)
def get(key, default = None, required = False):
    return getConfigVar(key, default, required)
def contains(key):
    return isConfigVar(key)
