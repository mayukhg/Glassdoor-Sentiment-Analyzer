#from Reviewer import unigramCounts, bigramCounts
from CreateClassifiers import third_word_test, second_word_test
import math,collections
import ClassifierData

bigramCounts = ClassifierData.get_bicounts()
bigramPositive = ClassifierData.get_bipos()
bigramNegative = ClassifierData.get_bineg()
	
unigramCounts = ClassifierData.get_unicounts()
unigramPositive = ClassifierData.get_unipos()
unigramNegative = ClassifierData.get_unineg()

def get_probs_title(title, pros_prob, cons_prob):
	for i in range(0, len(title)):
		word1 = title[i]
		if len(word1) > 1:
			pos = word1[1]
		else:
			return pros_prob, cons_prob
		if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
			if i+2 < len(title):
				word2 = title[i+1]
				word3 = title[i+2]
				if third_word_test(word1, word2, word3):
					pos_num = bigramPositive[(word1, word2)][0]
					neg_num = bigramNegative[(word1, word2)][0]
					denom = bigramCounts[(word1, word2)]
					pros_prob, cons_prob = update_probs(pos_num, neg_num, denom, pros_prob, cons_prob, word1)
    					#if unicounts is [1,1,1,1]:
    					#	unigramCounts["total"] = unigramCounts["total"] + 1
    					
    			#pass
			elif i+1 < len(title):
				word2 = title[i+1]
				if second_word_test(word1, word2):
					pos_num = bigramPositive[(word1, word2)][0]
					neg_num = bigramNegative[(word1, word2)][0]
					denom = bigramCounts[(word1, word2)]
					pros_prob, cons_prob = update_probs(pos_num, neg_num, denom, pros_prob, cons_prob, word1)
    		else:
    			pros_score = 0
			cons_score = 0
			
			upos_num = unigramPositive[word1][0]
			uneg_num = unigramNegative[word1][0]
			udenom = unigramCounts[word1]
						
			pros_score += math.log(upos_num)
			pros_score -= math.log(udenom)
				#pros_prob += math.log(0.4)
						
			cons_score += math.log(uneg_num)
			cons_score -= math.log(udenom)
				#cons_prob += math.log(0.4)
			pros_prob += pros_score
			cons_prob += cons_score
			
	return pros_prob, cons_prob
        
def get_probs_pros(pro, pros_prob, cons_prob):
	for i in range(0, len(pro)):
		word1 = pro[i]
		if len(word1) > 1:
			pos = word1[1]
		else:
			return pros_prob, cons_prob
		if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
			if i+2 < len(pro):
				word2 = pro[i+1]
				word3 = pro[i+2]
				if third_word_test(word1, word2, word3):
					pos_num = bigramPositive[(word1, word2)][0]
					neg_num = bigramNegative[(word1, word2)][0]
					denom = bigramCounts[(word1, word2)]
					pros_prob, cons_prob = update_probs(pos_num, neg_num, denom, pros_prob, cons_prob, word1)
    			#pass
			elif i+1 < len(pro):
				word2 = pro[i+1]
				if second_word_test(word1, word2):
					pos_num = bigramPositive[(word1, word2)][0]
					neg_num = bigramNegative[(word1, word2)][0]
					denom = bigramCounts[(word1, word2)]
					pros_prob, cons_prob = update_probs(pos_num, neg_num, denom, pros_prob, cons_prob, word1)
    			#pass
			else:
				upos_num = unigramPositive[word1][0]
				udenom = unigramCounts[word1]
				pros_score = 0
		
				pros_score += math.log(upos_num)
				pros_score -= math.log(udenom)
				pros_score += math.log(0.4)
				
				pros_prob += pros_score
	return pros_prob, cons_prob
	

def get_probs_cons(cons, pros_prob, cons_prob):
	for i in range(0, len(cons)):
		word1 = cons[i]
		if len(word1) > 1:
			pos = word1[1]
		else:
			return pros_prob, cons_prob
		if pos in ['JJ', 'NN', 'NNS', 'RB', 'RBR', 'RBS']:
			if i+2 < len(cons):
				word2 = cons[i+1]
				word3 = cons[i+2]
				if third_word_test(word1, word2, word3):
					pos_num = bigramPositive[(word1, word2)][0]
					neg_num = bigramNegative[(word1, word2)][0]
					denom = bigramCounts[(word1, word2)]
					pros_prob, cons_prob = update_probs(pos_num, neg_num, denom, pros_prob, cons_prob, word1)
    			#pass
			elif i+1 < len(cons):
				word2 = cons[i+1]
				if second_word_test(word1, word2):
					pos_num = bigramPositive[(word1, word2)][0]
					neg_num = bigramNegative[(word1, word2)][0]
					denom = bigramCounts[(word1, word2)]
					pros_prob, cons_prob = update_probs(pos_num, neg_num, denom, pros_prob, cons_prob, word1)
    			#pass
			else:
				uneg_num = unigramNegative[word1][0]
				udenom = unigramCounts[word1]
				cons_score = 0
		
				cons_score += math.log(uneg_num)
				cons_score -= math.log(udenom)
				cons_score += math.log(0.4)

				cons_prob += cons_score
	return pros_prob, cons_prob
	
def update_probs(pos_num, neg_num, denom, pros_p, cons_p, word1):
	pros_prob = 0
	cons_prob = 0
	if pos_num is not 0 and neg_num is not 0:
		pros_prob += math.log(pos_num)
		pros_prob -= math.log(denom)
						
		cons_prob += math.log(neg_num)
		cons_prob -= math.log(denom) 
					
	elif pos_num is 0 and neg_num is not 0:
		cons_prob += math.log(neg_num)
		cons_prob -= math.log(denom)
						
		upos_num = unigramPositive[word1][0]
		udenom = unigramCounts[word1]
						
		pros_prob += math.log(upos_num)
		pros_prob -= math.log(udenom)
		pros_prob += math.log(0.4)
					
	elif neg_num is 0 and pos_num is not 0:
		pros_prob += math.log(pos_num)
		pros_prob -= math.log(denom)
						
		uneg_num = unigramNegative[word1][0]
		udenom = unigramCounts[word1]
						
		cons_prob += math.log(uneg_num)
		cons_prob -= math.log(udenom)
		cons_prob += math.log(0.4)
    						
	else:
		upos_num = unigramPositive[word1][0]
		uneg_num = unigramNegative[word1][0]
		udenom = unigramCounts[word1]
						
		pros_prob += math.log(upos_num)
		pros_prob -= math.log(udenom)
		pros_prob += math.log(0.4)
						
		cons_prob += math.log(uneg_num)
		cons_prob -= math.log(udenom)
		cons_prob += math.log(0.4)

	pros_p += pros_prob
	cons_p += cons_prob
	return pros_p, cons_p
        
def guess_sentiment(pros_prob, cons_prob):
	if pros_prob > cons_prob and pros_prob is not 0:
		return "Positive"
	else:
		return "Negative"
