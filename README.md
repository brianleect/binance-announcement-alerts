# Binance Listing Alerts

NOTE THIS IS NO LONGER WORKING DUE TO POSSIBLE CHANGES ON BINANCE SIDE. This project was done about 6 months back and is no longer updated. 

While it was functioning, notifications were consistently received 30s to 1/2m in advance.

Old telegram channel: https://t.me/early_binance_announcements 
\n(Note that in the recent few week / month or two, the notifications were no longer faster than the official channels)
\n(The scraper is no longer being ran due to it no longer having an edge)

## Intent
Considering how fast crypto markets move and the impact listing on a major exchange has on price, getting information of the listing in the shortest time possible can be rather profitable.

This was thus created to ensure I receive the latest announcements from binance at the fastest possible time.

![image](https://user-images.githubusercontent.com/63389110/126191370-1db29746-f0e8-4735-bc82-596078dcea4f.png)

^ Example of a detected announcement **20 seconds in advance**.

## Feature
1. **Early detection** of new announcements (Sometimes a few minutes in advance) (Average 5-15s in advance)
2. Telegram updates
3. Listing Only Updates (Ignores all announcements except listings, reduces spam)

## Usage
1. In command line run ```pip install -r requirements.txt``` while located at folder with code.
2. Get telegram bot token from @botfather https://t.me/BotFather
3. Get telegram chat_id from @get_id_bot https://telegram.me/get_id_bot (Alternatively channel id can be used as well which is shown in demo)
4. Input telegram token details into '''params.py''' file
5. Set options in params.py to personal preference (Default works as well)
6. Run '''binance_scraper.py'''
Purpose: Scrapes binance annoucement page for updates on news

## Possible future todos
1. Send buy request on non-binance exchanges the moment a listing is detected
2. Integrate multiple exchanges for their updates
