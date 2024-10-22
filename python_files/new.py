import imp
import time
import datetime
import os
x = datetime.datetime.now()
print(x.strftime("%c"))
path = os.getcwd()
print(path)
print(type(path))
