#!/usr/bin/python
import sys
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob.classifiers import NaiveBayesClassifier


### Michael O'Malley, Jacob Dumford, Gregory Nemecek
### Social Sensing and Cyber Physical Systems
### Semster Project
### Graph Sentiment vs Time


### Main Execution ###


if __name__=="__main__":

	# Read in training data
	if len(sys.argv) <= 1:
		print "Please state the team you'd like to analyze."
		sys.exit()
	elif str(sys.argv[1]) != 'Heat' and str(sys.argv[1]) != 'Bulls' and str(sys.argv[1]) != 'Rockets':
		print "Given team is invalid. Please choose Bulls, Rockets, or Heat."
		sys.exit()
	else:
		data = pd.read_csv('../' + str(sys.argv[1]) + '-data-clean.txt', sep='\t')

	# Set times for the recorded games
	if str(sys.argv[1]) == 'Heat':
		starttimes = ['2018-03-21 23:30:00','2018-03-24 00:00:00','2018-04-03 23:30:00','2018-04-04 23:30:00','2018-04-09 23:30:00','2018-04-12 00:00:00']
	elif str(sys.argv[1]) == 'Bulls':
		starttimes = ['2018-03-22 00:00:00','2018-03-24 00:00:00','2018-03-24 23:00:00','2018-03-28 00:00:00','2018-04-04 00:00:00','2018-04-08 00:00:00','2018-04-09 23:30:00','2018-04-12 00:00:00']
	else:
		starttimes = ['2018-03-21 02:30:00','2018-03-23 00:00:00','2018-03-25 00:00:00','2018-03-28 00:00:00','2018-04-04 00:00:00','2018-04-06 00:00:00','2018-04-08 00:30:00','2018-04-11 02:30:00','2018-04-12 02:30:00']

	# Train sentiment model
	with open('../train-'+str(sys.argv[1])+'.csv', 'r') as fp:
		cl=NaiveBayesClassifier(fp, format="csv")
			
	# Examine each game in the given teams data
	for time in starttimes:

		# Record start time and end time metrics
		a = time.replace('-',' ').replace(':',' ').split()
		a = [int(x) for x in a]
		end_time = datetime.datetime(a[0],a[1],a[2],a[3],a[4],a[5])
		if a[3] < 6:
			start_time = datetime.datetime(a[0],a[1],a[2]-1,(a[3]-6)+24,a[4],a[5])
		else:
			start_time = datetime.datetime(a[0],a[1],a[2],a[3]-6,a[4],a[5])
		
		minutes = start_time.minute

		# Initialize loop variables
		interval = 5
		times = []
		labels = []
		tot_time = 0
		tot_sentiment = []
		sentiment = 0
		n = 0

		# Loop through all the data
		for index, row in data.iterrows():

			# Parse time of data point
			b = row['timestamp'].replace('-',' ').replace(':',' ').split()
			b = [int(x) for x in b]
			time = datetime.datetime(b[0],b[1],b[2],b[3],b[4],b[5])

			# Skip if not at time yet
			if start_time > time:
				continue

			# Break if past endtime
			if end_time < time:
				break

			# Add to sentiment
			n+=1
			newline=row['text'].decode('utf-8')
			prob_dist=cl.prob_classify(newline)
			line_sent = prob_dist.max()
			if line_sent==' pos':
				sentiment+=1
			elif line_sent==' neg':
				sentiment-=1

			# If interval has been reach, start a new bin
			if abs(time.minute - minutes) >= interval:

				# Record time variables
				times.append(tot_time)
				tot_time += interval
				labels.append(str(time.hour) + ':' + str(time.minute))
				minutes = time.minute

				# Record sentiment variable
				tot_sentiment.append(sentiment/float(n))
				
		# Drop used data
		data = data.loc[index:]

		# Format plot
		plt.figure(figsize=(12,6))
		plt.plot(times, tot_sentiment, color='b', label='Avg Sentiment')
		plt.title(str(sys.argv[1])+' Before Game: '+str(start_time)+'\nNaive Bayes: Avg Sentiment vs Time')
		plt.xlabel('Time Interval')
		plt.ylabel('Average Sentiment')
		plt.xticks(times, labels, rotation='vertical')
		plt.grid(which='minor', alpha=0.2)
		plt.grid(which='major', alpha=0.5)
		plt.tight_layout(w_pad=1.5, h_pad=1.5)

		# Show plot
		plt.savefig('./naivebayes-before-game/'+str(sys.argv[1])+' '+str(start_time)+'.png')

