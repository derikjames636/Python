from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current_time.strftime("%B-%d-%A %I:%M:%s:%p IST")
print(format2)
format3=current_time.strftime('%d-%m-%Y')
print(format3)