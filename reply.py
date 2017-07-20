import tweepy, serial, request, settings
from time import sleep

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status_id_old = 0
ser = serial.Serial('/dev/ttyACM0',9600)
ser.write("*".encode())

def serial_reply(serial_send,twitter_send):
    ser.write(serial_send)
    print("Serial OK")
    reply_text = "@"+screen_name+" "+twitter_send
    api.update_status(status = reply_text,in_reply_to_status_id = status_id)
    print("Reply OK!")

while True:
    timeline = api.mentions_timeline()
    for status in timeline:
        status_id = status.id
        print(status_id,status_id_old)

        if status_id > status_id_old:#Reply分析
            screen_name = status.author.screen_name
            status_text = status.text
            reply_text = status_text.replace('@awdaawvBot ','')
            status_id_old = status_id
            print(screen_name)
            print(reply_text)

            if screen_name == 'fraunet_':
                if reply_text == 'ぬべちょんぬ':
                    serial_reply(b"1","エアコンを起動しました")
                elif reply_text == 'シノアエアコン消して':
                    serial_reply(b"2","エアコンを停止しました")
                elif reply_text == 'シノア室温教えて':
                    temp = str(request.temp)
                    hum = str(request.hum)
                    reply_text = "@"+screen_name+" "+"現在の室温は"+temp+"C、湿度は"+hum+"% ですよ"
                    api.update_status(status = reply_text,in_reply_to_status_id = status_id)
                    print("Reply OK!")
        else:
            print("待機しています")
    sleep(30)
