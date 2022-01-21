 #### Kucoin-bot-assistor-python ####
 <br> 
This is a simple python script using selenium that will do the following: 
<br>
1. Log you into kucoin (requires user to complete captcha and or 2FA)<br>
2. Create a spot grid bot using the highest returning bot for the day using 100% of the USDT in the users' trading account <br>
3. Automatically take profit at the specified amount (default is 1.0%) <br>
4. Automatically Sell at a loss equal to or greater than the specified amount (default is 4.5%)<br>
5. Upon taking profit or selling, re-create a new spot grid bot, starting from step 2 and repeating forever. <br> <br>

Use at your own risk, while this tends to get better returns than simply leaving a bot running on kucoin, it is possible to loose with it, especially since it can get into sell loops if the asset being botted is dumping significantly enough. 
<br>
### this script is intended to be watched and used as a tool to help you with your bot trading, NOT to be ran without some supervision! ### 
