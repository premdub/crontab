HHA 507 Assignment 6

1.  Create a new GitHub repo called crontab

2.  Create 1 python file that pulls down data from an API and then create 3 cron jobs for that python API based on the following parameters:

      -  One should pull down data from an API once a day (don’t care about what time); 
      -  One should pull down data every Sunday night at 10:00pm; 
      -  And another one should pull down data at the end of every quarter

    Report the appropriate cron job command (like in page 12 of this presentation) within the GitHub repo within the markdown file

So repo should contain two files:

    -markdown file (.md) with instructions for how the python files were automated using crontab

    -a python file (.py) that contains the python code for pulling down the data /// the retrieved data should then be saved locally on that machine where the cron job is running - e.g., should be part of the python code (e.g., df.to_csv(‘path/to/file/saved/data_10-10-10.csv)

Crontab jobs (required for assignment)
to run every day @ 08:00 pm (@ 20:00 military time) 

2 0 * * * usr/bin/python3 location/of/script (ex. /Users/lozo/Developer/AHI_Github/crontab/cronJob.py)

to run every Sunday night at 10:00pm (or 22:00 military time)

0 22 * * SUN usr/bin/python3 location/of/script (ex. /Users/lozo/Developer/AHI_Github/crontab/cronJob.py)

to run every quarter 

0 3 13 */3 * usr/bin/python3 location/of/script (ex. /Users/lozo/Developer/AHI_Github/crontab/cronJob.py)

** If there is a print function in the script please add '> log.txt 2>&1 &' to the end of crontab file **

Example: 0 3 13 */3 * usr/bin/python3 location/of/script > log.txt 2>&1 & (ex. /Users/lozo/Developer/AHI_Github/crontab/cronJob.py > log.txt 2>&1 &)

crontab jobs can also be setup in virtual machine (GCP, Azure, or AWS)
Create a virtual machine using Ubuntu Linux OS due to convenvience of OS

Ensure all programs are install with sudo apt-get upgrade

Clone the repo from GitHub

Use crontab -h to check if crontab was installed

if not use sudo-apt get install crontab

cd into working directory

in this case it would be /crontab

Use nano cronJob.py to make last minute changes to script

Input crontab -e in terminal shell

input any crontab time/date with location of script

refer to Crontab jobs above

save and close crontab

Successfully installed crontab

Sources
Data was pulled from NYC Department of Homeless Services Daily Report (https://query.data.world/s/vmrmccy7wb66inil533jtzpfnuzy7w)




# crontab
df = pd.read_csv('https://query.data.world/s/vmrmccy7wb66inil533jtzpfnuzy7w')
df.to_csv('/home/premdub/crontab/data.csv')
df.to_csv('Users\premd\OneDrive\Desktop\HHA_507_\crontab\saved_data_locally.csv')


Instructions for how the python files were automated using crontab :




Within crontab : 
<<<<<<< HEAD
-data pull down from an API once a day @ 08:00 pm (@ 20:00 military time) 
=======

-data pull down from an API once a day (@ 18:15 military time) 

>>>>>>> 53633e3c25ed7cd006d40b7e53a0b6d238b80d4f
-data pull down every Sunday night at 10:00pm (or 22:00 military time)

-data pull down at the end of every quarter.

I haved added data pull down from an API every minute to ensure command run successfully. 
After it's successfully ran, i added hashtag to stop.

-report data is to be saveed to local data file (data.csv).
