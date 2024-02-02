import datetime

# Get the date of today, yesterday, and the day before yesterday
# data format: yyyy-mm-dd
YESTERDAY = datetime.date.today() - datetime.timedelta(days=1)
YESTERDAY = YESTERDAY.strftime('%Y-%m-%d')
DAY_BEFORE_YESTERDAY = datetime.date.today() - datetime.timedelta(days=2)
DAY_BEFORE_YESTERDAY = DAY_BEFORE_YESTERDAY.strftime('%Y-%m-%d')


THRESHOLD = 1
