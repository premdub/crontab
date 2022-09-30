from asyncore import write
import pandas as pd
import os
import sys
import time


# get current time
now = time.time()
timestart = time.strftime("%Y-%m-%d_$H:%M:%S", time.localtime(now))
print('this program started running at: ', timestart)

# get current working directory
cwd = os.getcwd()

# print cwd
print (cwd)

# create a new dictionary with data
df = pd.read_csv('https://query.data.world/s/vmrmccy7wb66inil533jtzpfnuzy7w')
df.to_csv('/home/premdub/crontab/data.csv')
df.to_csv('Users\premd\OneDrive\Desktop\HHA_507_\crontab\saved_data_locally.csv')

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_$H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open('/home/premdub/crontab/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(df))

# time end
now = time.time()
endTime = time.strftime("%Y-%m-%d_$H:%M:%S", time.localtime(now))
print ('Time that the program finished running: ', endTime)
