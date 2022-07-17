#class Params:
# def __init__(self):
    
import datetime
import pytz
from pytz import timezone
from datetime import datetime
tz = 'Asia/Kolkata'
#for tz in timezones:
 # 
    
 # print(f"Date Time in {tz} is {dateTime}")

dateTime = datetime.now(timezone(tz))


txt1 = "Date is {DD}{MM}{YY}".format(H = dateTime.hour, 
M = dateTime.minute,
S = dateTime.second,
DD = dateTime.day,
MM = dateTime.month,
YY = dateTime.year)
print(txt1)
 
    #proposed use of mediainfo but as codecs are limited and not lot of variety so not sure.