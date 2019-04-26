import datetime
import time


#dirpath_time = datetime.strftime().weekday()
dirpath_time = datetime.datetime.strptime('20190430', "%Y%m%d").strftime("%w")
print(dirpath_time)