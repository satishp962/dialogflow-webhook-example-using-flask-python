## DialogFlow webhook example using Flask in Python

This repository contains the flask app that serves as a webhook for Dialogflow chatbot

The app.py contains the flask app script.

You can run the webhook using the **ngrok** tunneling tool. Steps to run the webhook.

 - Run the flask app
	 - `python app.py or flask app.py`
 - The flask app will be served on th localhost with the 5000 defualt port. ex. `http://localhost:5000`
 - Run the Ngrok tool using the following command
	 - `ngrok http 5000`
 - The ngrok will generate a random url for the webhook. ex. `http://e5c224e2.ngrok.io`. 
 - There is a time limitation if you have not registered on ngrok.io. Register to remove the time limit. It's free.
 - You can inspect the requests on `localhost:4040`
 - Now add the ngrok generated URL in the Dialogflow webhook url options and hit the save button.
 - That's it now your dialogflow bot is able to communicate with the webhook.

**See this repo for response JSON formats for Rich Responses:** https://github.com/dialogflow/fulfillment-webhook-json
 

