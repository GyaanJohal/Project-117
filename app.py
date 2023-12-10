# This code is importing necessary modules and functions for the Flask web application.
from flask import Flask, render_template, request, jsonify
from text_sentiment_prediction import *

# `app = Flask(__name__)` creates an instance of the Flask class and assigns it to the variable `app`.
# The `__name__` argument is a special Python variable that represents the name of the current module.
# By passing `__name__` as an argument, Flask knows where to find the static and template files for
# the application.
app = Flask(__name__)


# `@app.route('/')` is a decorator in Flask that associates a URL route with a function. In this case,
# it associates the root URL ("/") with the `index()` function. So when a user visits the root URL of
# the web application, the `index()` function will be executed and the returned value will be
# displayed in the browser.
@app.route('/')
def index():
    """
    The function returns the rendered template for the index.html file.
    :return: the result of the `render_template('index.html')` function call.
    """
    return render_template('index.html')
 
# `@app.route('/predict-emotion', methods=["POST"])` is a decorator in Flask that associates the URL
# route "/predict-emotion" with the `predict_emotion()` function. It specifies that the function
# should be executed when a POST request is made to the "/predict-emotion" URL.
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    """
    The function `predict_emotion()` takes input text from a POST request, predicts the emotion
    associated with the text, and returns the predicted emotion and an image URL representing the
    emotion.
    :return: a JSON response. If the input text is undefined, it returns an error response with a
    message. If the input text is defined, it returns a success response with the predicted emotion and
    the URL of an image representing the predicted emotion.
    """
    
    # Get Input Text from POST Request
    input_text = request.json.get("text")  
    
    if not input_text:
        # Response to send if the input_text is undefined
        response = {
                    "status": "error",
                    "message": "Please enter some text to predict emotion!"
                  }
        return jsonify(response)
    else:  
        predicted_emotion,predicted_emotion_img_url = predict(input_text)
        
        # Response to send if the input_text is not undefined
        response = {
                    "status": "success",
                    "data": {
                            "predicted_emotion": predicted_emotion,
                            "predicted_emotion_img_url": predicted_emotion_img_url
                            }  
                   }

        # Send Response         
        return jsonify(response)
       
# `app.run(debug=True)` starts the Flask development server. The `debug=True` argument enables debug
# mode, which provides more detailed error messages and automatically reloads the server when changes
# are made to the code. This is useful during development to quickly see any errors and test changes
# without manually restarting the server.
app.run(debug=True)



    