HHA 507 Assignment 6

1.  Create a new GitHub repo called crontab

2.  Create 1 python file that pulls down data from an API and then create 3 cron jobs for that python API based on the following parameters:

      -  One should pull down data from an API once a day (don’t care about what time); 
      -  One should pull down data every Sunday night at 10:00pm; 
      -  And another one should pull down data at the end of every quarter

    Report the appropriate cron job command (like in page 12 of this presentation) within the GitHub repo within the markdown file

So repo should contain two files:
- markdown file (.md) with instructions for how the python files were automated using crontab 
- a python file (.py) that contains the python code for pulling down the data /// the retrieved data should then be saved locally on that machine where the cron job is running - e.g., should be part of the python code (e.g., df.to_csv(‘path/to/file/saved/data_10-10-10.csv)

Crontab jobs (required for assignment)
to run every day @ 08:00 pm (@ 20:00 military time) 

2 0 * * * usr/bin/python3 location/of/script (ex. \Users\premd\OneDrive\Desktop\HHA_507_\crontab\testFile.py)

to run every Sunday night at 10:00pm (or 22:00 military time)

0 22 * * SUN usr/bin/python3 location/of/script (ex. \Users\premd\OneDrive\Desktop\HHA_507_\crontab\testFile.py)

to run every quarter on the 1st day @ 00:00

0 0 1 */3 * usr/bin/python3 location/of/script (ex. \Users\premd\OneDrive\Desktop\HHA_507_\crontab\testFile.py)

** If there is a print function in the script please add '> log.txt 2>&1 &' to the end of crontab file **

Example: 0 0 1 */3 * usr/bin/python3 location/of/script > log.txt 2>&1 & (ex.\Users\premd\OneDrive\Desktop\HHA_507_\crontab\testFile.py > log.txt 2>&1 &)

crontab jobs can also be setup in virtual machine (GCP, Azure, or AWS)
      1. Create a virtual machine using Ubuntu Linux OS due to convenvience of OS

      2. Ensure all programs are install with sudo apt-get upgrade

      3. Clone the repo from GitHub

      4. Use crontab -h to check if crontab was installed

      if not use sudo-apt get install crontab

      5. cd into working directory

      in this case it would be /crontab

      6. Use nano cronJob.py to make last minute changes to script

      7.Input crontab -e in terminal shell

      input any crontab time/date with location of script

      refer to Crontab jobs above

      save and close crontab

      8.Successfully installed crontab

Sources
Data was pulled from NYC Department of Homeless Services Daily Report (https://query.data.world/s/vmrmccy7wb66inil533jtzpfnuzy7w)

