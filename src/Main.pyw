
import Config as cfg
from Logger import log
from datetime import datetime
from FileLoader import *


def loadConfig(path, conf = {}, badcom = []):
    import csv
    with offsetOpen(path) as f:
        r = csv.reader(f, delimiter=' ', skipinitialspace = True)
        for e in r:
            if len(e) == 0: continue # Empty lines
            if len(e) != 2: # Lines that arent 2 elements
                badcom.append(f"\t{path} {e}")
                continue
            conf[e[0]] = e[1]
    return conf, badcom


def main():
    cfg.setConfigVar("pathOffset", "../")
    # back out of src folder

    # Load configs
    conf, badcommands = loadConfig("rsc/default.cfg")
    conf, badcommands = loadConfig("settings.cfg", conf, badcommands)
    for k, v in conf.items():
        cfg.setConfigVar(k, v)
    # Store bad commands so we can log start time first

    # Config data is needed to log properly
    theTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log(f"Program started on {theTime}")

    if len(badcommands):
        log(f"Bad config command(s)", *badcommands)

    try:
        bootup()
    except Exception as e:
        import traceback
        log("Fatal Error", "\t" + str(e))
        log("", traceback.format_exc())
    else:
        theTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log(f"Program closed normally on {theTime}")


def bootup():
    import Bot
    Bot.start()


if __name__ == "__main__":
    main()

