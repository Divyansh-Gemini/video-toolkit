from video_toolkit.utils.path_utils import get_downloads_dir
import os
import subprocess


def trim_video(input_video_path: str, start_time: str, end_time: str, output_path: str = None):
    """
    Trim a video from start_time to end_time.

    Args:
        input_video_path (str): Full path of video to trim
        start_time (str): Start time HH:MM:SS(.mmm)
        end_time (str): End time HH:MM:SS(.mmm)
        output_path (str): Directory to save trimmed video

    Returns:
        str: Path to trimmed video
    """

    def time_to_seconds(time_str: str) -> float:
        """Convert HH:MM:SS(.mmm) to seconds."""
        parts = time_str.split(":")
        if len(parts) != 3:
            raise ValueError("Time must be HH:MM:SS or HH:MM:SS.mmm")
        hours, minutes, seconds = int(parts[0]), int(parts[1]), float(parts[2])
        return hours * 3600 + minutes * 60 + seconds

    if not os.path.exists(input_video_path):
        raise FileNotFoundError("Input video not found")
    if output_path is None:
        output_path = get_downloads_dir()
    os.makedirs(output_path, exist_ok=True)

    file_name = os.path.basename(input_video_path)
    name, _ = os.path.splitext(file_name)
    output_file = os.path.join(output_path, f"{name}_trimmed.mp4")

    start_sec, end_sec = time_to_seconds(start_time), time_to_seconds(end_time)
    duration = end_sec - start_sec
    if duration <= 0:
        raise ValueError("End time must be after start time")

    # ffmpeg command for trimming
    command = [
        "ffmpeg",
        "-y",
        "-ss", start_time,
        "-i", input_video_path,
        "-t", f"{duration:.3f}",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-preset", "veryfast",
        "-movflags", "+faststart",
        output_file
    ]
    subprocess.run(command, check=True)

    print(f"\n✅ Trim complete! Duration: {duration:.3f}s, Saved to: {output_file}")
    return output_file
