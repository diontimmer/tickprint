import threading, time


def tickprint(object, attribute, interval):
    def p():
        while True:
            print(getattr(object, attribute, "Error"))
            time.sleep(interval)

    threading.Thread(target=p, daemon=True).start()
