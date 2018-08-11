# import flask modules
from flask import Flask, make_response, request, jsonify

# build the flask app
app = Flask(__name__)

# definition of the results function
def results():
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')

    if action == "<your_custom_action_name_from_dialogflow>":
        # your action statements here
        # do whatever you want
        # return response in dialogflow response format
        # i am going to use Dialogflow JSON reponse format
        # first build result json

        result = {} # an empty dictionary

        # fulfillment text is the default response that is returned to the dialogflow request
        result["fulfillmentText"] = "your response message here"

        # you can also make rich respones like basic card, simple responses, list, table card etc.
        # you can refer this for rich response formats
        # https://github.com/dialogflow/fulfillment-webhook-json

        # you can also use custom payloads for different services like messenger or google assistant
        # below is an example of google assistant payload
        # the following paylod contains a simple response, a basic card and some suggestion chips.

        reply["payload"] = {
            "google": {
            "expectUserResponse": True,
            "richResponse": {
                "items": [
                {
                    "simpleResponse": {
                        "displayText": 'text to be displayed',
                        "textToSpeech": 'text that will be used for text to speech'
                    }
                },
                {
                    "basicCard": {
                        "title": "card title",
                        "subtitle": "card subtitle",
                        "imageDisplayOptions": "WHITE"
                    }
                }
                ],
                "suggestions": [
                    {
                        "title": "chip 1"
                    },
                    {
                        "title": "chip 2"
                    }
                ],
            }
            }
        }
        
        # jsonify the result dictionary
        # this will make the response mime type to application/json
        result = jsonify(result)

        # return the result json
        return make_response(result)

# default route for the webhook
# it accepts both the GET and POST methods
@app.route('/webhook', methods=['GET', 'POST'])
def index():
    # calling the result function for response
    return results()

# call the main function to run the flask app
if __name__ == '__main__':
   app.run(debug=True)