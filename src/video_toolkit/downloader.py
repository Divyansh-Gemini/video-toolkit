import os
import yt_dlp
from video_toolkit.utils.path_utils import get_downloads_dir


def download_best_quality_mp4(url, output_path=None):
    """
    Download YT video in best quality (H.264 video + M4A audio) as MP4.

    Args:
        url (str): YT URL
        output_path (str): Directory to save video

    Returns:
        bool: True if successful, False otherwise
    """
    if output_path is None:
        output_path = get_downloads_dir()
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],
        'writethumbnail': False,
        'embedthumbnail': False,
        'add_metadata': True,
        'quiet': False,
        'no_warnings': False,
        'progress': True,
        'prefer_free_formats': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"\n🔅 Title: {info['title']}")
            print(f"🔅 Duration: {info['duration']}s")
            print(f"🔅 Uploader: {info['uploader']}")
            print("\nDownloading...")
            ydl.download([url])
            print(f"\n✅ Download complete! Saved to: {output_path}")
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

    return True
