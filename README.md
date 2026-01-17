# Batch Speech-to-Text Transcription using Faster-Whisper

This project provides a **fully open-source, offline speech-to-text implementation** using **faster-whisper**. It processes multiple **`.m4a` audio files** from an input folder and generates **text document files** (`.txt`) in an output folder with timestamps and metadata.

---

## 🚀 Features

- **100% Offline Transcription** - No API keys, no internet connection required
- **Batch Processing** - Transcribe multiple audio files automatically
- **High Performance** - Uses faster-whisper (optimized version of OpenAI's Whisper)
- **Voice Activity Detection (VAD)** - Automatically filters out silence
- **Timestamped Output** - Each transcript includes precise timestamps
- **Language Detection** - Automatically detects spoken language
- **Multiple Output Formats** - Timestamped and plain text versions
- **Comprehensive Metadata** - Duration, language probability, processing date
- **Error Handling** - Continues processing even if individual files fail

---

## 📁 Project Structure

```text
stt/
│
├── audio/                 # Input folder containing audio files
│   ├── Anjani_.m4a
│   ├── chutki akka 1.m4a
│   ├── chutki akka 2 .m4a
│   ├── dimple friend .m4a
│   ├── Dolly Akka .m4a
│   ├── graphic designer .m4a
│   ├── Pavitra Dad 1.m4a
│   ├── Pavitra Dad 2.m4a
│   ├── R.k sir .m4a
│   ├── recruiter .m4a
│   ├── Ruch✨️ 2.m4a
│   ├── Ruch✨️1.m4a
│   ├── surya friend.m4a
│   ├── Vinni Anna 1.m4a
│   ├── Vinni Anna 2.m4a
│   └── Vinni Anna 3.m4a
│
├── transcripts/           # Output folder (auto-created)
│   ├── Anjani_.txt
│   ├── chutki akka 1.txt
│   └── ...
│
├── transcribe.py          # Main transcription script
├── requirements.txt       # Python dependencies
└── README.md              # This file

```

---

## 📋 Prerequisites

- **Python 3.8+** (Python 3.9 or higher recommended)
- **pip** (Python package installer)
- **~1GB disk space** for model files (downloaded automatically on first run)
- **Sufficient RAM** - Minimum 4GB RAM (8GB+ recommended for larger models)

### Optional (for GPU acceleration):
- **CUDA-compatible GPU** (NVIDIA)
- **CUDA Toolkit 11.x or 12.x**

---

## 🛠️ Installation

### Step 1: Clone or Download the Project

If you have this project locally, navigate to the project directory:

```bash
cd c:\Users\tj_20\Desktop\personal\stt
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `faster-whisper` - The core transcription library
- `ctranslate2` - Inference engine (installed as dependency)
- Other required dependencies

### Step 4: Verify Installation

```bash
python -c "from faster_whisper import WhisperModel; print('Installation successful!')"
```

---

## 🎯 Usage

### Basic Usage

Simply run the transcription script:

```bash
python transcribe.py
```

This will:
1. Load the Whisper model (downloaded automatically on first run)
2. Scan the `audio/` folder for all `.m4a` files
3. Transcribe each audio file
4. Save transcripts to the `transcripts/` folder
5. Display progress in the terminal

### Expected Output

```
================================================================================
Batch Speech-to-Text Transcription using Faster-Whisper
================================================================================

Loading Faster-Whisper model: base
Device: cpu, Compute Type: int8

Found 16 audio file(s) to transcribe.

[1/16] Processing: Anjani_.m4a
✓ Saved transcription to: transcripts\Anjani_.txt

[2/16] Processing: chutki akka 1.m4a
✓ Saved transcription to: transcripts\chutki akka 1.txt

...

================================================================================
Transcription complete!
All transcripts saved to: transcripts/
```

---

## ⚙️ Configuration

You can customize the transcription settings by editing the configuration section in `transcribe.py`:

```python
# Model options: "tiny", "base", "small", "medium", "large-v2", "large-v3"
MODEL_SIZE = "base"

# Device options: "cpu" or "cuda" (for GPU)
DEVICE = "cpu"

# Compute type: "int8" (fastest, CPU), "float16" (GPU), "float32" (highest quality)
COMPUTE_TYPE = "int8"
```

### Model Size Comparison

| Model     | Size   | Speed  | Accuracy | Best For                    |
|-----------|--------|--------|----------|-----------------------------|
| `tiny`    | ~75MB  | Fastest| Low      | Quick tests, low resource   |
| `base`    | ~145MB | Fast   | Good     | General use (default)       |
| `small`   | ~466MB | Medium | Better   | Higher accuracy needed      |
| `medium`  | ~1.5GB | Slow   | High     | Professional transcription  |
| `large-v2`| ~3GB   | Slowest| Highest  | Maximum accuracy            |
| `large-v3`| ~3GB   | Slowest| Highest  | Latest, best quality        |

### GPU Acceleration (Optional)

If you have an NVIDIA GPU with CUDA installed:

```python
DEVICE = "cuda"
COMPUTE_TYPE = "float16"
```

This can provide **5-10x faster** transcription speeds.

---

## 📄 Output Format

Each transcription file contains:

### 1. **Header Section** (Metadata)
```
Transcription of: Anjani_.m4a
Date: 2026-01-17 14:30:45
Language: en (probability: 0.98)
Duration: 123.45 seconds
================================================================================
```

### 2. **Timestamped Transcription**
```
TIMESTAMPED TRANSCRIPTION:
--------------------------------------------------------------------------------

[0.00s -> 3.45s]
Hello, how are you doing today?

[3.45s -> 7.23s]
I'm doing great, thanks for asking.

...
```

### 3. **Full Text (No Timestamps)**
```
================================================================================
FULL TRANSCRIPTION (no timestamps):
================================================================================

Hello, how are you doing today? I'm doing great, thanks for asking. ...
```

---

## 🔧 Advanced Configuration

### VAD (Voice Activity Detection) Parameters

Edit the `vad_parameters` in `transcribe.py` to fine-tune silence detection:

```python
segments, info = model.transcribe(
    str(audio_file),
    beam_size=5,
    vad_filter=True,
    vad_parameters=dict(
        min_silence_duration_ms=500,  # Minimum silence duration (ms)
        threshold=0.5,                # VAD threshold (0-1)
        min_speech_duration_ms=250    # Minimum speech duration (ms)
    )
)
```

### Beam Size

Higher beam size = more accurate but slower:

```python
beam_size=5  # Default, good balance
beam_size=1  # Fastest, greedy decoding
beam_size=10 # Most accurate, slower
```

### Language Specification

Force a specific language instead of auto-detection:

```python
segments, info = model.transcribe(
    str(audio_file),
    language="en",  # Force English
    # Other options: "es", "fr", "de", "hi", "zh", etc.
)
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'faster_whisper'"

**Solution:**
```bash
pip install --upgrade faster-whisper
```

### Issue: Model download is slow or failing

**Solution:** The model is downloaded automatically on first run. If it fails:
1. Check your internet connection
2. Clear the cache: Delete `~/.cache/huggingface/` (Linux/Mac) or `%USERPROFILE%\.cache\huggingface\` (Windows)
3. Try again

### Issue: "Out of memory" error

**Solution:**
1. Use a smaller model (e.g., `tiny` or `base`)
2. Close other applications
3. Increase system RAM or use swap space

### Issue: Transcription is very slow

**Solutions:**
1. Use a smaller model (`tiny` or `base`)
2. Enable GPU acceleration if available
3. Reduce beam size to 1
4. Use `compute_type="int8"` for CPU

### Issue: Transcription quality is poor

**Solutions:**
1. Use a larger model (`medium` or `large-v3`)
2. Ensure audio quality is good (clear, minimal background noise)
3. Increase beam size to 10
4. Specify the correct language manually

### Issue: Some audio files fail to process

**Solution:** The script continues even if individual files fail. Check:
1. File is not corrupted
2. File format is supported (`.m4a`, `.mp3`, `.wav`, `.flac`, etc.)
3. File is not empty or too short
4. Check the error message for specific issues

---

## 🎓 How It Works

1. **Model Loading**: Faster-Whisper loads the specified model (downloads on first run)
2. **Audio Processing**: Each audio file is converted to the format Whisper expects
3. **Voice Activity Detection**: VAD filters out silence and non-speech segments
4. **Transcription**: The model processes audio in segments and generates text
5. **Language Detection**: The model automatically detects the spoken language
6. **Output Generation**: Results are formatted and saved to text files

### Technologies Used

- **Faster-Whisper**: Optimized implementation of OpenAI's Whisper using CTranslate2
- **CTranslate2**: Fast inference engine for Transformer models
- **Silero VAD**: Voice Activity Detection to filter silence
- **Python 3**: Core programming language

---

## 📊 Performance Tips

1. **First Run**: Model download takes time (5-30 minutes depending on size)
2. **Subsequent Runs**: Model is cached, transcription starts immediately
3. **Batch Processing**: Processing 16 files takes ~10-60 minutes depending on:
   - Model size
   - Audio duration
   - CPU/GPU performance
   - Audio quality

### Estimated Transcription Times (Base Model, CPU)

| Audio Duration | Transcription Time |
|----------------|-------------------|
| 1 minute       | ~30 seconds       |
| 10 minutes     | ~5 minutes        |
| 60 minutes     | ~30 minutes       |

*Times vary significantly based on hardware and model size*

---

## 🔒 Privacy & Security

- **100% Offline**: All processing happens locally on your machine
- **No Data Transmission**: Audio files never leave your computer
- **No API Keys**: No external services or accounts required
- **No Logging**: No usage data is collected or transmitted

---

## 📝 Supported Audio Formats

While this project is configured for `.m4a` files, faster-whisper supports:

- `.m4a` (Apple Audio)
- `.mp3` (MPEG Audio)
- `.wav` (Waveform Audio)
- `.flac` (Free Lossless Audio Codec)
- `.ogg` (Ogg Vorbis)
- `.aac` (Advanced Audio Coding)

To process other formats, modify the glob pattern in `transcribe.py`:

```python
# For multiple formats:
audio_files = list(input_path.glob("*.m4a"))
audio_files += list(input_path.glob("*.mp3"))
audio_files += list(input_path.glob("*.wav"))
```

---

## 🤝 Contributing

Feel free to:
- Report bugs or issues
- Suggest new features
- Improve documentation
- Optimize performance

---

## 📚 Additional Resources

- [Faster-Whisper Documentation](https://github.com/guillaumekln/faster-whisper)
- [OpenAI Whisper Paper](https://arxiv.org/abs/2212.04356)
- [CTranslate2 Documentation](https://opennmt.net/CTranslate2/)

---

## ⚖️ License

This project uses open-source libraries:
- Faster-Whisper: MIT License
- OpenAI Whisper: MIT License

---

## 🎉 Getting Started Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Audio files in `audio/` folder
- [ ] Run `python transcribe.py`
- [ ] Check `transcripts/` folder for results

---

**Happy Transcribing! 🎤✨**
