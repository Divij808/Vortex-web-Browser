# Vortex Web Browser
<img width="1600" height="865" alt="image" src="https://github.com/user-attachments/assets/fdc4bfbf-dd09-441e-84f9-8c0982491ced" />


Vortex is a simple desktop web browser built with Python and PyQt5. It provides a lightweight browser interface with tabs, navigation controls, and a URL bar, all running in a native Windows application.

I started this project to learn more about PyQt5, desktop application development, and how web browsers work behind the scenes.

## Features

* Multiple browser tabs
* Open and close tabs
* Back and forward navigation
* Reload the current page
* URL and search bar
* Tab titles update automatically
* Maximised browser window
* Built using Python and PyQt5
* Uses Qt WebEngine to display websites

## Technologies Used

* Python
* PyQt5
* PyQtWebEngine
* Qt WebEngine

## Requirements

If you want to run the project from the source code, you will need:

* Python 3.9 or later
* pip
* An internet connection

You can check whether Python is installed by running:

```bash
python --version
```

## Installation

Download the ZIP file
<img width="1099" height="610" alt="image" src="https://github.com/user-attachments/assets/c211c374-03fc-40fd-8a76-a95645ffdf68" />


Install the required packages:

```bash
pip install PyQt5 PyQtWebEngine
```

Then run the browser:

```bash
python main.py
```


## How It Works

Vortex uses `QWebEngineView` from PyQt5 to display websites inside the application.

The browser interface is built around a `QMainWindow`, with a toolbar containing the navigation controls and URL bar. Each browser tab contains its own `QWebEngineView`, allowing multiple websites to be open at the same time.

When the user enters a URL, Vortex loads it directly into the current browser tab. If the entered address does not start with `http`, the application currently adds `http://` automatically.

## License

This project is currently intended as a personal learning project.

Its licenced with CC

## Author

Developed by Divij.

Vortex is an ongoing project and will continue to change as new features are added.
