import os
from flask import Flask, request, render_template
from model import model, extract_features, emotions
from pydub import AudioSegment
import mysql.connector

app = Flask(__name__)

# Function to predict emotion from audio file
def predict_emotion(audio_file):
    try:
        # Extract features from audio file
        features = extract_features(audio_file)
        if features is not None:
            # Predict emotion using the loaded model
            predicted_emotion_index = model.predict(features.reshape(1, -1))[0]
            predicted_emotion = emotions[predicted_emotion_index]
            return predicted_emotion
        else:
            return "Error extracting features from audio"
    except Exception as e:
        return str(e)

# Function to save result in the database
def save_result_in_database(audio_file_name, predicted_emotion):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Devalla@1234",
            database="emotion_recognition_db"
        )
        cursor = connection.cursor()
        sql_query = "INSERT INTO emotion_results (audio_file_name, predicted_emotion) VALUES (%s, %s)"
        cursor.execute(sql_query, (audio_file_name, predicted_emotion))
        connection.commit()
        connection.close()
    except Exception as e:
        print("Error:", e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file part")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No selected file")
        if file:
            try:
                # Save the uploaded audio file
                audio_path = "uploaded_audio.wav"
                file.save(audio_path)
                # Predict emotion from the uploaded audio file
                emotion = predict_emotion(audio_path)
                # Save the result in the database
                save_result_in_database(file.filename, emotion)
                os.remove(audio_path)  # Remove the temporary audio file
                return render_template('result.html', emotion=emotion)
            except Exception as e:
                return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
