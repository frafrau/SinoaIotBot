import tweepy, serial, request, settings
from time import sleep

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status_id_old1 = 887852672006602752
ser = serial.Serial('/dev/ttyACM0',9600)
ser.write("*".encode())

def reply(twitter_send):
    reply_text = "@"+screen_name+" "+twitter_send
    api.update_status(status = reply_text,in_reply_to_status_id = status_id)
    print("Reply OK!")

def main(status_id,screen_name):
    if screen_name == 'fraunet_':
        if tweet_text == 'ぬべちょんぬ':
            ser.write(b"1")
            reply("エアコンを起動しました")
        elif tweet_text == 'シノアエアコン消して':
            ser.write(b"2")
            reply("エアコンを停止しました")
        elif tweet_text == 'シノア室温教えて':
            temp = str(request.temp)
            hum = str(request.hum)
            tweet_send = "現在の室温は"+temp+"C、湿度は"+hum+"% ですよ"
            reply(tweet_send)

while True:
    timeline = api.mentions_timeline(count=5)[::-1]
    #home = api.home_timeline(count=5)[::-1]
    #status = timeline
    for status in timeline:

        status_id = status.id
        print(status_id,status_id_old1)

        if status_id > status_id_old1:#Reply分析
            screen_name = status.author.screen_name
            status_text = status.text
            tweet_text = status_text.replace('@awdaawvBot ','')
            status_id_old1 = status_id
            print(screen_name)
            print(tweet_text)
            main(status_id,screen_name)

    sleep(60)
