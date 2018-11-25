from datetime import datetime ,timedelta
now = datetime.now()
print(now)

dt = datetime(2014, 2, 2, 2, 2, 2)
print(dt)

print(dt.timestamp())
print(now.timestamp())

print(datetime.fromtimestamp(dt.timestamp()))

print(now.strftime('%a,%b %d %H:%M'))

# datetime(2013,3,3,3,3)

print(now+timedelta(hours=10))