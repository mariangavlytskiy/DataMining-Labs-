import string, re, math
from itertools import izip, cycle, tee

def openfile(filename):
    with open(filename) as file:
        text = file.read().lower().strip()
        text_for_work = re.sub(r"\W+", " ", text).split(" ")     
    return text

def fix_hist(text):
    hist = {}
    for word in text:
        hist[word] = hist.get(word, 0) + 1
    return hist    

def zipflaw(hist):
    l=[]
    for word, fr in hist.items():
        l.append((fr, word))
    l.sort(reverse=True)    
    return l

def heapslaw(text):
    length = 100
    l=[]
    while length <= len(text):
        hist = fhist(text[:length])
        l.append((length, len(hist)))
        length+=100   
    return l

def computetf(word, text):
    hist = fhist(text)
    text_length = float(len(text))
    return hist[word]/text_length

def computeidf(word, container):
    return math.log10(len(container)/sum([1.0 for text in container if word in text]))
 
def tfidf(text, container):
    l = []
    hist = fhist(text)
    for word in hist:
        l.append((computetf(word, text)*computeidf(word, container), word))
    l.sort(reverse=True)    
    return l  

def makebigramms(text):
    l = []
    for i in range(len(text)-1):
        # l.append(' '.join([text[i], text[i+1]]))
        l.append(text[i] + ' ' + text[i+1])
    return l

def maketriads(text, stop_words): 
    return [text[i] + ' ' + text[i+1] + ' ' + text[i+2] for i in range(len(text)-2) if text[i] not in stop_words]


#stopwords = openfile('text.txt')

text = openfile('text.txt')
#container = [text, openfile('text.txt'), openfile('text.txt'), openfile('text.txt'), openfile('text.txt')]
hist = fix_hist(text)
heaps = heapslaw(text)
zipf = zipflaw(hist)

# for i in zipf:
#     print i

for i in heaps:
    print i

# for word in tfidf(text, container):
#     print word


# btext = makebigramms(text)
# bhist = fix_hist(btext)
# bcontainer = [makebigramms(text) for  text in container]
 

# for word in tfidf(btext, bcontainer):
#     print word 

# trtext = maketriads(text, stopwords)
# trhist = fhist(trtext)
# trcontainer = [maketriads(text, stopwords) for text in container] 

# for word in tfidf(trtext, trcontainer):
#     print word

