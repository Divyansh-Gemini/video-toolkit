import os
import sys


def get_downloads_dir() -> str:
    """Return system Downloads folder path (Windows/macOS/Linux)."""
    if sys.platform.startswith("win"):
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    else:
        return os.path.join(os.path.expanduser("~"), "Downloads")
