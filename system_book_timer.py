import time


def timer_setting():
    while True:
        now = time.localtime()
        year = now.tm_year
        month = now.tm_mon
        day = now.tm_mday
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec
        my_time = str(year)+'-'+str(month)+'-'+str(day)+'-'+str(hour)+'-49'+'-59'
        goal = time.strptime(my_time, '%Y-%m-%d-%H-%M-%S')
        if now>goal:
            break
        else:
            goal = time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))
            print("系统时间："+str(now)+"目标时间：北京时间19:50分\t"+"预计等待："+str(int(int(goal)-int(time.time())))+"秒")
            time.sleep(0.5)
timer_setting()
