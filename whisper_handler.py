import whisper

model= whisper.load_model("base")

def transcribe_bangla(audio_path):
    result = model.transcribe(audio_path, language='bn')
    return result['text']