import requests
import json

def  emotion_detector (text_to_analyse):    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobject = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobject, headers=headers )

    formatted_response = json.loads(response.text)

    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        
    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']

    max_emotion = max(emotion_data, key=emotion_data.get)
    
    res = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': max_emotion
    }

    return res