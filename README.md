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


**Champions League Top Performing Players in 2021-2022 Data**
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

**Now we will loop through the champions league 2021-2022 files and join them using the player name**

```Python
CL_22 = []

for cl_file in csv_files_champions_league_2022:
    cl_df = pl.read_csv(cl_file, encoding='ISO-8859-1', infer_schema_length=10000, ignore_errors=True )
    CL_22.append(cl_df)

##print(CL_22)

# Merge all DataFrames by performing a join on the common column
Champions_League2022 = CL_22[0]
for df in CL_22[1:]:
    Champions_League2022 = Champions_League2022.join(df, on='player_name', how='inner')

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
- Looks like the join only got very few matched results because the player name field is pretty dirty. Will take work to clean up the strings so let's look into key champions league stats for now

**Champions League top stats**
```Python
Champions_League_2022_top_stats = pl.read_csv(csv_files_champions_league_2022[3], encoding='ISO-8859-1', infer_schema_length=10000, ignore_errors=True )
print(Champions_League_2022_top_stats)

shape: (747, 8)
┌─────────────┬─────────────┬────────────┬─────────────┬────────────┬───────┬─────────┬────────────┐
│ player_name ┆ club        ┆ position   ┆ minutes_pla ┆ match_play ┆ goals ┆ assists ┆ distance_c │
│ ---         ┆ ---         ┆ ---        ┆ yed         ┆ ed         ┆ ---   ┆ ---     ┆ overed     │
│ str         ┆ str         ┆ str        ┆ ---         ┆ ---        ┆ i64   ┆ i64     ┆ ---        │
│             ┆             ┆            ┆ i64         ┆ i64        ┆       ┆         ┆ str        │
╞═════════════╪═════════════╪════════════╪═════════════╪════════════╪═══════╪═════════╪════════════╡
│ Courtois    ┆ Real Madrid ┆ Goalkeeper ┆ 1230        ┆ 13         ┆ 0     ┆ 0       ┆ 64.2       │
│ Vinicius    ┆ Real Madrid ┆ Forward    ┆ 1199        ┆ 13         ┆ 4     ┆ 6       ┆ 133        │
│ Junior      ┆             ┆            ┆             ┆            ┆       ┆         ┆            │
│ Benzema     ┆ Real Madrid ┆ Forward    ┆ 1106        ┆ 12         ┆ 15    ┆ 1       ┆ 121.5      │
│ ModriÛ     ┆ Real Madrid ┆ Midfielder ┆ 1077        ┆ 13         ┆ 0     ┆ 4       ┆ 124.5      │
│ íder       ┆ Real Madrid ┆ Defender   ┆ 1076        ┆ 12         ┆ 0     ┆ 0       ┆ 110.4      │
│ Milití£o    ┆             ┆            ┆             ┆            ┆       ┆         ┆            │
│ …           ┆ …           ┆ …          ┆ …           ┆ …          ┆ …     ┆ …       ┆ …          │
│ Gil Dias    ┆ Benfica     ┆ Midfielder ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.7        │
│ Rodrigo     ┆ Sporting CP ┆ Forward    ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.7        │
│ Ribeiro     ┆             ┆            ┆             ┆            ┆       ┆         ┆            │
│ Cojocari    ┆ Sheriff     ┆ Defender   ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.5        │
│ Maouassa    ┆ Club Brugge ┆ Defender   ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.2        │
│ Zesiger     ┆ Young Boys  ┆ Defender   ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0          │
```


***


### SQL TIME IN POLARS YAYYY


**Most goals scored by players in 2021-2022 champions league season**
```Python
##SQL QUERY Test
result = pl.sql("""
    SELECT "*"
    FROM Champions_League_2022_top_stats
    ORDER BY goals DESC
""").collect()

print(result)

shape: (747, 8)
┌─────────────┬─────────────┬────────────┬─────────────┬────────────┬───────┬─────────┬────────────┐
│ player_name ┆ club        ┆ position   ┆ minutes_pla ┆ match_play ┆ goals ┆ assists ┆ distance_c │
│ ---         ┆ ---         ┆ ---        ┆ yed         ┆ ed         ┆ ---   ┆ ---     ┆ overed     │
│ str         ┆ str         ┆ str        ┆ ---         ┆ ---        ┆ i64   ┆ i64     ┆ ---        │
│             ┆             ┆            ┆ i64         ┆ i64        ┆       ┆         ┆ str        │
╞═════════════╪═════════════╪════════════╪═════════════╪════════════╪═══════╪═════════╪════════════╡
│ Benzema     ┆ Real Madrid ┆ Forward    ┆ 1106        ┆ 12         ┆ 15    ┆ 1       ┆ 121.5      │
│ Lewandowski ┆ Bayern      ┆ Forward    ┆ 876         ┆ 10         ┆ 13    ┆ 3       ┆ 99.7       │
│ Haller      ┆ Ajax        ┆ Forward    ┆ 668         ┆ 8          ┆ 11    ┆ 1       ┆ 82.2       │
│ Salah       ┆ Liverpool   ┆ Forward    ┆ 1008        ┆ 13         ┆ 8     ┆ 2       ┆ 112        │
│ Mahrez      ┆ Man. City   ┆ Midfielder ┆ 986         ┆ 12         ┆ 7     ┆ 2       ┆ 120.1      │
│ …           ┆ …           ┆ …          ┆ …           ┆ …          ┆ …     ┆ …       ┆ …          │
│ Gil Dias    ┆ Benfica     ┆ Midfielder ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.7        │
│ Rodrigo     ┆ Sporting CP ┆ Forward    ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.7        │
│ Ribeiro     ┆             ┆            ┆             ┆            ┆       ┆         ┆            │
│ Cojocari    ┆ Sheriff     ┆ Defender   ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.5        │
│ Maouassa    ┆ Club Brugge ┆ Defender   ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0.2        │
│ Zesiger     ┆ Young Boys  ┆ Defender   ┆ 1           ┆ 1          ┆ 0     ┆ 0       ┆ 0          │
└─────────────┴─────────────┴────────────┴─────────────┴────────────┴───────┴─────────┴────────────┘
```
- Wow Benzema was on fire that season in terms of goals. It's no wonder he won the Balon Dor that year. He had big performances against Chelsea in the Quarter final and Manchester City in the Semis. Oh yes and a hattrick against PSG in the second leg of the first knockout round.
- Those are big teams that he took out in order to win the trophy later on against my team Liverpool as they unfortunately lost to Benzema's Real Madrid.
- Lewandowski was pretty good for Bayern as well as well as Haller from Ajax.

**Club Statistics Goals and Assists**
```Python
##SQL QUERY Club Stats
result = pl.sql("""
    SELECT "player_name",
    "club", 
    SUM(goals) AS Total_Goals,
    SUM(assists) AS Total_Assists,
    (SUM(goals) + SUM(assists)) AS G_A
    FROM Champions_League_2022_top_stats
    GROUP BY "player_name", "club"
    ORDER BY G_A DESC
""").collect()

