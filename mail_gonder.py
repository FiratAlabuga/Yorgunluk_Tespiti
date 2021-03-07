import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
import json

def SendMail(ImgFileName):
    fromaddr="hunterkiller0421@gmail.com"  #sender gmail address
    toaddr="jfa3476@gmail.com"   #reciver gmail address
    send_url = "http://api.ipstack.com/check?access_key='Your API Key"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    enlem = geo_json['latitude']
    boylam = geo_json['longitude']
    sehir = geo_json['city']
    msg=MIMEMultipart()
    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']="Şoför Tespit Görseli"
    body=f"Şoförün direksiyon başında uyukladığı tespit edildi. Şoförün Konumu : {enlem} , {boylam} , {sehir}"
    msg.attach(MIMEText(body,'plain'))
    filename="sofor.jpg"
    attachment=open("sofor.jpg","rb") #image folder


    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
    msg.attach(p)

    s=smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()


    text=msg.as_string()

    s.sendmail(fromaddr,toaddr,text)

    s.quit()
