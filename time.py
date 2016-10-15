# 时间日期处理

import datetime
import time



if __name__ == '__main__':
    # 获取当前时间
    d1 = datetime.datetime.now()
    print(d1)
    # 当前时间加上半小时
    d2 = d1 + datetime.timedelta(hours=0.5)
    print(d2)
    # 格式化字符串输出
    d3 = d2.strftime('%Y-%m-%d %H:%M:%S')
    print(d3)
    # 将字符串转化为时间类型
    d4 = datetime.datetime.strptime(d3, '%Y-%m-%d %H:%M:%S')
    print(d4)
    # 修改日期
    d5 = d4.replace(d4.year, d4.month, 1)
    print(d5)
    # 年、月、日、星期几
    print('year:%s' % d4.year)
    print('month:%s' % d4.month)
    print('day:%s' % d4.day)
    print('星期%s' % d4.isoweekday())
    #小时、分、秒
    print('hour:%s' % d4.time().hour)
    print('minute:%s' % d4.time().minute)
    print('second:%s' % d4.time().second)



