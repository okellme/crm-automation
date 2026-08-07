from datetime import datetime

today = datetime.now()
print(today)

today_string = today.strftime("%Y-%m-%d")
print(today_string)