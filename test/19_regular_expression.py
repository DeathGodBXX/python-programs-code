import re
s = 'se234 1987-02-09 07:30:00 1987-02-10 07:25:00'
date = re.findall("(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})", s)
print(date)
