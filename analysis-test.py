#!/usr/bin/python
import sys
import pandas as pd
from textblob import TextBlob
import re
import string

### Michael O'Malley, Jacob Dumford, Gregory Nemecek
### Social Sensing and Cyber Physical Systems
### Semster Project
### Data Parser

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

	text=[]
	index=0
	for line in data.values:
		dt = pd.to_datetime(data.values[index][2], format='%Y-%m-%d %H:%M:%S')
		if dt > pd.to_datetime('2018-03-10 12:00:00', format='%Y-%m-%d %H:%M:%S') and dt < pd.to_datetime('2018-03-10 23:30:00', format='%Y-%m-%d %H:%M:%S'):
			# Set time range for the day to gather sentiment for
			# Note: 4 hour time conversion from tweet time UTC-4
			text.append(data.values[index][1])
		index+=1

	sentiment=0.
	n=0
	sent_m=0.
	m=0
	pos=0
	neg=0
	for line in text:
		testimonial=TextBlob(line)
		sentiment+=testimonial.sentiment.polarity
		n+=1
		if testimonial.sentiment.polarity!=0:
			sent_m+=testimonial.sentiment.polarity
			m+=1
		if testimonial.sentiment.polarity>0:
			pos+=1
		elif testimonial.sentiment.polarity<0:
			neg+=1
	print "Sentiment: ", sentiment
	print "N: ", n
	print "pos: ", pos
	print "neg: ", neg
	print "Average Sentiment: ", sentiment/n
	print "Non-null Sentiment: ", sentiment/(pos+neg)

