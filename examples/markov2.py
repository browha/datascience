# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:02:54 2017

@author: henry
"""

#Markov 2

import os, string
import random as random
files=os.listdir('markovmodel')

dict={}
initial_one={}
initial_two={}

def add2dict(d, k, v):
    if k not in d:
        d[k] = []
    d[k].append(v)


for j in files:
    it=0
    for line in open('markovmodel/'+j):
        tokens=line.translate(None, string.punctuation).split(' ')
        if it==0:
            initial_one[tokens[0]]=initial_one.get(tokens[0],0)+1
            initial_two[tokens[1]]=initial_two.get(tokens[1],0)+1
            for word_it in range(2,len(tokens)):
                add2dict(dict, (tokens[word_it-2],tokens[word_it-1]),tokens[word_it])
            add2dict(dict, (tokens[word_it-1],tokens[word_it]),'THEEND')
        it+=1


def weighted_choice(choices):
        total = sum(w for c, w in choices.iteritems())
        r=random.uniform(0, total)
        upto=0
        for c, w in choices.iteritems():
            if upto+w >= r:
                return c
            upto+=w
        assert False, 'Shouldnt get here'


def generate_output():
    output_text=[]
    
    while len(output_text)<3:
        first_word=weighted_choice(initial_one)
        second_word=weighted_choice(initial_two)
        output_text.append(first_word)
        output_text.append(second_word)
        try:
            word=random.choice(dict[(first_word,second_word)])
            output_text.append(word)
        except KeyError:
            continue
    word=''
    while word!='THEEND':
        try:
            word=random.choice(dict[(output_text[-2],output_text[-1])])
            output_text.append(word)
        except KeyError:
            break

    del output_text[-1]
    output_text.append('\n')
    writer=''
    for j in output_text:
        writer+=j
        writer+=' '
    return writer

output=''
while len(output)<15:
    output=generate_output()
    
print output
