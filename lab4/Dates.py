import datetime 

#1
current = datetime.datetime.now()
new = current - datetime.timedelta(days=5)
print(new.strftime("%Y-%m-%d"))

#2
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tommorow = today + datetime.timedelta(days=1)

print("Today", today.strftime("%Y-%m-%d"))
print("Yesterday", yesterday.strftime("%Y-%m-%d"))
print("Tommorow", tommorow.strftime("%Y-%m-%d"))

#3
now = datetime.datetime.now()
without = now.replace(microsecond=0)
print(without)

#4
current_date = datetime.datetime.today()
later_date = datetime.datetime.today()
diffirence = later_date - current_date
seconds = diffirence.total_seconds()
print(f"Diffirence between two date in seconds: {round(seconds,2)}")
