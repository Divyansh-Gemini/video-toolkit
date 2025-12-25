# Video Toolkit

A simple **CLI tool** to **download YT videos** and **trim local videos** easily. Supports single commands for
downloading, trimming, or both in one step.

---

## Features

- Download YT videos in **best quality MP4** (H.264 video + M4A audio)
- Trim local videos using **start** and **end times** (`HH:MM:SS` or `HH:MM:SS.mmm`)
- Download a video and trim it in **one command**
- Cross-platform support (Windows, macOS, Linux)
- Saves files to system **Downloads folder** by default

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Divyansh-Gemini/video-toolkit.git
cd video-toolkit
```

### As an end user (recommended)

#### 1. Install pipx

**macOS (Homebrew – recommended)**

```bash
brew install pipx
pipx ensurepath
```

Restart your terminal after this.

**Windows**

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

**Linux (Debian / Ubuntu)**

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Restart your terminal after installation.

Verify pipx:

```bash
pipx --version
```

#### 2. Install Video Toolkit using pipx

```bash
cd video-toolkit
pipx install .
```

### As a developer

#### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows
```

#### 2. Install the tool

```bash
python -m pip install -e .
```

This allows you to run `video-toolkit` from the terminal **and reflect code changes immediately**.

---

## Dependencies / Setup

### 1. Python

* Requires **Python 3.9+**.
* Install Python from [python.org](https://www.python.org/downloads/) or via your system package manager.

---

### 2. Python packages

#### For end users (pipx)

> No action required.
> All Python dependencies (e.g. `yt-dlp`) are installed automatically by `pipx`.

#### For developers

Install dependencies manually if needed:

```bash
pip install -r requirements.txt
```

or via editable install:

```bash
python -m pip install -e .
```

Dependencies:

* [yt-dlp](https://github.com/yt-dlp/yt-dlp) – For downloading YT videos

---

### 3. FFmpeg (Required for everyone)

`ffmpeg` is a **system-level dependency** and must be installed manually.
It is **not installed by pip, pipx, or yt-dlp**.

Required for:

* Merging video + audio streams
* Trimming videos

Installation:

* **Windows**

    1. Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
    2. Extract and add the `bin` folder to your `PATH`

* **macOS**

  ```bash
  brew install ffmpeg
  ```

* **Linux (Debian/Ubuntu)**

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

Verify installation:

```bash
ffmpeg -version
```

---

## Usage

The CLI command is:

```bash
video-toolkit <command> [options]
```

### Commands

#### 1. Download a YT video

```bash
video-toolkit download "<video_url>"
```

Example:

```bash
video-toolkit download "https://youtu.be/VIDEO_ID"
```

#### 2. Trim a local video

```bash
video-toolkit trim --path <video_path> --start <start_time> --end <end_time>
```

Example:

```bash
video-toolkit trim --path video.mp4 --start 00:01:00 --end 00:02:30
```

#### 3. Download & Trim YT video in one step

```bash
video-toolkit download-trim "<video_url>" --start <start_time> --end <end_time>
```

Example:

```bash
video-toolkit download-trim "https://youtu.be/VIDEO_ID" --start 00:01:00 --end 00:02:00
```

---

If you ever get the following error try updating `yt-dlp` or using a VPN.

<img width="1512" height="407" alt="image" src="https://github.com/user-attachments/assets/eeaa0e04-b45c-4777-af6d-c918da752c74" />

---

## Development / Local Testing

If you want to test the CLI **without installing globally**:

```bash
python -m video_toolkit.cli
```

---

## System-wide CLI Usage

After installing (globally or in editable mode), you can run `video-toolkit` from **any terminal**:

```bash
video-toolkit --help
```

This displays the list of all available commands:

* `download`
* `trim`
* `download-trim`

### Command-specific help

You can also view detailed help for any individual command:

```bash
video-toolkit download --help
video-toolkit trim --help
video-toolkit download-trim --help
```

Each command help shows:

* Required and optional arguments
* Expected formats (e.g., time format `HH:MM:SS(.mmm)`)
* Example usage

This makes it easy to understand and use each command without referring to the documentation every time.


---

## Notes

* Python dependencies are handled automatically when installing via pipx
* The trimmed video is saved as `<original_name>_trimmed.mp4` in the Downloads folder by default.
* Supports fractional seconds in trim times: `HH:MM:SS.mmm`
* Make sure `ffmpeg` is installed and added to your PATH.

---

## Project Structure

```
video-toolkit/
├─ src/video_toolkit/
│  ├─ cli.py                 # Main CLI entrypoint
│  ├─ downloader.py          # YT download functions
│  ├─ main.py                # Interactive script
│  ├─ trimmer.py             # Video trimming functions
│  └─ utils/
│     └─ path_utils.py       # Downloads folder detection
├─ pyproject.toml            # Project metadata & CLI script entry
├─ requirements.txt          # Python dependencies
└─ README.md
```
