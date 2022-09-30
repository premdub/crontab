from asyncore import write
import pandas as pd
import os
import sys
import time
#df = pd.read_csv('https://query.data.world/s/vmrmccy7wb66inil533jtzpfnuzy7w')

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

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_$H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open('/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(df))

# time end
now = time.time()
endTime = time.strftime("%Y-%m-%d_$H:%M:%S", time.localtime(now))
print ('Time that the program finished running: ', endTime)


## EVERY SUNDAY AT 10 PM
##  0 20 * * SUN

## EVERY 6 AM ONCE A DAY
##  0 6 * * *

## EVERY QUARTER
## 0 0 1 */3 *