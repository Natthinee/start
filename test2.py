﻿

##print(score)   
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:02:33 2018

@author: khimmee
"""
i = 0
import random
while i >= 0:
  text = input("> ")
  sayhi = ['สวัสดีจ้า','สวัสดี','ดี','ดีดี','ดีดีดี','Hi','good morning','เฮ้','ว่าไง','สวัสดีครับ','สวัสดีดีค่ะ','สวัสดีจ้า','ดีจ้า']
  answer = ['Hello :D','ดีดี','สวัสดีจ้า','ไฮ้']
  c = ['เเบบประเมิน','เป็นโรคซึมเศร้า','นอนไม่หลับ','เบื่อ','กินข้าวไม่ลง','น้ำหนัดลด','น้ำหนักขึ้น','นอนเยอะ','นอนมาก','ช้าลง',
       'ไม่มีสติ','ไม่มีสมาธิ','น้อยลง','ไม่อยากออกไปข้างนอก','ไม่ตื่นเต้น','รู้สึกฉยๆ','ไม่สนุก','เคยใช้สารเสพติด','มีโรคประจำตัว',
       'ไทรอยด์','โรคประจำตัว','...']
  d = ['เบื่อหรือมีความรู้สึก ไม่สนใจอยากทำอะไรเลย ไหมเอ่ย ??',
       'เคยมีความรู้สึกไม่สบายใจ ซึมเศร้า ท้อแท้ บ้างป่ะ?? 😊',
       'รู้สึกหลับยาก หรือหลับๆ ตื่นๆ หรือหลับมากไป บ้างหรือเปล่าอ่ะ ?? Zzzz',
       'เริ่มรู้สึกเหนื่อยง่าย หรือ ไม่ค่อยมีแรง บ้างไหมน้าาาาาา??',
       'เวลาจะกินอะไรที รู้สึกเบื่ออาหาร หรือกินมากเกินไป บ้างป่าว??  😚',
       'รู้สึกไม่ดีกับตัวเอง คิดว่าตัวเองล้มเหลว หรือทำให้ตัวเองหรือครอบครัวผิดหวัง บ้างม่ะ ?? 😣"',
       'รู้สึกสมาธิไม่ดีเวลาทำอะไร เช่น ดูโทรทัศน์ ฟังวิทยุ หรือทำงานที่ต้องใช้ความตั้งใจ บ้างไหมน้าาา ??',
       'รู้สึกว่าตัวเอง พูดช้า ทำอะไรช้าลง จนคนอื่นสังเกตเห็นได้ หรือกระสับกระส่ายไม่สามารถอยู่นิ่งได้เหมือนที่เคยเป็นบ้างม่ะ ??',
       'เคยคิดทำร้ายตัวเอง หรือคิดว่าถ้าตายไปคงจะดีหรือเปล่า ??']
  
  wordappend = ['ช่วงนี้ ... ','ช่วงๆ 2 สัปดาห์ที่ผ่านมา ...','หนิ หนิ ช่วง 2 สัปดาห์มานี้ ... ','ช่วงนี้ฝนตกบ่อย เอ้ย!! ม่ายช่ายย ช่วงนี้ ... '
                ,'...  ช่วงนี้อ่ะ ','นี่ๆ ช่วง 2 สัปดาห์นี้อ่ะ ... ','เดี๋ยวนี้ ...','มีบ้างไหมที่ ','สองสัปดาห์ที่ผ่านมา...']
  e = ['มีความคิดอยากตาย หรือคิดว่าตายไปจะดีกว่า',
       'อยากทำร้ายตัวเอง หรือทำให้ตัวเองบาดเจ็บ',
       'มีความคิดเกี่ยวกับการฆ่าตัวตาย',
       'มีแผนการที่จะฆ่าตัวตาย',
       'ได้เตรียมการที่จะทำร้ายตนเอง หรือเตรียมการจะฆ่าตัวตาย โดยตั้งใจว่าจะให้ตายจริงๆ',
       'ได้ทำให้ตนเองบาดเจ็บ แต่ไม่ตั้งใจที่จะทำให้เสียชีวิต',
       'ได้พยายามฆ่าตัวตาย โดยคาดหวัง/ตั้งใจที่จะให้ตาย',
       'ตลอดชีวิตที่ผ่านมา... ท่านเคยพยายามฆ่าตัวตาย']
  
  wordappende =['ช่วง 1 เดือนที่ผ่านมา...',
                'ระยะเวลา 1 เดือนที่ผ่านมา...',
                'ในช่วง 1 เดือนที่ผ่ามานั้น...',
                'จากระยะเวลา 1 เดือนที่ผ่านมา',
                'ใน 1 เดือนที่ผ่านมานี้',
                'พฤติกรรมใน 1 เดือนที่ผ่านมา','','','','','','','','','']
  qq2 = ['ใน 2 สัปดาห์ที่ผ่านมารวมวันนี้ “ท่านรู้สึก หดหู่ เศร้า หรือท้อแท้สิ้นหวังหรือไม่”',
         'ใน 2 สัปดาห์ที่ผ่านมารวมวันนี้ “ท่านรู้สึก เบื่อ ทำอะไรก็ไม่เพลิดเพลินหรือไม่”']
  
  #### 0,1,2,3
  
  
  score = 0
  nn = 0
  answer0 = 'ไม่มีเลย'
  answer1 = 'เป็นบางวัน'
  answer2 = 'เป็นบ่อย'
  answer3 = 'เป็นทุกวัน'
  listanswer = []
  question = ''
  sc = 0
  face = ''
  qe = ''
  faceqe = ''
  appe = []
  score = 0
  number = ['0','1','2','3']
  qqq2 =[]
  q2q = ''
  if text in sayhi :
    print('--' + random.choice(answer))
  
  elif text in c :
    for j in d:
        if question != listanswer:
            question = random.choice(d)
            face = random.choice(wordappend)
            listanswer.append(question)
            print(face+question)
            print(' 0 = ไม่มีเลย\n','1 = เป็นบางวัน\n','2 = เป็นบ่อย\n', '3 = เป็นทุกวัน\n')
            print('กรุณาพิมพ์หมายเลข 0 1 2 3 ตามระดับของอาการที่เป็นหน่อยน้าาา')
            #print(len(d))
            n = int(input())
            nn = n
            score = score + nn
            i+=1
            if i == 9:
                print(score)
                i=0
                #break
                for h in qq2:
                    if q2q != qqq2:
                        q2q = random.choice(qq2)
                        qqq2.append(qq2)
                        print(q2q)
                        print('พิมพ์ "มี" หน่อยนะถ้ามีอาการ พิมพ์ "ไม่มี" ถ้าไม่มีอาการน้าาา')
                        aq2 = input()
                        if aq2=='มี':
                            sc+=1
                            i+=1
                        else:
                            sc+=0
                            i+=1
                            if i==2:
                                print(sc)
                                break
        
 
    
       
              
       
  
  
    
  else:
    print("-- เอ๊ะ! พิมพ์ผิดหรือเปล่าน้าาาา กอดอุ่นไม่เห็นเข้าใจเลย :/" )
    
