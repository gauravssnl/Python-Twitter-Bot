# Python-Twitter-Bot
Python Twitter Bot 

1. To use this bot,you need to have Python 3 installed .This bot uses twweepy module.You can install tweepy by using pip.To install tweepy, use this command :

 $ pip install tweepy

2. Now,you need to create a new application on Twitter. Either you can use your existing account or you can create a new one.Creating a new account for bot  is better so that your original Twitter account does not get banned.To create a new application on Twitter,open this URL in your browser :
 https://apps.twitter.com/

3. Fill all details required to create the new app.After that ,click on "Key and Access Token" tab under app settings.You will get your app's Consumer Key (API Key , Consumer Secret (API Secret) .You also need to get Access Token and Access Token Secret of your app.We will use these valuse in next step.You need to generate Access Token for first time.


4. Edit credentials.py and copy-paste  all your details carefully.


5. Now,you can run  twitterbot_text.py file to run bot which will tweet The Zen of Python texts by using this command :


 $ python twitterbot_text.py 


6.You can also use any file instead of sample.txt . To do that,you need to open twitterbot_text.py file and edit this line my_file=open('sample.txt','r') and enter your desired filename instead of 'sample.txt' .


7.Enjoy the service of Twitter Bot



