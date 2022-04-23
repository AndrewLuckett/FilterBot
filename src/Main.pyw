
import Config as cfg
from Logger import log
from datetime import datetime
from FileLoader import *


def loadConfig(path):
    import csv
    badcommands = []
    with offsetOpen(path) as f:
        r = csv.reader(f, delimiter=' ', skipinitialspace = True)
        for e in r:
            if len(e) == 0: continue # Empty lines
            if len(e) != 2: # Lines that arent 2 elements
                badcommands.append(f"\t{e}")
                continue
            try:
                e[1] = float(e[1])
            except:
                pass
            cfg.setConfigVar(*e)
    return {path: badcommands}


def main():
    cfg.setConfigVar("pathOffset", "../")
    # back out of src folder

    # Load configs
    badcommands = {}
    badcommands.update(loadConfig("rsc/default.cfg"))
    badcommands.update(loadConfig("settings.cfg"))
    # Store bad commands so we can log start time first

    theTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log(f"Program started on {theTime}")

    for path, badcom in badcommands.items():
        if len(badcom):
            log(f"Bad config command(s) in {path}", *badcom)

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