Club_stats = result
print(Club_stats)

┌─────────────┬─────────────┬─────────────┬───────────────┬─────┐
│ player_name ┆ club        ┆ Total_Goals ┆ Total_Assists ┆ G_A │
│ ---         ┆ ---         ┆ ---         ┆ ---           ┆ --- │
│ str         ┆ str         ┆ i64         ┆ i64           ┆ i64 │
╞═════════════╪═════════════╪═════════════╪═══════════════╪═════╡
│ Benzema     ┆ Real Madrid ┆ 15          ┆ 1             ┆ 16  │
│ Lewandowski ┆ Bayern      ┆ 13          ┆ 3             ┆ 16  │
│ Haller      ┆ Ajax        ┆ 11          ┆ 1             ┆ 12  │
│ Saní©       ┆ Bayern      ┆ 6           ┆ 6             ┆ 12  │
│ Salah       ┆ Liverpool   ┆ 8           ┆ 2             ┆ 10  │
│ …           ┆ …           ┆ …           ┆ …             ┆ …   │
│ Meraô      ┆ Beôiktaô  ┆ 0           ┆ 0             ┆ 0   │
│ Trippier    ┆ Atlí©tico   ┆ 0           ┆ 0             ┆ 0   │
│ Mbemba      ┆ Porto       ┆ 0           ┆ 0             ┆ 0   │
│ Batshuayi   ┆ Beôiktaô  ┆ 0           ┆ 0             ┆ 0   │
│ Taarabt     ┆ Benfica     ┆ 0           ┆ 0             ┆ 0   │
└─────────────┴─────────────┴─────────────┴───────────────┴─────┘

```
- Lewandowski and Benzema tied with 16 G_A(Goals + assists) for the 2021-2022 champions league season

**Ranking the clubs with highest Total Goals and Assists**

```Python
sql_query = pl.sql("""
    WITH TotalStats AS 
    (
        SELECT 
        "club",
        SUM(goals) AS Total_Goals,
        SUM(assists) AS Total_Assists,
        (SUM(goals) + SUM(assists)) AS G_A
        FROM Champions_League_2022_top_stats
        GROUP BY "club"
    )
    SELECT 
        *,
    FROM TotalStats
    ORDER BY G_A DESC
""").collect()

Ranked_clubs = sql_query
print(Ranked_clubs)

shape: (32, 4)
┌──────────────────┬─────────────┬───────────────┬─────┐
│ club             ┆ Total_Goals ┆ Total_Assists ┆ G_A │
│ ---              ┆ ---         ┆ ---           ┆ --- │
│ str              ┆ i64         ┆ i64           ┆ i64 │
╞══════════════════╪═════════════╪═══════════════╪═════╡
│ Bayern           ┆ 30          ┆ 24            ┆ 54  │
│ Liverpool        ┆ 28          ┆ 23            ┆ 51  │
│ Man. City        ┆ 28          ┆ 23            ┆ 51  │
│ Real Madrid      ┆ 28          ┆ 21            ┆ 49  │
│ Ajax             ┆ 21          ┆ 17            ┆ 38  │
│ …                ┆ …           ┆ …             ┆ …   │
│ Porto            ┆ 2           ┆ 3             ┆ 5   │
│ Shakhtar Donetsk ┆ 2           ┆ 2             ┆ 4   │
│ Barcelona        ┆ 2           ┆ 1             ┆ 3   │
│ Malmí_           ┆ 1           ┆ 1             ┆ 2   │
│ Dynamo Kyiv      ┆ 1           ┆ 1             ┆ 2   │
```
- Bayern had the highest Goals and Assists contributions overall in the entire 2021-2022 season with Liverpool right behind.


***

### Links

- The link to the Polars user guide can be found [here](https://docs.pola.rs/)
- The link to the Data Camp introduction to Polars can be found [here](https://www.datacamp.com/blog/an-introduction-to-polars-python-s-tool-for-large-scale-data-analysis)
- The link to the CSV files can be found [here](https://www.kaggle.com/code/alisultanov/eda-champions-league-21-22/input?select=defending.csv)

