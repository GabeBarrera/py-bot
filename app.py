import requests, json, twilio, config
from config import APP_ID,SUB_KEY,SID,AUTH_TOKEN,GABE,BOT
from twilio.rest import Client  

# M.E.L.I.N.A. Tokens
query = input('Input query: ')
url1 = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/"
url2 = "?verbose=true&timezoneOffset=-360&subscription-key="
app_id = str(APP_ID)
sub_key = str(SUB_KEY)
url = url1+app_id+url2+sub_key+"&q="+query

client = Client(SID, AUTH_TOKEN)

message = client.messages \
    .create(
        body='Test',
        from_=BOT,
        to=GABE
    )
print(message.sid)

# r = requests.get(url)
# y = json.loads(r.text)
# print(y["topScoringIntent"]["intent"])
# print(y["sentimentAnalysis"]["label"])
# print(r.text)

