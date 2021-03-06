from GlassdoorReview import *
import nltk.data
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import math, collections, pickle

# maybe I should have two dicts 
# one for positive reviews
# one for negative reviews
# for each n-gram -> [x, y] x = pros count, y = cons count
# keep a third that holds all the totals for the n-grams

# [title counts, pros counts, cons counts]
bigramPositive = collections.defaultdict(lambda: [0,0,0])
bigramNegative = collections.defaultdict(lambda: [0,0,0])
#bigramNeutral = collections.defaultdict(lambda: [0,0,0])

unigramPositive = collections.defaultdict(lambda: [1,1,1])
unigramNegative = collections.defaultdict(lambda: [1,1,1])
#unigramNeutral = collections.defaultdict(lambda: [1,1,1])

unigramCounts = collections.defaultdict(lambda: 6)
bigramCounts = collections.defaultdict(lambda: 0)


def train_title_pos(title):
	for i in range(0, len(title)):
		word1 = title[i]
		pos = word1[1]
		if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
			if i+2 < len(title):
				word2 = title[i+1]
				word3 = title[i+2]
				if third_word_test(word1, word2, word3):
					counts = bigramPositive[(word1, word2)]
					counts[0] += 1
					bigramPositive[(word1, word2)] = counts
    				
					counts = unigramPositive[word1]
					counts[0] += 1
					unigramPositive[word1] = counts
    				
					bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
					unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
			elif i+1 < len(title):
				word2 = title[i+1]
				if second_word_test(word1, word2):
					counts = bigramPositive[(word1, word2)]
					counts[0] += 1
					bigramPositive[(word1, word2)] = counts
    				
					counts = unigramPositive[word1]
					counts[0] += 1
					unigramPositive[word1] = counts
    				
					bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
					unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
			else:
				counts = unigramPositive[word1]
				counts[0] += 1
				unigramPositive[word1] = counts
    			
				unigramCounts[word1] = 1 + unigramCounts[word1]

def train_title_neg(title):
	for i in range(0, len(title)):
		word1 = title[i]
		pos = word1[1]
		if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
			if i+2 < len(title):
				word2 = title[i+1]
				word3 = title[i+2]
				if third_word_test(word1, word2, word3):
					counts = bigramNegative[(word1, word2)]
					counts[1] += 1
					bigramNegative[(word1, word2)] = counts
    				
					counts = unigramNegative[word1]
					counts[1] += 1
					unigramNegative[word1] = counts
    				
					bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
					unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
			elif i+1 < len(title):
				word2 = title[i+1]
				if second_word_test(word1, word2):
					counts = bigramNegative[(word1, word2)]
					counts[1] += 1
					bigramNegative[(word1, word2)] = counts
    				
					counts = unigramNegative[word1]
					counts[1] += 1
					unigramNegative[word1] = counts
					
					bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
					unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
			else:
				counts = unigramNegative[word1]
				counts[1] += 1
				unigramNegative[word1] = counts
    			
				unigramCounts[word1] = 1 + unigramCounts[word1]


