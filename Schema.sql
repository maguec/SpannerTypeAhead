-- Node Tables

CREATE TABLE Station (
  id INT64 NOT NULL,
  name STRING(MAX),
  lc STRING(MAX),
  latitude FLOAT64,
  longitude FLOAT64,
  name_Tokens TOKENLIST AS (TOKENIZE_NGRAMS(lc, ngram_size_min=>2, ngram_size_max=>4)) HIDDEN,
) PRIMARY KEY (id);

-- Create the Search Indexes
CREATE SEARCH INDEX StationIndex ON Station(name_Tokens);

