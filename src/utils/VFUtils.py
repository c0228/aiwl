import subprocess

def convert_webm_to_mp4(webm_path, mp4_path):
    """Convert WebM to MP4 using FFmpeg"""
    subprocess.run([
        "ffmpeg", "-i", webm_path,
        "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental",
        mp4_path
    ], check=True)

def convert_mp4_to_wav(mp4_path, wav_path):
    """Extract WAV audio from MP4 using FFmpeg"""
    subprocess.run([
        "ffmpeg", "-i", mp4_path,
        "-vn",  # ignore video
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        wav_path
    ], check=True)