def train_pros_pos(pro):
    for i in range(0, len(pro)):
    	word1 = pro[i]
    	pos = word1[1]
    	if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
    		if i+2 < len(pro):
    			word2 = pro[i+1]
    			word3 = pro[i+2]
    			if third_word_test(word1, word2, word3):
    				counts = bigramPositive[(word1, word2)]
    				counts[1] += 1
    				bigramPositive[(word1, word2)] = counts
    				
    				counts = unigramPositive[word1]
    				counts[1] += 1
    				unigramPositive[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    				
    			#pass
    		elif i+1 < len(pro):
    			word2 = pro[i+1]
    			if second_word_test(word1, word2):
    				counts = bigramPositive[(word1, word2)]
    				counts[1] += 1
    				bigramPositive[(word1, word2)] = counts
    				
    				counts = unigramPositive[word1]
    				counts[1] += 1
    				unigramPositive[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
    		else:
    			counts = unigramPositive[word1]
    			counts[1] += 1
    			unigramPositive[word1] = counts
    			
    			unigramCounts[word1] = 1 + unigramCounts[word1]
    #pass

def train_pros_neg(pro):
    for i in range(0, len(pro)):
    	word1 = pro[i]
    	pos = word1[1]
    	if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
    		if i+2 < len(pro):
    			word2 = pro[i+1]
    			word3 = pro[i+2]
    			if third_word_test(word1, word2, word3):
    				counts = bigramNegative[(word1, word2)]
    				counts[1] += 1
    				bigramNegative[(word1, word2)] = counts
    				
    				counts = unigramNegative[word1]
    				counts[1] += 1
    				unigramNegative[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
    		elif i+1 < len(pro):
    			word2 = pro[i+1]
    			if second_word_test(word1, word2):
    				counts = bigramNegative[(word1, word2)]
    				counts[1] += 1
    				bigramNegative[(word1, word2)] = counts
    				
    				counts = unigramNegative[word1]
    				counts[1] += 1
    				unigramNegative[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
    		else:
    			counts = unigramNegative[word1]
    			counts[1] += 1
    			unigramNegative[word1] = counts
    			
    			unigramCounts[word1] = 1 + unigramCounts[word1]


def train_cons_pos(con):
    for i in range(0, len(con)):
    	word1 = con[i]
    	pos = word1[1]
    	if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
    		if i+2 < len(con):
    			word2 = con[i+1]
    			word3 = con[i+2]
    			if third_word_test(word1, word2, word3):
    				counts = bigramPositive[(word1, word2)]
    				counts[2] += 1
    				bigramPositive[(word1, word2)] = counts
    				
    				counts = unigramPositive[word1]
    				counts[2] += 1
    				unigramPositive[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
    		elif i+1 < len(con):
    			word2 = con[i+1]
    			if second_word_test(word1, word2):
    				counts = bigramPositive[(word1, word2)]
    				counts[2] += 1
    				bigramPositive[(word1, word2)] = counts
    				
    				counts = unigramPositive[word1]
    				counts[2] += 1
    				unigramPositive[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
    		else:
    			counts = unigramPositive[word1]
    			counts[2] += 1
    			unigramPositive[word1] = counts
    			
    			unigramCounts[word1] = 1 + unigramCounts[word1]

def train_cons_neg(con):
    for i in range(0, len(con)):
    	word1 = con[i]
    	pos = word1[1]
    	if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
    		if i+2 < len(con):
    			word2 = con[i+1]
    			word3 = con[i+2]
    			if third_word_test(word1, word2, word3):
    				counts = bigramNegative[(word1, word2)]
    				counts[2] += 1
    				bigramNegative[(word1, word2)] = counts
    				
    				counts = unigramNegative[word1]
    				counts[2] += 1
    				unigramNegative[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
    		elif i+1 < len(con):
    			word2 = con[i+1]
    			if second_word_test(word1, word2):
    				counts = bigramNegative[(word1, word2)]
    				counts[2] += 1
    				bigramNegative[(word1, word2)] = counts
    				
    				counts = unigramNegative[word1]
    				counts[2] += 1
    				unigramNegative[word1] = counts
    				
    				bigramCounts[(word1, word2)] = 1 + bigramCounts[(word1, word2)]
    				unigramCounts[word1] = 1 + unigramCounts[word1]
    			#pass
    		else:
    			counts = unigramNegative[word1]
    			counts[2] += 1
    			unigramNegative[word1] = counts
    			
    			unigramCounts[word1] = 1 + unigramCounts[word1]

# determines wether or not a bigram should be counted
# depending upon the third word in sequence
def third_word_test(w1, w2, w3):
	if w1[1] == 'JJ':
		if w2[1] in ['NN', 'NNS']:
			return True
		elif w2[1] == 'JJ' and w3[1] not in ['NN', 'NNS']:
			return True
		else:
			return False
	if w1[1] in ['NN', 'NNS']:
		if w2[1] == 'JJ' and w3[1] not in ['NN', 'NNS']:
			return True
		else:
			return False
	if w1[1] in ['RB', 'RBR', 'RBS']:
		if w2[1] == 'JJ' and w3[1] not in ['NN', 'NNS']:
			return True
		elif w2[1] in ['VB', 'VBD', 'VBN', 'VBG']:
			return True
		else:
			return False
	else:
		return False

def second_word_test(w1, w2):
	if w1[1] == 'JJ':
		if w2[1] in ['JJ','NN', 'NNS']:
			return True
		else:
			return False
	if w1[1] in ['NN', 'NNS']:
		if w2[1] == 'JJ':
			return True
		else:
			return False
	if w1[1] in ['RB', 'RBR', 'RBS']:
		if w2[1] in ['JJ', 'VB', 'VBD', 'VBN', 'VBG']:
			return True
		else:
			return False
	else:
		return False


def train_classifier(training_set):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    for review in training_set:

       # star_weight = create_star_weight(review.rating)
        title = tokenizer.tokenize(review.title)
        pros = tokenizer.tokenize(review.pros)
        cons = tokenizer.tokenize(review.cons)
        
        #tagged_title = pos_tag(word_tokenize(title[0]))
        #tagged_pros = pos_tag(word_tokenize(pros[0]))
        #tagged_cons = pos_tag(word_tokenize(cons[0]))
		
	if review.rating > 3:
        	for t in title:
			tagged_title = pos_tag(word_tokenize(t))
			train_title_pos(tagged_title)
        	for p in pros:
			tagged_pros = pos_tag(word_tokenize(p))
			train_pros_pos(tagged_pros)
		for c in cons:
			tagged_cons = pos_tag(word_tokenize(c))
			train_cons_pos(tagged_cons)
        else:
        	for t in title:
                        tagged_title = pos_tag(word_tokenize(t))
                        train_title_neg(tagged_title)
                for p in pros:
                        tagged_pros = pos_tag(word_tokenize(p))
                        train_pros_neg(tagged_pros)
                for c in cons:
                        tagged_cons = pos_tag(word_tokenize(c))
                        train_cons_neg(tagged_cons)
        

def main():
    training_set = GlassdoorReview.get_training_set()
    train_classifier(training_set)
    
    bg_output = open('bicounts.pkl', 'wb')
    pickle.dump(dict(bigramCounts), bg_output)
    bg_output.close()
    
    ug_output = open('unicounts.pkl', 'wb')
    pickle.dump(dict(unigramCounts), ug_output)
    ug_output.close()
    
    bp_output = open('bipos.pkl', 'wb')
    pickle.dump(dict(bigramPositive), bp_output)
    bp_output.close()
    
    up_output = open('unipos.pkl', 'wb')
    pickle.dump(dict(unigramPositive), up_output)
    up_output.close()
    
    bn_output = open('bineg.pkl', 'wb')
    pickle.dump(dict(bigramNegative), bn_output)
    bn_output.close()
    
    un_output = open('unineg.pkl', 'wb')
    pickle.dump(dict(unigramNegative), un_output)
    un_output.close()


if __name__ == "__main__": main()
