# Discord Nitro Generator and Checker

A sophisticated tool designed for generating and checking Discord Nitro codes efficiently, meeting all your Nitro needs.

## Features

- Simultaneous generation and checking of Discord Nitro codes for maximum efficiency.
- Utilizes Requests, Discord webhook, and Colored for seamless functionality.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python installed. If not, you can [install Python here](https://www.python.org/downloads/).

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
