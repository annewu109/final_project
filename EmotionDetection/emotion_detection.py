import json
import requests

def emotion_detector(text_to_analyze):
    """Returns the emotions detected from string text_to_analyze"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json = json_input, headers = header)
    json_response = response.json()

    #find all emotion scores
    anger_score = json_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = json_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = json_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = json_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = json_response['emotionPredictions'][0]['emotion']['sadness']
    
    #insert emotion scores into dictionary
    dict_to_return = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    # find dominant emotion
    dominant_emotion = max(dict_to_return, key=dict_to_return.get)

    dict_to_return['dominant_emotion'] = dominant_emotion

    return dict_to_return