#!/usr/bin/python
import sys
import pandas as pd
from textblob import TextBlob
import re
import string
from textblob.classifiers import NaiveBayesClassifier

### Michael O'Malley, Jacob Dumford, Gregory Nemecek
### Social Sensing and Cyber Physical Systems
### Semster Project
### Sentiment Analysis - trained by team tweets

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

	print "Running..."

	text=[]
	starttime='2018-03-21 12:00:00'
	endtime='2018-03-21 23:30:00'
	# Set time range for the day to gather sentiment for
	# Note: 4 hour time conversion from tweet time (UTC-4)
	for line in data.values:
		dt = pd.to_datetime(line[2], format='%Y-%m-%d %H:%M:%S')
		if dt > pd.to_datetime(starttime, format='%Y-%m-%d %H:%M:%S') and dt < pd.to_datetime(endtime, format='%Y-%m-%d %H:%M:%S'):
			text.append(line[1])
		elif dt > pd.to_datetime(endtime, format='%Y-%m-%d %H:%M:%S'):
			break

	sentiment=0.
	n=0.
	#sent_m=0.
	#m=0.
	pos=0.
	neg=0.
	with open('train-'+str(sys.argv[1])+'.csv', 'r') as fp:
		cl=NaiveBayesClassifier(fp, format="csv")
	for line in text:
		newline=line.decode('utf-8')
		#testimonial=TextBlob(newline)
		#sentiment+=testimonial.sentiment.polarity
		prob_dist=cl.prob_classify(newline)
		#print prob_dist.prob("pos")
		#print prob_dist.prob("neg")
		#print prob_dist.prob("neu")
		#print '"'+str(prob_dist.max())+'"'
		#print "\n"
		#line_sent = round(prob_dist.prob("pos"),2)
		line_sent = prob_dist.max()
		#sentiment += line_sent*2-1 # change scale from [0,1] to [-1,1]
		n+=1
		#if testimonial.sentiment.polarity!=0:
		#if line_sent!=0.5:
		#if line_sent!=' neu':
			#sent_m+=testimonial.sentiment.polarity
			#sent_m+=line_sent
			#sent_m+=1
			#m+=1
		#if testimonial.sentiment.polarity>0:
		#if line_sent>0.5:
		if line_sent==' pos':
			pos+=1
			sentiment+=1
		#elif testimonial.sentiment.polarity<0:
		#elif line_sent<0.5:
		elif line_sent==' neg':
			neg+=1
			sentiment-=1
	print "Sentiment: ", sentiment
	print "N: ", n
	print "pos: ", pos
	print "neg: ", neg
	print "Average Sentiment: ", sentiment/n
	print "Non-null Sentiment: ", sentiment/(pos+neg)

