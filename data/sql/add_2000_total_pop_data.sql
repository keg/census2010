-- add missing 2000 total population data that is missing

BEGIN;
ALTER TABLE data_ages ADD COLUMN total_population_2000 INTEGER NULL;
ALTER TABLE data_ninetytohundred ADD COLUMN total_population_2000 INTEGER NULL;
COMMIT;
