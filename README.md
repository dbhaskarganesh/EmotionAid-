# 🎙️ Emotion Speech Recognition for Disorder Speech

Emotion_Speech_Recognition_for_Disorder_Speech is an advanced emotion recognition system that leverages **signal processing** and **machine learning** techniques to analyze speech patterns in disordered speech. This tool aims to enhance applications in **mental health, assistive communication, and AI-driven interactions**, enabling a more **empathetic and intelligent** human-computer experience.

---

## 🚀 Key Features  

✅ **Emotion Detection for Disordered Speech** – Identifies emotions such as happiness, sadness, anger, and fear with high precision.  
✅ **Advanced Signal Processing** – Extracts meaningful speech features using industry-standard techniques.  
✅ **Machine Learning-Powered** – Utilizes **deep learning models** for enhanced recognition.  
✅ **Real-Time Analysis** – Processes live or recorded audio input for **instant** emotion classification.  
✅ **Database Integration** – Stores results in a **MySQL** database for further analysis.  

---

## 🏗️ Tech Stack  

- **Programming Language:** Python 🐍  
- **Libraries & Frameworks:** Flask, TensorFlow, Scikit-learn  
- **Audio Processing:** Librosa 🎵, pydub 🎧  
- **Database:** MySQL 🗄️  
- **Visualization:** Matplotlib, Seaborn 📊  

---

## 📦 Installation  

### 🔹 Prerequisites  
Ensure you have **Python 3.8+** installed.  

### 🔹 Setup Instructions  

1️⃣ Clone the repository:  
```bash
git clone https://github.com/yourusername/Emotion_Speech_Recognition_for_Disorder_Speech.git
cd Emotion_Speech_Recognition_for_Disorder_Speech
```

2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```

3️⃣ Set up the MySQL database:
```sql
CREATE DATABASE emotion;
USE emotion;
CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emotion VARCHAR(255),
    sample_rate INT,
    channels INT,
    decibel FLOAT,
    bit_depth INT,
    audio_length FLOAT
);
```

---

## 🚀 Usage  

### 🔹 Running the Application  

Run the Flask server:  
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.

### 🔹 Uploading an Audio File  
1. Open the web interface.  
2. Upload an audio file (.wav format recommended).  
3. View the detected emotion and audio information.  

### 🔹 Sample Output  
```
Detected Emotion: Happy 😊  
Confidence Score: 92%  
```

---

## 🤝 Contributing  

We welcome contributions! Please check our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

## 📄 License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact  

💡 **Developed by:** Devalla Bhaskar Ganesh  
📩 Email: devallabhaskarganesh@gmail.com  
🔗 LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/devallabhaskarganesh/)  
🌎 GitHub: [Your GitHub Profile](https://github.com/dbhaskarganesh/)  

