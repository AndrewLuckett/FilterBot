
import Config as cfg
from FileLoader import *

_logPath = ""
_used = False

def log(*lines):
    global _logPath, _used
    if not _used:
        _logPath = cfg.get("logPath", default = "Logs.log")
        _clearFile()
        _used = True

    _log(*lines)
    

def _log(*lines):
    if cfg.get("printlogs"):
        print(*lines, sep = "\n")

    with offsetOpen(_logPath, "a") as f:
        for line in lines:
            f.write(str(line))
            f.write("\n")


def _clearFile():
    with offsetOpen(_logPath, "w"):
        pass

