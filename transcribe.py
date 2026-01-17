"""
Batch Speech-to-Text Transcription using Faster-Whisper
This script transcribes audio files from the 'audio/' folder
and saves the transcriptions to the 'transcripts/' folder.
"""

import os
from pathlib import Path
from faster_whisper import WhisperModel
from datetime import datetime


def transcribe_audio_files(
    input_folder="audio",
    output_folder="transcripts",
    model_size="base",
    device="cpu",
    compute_type="int8"
):
    """
    Transcribe all .m4a files in the input folder.
    
    Args:
        input_folder (str): Path to folder containing audio files
        output_folder (str): Path to folder for output transcripts
        model_size (str): Whisper model size (tiny, base, small, medium, large-v2, large-v3)
        device (str): Device to use for inference (cpu, cuda)
        compute_type (str): Compute type (int8, float16, float32)
    """
    
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Initialize the Faster-Whisper model
    print(f"Loading Faster-Whisper model: {model_size}")
    print(f"Device: {device}, Compute Type: {compute_type}")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    
    # Get all .m4a files from input folder
    input_path = Path(input_folder)
    audio_files = list(input_path.glob("*.m4a"))
    
    if not audio_files:
        print(f"No .m4a files found in {input_folder}/")
        return
    
    print(f"\nFound {len(audio_files)} audio file(s) to transcribe.\n")
    
    # Process each audio file
    for idx, audio_file in enumerate(audio_files, 1):
        print(f"[{idx}/{len(audio_files)}] Processing: {audio_file.name}")
        
        try:
            # Transcribe the audio file
            segments, info = model.transcribe(
                str(audio_file),
                beam_size=5,
                vad_filter=True,  # Voice Activity Detection
                vad_parameters=dict(min_silence_duration_ms=500)
            )
            
            # Prepare output file name
            output_filename = audio_file.stem + ".txt"
            output_path = Path(output_folder) / output_filename
            
            # Write transcription to file
            with open(output_path, "w", encoding="utf-8") as f:
                # Write header with metadata
                f.write(f"Transcription of: {audio_file.name}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Language: {info.language} (probability: {info.language_probability:.2f})\n")
                f.write(f"Duration: {info.duration:.2f} seconds\n")
                f.write("=" * 80 + "\n\n")
                
                # Write timestamped segments
                f.write("TIMESTAMPED TRANSCRIPTION:\n")
                f.write("-" * 80 + "\n\n")
                
                full_text = []
                for segment in segments:
                    timestamp = f"[{segment.start:.2f}s -> {segment.end:.2f}s]"
                    f.write(f"{timestamp}\n{segment.text.strip()}\n\n")
                    full_text.append(segment.text.strip())
                
                # Write full text without timestamps
                f.write("\n" + "=" * 80 + "\n")
                f.write("FULL TRANSCRIPTION (no timestamps):\n")
                f.write("=" * 80 + "\n\n")
                f.write(" ".join(full_text))
            
            print(f"✓ Saved transcription to: {output_path}\n")
            
        except Exception as e:
            print(f"✗ Error processing {audio_file.name}: {str(e)}\n")
            continue
    
    print("=" * 80)
    print("Transcription complete!")
    print(f"All transcripts saved to: {output_folder}/")


if __name__ == "__main__":
    # Configuration
    INPUT_FOLDER = "audio_files"
    OUTPUT_FOLDER = "transcripts_output"
    
    # Model options: "tiny", "base", "small", "medium", "large-v2", "large-v3"
    # Larger models are more accurate but slower
    MODEL_SIZE = "base"
    
    # Device options: "cpu" or "cuda" (for GPU)
    DEVICE = "cpu"
    
    # Compute type: "int8" (fastest, CPU), "float16" (GPU), "float32" (highest quality)
    COMPUTE_TYPE = "int8"
    
    print("=" * 80)
    print("Batch Speech-to-Text Transcription using Faster-Whisper")
    print("=" * 80)
    print()
    
    # Run transcription
    transcribe_audio_files(
        input_folder=INPUT_FOLDER,
        output_folder=OUTPUT_FOLDER,
        model_size=MODEL_SIZE,
        device=DEVICE,
        compute_type=COMPUTE_TYPE
    )
