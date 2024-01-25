# Discord Nitro Generator and Checker

Welcome to a sophisticated tool meticulously crafted for generating and checking Discord Nitro codes with maximum efficiency, catering to all your Nitro needs.

## Features

- Simultaneous generation and checking of Discord Nitro codes for optimal performance.
- Utilizes Requests, Discord webhook, and Colored for seamless functionality.

## Getting Started

To get a local copy up and running, follow these straightforward steps.

### Prerequisites

Ensure you have Python installed. If not, you can [install Python here](https://www.python.org/downloads/).

### Virus Total Scans

This program may have false positives due to the way it was converted to an EXE, how it checks codes, files being created/deleted, Python modules, Sysmon detection, Python Image Load By Non-Python Process, and more. The program is fully open-source!

Matches rule PyInstaller from ruleset PyInstaller at [https://github.com/bartblaze/Yara-rules](https://github.com/bartblaze/Yara-rules) by @bartblaze

- [Windows DETECTION 7/71](https://go.3mpire.shop/nitrovts): 7 security vendors and no sandboxes flagged this file as malicious.
  
  - Windows BEHAVIOR: Microsoft Sysinternals - CLEAN -- CAPA - CLEAN -- VIRUSTOTAL JUJUBOX - CLEAN -- VIRUSTOTAL OBSERVER - CLEAN -- ZENBOX
  - Activity Summary: DETECTIONS NOT FOUND, MITRE SIGNATURES 20 INFO, IDS RULES NOT FOUND, SIGMA RULES 1 HIGH 1 MEDIUM, DROPPED FILES 83 OTHER 1 PE-EXE 1 ZIP 1 TEXT, NETWORK COMMS 3 IP

- [Python DETECTION 0/61](https://go.3mpire.shop/nitrovtsp): No security vendors and no sandboxes flagged this file as malicious
  
  - Python BEHAVIOR: ZENBOX - CLEAN -- VIRUSTOTAL BOX OF APPLES - CLEAN -- OS X SANDBOX - CLEAN
  - Activity Summary: DETECTIONS NOT FOUND, MITRE SIGNATURES NOT FOUND, IDS RULES NOT FOUND, SIGMA RULES NOT FOUND, DROPPED FILES NOT FOUND, NETWORK COMMS NOT FOUND

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MrPrinceV2/Discord-Nitro-Generator-Checker.git
    ```

2. Install Python packages:

    - Windows:

        ```bash
        py -3 -m pip install -r requirements.txt
        ```

    - Unix:

        ```bash
        python3.8 -m pip install -r requirements.txt
        ```

    Alternatively, for Android using unrooted Termux:

    ```bash
    pkg install git
    git clone https://github.com/MrPrinceV2/Discord-Nitro-Generator-Checker
    pkg install python
    cd Discord-Nitro-Generator-Checker
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python3 main.py
    ```

## Usage

Execute the `main.py` file using:

```bash
py -3 main.py
```

The application will prompt you for:

1. Number of codes to generate.
2. If you want to use a Discord webhook. If you don't know how to get a Discord webhook URL, find it at:
   `channel settings » integrations » webhooks » create webhook`. Leave it blank if you don't want to use a webhook.

The code will start generating and checking after these steps.

## Roadmap

Check the [open issues](https://github.com/MrPrinceV2/Discord-Nitro-Generator-Checker/issues) for a list of proposed features and known issues.

## Contributing

Contributions are welcome and appreciated. Join the open-source community to learn, inspire, and create together. Feel free to contribute to make this tool even better!
