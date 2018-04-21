from flask import Flask, request
import json
import requests

# ตรง YOURSECRETKEY ใส่ TOKEN
global LINE_API_KEY
LINE_API_KEY = 'Bearer IzXs2WdxBaxjM/BTdVQ43pEYgt1O8BRRrEAOztjHPMfRUmM0BYtD4VRZg7MLMSyi1mWqI3vdPl08HfmsCUiBM1QJKc0OF89EfbEPIHEG+pKHO85//3Zvo+Qcf9MDZoFwe2m+cjasnyvwYZ3xPQNWPgdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'สวัสดีชาวโลก'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyStack = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']     #### ดึงข้อมูลจากส่วนนี้มาเเสดง
   

    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไป-มา (แบบ json)
    replyStack.append(msg_in_string)
    reply(replyToken, replyStack[:5])
    
    return 'OK',200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    
    
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        
        msgs.append({
            "type":"text",
            ###"text": text
            "text":"สวัสดีคร้าบบบ ผมกอดอุ่น ยินดีให้บริการครับ"
  })
        
    msgs14 = []
    for text in textList:
        
        msgs14.append({
      
  "type": "template",
  "altText": "this is a confirm template",
  "template": {
      "type": "confirm",
      "text": "Are you sure?",
      "actions": [
          {
            "type": "message",
            "label": "Yes",
            "text": "จ้าา"
          },
          {
            "type": "message",
            "label": "No",
            "text": "โอเคร"
          }
      ]
  }
}
  )     
        

        
        
   # msgs = []
  #  for text in textList:
           #  msgs.append({
            #"type":"text",
            ###"text": text
            #"text":"สวัสดีคร้าบบบ ผมกอดอุ่น ยินดีให้บริการครับ"
           # "type":"sticker",
           #  "packageId": "1",
           #  "stickerId": "1"
            ###"text": text
            
       # })
        
        
    data = json.dumps({
       "replyToken": replyToken,
       "messages": msgs14
       
    })
    requests.post(LINE_API, headers=headers, data=data)
    return


if __name__ == '__main__':
    app.run()