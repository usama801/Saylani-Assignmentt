from datetime import datetime

nowdt = datetime.now()
date = nowdt.strftime(" %d-%m-%Y")
time = nowdt.strftime(" %H:%M:%S")
print("Date:",date)
print("Time:",time)
