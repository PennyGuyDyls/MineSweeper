from pynput.mouse import Listener

mx=0
my=0
click=0
def on_click(x, y, button, pressed):
    global mx
    global my
    global click
    if pressed:
        click=1
        mx = x
        my = y

listener = Listener(on_click=on_click)
listener.start()



while True:
    if click:
        print(mx,my)
        click = False
