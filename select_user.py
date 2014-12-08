#-*- coding=utf-8 -*-
import os

def mytimescmp(a, b):  
    return cmp(int(a.split(',')[1]), int(b.split(',')[1]))

def mydayscmp(a, b):  
    return cmp(int(a.split(',')[2]), int(b.split(',')[2]))

if __name__ == '__main__':
    dirPath = 'origin'
    fileList = os.listdir(dirPath)
    count = 0
    results = []
    for f in fileList:
        #print f
        f = dirPath+'/'+f
        count = count+1
        print count
        inputFile = open(f, 'r')
        macid = f.split(' ')[1]
        times = 0
        days = 0
        lastDay = ''
        for line in inputFile:
            times = times+1
            if times == 1:
                continue
            line = line[:-1].split(',')
            if lastDay != line[5][1:11]:
                days = days+1
                lastDay = line[5][1:11]
        times = times-1
        inputFile.close()
        oneInfo = macid+','+str(times)+','+str(days)+'\n'
        results.append(oneInfo)
    #sort with times
    userTimesInfo = open('user_times_info.csv', 'w')
    userTimesInfo.write('mac_id,total_times,total_days\n')
    results.sort(mytimescmp)
    for info in results:
        userTimesInfo.write(info)
    userTimesInfo.close()
    #sort with days
    userTimesInfo = open('user_days_info.csv', 'w')
    userTimesInfo.write('mac_id,total_times,total_days\n')
    results.sort(mydayscmp)
    for info in results:
        userTimesInfo.write(info)
    userTimesInfo.close()
