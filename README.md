# Spanner FTS Type Ahead Example

This is a demo on how to use Spanner Full text search for Type ahead

## Setup Gcloud 

```bash
gcloud auth application-default login
make instancecreate
make loadschema
```


## Get Python setup and load the Data

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./load_data.py
```

## Run the Webapp

```bash
./app.py
```
