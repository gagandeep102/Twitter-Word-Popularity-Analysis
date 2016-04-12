import sys
import json
import re

#Function to check if word is in text using regular expression
def wordInText(word, text):
    word = word.lower()
    text = text.lower()
    result = re.search(word, text)
    if result:
        return True
    else:
        return False

#Check the number of arguments passed while running script
files = len(sys.argv)
tweets = []
#If file name is passed as argument
if files == 2:
    fileName = sys.argv[1]
    #Open the file in read mode
    f = open(fileName, "r")
    #Read file line by line
    for line in f:
        try:
            #Create json object from line string
            tweet=json.loads(line)
            #Append json object to tweets list
            tweets.append(tweet)
        except:
            continue
print(str(len(tweets)) + " Tweets collected.")
numWord1 = 0
numWord2 = 0
word1 = 'google'
word2 = 'tesla'

for i in range(len(tweets)):
    oneTweet = tweets[i]
    #Check is tweet json obj has 'text'
    if 'text' in oneTweet:
        text = oneTweet["text"]
        if wordInText(word1, text):
            numWord1 += 1
        if wordInText(word2, text):
            numWord2 += 1

print(word1 +': ' + str(numWord1))
print(word2 +': ' + str(numWord2))




