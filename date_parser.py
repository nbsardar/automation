from datetime import datetime

now = datetime.now()

#print(now)

mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hr = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

print(mm + "/" + dd + "/" + yyyy + " " + hr + ":" + mi + ":" + ss)
