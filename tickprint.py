import threading
import time


def tickprint(object, attribute, interval):
    """Print attribute of object every interval seconds"""

    def printit():
        while True:
            try:
                attr = getattr(object, attribute)
                print(attr)
            except Exception as e:
                print(f"Error printing vars: {e}")
            time.sleep(interval)

    thread = threading.Thread(target=printit)
    thread.daemon = (
        True  # Daemonize the thread so that it will exit when the main program exits
    )
    thread.start()
