from pybricks.tools import wait


def countdown(hub, count):
    if count > 0:
        if count < 10:
            for i in reversed(range(1, count + 1)):
                hub.display.char(str(i))
                wait(1000)
        elif count > 9 and count < 100:
            for i in reversed(range(1, count + 1)):
                hub.display.number(i)
                wait(1000)
        else:
            hub.display.text("error", 500, 250)
    else:
        hub.display.text("error", 500, 250)
