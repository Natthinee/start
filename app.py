from flask import Flask, request
import json
import requests

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
LINE_API_KEY = 'Bearer IzXs2WdxBaxjM/BTdVQ43pEYgt1O8BRRrEAOztjHPMfRUmM0BYtD4VRZg7MLMSyi1mWqI3vdPl08HfmsCUiBM1QJKc0OF89EfbEPIHEG+pKHO85//3Zvo+Qcf9MDZoFwe2m+cjasnyvwYZ3xPQNWPgdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyStack = list()
    replyWord = list() #เพิ่มเอง
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    
    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID =  msg_in_json["events"][0]['source']['userId']
    msgType =  msg_in_json["events"][0]['message']['type']
    
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    #if msgType != 'text':
    #    reply(replyToken, ['Only text is allowed.'])
    #    return 'OK',200
    
    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ
    #text = msg_in_json["events"][0]['message']['text'].lower().strip()
    
   
    
    text = msg_in_json["events"][0]['message']['text'].lower().strip()

    # ตอบข้อความ "text" กลับไป ส่ง ไรมาตอบอันนั้น
    ll = replyStack.append(text)
    tt = list()
    kk = list()
    kk.append("สวัสดีจ้า.")
    tt.append(replyStack)
    if replyStack == kk :
        replyStack.append("สวัสดีจ้า....")
    else:
        replyStack.append("88888")
            
    
 
    
    # Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    replyStack.append(msg_in_string)
    reply(replyToken, replyStack[:5])

    
    return 'OK', 200
 
def reply(replyToken, textList):
    # Method ตอบกลับข้อความประเภท text 
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type": "template",
          "altText": "this is a confirm template",
          "template": {
          "type": "confirm",
          "text": "Are you sure?",
          "actions": [
              {
                "type": "message",
                "label": "Yes",
                "text": "yes"
              },
              {
                "type": "message",
                "label": "No",
                "text": "no"
          }
      ]
  }

        })
        
        data = json.dumps({
        "replyToken":replyToken,
        "messages":  msgs
    })
        
  
        
        requests.post(LINE_API, headers=headers, data=data)
   
    
    return

if __name__ == '__main__':
    app.run()