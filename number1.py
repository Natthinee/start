# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 00:21:57 2018

@author: khimmee
"""
#### กากเด่วดูใหม่
elif text in number :
      if question != listanswer:
         question = random.choice(d)
         face = random.choice(wordappend)
         listanswer.append(question)
         print(face+question)
         print(' 0 = ไม่มีเลย\n','1 = เป็นบางวัน\n','2 = เป็นบ่อย\n', '3 = เป็นทุกวัน\n')
      if text == answer0 :
           if question != listanswer:
              question = random.choice(d)
              face = random.choice(wordappend)
              listanswer.append(question)
              score = score + 0
              print(face+question)
              print(' 0 = ไม่มีเลย\n','1 = เป็นบางวัน\n','2 = เป็นบ่อย\n', '3 = เป็นทุกวัน\n')
      if text == answer1 :
            if question != listanswer:
              question = random.choice(d)
              face = random.choice(wordappend)
              listanswer.append(question)
              score = score + 1
              print(face+question)
              print(' 0 = ไม่มีเลย\n','1 = เป็นบางวัน\n','2 = เป็นบ่อย\n', '3 = เป็นทุกวัน\n')
      if text == answer2:
            if question != listanswer:
              question = random.choice(d)
              face = random.choice(wordappend)
              listanswer.append(question)
              score = score + 2 
              print(face+question)
              print(' 0 = ไม่มีเลย\n','1 = เป็นบางวัน\n','2 = เป็นบ่อย\n', '3 = เป็นทุกวัน\n')
      if text == answer3:
            if question != listanswer:
              question = random.choice(d)
              face = random.choice(wordappend)
              listanswer.append(question)
              score = score + 3 
              print(face+question)
              print(' 0 = ไม่มีเลย\n','1 = เป็นบางวัน\n','2 = เป็นบ่อย\n', '3 = เป็นทุกวัน\n')
 
 