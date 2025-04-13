from datetime import datetime, timedelta
import random
def random_datetime(start_date, end_date):
    delta=end_date-start_date
    random_seconds=random.randint(0, int(delta.total_seconds()))
    return start_date+timedelta(seconds=random_seconds)
start_date=datetime(2020, 1, 1)
end_date=datetime(2025, 12, 31)
random_time=random_datetime(start_date, end_date)
formatted_time=random_time.strftime("%Y-%m-%d %H:%M:%S")
print("Random Date and Time: ", formatted_time)