from datetime import datetime
import sys

now_day = sys.stdin.readline().rstrip()
now_day = datetime.strptime(now_day, '%B %d, %Y %H:%M')
start_d = datetime.strptime(str(now_day.year),'%Y')
end_d = datetime.strptime(str(now_day.year+1),'%Y')
print(100 - (end_d - now_day)/(end_d - start_d)*100)