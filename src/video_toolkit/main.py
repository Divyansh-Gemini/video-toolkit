from src.main.video_downloader import download_best_quality_mp4
from src.main.video_trimmer import trim_video
from src.main.video_utils.path_utils import get_downloads_dir
import os


def get_trim_inputs():
    """Prompt user for start & end times."""
    start_time = input("Enter start time (HH:MM:SS or HH:MM:SS.mmm): ")
    end_time = input("Enter end time (HH:MM:SS or HH:MM:SS.mmm): ")
    return start_time, end_time


if __name__ == "__main__":
    print("Select option:")
    print("1. Download YT video")
    print("2. Trim video")
    print("3. Download & trim")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        video_url = input("Enter YT video URL: ")
        download_best_quality_mp4(video_url)

    elif choice == '2':
        video_path = input("Enter video path: ")
        start_time, end_time = get_trim_inputs()
        trim_video(input_video_path=video_path, start_time=start_time, end_time=end_time)

    elif choice == '3':
        video_url = input("Enter YT video URL: ")
        output_dir = get_downloads_dir()
        success = download_best_quality_mp4(video_url, output_path=output_dir)

        if success:
            # Pick latest downloaded video
            downloaded_files = sorted(
                [os.path.join(output_dir, f) for f in os.listdir(output_dir)],
                key=os.path.getmtime,
                reverse=True
            )
            latest_video = downloaded_files[0]
            print(f"\n📁 Latest downloaded video: {latest_video}")

            start_time, end_time = get_trim_inputs()
            trim_video(input_video_path=latest_video, start_time=start_time, end_time=end_time)

    else:
        print("Invalid choice. Exiting...")
