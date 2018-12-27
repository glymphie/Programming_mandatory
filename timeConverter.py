import time
import tkinter as tk
# while True:

t = time.time() + 60*60
c = time.gmtime(t)
print(c)


x = time.strftime("%a, %d %b %Y %H:%M:%S CET", c)
print(x)

now = time.strftime("%H:%M:%S", c)
print(now)


acttime = time.asctime(time.localtime())
print(acttime)
acttime = acttime.split()
print(acttime)

tkWindow = tk.Tk()
tkWindow.geometry("250x170")
tkWindow.title("Time")

tfloor1 = tk.Label(tkWindow,text=now)

tfloor1.grid(column=1, row=1)

while True:
    t = time.time() + 60*60
    c = time.gmtime(t)
    now = time.strftime("%H:%M:%S", c)
    tfloor1 = tk.Label(tkWindow,text=now)
    tk.mainloop()