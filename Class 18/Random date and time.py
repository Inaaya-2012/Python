import random
import datetime

def random_date(start,end):

    random_sec = random.randint(0,int((end - start).total_seconds()))
    
    rdate= datetime.timedelta(seconds = random_sec)
    #pint(rdate)
    return start + rdate

start = datetime.datetime(2019,1,1)
end =  datetime.datetime(2025,1,1)
rdate = random_date(start,end)
print("The random date between",start.date(),"and",end.date(),"is",rdate.date())
