import sys
import tweepy
import datetime

### Michael O'Malley, Jacob Dumford, Gregory Nemecek
### Social Sensing and Cyber Physical Systems
### Semster Project
### Data Scraper

# Stream Listener for Location problem
class StreamListener(tweepy.StreamListener):

	# Get next tweet id
	if len(sys.argv) <= 1:
		print "Please state the team you'd like to analyze."
		sys.exit()
	elif str(sys.argv[1]) != 'Heat' and str(sys.argv[1]) != 'Bulls' and str(sys.argv[1]) != 'Rockets':
		print "Given team is invalid. Please choose Bulls, Rockets, or Heat."
		sys.exit()
	else:
		try:
			data = open(str(sys.argv[1]) + '-data.txt', 'r')
			lines = data.readlines()

			# Check where to start next id's by looking at old file
			have_id = False
			i = 1
			while not have_id:
				try:
					id = int(lines[len(lines)-i].split('\t')[0])
					have_id = True
				except ValueError:
					i += 1
			data.close()
		except IOError:
			data = open(str(sys.argv[1]) + '-data.txt', 'w+')
			data.write("id\ttext\ttimestamp\tlocation\n")
			id = 0
			data.close()
		
		# Open output file to append to
		output = open(str(sys.argv[1]) + '-data.txt', 'a+')

	# When a status is found, record the necessary information
	def on_status(self, status):
                if datetime.datetime.now() > datetime.datetime(2018, 4, 22, 4):
                        quit()
                self.id += 1			
                print "Hit: " + str(self.id)						
                self.output.write(str(self.id) + '\t')
                self.output.write(str(status.user.id_str) + '\t')
                self.output.write(status.text.encode('utf 8').replace('\n','') + '\t')
                self.output.write(str(status.created_at) + '\t')
                self.output.write(str(status.coordinates) + '\n')

	# Stop if an error occurs
	def on_error(self, status_code):
        	print "Error Code: " + str(status_code)
        	return False


# Run main script
if __name__ == "__main__":

	# Consumer keys and access token
        if sys.argv[1] == "Bulls":
                consumer_key = 'mpYkPEvyCOmgYNhAolUy2vkjR'
                consumer_secret = 'EeGj9wOcvGdJID7BgN1YhwSrhS21BlLNfgQ0oszenDxxHPvlxt'
                access_token = '918814989321949186-CLvmoUgBZ5DM148E4UmE88sqXSxPYmY'
                access_token_secret = 'ajQQjV3G2kEs42Y7F12UT4swJiQdOvLeOXch6gweWWIQm'
        elif sys.argv[1] == "Heat":
                consumer_key = 'l6h9Z40w3SM3QdFrRWH2hKVoL'
                consumer_secret = 'tPB3xDHDTnr3FjgV2pRKnc4mMBQyviPWyVmLqgYU4WaBc9BVI0'
                access_token = '960373416892170240-omnMrJJ2NDSkSL4HTEMEqgQlpIPsjQw'
                access_token_secret = 'KXs1K4jgmSe5pWCCWEhNZxiUR7wEkeo9KxNrSfhG7bk8a'
        else:
                consumer_key = 'KOBww3arz3J0v0fD81ucdkm51'
                consumer_secret = 'B0ttUv182vk1LrGtKrMi2kwo73KdLYJaqMMsDDocWJ8GB3yrBZ'
                access_token = '888969227046191105-iNSWv2NJpvoHLbVNHIws2W7Wz1nXYmB'
                access_token_secret = 'gR5yfLZIAFMuWkHmjNwNYAUK6TID68OXLwUXCjughWtJ2'

	# OAuth process
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	 
	# Interface creation
	api = tweepy.API(auth)

	# Read keywords into list
	keywords = []
	for line in open(str(sys.argv[1]) + '-keywords.txt', 'r'):
		key = line.strip()
		keywords.append(key)

	# Produce Stream results
	stream = tweepy.streaming.Stream(auth, StreamListener())
	stream.filter(track=keywords)


