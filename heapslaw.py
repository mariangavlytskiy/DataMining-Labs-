import re

list_with_words = list()
f = open('result.txt','w')

with open('text.txt','r') as used_file:
	for line in used_file:
		list_with_words.extend(re.sub('[^\w]',' ',line).lower().strip().split())
	#print list_with_words
		
def heaps_law(used_list):
	result = dict((word, used_list.count(word)) for word in set(used_list) if word != '')
	for key in result.keys():
		print key
		f.write('{0:s} ==> {1:d} \n'.format(key, result[key]))

heaps_law(list_with_words)
