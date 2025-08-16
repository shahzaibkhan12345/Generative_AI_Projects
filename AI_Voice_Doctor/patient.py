# Step1:Audio Recorder(ffmpeg or portaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path,timeout=20,phrase_time_limit=None):
    """
    Records audio from the microphone for a specified duration and saves it to a file.
    
    :param duration: Duration in seconds to record audio.
    :param filename: Name of the file to save the recorded audio.
    """
    recognizer = sr.Recognizer()
    try:
      with sr.Microphone() as source:
        logging.info("Recording audio...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        logging.info('Please start speaking...')
        audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        logging.info("Recording complete.")
        
        wav_data=audio_data.get_wav_data()
        audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
        audio_segment.export(file_path, format="mp3",bitrate='128k')
        logging.info(f"Audio saved to {file_path}")
    except Exception as e:
       logging.error(f'An error occured: {e}')
       
       audio_file_path='patient_test.mp3'       
       return record_audio(file_path=audio_file_path)
# Step 2:Setup Speech to Text Trascription

import os
from groq import Groq

groq_api_key=os.getenv('GROQ_API_KEY')
sttd_model="whisper-large-v3-turbo"
def Transcribe(audio_file_path,groq_api_key,sttd_model):
   client = Groq(api_key=groq_api_key)
   file=open(audio_file_path, "rb")
   transcription = client.audio.transcriptions.create(
   file=file,
   model=sttd_model,
   language='en'
   )
   return transcription.text
      