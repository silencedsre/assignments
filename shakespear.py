import re
file=open('shakespeare.txt' ,'r')
words=[]
words_extended=[]
for lines in file:
    words.extend(re.findall('[a-z]+',lines.lower()))
print("total words: "+str(len(words)))
choosen_words=['i','rare','young','the','his']
dict_words={items:0 for items in choosen_words}

for item in dict_words:
    for word in words:
        if item==word:
            dict_words[item]+=1
print(dict_words)


for items in range(len(words)-1):
    biagram=words[items]+ " " +words[items+1]
    words_extended.append(biagram.lower())

choosen_words_extended=["i am", "rare qualities", "young men", "the court", "his words"]
dict_words_extended={items:0 for items in choosen_words_extended}

# print(words_extended)
for item1 in dict_words_extended:
    for word in words_extended:
        if item1==word:
            dict_words_extended[item1]+=1
print(dict_words_extended)

p_am_i=dict_words_extended["i am"]/dict_words["i"]
p_qualities_rare=dict_words_extended["rare qualities"]/dict_words["rare"]
p_men_young=dict_words_extended["young men"]/dict_words["young"]
p_court_the=dict_words_extended["the court"]/dict_words["the"]
p_words_his=dict_words_extended["i am"]/dict_words["his"]
print("p_am/i:"+str(p_am_i)+"\np_qualities/rare:"+str(p_qualities_rare)+"\np_men/young"+str(p_men_young)+"\np_court/the:"+str(p_court_the)+"\np_words/his:"+
      str(p_words_his))