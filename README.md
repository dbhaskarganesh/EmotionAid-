Emotion_Speech_Recognition_for_Disorder_Speech



🎤 Introduction

Emotion_Speech_Recognition_for_Disorder_Speech is a Flask-based web application that processes audio recordings to recognize emotions in disordered speech. The system extracts features from audio files, predicts emotions using a machine learning model, and stores the results in a MySQL database.

✨ Features

🎵 Upload audio files via a web interface.

📊 Extract features such as sample rate, channels, decibel level, bit depth, and audio length.

🤖 Predict emotions using a trained machine learning model.

💾 Store results in a MySQL database.

🖥️ Display results on a web interface.

🛠 Technologies Used

Backend: Flask 🐍

Database: MySQL 🗄️

Machine Learning: Scikit-learn 🤖, TensorFlow 🔥

Audio Processing: pydub 🎼, librosa 🎧

⚡ Installation

Prerequisites

Ensure you have Python installed (>=3.7). Install the required dependencies:

pip install -r requirements.txt

🏛️ Database Setup

Install MySQL and create a database named emotion.

Create a table results inside the emotion schema using the following SQL query:

CREATE TABLE emotion.results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emotion VARCHAR(255),
    sample_rate INT,
    channels INT,
    decibel FLOAT,
    bit_depth INT,
    audio_length FLOAT
);

🚀 Usage

Running the Application

Start the Flask server:

python app.py

The application will be available at http://127.0.0.1:5000/.

🎤 Uploading an Audio File

Open the web browser and navigate to the application.

Upload an audio file (.wav format recommended).

View the detected emotion and audio information.

📂 Project Structure

Emotion_Speech_Recognition_for_Disorder_Speech/
│── app.py
│── model.py
│── templates/
│   ├── upload.html
│   ├── result.html
│── static/
│── requirements.txt
│── README.md

🤝 Contributing

If you want to contribute, fork the repository and submit a pull request.

📜 License

This project is licensed under the MIT License.

📧 Contact

👨‍💻 Author: Devalla Bhaskar Ganesh📩 Email: devallabhaskarganesh@gmail.com🔗 LinkedIn: linkedin.com/in/devallabhaskarganesh/

