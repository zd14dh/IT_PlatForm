import datetime

#
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# print(datetime.date.today())
# print(datetime.datetime.now())
#
#
#
#
# def job1(text):
#     print('job1',datetime.datetime.now(),text)
#
# scheduler = BlockingScheduler()
# scheduler.add_job(job1,'date',run_date=datetime.datetime(2022,12,22,14,54,0,0,),args=['ws'],id='job1')
# scheduler.start()

now =datetime.datetime.now()
last_year =now.year -1
print(last_year)
today_year_mouths= range(1,now.month+1)

last_year_mouths = range(now.month+1,13)

data_list_lasts=[]
for last_year_mouth in today_year_mouths:
    print(last_year_mouth)
    data_list_lasts.append(last_year_mouth)

print(data_list_lasts)