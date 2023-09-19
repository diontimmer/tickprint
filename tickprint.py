# start a thread that prints input variables every set interval
import threading


def tickprint(object, attribute, interval):
    """Print args every interval seconds"""

    def printit():
        threading.Timer(interval, printit).start()
        try:
            attr = getattr(object, attribute)
            print(attr)
        except:
            print("Error printing vars..")

    printit()
