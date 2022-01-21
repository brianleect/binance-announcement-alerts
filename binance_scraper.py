import time
from time import sleep
import requests
from playsound import playsound
from datetime import datetime
import telegram as telegram
from params import token, chat_id, LISTING_ONLY , PRINT_DEBUG, TRIGGER_SOUND, CHECK_INTERVAL

# Initialize telegram bot
bot = telegram.Bot(token=token)

# Wrapper for sending tele message to me
def send_message(message):
    bot.send_message(chat_id=chat_id,text=message)

send_message("Scraper is running!")

r = requests.get("https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&pageNo=1&pageSize=5")
data = r.json()['data']['catalogs']

print("Intialization\n---------------------------------------")
# Initialization phase
initial_articles = []
for catalog in data:
    print("Title:",catalog['catalogName'])
    print(catalog['articles'][0]['title']) # Get first title of each category
    print()
    initial_articles.append(catalog['articles'][0]['title'])

print("----------------------------------------------------")

#initial_articles = ['','','','','',''] # Used for testing 

count=0 # Tracks total number of times we request
changes = 0 # Tracks total number of article change detected

while True:
    start = time.time()
    print("Time to get request:",time.time()-start)

    try:
        r = requests.get("https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&pageNo=1&pageSize=5")
        data = r.json()['data']['catalogs']
    except:
        with open("output.txt", "a") as f:
            print("Error triggered",file=f)
            print("Current Time:",datetime.now(),file=f)

        send_message("Error triggered retrying in 5s")

        sleep(5) # Running code usually solves problem so it should work as well 
        continue

    i=0
    for index in range(0,len(data)):
        if data[index]['articles'][0]['title'] not in initial_articles: # Note: Latest article is data[index]['articles'][0],
            
            initial_articles.append(data[index]['articles'][0]['title']) # Adds it to list
            changes += 1 # Increments total number of changes recorded thus far
            if TRIGGER_SOUND: playsound('sound.wav')
            
            message ='Change found: {}\nCurrent Time: {}\nTime taken: {}'.format(data[index]['articles'][0]['title'],datetime.now(),time.time()-start)
            print(message)
            if not LISTING_ONLY: send_message(message)
            elif index == 0: send_message(message) # Only sends listing since LISTING_ONLY has to be True + index==0 for listing

            initial_articles[i] = data[index]['articles'][0]['title'] # Updates list

        i+=1 # Used to track current index
    count+=1 
    if PRINT_DEBUG: print("Loop time taken:",time.time()-start)
    if PRINT_DEBUG: print("Pings:",count,"Changes:",changes)
    sleep(CHECK_INTERVAL)


