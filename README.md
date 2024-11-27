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

## Some Queries

```sql
SELECT name FROM Station WHERE SEARCH_NGRAMS(name_Tokens,'bon') ORDER BY SCORE_NGRAMS(name_Tokens, 'bon' ) DESC
```

## Snippets

This will high light for Full Text and Substring  search so you can see what exactly matched

```sql
SELECT name, SNIPPET(name, "Bond") FROM Station WHERE SEARCH(name_FullText,'Bond')
SELECT name, SNIPPET(name, "Bond") FROM Station WHERE SEARCH_SUBSTRING(name_SubString,'Bond')
```
