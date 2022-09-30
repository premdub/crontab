# crontab

Instructions for how the python files were automated using crontab :

-Import dataset from NYC Department of Homeless Services Daily Report (https://query.data.world/s/vmrmccy7wb66inil533jtzpfnuzy7w)


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
