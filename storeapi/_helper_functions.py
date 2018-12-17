import requests
import json
import subprocess
import string


def get_lemmatised_word(word,path_to_python2exe="C:/python27/python.exe"):
	script = [path_to_python2exe, "test2.py", word]
	process = subprocess.Popen(" ".join(script),
	                                        shell=True,  
	                                        env={"PYTHONPATH": "."}, stdout=subprocess.PIPE)

	output, error = process.communicate()
	return output.decode("latin-1")

def get_lemmatised_list(string,path_to_python2exe="C:/python27/python.exe"):
	script = [path_to_python2exe, "C:\\Users\\dis\\Documents\\JanJezersek\\EkoSmart\\apistoreapi\\storeapi\\_lemmatiser_script.py", string]
	process = subprocess.Popen(" ".join(script),
	                                        shell=True,  
	                                        env={"PYTHONPATH": "."}, stdout=subprocess.PIPE)

	output, error = process.communicate()
	return output.decode("latin-1").strip().split(" ")

def get_api_list(url="https://wso2.lavbic.net:9443/api/am/store/v0.11/apis"):
	r = requests.get(url)
	return json.loads(r.text)["list"]

def remove_None(a):
	for i,e in enumerate(a):
		if e == None:
			a[i] = ""
	return a

def remove_punctuation(a):
	return a.translate(str.maketrans('','',string.punctuation))

def levenshteinDistance(s1, s2):
	if len(s1) > len(s2):
	    s1, s2 = s2, s1

	distances = range(len(s1) + 1)
	for i2, c2 in enumerate(s2):
	    distances_ = [i2+1]
	    for i1, c1 in enumerate(s1):
	        if c1 == c2:
	            distances_.append(distances[i1])
	        else:
	            distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
	    distances = distances_
	return distances[-1]

def compare_api_userword(description,tags,name,user_keywords,filter_short=True,cutoff=4):
	description,tags,name = remove_None([description,tags,name])
	score = 0

	words = remove_punctuation(" ".join([description,tags,name])).lower()
	words = get_lemmatised_list(words)
	print("***LEMMATISED WORDS***  ",words)

	if filter_short:
		words = list(filter(lambda x: len(x) > 2, words))
		user_keywords = list(filter(lambda x: len(x) > 2, user_keywords))
		print(words,user_keywords,"\n")

	for keyword in user_keywords:
		if not keyword:
			continue

		for word in words:
			if not word:
				continue

			similarity_score = levenshteinDistance(keyword,word)
			print(word,keyword,similarity_score)

			if similarity_score == 0:
				score += 10
				print(keyword,word)
			elif keyword in word and len(keyword) >= cutoff or word in keyword and len(word) >= cutoff:
					score += 5
			elif similarity_score < cutoff:
				score += 1.0/similarity_score

		# if word in words:
		# 	#print("***",word,"***")
		# 	score += 1
	print("Final score:",score,"\n")
	return score

def get_tags(id,url="https://wso2.lavbic.net:9443/api/am/store/v0.11/apis/"):
	r = requests.get(url+id)
	return json.loads(r.text)["tags"]	

def get_details(id,url="https://wso2.lavbic.net:9443/api/am/store/v0.11/apis/"):
	r = requests.get(url+id)
	return json.loads(r.text)

def get_related_apis(apis,user_keyword):
	related = []

	for i,api in enumerate(apis):
		tags = " ".join(get_tags(api["id"]))
		score = compare_api_userword(api["description"],tags,api["name"],user_keyword)

		if score:
			related.append((score,api))

	return related

def search(user_keyword):
	user_keyword = get_lemmatised_list(user_keyword.lower())
	apis = get_api_list()
	print(apis)
	related = get_related_apis(apis,user_keyword)

	return sorted(related,key=lambda l:l[0],reverse=True)