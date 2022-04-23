from os import path as p
import Config as cfg

_pathOffset = ""
_used = False


def init():
    global _pathOffset, _used
    if not _used:
        _pathOffset = cfg.get("pathOffset", required = True)
        _used = True


def offsetOpen(path, *args, **kwargs):
    init()
    return open(getOffsetPath(path), *args, **kwargs)


def getOffsetPath(path):
    init()
    return _pathOffset + path


def getFullPath(path):
    path = getOffsetPath(path)
    return p.abspath(path)
