from datetime import *
y = int(input())
x = datetime.now() + timedelta (days=y)
print(x.strftime("%A, %B %d, %Y"))
