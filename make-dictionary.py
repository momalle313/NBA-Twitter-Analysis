#!/usr/bin/python
import sys
import pandas as pd
from textblob import TextBlob
import re
import string
from textblob.classifiers import NaiveBayesClassifier
import math

### Michael O'Malley, Jacob Dumford, Gregory Nemecek
### Social Sensing and Cyber Physical Systems
### Semster Project
### Create dictionary of tweets to train the sentiment analysis

# Run main
if __name__ == "__main__":

	# Read in training data
	if len(sys.argv) <= 1:
		print "Please state the team you'd like to analyze."
		sys.exit()
	elif str(sys.argv[1]) != 'Heat' and str(sys.argv[1]) != 'Bulls' and str(sys.argv[1]) != 'Rockets':
		print "Given team is invalid. Please choose Bulls, Rockets, or Heat."
		sys.exit()
	else:
		data = pd.read_csv(str(sys.argv[1]) + '-data-clean.txt', sep='\t')
		# Note: I copied the data to a new file, named Heat-data-clean.txt (or variation for another team)
		# and then in vim I ran command ":%s/\r/ /g" to remove the weird ^M newline characters from occassional tweets
		# This allows the sentiment analysis library to run without error.
		# I copied it to a new file before cleaning data to preserve the original integrity of the data

	total=200 # total tweets to classify for that team
	lines=len(data.values)
	teamname=sys.argv[1]
	if teamname=='Heat':
		mymod=int(math.floor(lines/total)) #~1474
	elif teamname=='Bulls':
		mymod=int(math.floor(lines/total)) #~148
	elif teamname=='Rockets':
		mymod=int(math.floor(lines/total)) #~2126
	#index=0
	tweetcount=0
	file1=open('train-' + str(sys.argv[1]) + '.csv',"a")
	print "1=pos, 2=neg, 3=neu"
	for index in range(total):
		#print index
		#print index*mymod
		newline=data.values[index*mymod][1].replace(',','') # take every n-th tweet; it also removes commas because it will be output as csv
		#newline=newline.decode('utf-8')
		tweetcount+=1
		print "Tweet " + str(tweetcount) + ": " + newline
		tweet_sent = input("1=pos, 2=neg, 3=neu? ")
		while tweet_sent!=1 and tweet_sent!=2 and tweet_sent!=3 and tweet_sent!=9:
			print "Invalid input"
			print "Tweet " + str(tweetcount) + ": " + newline
			tweet_sent = input("1=pos, 2=neg, 3=neu? ")
		if tweet_sent==1:
			file1.write(newline)
			file1.write(", ")
			file1.write("pos\n")
		elif tweet_sent==2:
			file1.write(newline)
			file1.write(", ")
			file1.write("neg\n")
		elif tweet_sent==3:
			file1.write(newline)
			file1.write(", ")
			file1.write("neu\n")
		elif tweet_sent==9:
			pass # in case acidentally error out while classifying tweets, can use 9 to skip ahead until where you were; file automatically appends without overwriting

	file1.close()
	print "Made file train-" + teamname + ".csv"

