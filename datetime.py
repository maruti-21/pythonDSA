import datetime

date = datetime.datetime.now()

print("Its now: {:%d/%m/%Y %H:%M:%S}".format(date))