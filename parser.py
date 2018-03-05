import sys
import pandas as pd

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
		data = pd.read_csv(str(sys.argv[1]) + '-data.txt', sep='\t')

	print data
