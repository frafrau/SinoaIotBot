import tweepy, request, settings

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

temp = str(request.temp)
hum = str(request.hum)

tweet = "現在 室温"+temp+"C" "湿度"+hum+"% です"
api.update_status(tweet)
print("定期ツイートを行いました")
