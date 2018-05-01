#!/usr/bin/python
import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### Michael O'Malley, Jacob Dumford, Gregory Nemecek
### Social Sensing and Cyber Physical Systems
### Semster Project
### Graph Sentiment Progress


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
		data = pd.read_csv(str(sys.argv[1]) + '-data-clean.txt', sep='\t')

	# Record start time metrics
	start_time = data['timestamp'].iloc[0].split()[1].split(':')
	
	start_hour = start_time[0]
	start_min = start_time[1]
	start_sec = start_time[2]

	interval = 5

	times = []
	tot_tweets = []
	labels = []
	tot_time = 0
	tweet_count = 0
	for index, row in data.iterrows():

		tweet_count += 1
		time = row['timestamp'].split()[1].split(':')

		if abs(int(time[0]) - int(start_hour)) > 1:
			print "New game"

		if abs(int(time[1]) - int(start_min)) == interval:

			times.append(tot_time)
			tot_time += interval
			labels.append(str(time[0]) + ':' + str(time[1]))
			start_min = time[1]

			tot_tweets.append(tweet_count)		
			tweet_count = 0

		if tot_time >= 100:
			break

	plt.plot(times, tot_tweets, 'ro')
	plt.title('Number of Tweets per ' + str(interval) + ' Minute Interval')
	plt.xlabel('Time Interval')
	plt.ylabel('Number of Tweets')
	plt.xticks(times, labels, rotation='vertical')
	plt.show()
	plt.close()





