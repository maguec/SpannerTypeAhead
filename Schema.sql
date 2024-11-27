-- Node Tables

CREATE TABLE Station (
  id INT64 NOT NULL,
  name STRING(MAX),
  lc STRING(MAX),
  latitude FLOAT64,
  longitude FLOAT64,
  name_Tokens TOKENLIST AS (TOKENIZE_NGRAMS(lc, ngram_size_min=>2, ngram_size_max=>4)) HIDDEN,
  name_FullText TOKENLIST AS (TOKENIZE_FULLTEXT(lc)) HIDDEN,
  name_SubString TOKENLIST AS (TOKENIZE_SUBSTRING(lc)) HIDDEN,
) PRIMARY KEY (id);

-- Create the Search Indexes
CREATE SEARCH INDEX StationIndex ON Station(name_Tokens);
CREATE SEARCH INDEX StationIndexFullText ON Station(name_FullText);
CREATE SEARCH INDEX StationIndexSubString ON Station(name_SubString);

