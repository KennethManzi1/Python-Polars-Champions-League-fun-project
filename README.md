<h1 align="center">
  <img src="https://raw.githubusercontent.com/pola-rs/polars-static/master/banner/polars_github_banner.svg" alt="Polars logo">
  <br>
</h1>


## Polars: Introduction 

Polars is a robust Python library for high-performance data manipulation and analysis.

**Key Features of Polars**
- **Speed and performance**: Polars leverages parallel processing and memory optimization techniques, allowing it to process large datasets significantly faster than traditional methods.
- **Data manipulation capabilities**: Polars provides features for data manipulation such as filtering, sorting, grouping, joining, and aggregating data. While Polars may not have the same extensive functionality as pandas due to its relative novelty, it covers approximately 80% of the common operations found in Pandas.
- **Expressive syntax**: Polars employs a concise and intuitive syntax, making it easy to learn and use. Its syntax is similar to pandas, allowing users to quickly adapt to Polars and leverage their existing knowledge.
- **DataFrame and series structures**
- **Ability to code SQL within Polars with ease**

To learn more, read the [user guide](https://docs.pola.rs/) and [Data Camp introduction to Polars](https://www.datacamp.com/blog/an-introduction-to-polars-python-s-tool-for-large-scale-data-analysis)

***

## Polars: Champions League fun project 
![download](https://github.com/user-attachments/assets/bef70db7-d093-4580-8a13-d6c3ac48f444)

**Installing Polars**
```Python
!pip install Polars
!pip install pyarrow
```


**Champions League Top Performing Players in 2022 Data**
```Python
import polars as pl

##Getting Data of Champions League Players 2021-2022

# List of file paths for CSVs
csv_files_champions_league_2022 = ['/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/attacking.csv', '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/disciplinary.csv', '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/distributon.csv', 
                                   '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/key_stats.csv', '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/goals.csv', 
                                   '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/defending.csv','/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/goalkeeping.csv']


#test it out by reading the first file which is the attacking csv file

combined_df = pl.read_csv(csv_files_champions_league_2022[0], encoding='ISO-8859-1', infer_schema_length=10000, ignore_errors=True )

print(combined_df)

shape: (176, 5)
┌────────┬────────────┬────────────┬────────────┬───┬────────────┬──────────┬──────────┬───────────┐
│ serial ┆ player_nam ┆ club       ┆ position   ┆ … ┆ corner_tak ┆ offsides ┆ dribbles ┆ match_pla │
│ ---    ┆ e          ┆ ---        ┆ ---        ┆   ┆ en         ┆ ---      ┆ ---      ┆ yed       │
│ i64    ┆ ---        ┆ str        ┆ str        ┆   ┆ ---        ┆ i64      ┆ i64      ┆ ---       │
│        ┆ str        ┆            ┆            ┆   ┆ i64        ┆          ┆          ┆ i64       │
╞════════╪════════════╪════════════╪════════════╪═══╪════════════╪══════════╪══════════╪═══════════╡
│ 1      ┆ Bruno      ┆ Man.       ┆ Midfielder ┆ … ┆ 10         ┆ 2        ┆ 7        ┆ 7         │
│        ┆ Fernandes  ┆ United     ┆            ┆   ┆            ┆          ┆          ┆           │
│ 2      ┆ VinÃ­cius   ┆ Real       ┆ Forward    ┆ … ┆ 3          ┆ 4        ┆ 83       ┆ 13        │
│        ┆ JÃºnior    ┆ Madrid     ┆            ┆   ┆            ┆          ┆          ┆           │
│ 2      ┆ SanÃ©      ┆ Bayern     ┆ Midfielder ┆ … ┆ 3          ┆ 3        ┆ 32       ┆ 10        │
│ 4      ┆ Antony     ┆ Ajax       ┆ Forward    ┆ … ┆ 3          ┆ 4        ┆ 28       ┆ 7         │
│ 5      ┆ Alexander- ┆ Liverpool  ┆ Defender   ┆ … ┆ 36         ┆ 0        ┆ 9        ┆ 9         │
│        ┆ Arnold     ┆            ┆            ┆   ┆            ┆          ┆          ┆           │
│ …      ┆ …          ┆ …          ┆ …          ┆ … ┆ …          ┆ …        ┆ …        ┆ …         │
│ 64     ┆ Tolisso    ┆ Bayern     ┆ Midfielder ┆ … ┆ 0          ┆ 0        ┆ 0        ┆ 4         │
│ 64     ┆ Schuurs    ┆ Ajax       ┆ Defender   ┆ … ┆ 0          ┆ 0        ┆ 0        ┆ 3         │
│ 64     ┆ Kryvtsov   ┆ Shakhtar   ┆ Defender   ┆ … ┆ 0          ┆ 0        ┆ 0        ┆ 3         │
│        ┆            ┆ Donetsk    ┆            ┆   ┆            ┆          ┆          ┆           │
│ 64     ┆ StaniÅ¡iÄ ┆ Bayern     ┆ Defender   ┆ … ┆ 0          ┆ 0        ┆ 0        ┆ 2         │
│ 64     ┆ Bernardo   ┆ Salzburg   ┆ Defender   ┆ … ┆ 0          ┆ 0        ┆ 0        ┆ 2         │
└────────┴────────────┴────────────┴────────────┴───┴────────────┴──────────┴──────────┴───────────┘

```

**Now we will loop through the champions league 2022 files and join them using the player name**

```Python
CL_22 = []

for cl_file in csv_files_champions_league_2022:
    cl_df = pl.read_csv(cl_file, encoding='ISO-8859-1', infer_schema_length=10000, ignore_errors=True )
    CL_22.append(cl_df)

##print(CL_22)

# Merge all DataFrames by performing a join on the common column
Champions_League2022 = CL_22[0]
for df in CL_22[1:]:
    Champions_League2022  = Champions_League2022.join(df, on='player_name', how='inner')

print(Champions_League2022)

shape: (2, 46)
┌────────┬────────────┬───────────┬────────────┬───┬──────────┬────────────┬───────────┬───────────┐
│ serial ┆ player_nam ┆ club      ┆ position   ┆ … ┆ conceded ┆ saved_pena ┆ cleanshee ┆ punches   │
│ ---    ┆ e          ┆ ---       ┆ ---        ┆   ┆ ---      ┆ lties      ┆ ts        ┆ made      │
│ i64    ┆ ---        ┆ str       ┆ str        ┆   ┆ i64      ┆ ---        ┆ ---       ┆ ---       │
│        ┆ str        ┆           ┆            ┆   ┆          ┆ i64        ┆ i64       ┆ i64       │
╞════════╪════════════╪═══════════╪════════════╪═══╪══════════╪════════════╪═══════════╪═══════════╡
│ 24     ┆ Henderson  ┆ Liverpool ┆ Midfielder ┆ … ┆ 1        ┆ 0          ┆ 0         ┆ 1         │
│ 24     ┆ Henderson  ┆ Liverpool ┆ Midfielder ┆ … ┆ 1        ┆ 0          ┆ 0         ┆ 1         │

```
-Looks like the join only got very few matched results because the player name field is pretty dirty. Will take work to clean up the strings so let's look into key champions league stats for now




