Below is **only the modified content**, corrected to properly reflect **pipx behavior** and remove confusion for end users 👇

---

### As an end user (recommended)

```bash
pipx install video-toolkit
```

> `pipx` automatically installs all required **Python dependencies**.
> You **do NOT** need to run `pip install -r requirements.txt`.

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

## Notes

* Python dependencies are handled automatically when installing via **pipx**
* `ffmpeg` must always be installed manually
* The trimmed video is saved as `<original_name>_trimmed.mp4` in the Downloads folder by default
* Supports fractional seconds in trim times: `HH:MM:SS.mmm`

---

This version is now **technically correct**, beginner-friendly, and aligned with Python CLI best practices.
