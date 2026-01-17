# Audio Transcription & PDF Conversion Pipeline

This project provides a **complete end-to-end solution** for converting audio recordings to professional PDF documents. It consists of two main components:

1. **Speech-to-Text Transcription** - Converts audio files (`.m4a`) to text using faster-whisper
2. **Text-to-PDF Conversion** - Transforms transcription text files into formatted PDF documents

**100% offline, no API keys required, fully open-source.**

---

## 🚀 Features

### Speech-to-Text (transcribe.py)

- **100% Offline Transcription** - No API keys, no internet connection required
- **Batch Processing** - Transcribe multiple audio files automatically
- **High Performance** - Uses faster-whisper (optimized version of OpenAI's Whisper)
- **Voice Activity Detection (VAD)** - Automatically filters out silence
- **Timestamped Output** - Each transcript includes precise timestamps
- **Language Detection** - Automatically detects spoken language
- **Comprehensive Metadata** - Duration, language probability, processing date

### Text-to-PDF Converter (txt_to_pdf.py)

- **Professional PDF Generation** - Clean, formatted PDF documents
- **Automatic Styling** - Headers, timestamps, metadata sections
- **Batch Conversion** - Process all transcripts at once
- **Unicode Support** - Handles special characters and emojis
- **Page Management** - Automatic page breaks and spacing
- **Configurable Layout** - Customizable fonts, sizes, and page formats

### General

- **Error Handling** - Continues processing even if individual files fail
- **Progress Tracking** - Real-time feedback during processing
- **Flexible Configuration** - Easy customization for different use cases

---

## 📁 Project Structure

```text
stt/
│
├── audio/                 # Input folder - place audio files here
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
├── transcripts/           # Intermediate folder - text transcriptions
│   ├── Anjani_.txt
│   ├── chutki akka 1.txt
│   └── ...
│
├── output/                # Final folder - PDF documents
│   ├── Anjani_.pdf
│   ├── chutki akka 1.pdf
│   └── ...
│
├── transcribe.py          # Speech-to-text transcription script
├── txt_to_pdf.py          # Text-to-PDF conversion script
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
├── venv/                  # Virtual environment (created during setup)
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
- `reportlab` - PDF generation library
- `ctranslate2` - Inference engine (installed as dependency)
- Other required dependencies

### Step 4: Verify Installation

```bash
python -c "from faster_whisper import WhisperModel; from reportlab.pdfgen import canvas; print('Installation successful!')"
```

---

## 🎯 Complete Workflow

### Full Pipeline: Audio → Text → PDF

The complete process involves two steps:

```bash
# Step 1: Transcribe audio files to text
python transcribe.py

# Step 2: Convert text files to PDFs
python txt_to_pdf.py
```

### Quick Start Guide

1. **Place audio files** in the `audio/` folder
2. **Run transcription**: `python transcribe.py`
   - Creates text files in `transcripts/` folder
3. **Generate PDFs**: `python txt_to_pdf.py`
   - Creates PDF files in `output/` folder
4. **Done!** Check the `output/` folder for your PDF documents

---

## 📝 Usage Details

### Part 1: Speech-to-Text Transcription

#### Basic Usage

```bash
python transcribe.py
```

#### Expected Output

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

#### Text File Format

Each `.txt` file contains:

```
Transcription of: Anjani_.m4a
Date: 2026-01-17 14:30:45
Language: en (probability: 0.98)
Duration: 123.45 seconds
================================================================================

TIMESTAMPED TRANSCRIPTION:
--------------------------------------------------------------------------------

[0.00s -> 3.45s]
Hello, how are you doing today?

[3.45s -> 7.23s]
I'm doing great, thanks for asking.

...

================================================================================
FULL TRANSCRIPTION (no timestamps):
================================================================================

Hello, how are you doing today? I'm doing great, thanks for asking. ...
```

### Part 2: Text-to-PDF Conversion

#### Basic Usage

```bash
python txt_to_pdf.py
```

#### Expected Output

```
================================================================================
Text to PDF Converter
================================================================================

Found 16 text file(s) to convert.

[1/16] Converting: Anjani_.txt
✓ Saved PDF to: output\Anjani_.pdf

[2/16] Converting: chutki akka 1.txt
✓ Saved PDF to: output\chutki akka 1.pdf

...

================================================================================
Conversion complete!
Successfully converted: 16 file(s)
All PDFs saved to: output/
```

#### PDF Features

- **Professional Layout** with headers and sections
- **Styled Text** with different font sizes for headers/body
- **Preserved Timestamps** in bold formatting
- **Metadata Section** with file info and statistics
- **Automatic Page Breaks** between major sections
- **Unicode Support** for special characters

---

## ⚙️ Configuration

### Transcription Settings (transcribe.py)

Edit the configuration section in `transcribe.py`:

```python
# Model options: "tiny", "base", "small", "medium", "large-v2", "large-v3"
MODEL_SIZE = "base"

# Device options: "cpu" or "cuda" (for GPU)
DEVICE = "cpu"

# Compute type: "int8" (fastest, CPU), "float16" (GPU), "float32" (highest quality)
COMPUTE_TYPE = "int8"
```

#### Model Size Comparison

| Model      | Size   | Speed   | Accuracy | Best For                   |
| ---------- | ------ | ------- | -------- | -------------------------- |
| `tiny`     | ~75MB  | Fastest | Low      | Quick tests, low resource  |
| `base`     | ~145MB | Fast    | Good     | General use (default)      |
| `small`    | ~466MB | Medium  | Better   | Higher accuracy needed     |
| `medium`   | ~1.5GB | Slow    | High     | Professional transcription |
| `large-v2` | ~3GB   | Slowest | Highest  | Maximum accuracy           |
| `large-v3` | ~3GB   | Slowest | Highest  | Latest, best quality       |

### PDF Conversion Settings (txt_to_pdf.py)

Edit the configuration section in `txt_to_pdf.py`:

```python
# Page size options: letter (US), A4 (International)
PAGE_SIZE = letter  # or A4

# Font size for body text
FONT_SIZE = 10  # Range: 8-12 typically
```

### GPU Acceleration (Optional)

If you have an NVIDIA GPU with CUDA installed:

```python
# In transcribe.py
DEVICE = "cuda"
COMPUTE_TYPE = "float16"
```

This can provide **5-10x faster** transcription speeds.

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
    # Other options: "es", "fr", "de", "hi", "zh", "ta", "te", etc.
)
```

### PDF Styling Customization

In `txt_to_pdf.py`, you can customize fonts, colors, and spacing:

```python
# Title style
title_style = ParagraphStyle(
    'CustomTitle',
    fontSize=16,        # Adjust title size
    textColor='#2C3E50', # Change color (hex)
    spaceAfter=12,      # Space after title
)

# Body style
body_style = ParagraphStyle(
    'CustomBody',
    fontSize=10,        # Body text size
    leading=14,         # Line spacing
)
```

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "No module named 'faster_whisper'"

**Solution:**

```bash
pip install --upgrade faster-whisper
```

#### Issue: "No module named 'reportlab'"

**Solution:**

```bash
pip install --upgrade reportlab
```

#### Issue: Model download is slow or failing

**Solution:** The model is downloaded automatically on first run. If it fails:

1. Check your internet connection
2. Clear the cache: Delete `~/.cache/huggingface/` (Linux/Mac) or `%USERPROFILE%\.cache\huggingface\` (Windows)
3. Try again

#### Issue: "Out of memory" error during transcription

**Solution:**

1. Use a smaller model (e.g., `tiny` or `base`)
2. Close other applications
3. Increase system RAM or use swap space
4. Process fewer files at once

#### Issue: Transcription is very slow

**Solutions:**

1. Use a smaller model (`tiny` or `base`)
2. Enable GPU acceleration if available
3. Reduce beam size to 1
4. Use `compute_type="int8"` for CPU

#### Issue: Transcription quality is poor

**Solutions:**

1. Use a larger model (`medium` or `large-v3`)
2. Ensure audio quality is good (clear, minimal background noise)
3. Increase beam size to 10
4. Specify the correct language manually
5. Adjust VAD parameters for better silence detection

#### Issue: PDF generation fails for some files

**Solutions:**

1. Check that text files are not corrupted
2. Verify UTF-8 encoding
3. Check for extremely long lines that might cause issues
4. Review error messages for specific file issues

#### Issue: Special characters not displaying in PDF

**Solution:**
The script handles Unicode by default. If issues persist:

1. Ensure text files are UTF-8 encoded
2. Check that the font supports the characters
3. Consider using a different font that supports more Unicode characters

#### Issue: PDF formatting looks incorrect

**Solutions:**

1. Adjust `FONT_SIZE` in configuration (try 9 or 11 instead of 10)
2. Change `PAGE_SIZE` from `letter` to `A4` or vice versa
3. Modify spacing in paragraph styles
4. Check that the text file structure matches expected format

---

## 📊 Performance Tips

### Transcription Performance

1. **First Run**: Model download takes time (5-30 minutes depending on size)
2. **Subsequent Runs**: Model is cached, transcription starts immediately
3. **Batch Processing**: Processing 16 files takes ~10-60 minutes depending on:
   - Model size
   - Audio duration
   - CPU/GPU performance
   - Audio quality

### Estimated Transcription Times (Base Model, CPU)

| Audio Duration | Transcription Time | Speed Ratio |
| -------------- | ------------------ | ----------- |
| 1 minute       | ~30 seconds        | 0.5x        |
| 10 minutes     | ~5 minutes         | 0.5x        |
| 60 minutes     | ~30 minutes        | 0.5x        |

_Times vary significantly based on hardware and model size_

### PDF Conversion Performance

- Very fast: ~1-2 seconds per file
- Total time for 16 files: ~15-30 seconds
- Not CPU/GPU intensive

### Optimization Strategies

1. **For Speed**:

   - Use `tiny` or `base` model
   - Set `beam_size=1`
   - Use `compute_type="int8"`
   - Enable GPU if available

2. **For Quality**:

   - Use `large-v3` model
   - Set `beam_size=10`
   - Use `compute_type="float32"`
   - Ensure good audio quality

3. **Balanced Approach** (Recommended):
   - Use `base` or `small` model
   - Set `beam_size=5`
   - Use `compute_type="int8"` (CPU) or `"float16"` (GPU)

---

## 🔒 Privacy & Security

- **100% Offline**: All processing happens locally on your machine
- **No Data Transmission**: Audio files never leave your computer
- **No API Keys**: No external services or accounts required
- **No Logging**: No usage data is collected or transmitted
- **Complete Control**: You own all input and output files
- **GDPR Compliant**: No data sharing with third parties

---

## 📝 Supported Audio Formats

While this project is configured for `.m4a` files, faster-whisper supports:

- `.m4a` (Apple Audio) ← Current default
- `.mp3` (MPEG Audio)
- `.wav` (Waveform Audio)
- `.flac` (Free Lossless Audio Codec)
- `.ogg` (Ogg Vorbis)
- `.aac` (Advanced Audio Coding)
- `.opus` (Opus Audio)

### To Support Multiple Formats

Modify the glob pattern in `transcribe.py`:

```python
# For multiple formats:
audio_files = []
for ext in ['*.m4a', '*.mp3', '*.wav', '*.flac']:
    audio_files.extend(list(input_path.glob(ext)))
```

---

## 🎓 How It Works

### Transcription Pipeline

1. **Model Loading**: Faster-Whisper loads the specified model (downloads on first run)
2. **Audio Processing**: Each audio file is converted to the format Whisper expects
3. **Voice Activity Detection**: VAD filters out silence and non-speech segments
4. **Transcription**: The model processes audio in segments and generates text
5. **Language Detection**: The model automatically detects the spoken language
6. **Output Generation**: Results are formatted and saved to text files

### PDF Generation Pipeline

1. **Text File Reading**: Each `.txt` file is read and parsed
2. **Content Analysis**: The script identifies sections (metadata, timestamps, full text)
3. **Style Application**: Different styles are applied to different sections
4. **Layout Generation**: ReportLab creates the PDF structure
5. **PDF Creation**: The final PDF is generated and saved

### Technologies Used

- **Faster-Whisper**: Optimized implementation of OpenAI's Whisper using CTranslate2
- **CTranslate2**: Fast inference engine for Transformer models
- **Silero VAD**: Voice Activity Detection to filter silence
- **ReportLab**: Industry-standard PDF generation library for Python
- **Python 3**: Core programming language

---

## 📦 Dependencies

```
faster-whisper>=1.0.0    # Speech-to-text transcription
reportlab>=4.0.0         # PDF generation
```

Full dependency tree includes:

- `ctranslate2` (faster-whisper dependency)
- `tokenizers` (faster-whisper dependency)
- `onnxruntime` (VAD dependency)
- `pillow` (reportlab dependency)

---

## 🚀 Workflow Examples

### Example 1: Basic Workflow

```bash
# 1. Place audio files in audio/ folder
# 2. Run transcription
python transcribe.py

# 3. Generate PDFs
python txt_to_pdf.py

# 4. Your PDFs are ready in output/ folder!
```

### Example 2: High-Quality Workflow

```python
# Edit transcribe.py:
MODEL_SIZE = "large-v3"
BEAM_SIZE = 10

# Then run:
python transcribe.py
python txt_to_pdf.py
```

### Example 3: Fast Processing Workflow

```python
# Edit transcribe.py:
MODEL_SIZE = "tiny"
BEAM_SIZE = 1

# Then run:
python transcribe.py
python txt_to_pdf.py
```

### Example 4: GPU-Accelerated Workflow

```python
# Edit transcribe.py:
DEVICE = "cuda"
COMPUTE_TYPE = "float16"

# Then run:
python transcribe.py
python txt_to_pdf.py
```

---

## 📈 Project Workflow Diagram

```
┌─────────────────┐
│  Audio Files    │
│   (audio/)      │
│   16 × .m4a     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  transcribe.py  │◄── Uses faster-whisper
│                 │◄── Applies VAD
│                 │◄── Detects language
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Text Files     │
│ (transcripts/)  │
│   16 × .txt     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ txt_to_pdf.py   │◄── Uses reportlab
│                 │◄── Applies styling
│                 │◄── Formats content
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PDF Documents  │
│   (output/)     │
│   16 × .pdf     │
└─────────────────┘
```

---

## 🎯 Use Cases

1. **Interview Transcriptions** → Professional documentation
2. **Meeting Minutes** → Formatted meeting records
3. **Podcast Notes** → Searchable podcast transcripts
4. **Lecture Notes** → Student study materials
5. **Voice Memos** → Personal diary entries
6. **Customer Calls** → Support documentation
7. **Legal Recordings** → Court/deposition transcripts
8. **Research Interviews** → Academic research materials

---

## 🤝 Contributing

Feel free to:

- Report bugs or issues
- Suggest new features
- Improve documentation
- Optimize performance
- Add new export formats

---

## 📚 Additional Resources

### Faster-Whisper & Whisper

- [Faster-Whisper Documentation](https://github.com/guillaumekln/faster-whisper)
- [OpenAI Whisper Paper](https://arxiv.org/abs/2212.04356)
- [CTranslate2 Documentation](https://opennmt.net/CTranslate2/)
- [Whisper Model Card](https://github.com/openai/whisper/blob/main/model-card.md)

### ReportLab

- [ReportLab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [ReportLab GitHub](https://github.com/MrBitBucket/reportlab-mirror)

### Python

- [Python Official Documentation](https://docs.python.org/3/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

---

## ⚖️ License

This project uses open-source libraries:

- Faster-Whisper: MIT License
- OpenAI Whisper: MIT License
- ReportLab: BSD License

---

## 🎉 Complete Setup Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Audio files placed in `audio/` folder
- [ ] Run `python transcribe.py` (wait for model download on first run)
- [ ] Check `transcripts/` folder for text files
- [ ] Run `python txt_to_pdf.py`
- [ ] Check `output/` folder for PDF files
- [ ] Open a PDF to verify formatting
- [ ] Success! 🎊

---

## 💡 Pro Tips

1. **Model Selection**: Start with `base` model, upgrade to `medium` or `large` if accuracy is insufficient
2. **Backup Files**: Keep original audio files as backups
3. **Organize Output**: Create dated folders for different transcription batches
4. **Test First**: Test with 1-2 files before processing entire batch
5. **GPU Usage**: GPU acceleration is worth it for large batches (10+ hours of audio)
6. **Check Quality**: Review a few transcripts before generating all PDFs
7. **Customize PDFs**: Adjust font sizes if text is too small/large
8. **File Names**: Use clear, descriptive filenames for audio files

---

**Happy Transcribing & Converting! 🎤📄✨**

For questions, issues, or suggestions, please open an issue on the project repository.
