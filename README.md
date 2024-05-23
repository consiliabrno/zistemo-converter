# Zistemo Converter

## HowTo install & run (Docker)

## Prerequisites
```bash
docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
git
```

## Login to remote & clone the app
```bash
ssh server@ubuntumaster
git clone https://github.com/davidConsilia/zistemo_converter.git
cd zistemo_converter
```

## Execution

> [!IMPORTANT]
> For all the below to work, you need have pwd in the folder where you cloned the app earlier

### Start the app:

```bash
docker compose up -d
```

### Stop it:

```bash
docker compose down
```

### Update:

```bash
docker compose down
git pull
docker compose up -d --build
```

## HowTo install and run (bare-metal, without Docker)

### Prerequisites

Python3.8+ and Flask

### Setup

To install Python firstly create local enviroment

```bash
python3 -m venv venv
```

Activate venv

```bash
# Windows
.\venv\Scripts\activate

# Linux
. venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Run Website

```bash
python3 app.py
```
