import time

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

