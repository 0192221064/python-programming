import numpy as np
# Number of weekdays in March 2017
print("Number of weekdays in March 2017:",
      np.busday_count('2017-03', '2017-04'))

print("Number of Sunday in november 2020:",
      np.busday_count('2020-11', '2020-12',weekmask='Sun'))

# input year and month
yearMonth = '2017-05'
date = np.busday_offset(yearMonth, 0, roll='forward',weekmask='Mon')
# display date
print(date)
