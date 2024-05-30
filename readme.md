# YouTube Downloader

YouTube Downloader is a Python-based application with a graphical user interface (GUI) that allows users to download YouTube videos with both video and audio. The application is built using `tkinter` and `customtkinter` for the GUI, and `pytube` for downloading videos from YouTube.

## Features

- Enter a YouTube URL and download the highest resolution video with audio.
- Provides user feedback on download progress and errors.
- Simple and intuitive GUI.

## Requirements

- Python 3.11.4
- `pytube`
- `customtkinter`
- `tkinter`

## Installation

1. **Clone the repository** or download the source code:
    ```sh
    git clone https://github.com/osvaldas01/YouTube-Downloader.git
    cd youtube-downloader
    ```

2. **Install the required Python packages**:
    ```sh
    pip install pytube customtkinter
    ```

## Usage

1. **Run the application**:
    ```sh
    python youtube_downloader.py
    ```

2. **Enter the YouTube URL** in the input field.

3. **Click the "Download" button** to start downloading the video.

4. **Check the status label** for download progress and error messages.

## Code Overview

The main application code is contained in `youtube_downloader.py`:

```python
import tkinter
import cust
