Pre-requisites:
Python 3 installed
Create a twitter app here https://apps.twitter.com/
Add your app credentials to the script


How to run:

Run scripts using python commands shown in OUTPUT


Functionality:

tweets_script.py
This script will download tweets from twitter. Tweets are filtered using keywords.
Keywords can be configured in the script
Output of the script is tweets in JSON format and can be written to a file as shown in OUTPUT
NOTE: script will keep running and downloading tweets. Press Ctrl+C to terminate.

popularity_script.py
This script takes output file of 'tweets_script.py' as input. Pass the file when running the
script as shown in OUTPUT
Script outputs total number of tweets in the input file. 
Also outputs the number of times each keyword is in the tweets. 
Popularity can be analyzed by comparing the number for each keyword

tweetsTrends_script.py
This script will output the the trending tweets in a geographical location.
Locations are represented as woeid(where on earth id) and can be configured in the script
A list of woeid's can be obtained by enabling last two lines in the script
A text file with all woeid's is also included in the repo

