# Quotes

This python script uses the Twitter API (using the tweepy library) and python-notify to send inspirational quotes to your computer screen through a notification bubble, provided by a quote-posting Twitter page. 

For now, must be run with Python 2.7.

## How to use?
1. `git clone` this repo.
2. Install required packages:
	- Install tweepy using `pip install tweepy`.
	- Install python-notify using `apt-get install python-notify`
3. [Create a twitter app](https://apps.twitter.com/) in order to use their API and get the keys to use this script.
4. Edit your `config.py` with the generated keys (keep the keys as strings).
5. Edit your crontab and enter the following:
```
*/10 * * * * /usr/bin/python /home/user/path-to/quotes.py
```
This will make the program run every 10 minutes (you can change that by altering the first position).

__Note:__ If you encounter an error with your crontab not actually running, you can use the following instead
``` 
*/10 * * * * eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)"; /usr/bin/python /home/user/path-to/quotes.py
```
6. You're all set! A new quote will display every 10 minutes.

### Quotes
The quotes were taken from the twitter page @GreatestQuotes. 
