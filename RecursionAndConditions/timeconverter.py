import time
import math

time_since_epoch_seconds = time.time()

time_since_epoch_minutes = time_since_epoch_seconds / 60
time_since_epoch_hours = time_since_epoch_minutes / 60
time_since_epoch_days = time_since_epoch_hours / 24
time_since_epoch_years = time_since_epoch_days / 365

seconds = math.floor(time_since_epoch_seconds % 60)
minutes = math.floor(time_since_epoch_minutes % 60)
hours = math.floor(time_since_epoch_hours % 24)

print("Time in UTC timezone: " + str(hours) + ":" + str(minutes) + ":" + str(seconds))



