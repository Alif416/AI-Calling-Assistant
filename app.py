from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, AI Chat!'

if __name__ == '__main__':
    app.run(debug=True)
    
from whisper_handler import transcribe_bangla
print(transcribe_bangla("Audio.mp3"))