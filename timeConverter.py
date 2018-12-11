import time

# while True:
c = time.gmtime()
print(c)
c.tm = c.tm_hour 


x = time.strftime("%a, %d %b %Y %H:%M:%S CET", time.gmtime())
print(x)