"""
Initalizes the emotion detector function to be run on a 
Flask channel and deployed on localhost:5000
"""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emot_detect():
    """
    Receives text input from a html from within index.html and runs emotion detection
    on that text with emotion_detector(). Formats output showing the emotions scores for
    anger, disgust, fear, joy and sadness, and the strongest emotion for the string
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if not response['dominant_emotion']:
        response_msg = "Invalid text! Please try again!"
    else:
        response_msg = (
            "For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} "
            f"and 'sadness': {response['sadness']}. "
            f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>."
        )

    return response_msg

@app.route('/')
def render_index_page():
    """Initalizes rendering of main application page with flask"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
