# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:33:09 2018

@author: khimmee
"""
import json
import random
sayhi = open("C://Users//khimmee//Desktop//sayhi.txt","r",encoding='utf-8')
gre = sayhi.read()
answer = open("C://Users//khimmee//Desktop//answer.txt","r",encoding='utf-8')
ans = answer.read()
ques = open("C://Users//khimmee//Desktop//Ques.txt","r",encoding='utf-8')
quest = ques.read()
quest8 = open("C://Users//khimmee//Desktop//Quest8.txt","r",encoding='utf-8')
ques8 = quest8.read()
wordappende = open("C://Users//khimmee//Desktop//wordappende.txt","r",encoding='utf-8')
wordap = wordappende.read()
qq2 = open("C://Users//khimmee//Desktop//qq2.txt","r",encoding='utf-8')
qqq2 = qq2.read()

evaluation_form ={}

evaluation_form['eval'] ={'greet': gre,
                         'answer': ans,
                         'ques': quest,
                         'quest8': ques8,
                         'wordap': wordap,
                         'qq2': qqq2}


jj = (evaluation_form['eval']['greet'])
print(jj)
inputuser = input()
if(inputuser == jj):
    print("จ้าาาาา")
else:
    print('ขิม')



