import re

list_with_words = list()

with open('text.txt','r') as used_file:
	for line in used_file:
		list_with_words.extend(re.sub('[^\w]',' ',line).lower().strip().split())#change all enties of specials symbols to whitespace
	#print list_with_words
		
def heaps_law(used_list):
	"""Create dictionary of words in the text and amount of their frequency. And write the list with sorted values of word`s frequency."""
	f = open('output.txt','w')
	map_word_frequency = dict((word, used_list.count(word)) for word in set(used_list) if word != '')
	list_of_frequency = sorted(map_word_frequency.values())
	for val in list_of_frequency:
		f.write('{}\n'.format(val))
	#print list_of_frequency
	# for key in result.keys():
		# f.write('{0:s} ==> {1:d} \n'.format(key, result[key]))	
		
heaps_law(list_with_words)
