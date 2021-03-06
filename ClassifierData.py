import collections, pickle

bigramPositive = collections.defaultdict(lambda: [0,0,0])
bigramNegative = collections.defaultdict(lambda: [0,0,0])

unigramPositive = collections.defaultdict(lambda: [1,1,1])
unigramNegative = collections.defaultdict(lambda: [1,1,1])

unigramCounts = collections.defaultdict(lambda: 1)
bigramCounts = collections.defaultdict(lambda: 0)

def get_bicounts():
	bi_data = open('bicounts.pkl', 'rb')
	biCounts = pickle.load(bi_data)
	bi_data.close()
	
	for count in biCounts:
		bigramCounts[count] = biCounts[count]
	
	return bigramCounts
	
def get_unicounts():
	uni_data = open('unicounts.pkl', 'rb')
	uniCounts = pickle.load(uni_data)
	uni_data.close()
	
	for count in uniCounts:
		unigramCounts[count] = uniCounts[count]
	
	return unigramCounts
	
def get_bipos():
	bi_pos = open('bipos.pkl', 'rb')
	biPos = pickle.load(bi_pos)
	bi_pos.close()
	
	for count in biPos:
		bigramPositive[count] = biPos[count]
	return bigramPositive

def get_unipos():
	uni_pos = open('unipos.pkl', 'rb')
	uniPos = pickle.load(uni_pos)
	uni_pos.close()
	
	for count in uniPos:
		unigramPositive[count] = uniPos[count]
	
	return unigramPositive

def get_bineg():
	bi_neg = open('bineg.pkl', 'rb')
	biNeg = pickle.load(bi_neg)
	bi_neg.close()
	
	for count in biNeg:
		bigramNegative[count] = biNeg[count]
	
	return bigramNegative

def get_unineg():
	uni_neg = open('unineg.pkl', 'rb')
	uniNeg = pickle.load(uni_neg)
	uni_neg.close()
	
	for count in uniNeg:
		unigramNegative[count] = uniNeg[count]
	
	return unigramNegative

