# CheckinBot

CheckinBot is a Python script that automates sending a check-in message on a Discord channel. It supports two modes:

- **Hjemmekontor (Home Office):** Sends "gm(hk)".
- **School:** Sends "gm" and logs attendance for "kjøreliste" in your Documents folder.

## Features

- Automated message posting using Selenium.
- Supports headless mode with automatic fallback to visible mode if login is required.
- Uses a persistent browser profile so you don't have to log in every time.
- Logs attendance locally when running from school.

## Prerequisites

- Python 3.12 (or a compatible version)
- [Chromium Browser](https://www.chromium.org/getting-involved/download-chromium)
- [ChromeDriver](https://chromedriver.chromium.org/) 
- pip
- selenium installed in a virtual environment or globally

## Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/eirikkar/checkinbot.git

```

### 2. Create a Virtual Environment

In the project folder, open a terminal and run:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
On Linux/macOS:

```bash

source venv/bin/activate

```

On Windows:

```bash

venv\Scripts\activate

```

### 4. Install Required Packages
Install Selenium using pip:

```bash

pip install selenium

```

## Running the Script
The script requires a command-line parameter --location with one of two options:

For Hjemmekontor (home office):

```bash

venv/bin/python main.py --location hjemmekontor

```
This sends the message gm(hk).

For School:

```bash

venv/bin/python main.py --location school

```
This sends the message gm and logs your attendance in Documents/kjoreliste_log.txt.

If you have already activated the virtual environment, you can also run:

```bash

python main.py --location hjemmekontor

```
or

```bash

python main.py --location school

```
