def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   minutes = sec // 60
   sec %= 60
   print("seconds value in hours:",hour)
   print("seconds value in minutes:",minutes)
   return "%02d:%02d:%02d" % (hour, minutes, sec) 
n = 60   #in minutes
print("Time in preferred format :-",convert_to_preferred_format(n))

