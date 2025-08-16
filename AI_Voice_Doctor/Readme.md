# AI Voice Doctor

An interactive AI-powered medical consultation system that combines computer vision, speech recognition, and text-to-speech capabilities to provide a simulated doctor-patient interaction experience.

## 🏥 Features

- **Voice Input**: Record your symptoms or medical concerns using your microphone
- **Image Analysis**: Upload medical images (skin conditions, etc.) for AI analysis
- **AI Medical Consultation**: Get AI-generated medical insights and recommendations
- **Voice Response**: Receive spoken responses from the AI doctor
- **Web Interface**: User-friendly Gradio web interface for easy interaction

## 🚀 How It Works

1. **Voice Recording**: Speak your symptoms or medical concerns
2. **Speech-to-Text**: Your voice is converted to text using Whisper
3. **Image Analysis**: Upload medical images for visual analysis
4. **AI Processing**: The system combines your voice input and image for comprehensive analysis
5. **Medical Response**: AI generates a professional medical response
6. **Voice Output**: The response is converted to speech and played back

## 📋 Prerequisites

- Python 3.7+
- Microphone access
- Internet connection
- Groq API key

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AI_Voice_Doctor
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   - Copy the example environment file:
     ```bash
     cp env.example .env
     ```
   - Edit the `.env` file and add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

## 🔑 API Key Setup

1. Sign up for a Groq account at [https://console.groq.com/](https://console.groq.com/)
2. Generate an API key from your dashboard
3. Add the API key to your environment variables or `.env` file

## 🎯 Usage

1. **Run the application**:
   ```bash
   python gradio_app.py
   ```

2. **Open your web browser** and navigate to the provided local URL (usually `http://127.0.0.1:7860`)

3. **Using the interface**:
   - Click the microphone button to record your voice
   - Upload a medical image (optional)
   - Click "Submit" to process your inputs
   - Listen to the AI doctor's response

## 📁 Project Structure

```
AI_Voice_Doctor/
├── gradio_app.py          # Main Gradio web interface
├── brain.py              # Image analysis and AI processing
├── patient.py            # Voice recording and speech-to-text
├── voice_of_doctor.py    # Text-to-speech functionality
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── ffmpeg.exe           # Audio processing (Windows)
├── ffplay.exe           # Audio playback (Windows)
├── ffprobe.exe          # Audio metadata (Windows)
└── README.md            # This file
```

## 🔧 Technical Details

### Core Components

- **`gradio_app.py`**: Main application with Gradio interface
- **`brain.py`**: Handles image encoding and AI analysis using Groq's multimodal LLM
- **`patient.py`**: Manages audio recording and speech-to-text transcription
- **`voice_of_doctor.py`**: Converts AI responses to speech using gTTS

### AI Models Used

- **Vision Model**: `meta-llama/llama-4-scout-17b-16e-instruct` for image analysis
- **Speech-to-Text**: `whisper-large-v3-turbo` for voice transcription
- **Text-to-Speech**: Google Text-to-Speech (gTTS) for voice synthesis

## ⚠️ Important Notes

- **Educational Purpose Only**: This system is designed for learning and demonstration purposes
- **Not Medical Advice**: The AI responses should not be considered as professional medical advice
- **Privacy**: Be cautious when uploading medical images and ensure they don't contain sensitive information
- **API Limits**: Be aware of Groq API usage limits and costs

## 🐳 Docker Support

The project includes a Dockerfile for containerized deployment:

```bash
# Build the Docker image
docker build -t ai-voice-doctor .

# Run the container
docker run -p 7860:7860 -e GROQ_API_KEY=your_key ai-voice-doctor
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is for educational purposes. Please ensure compliance with all applicable laws and regulations when using this software.

## 🆘 Troubleshooting

### Common Issues

1. **Microphone not working**: Ensure microphone permissions are granted to your browser/application
2. **API key errors**: Verify your Groq API key is correctly set in environment variables
3. **Audio playback issues**: Check if your system's audio is working and volume is up
4. **Image upload problems**: Ensure the image format is supported (JPEG, PNG, etc.)

### Getting Help

If you encounter any issues, please:
1. Check the console output for error messages
2. Verify all dependencies are installed correctly
3. Ensure your API key is valid and has sufficient credits
4. Check your internet connection

## 🔮 Future Enhancements

- Support for multiple languages
- Integration with medical databases
- Enhanced image analysis capabilities
- Mobile app version
- Real-time video consultation features

