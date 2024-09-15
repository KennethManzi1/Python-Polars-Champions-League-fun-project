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


**Champions League Top Performing Players Data**
```Python
import polars as pl

ChampionsLeague_Top_players = pl.DataFrame(
    {
        "Ranking": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "Player": ['Salah', 'Haaland', 'Mbappe', 'Bellingham', 'Saka', 'Vinicius JR', 
                   "Valverde", "Van Dijk", "Kevin De Bruyne", "Trent", "Yamal"],
        "Club Name": ['Liverpool', 'Manchester City', 'Paris Saint-Germain', 'Real Madrid', 
                      'Arsenal', 'Real Madrid', 'Real Madrid', 'Liverpool', 'Manchester City', 
                      'Liverpool', 'Barcelona'],
        "Goals": [10, 15, 12, 7, 9, 11, 8, 3, 5, 2, 6],
        "Assists": [7, 4, 6, 8, 5, 7, 6, 2, 10, 4, 3],
        "Appearances": [12, 11, 13, 12, 11, 12, 11, 10, 13, 11, 10]
    }
)

# Show the DataFrame
print(ChampionsLeague_Top_players)
shape: (11, 6)
┌─────────┬─────────────────┬─────────────────────┬───────┬─────────┬─────────────┐
│ Ranking ┆ Player          ┆ Club Name           ┆ Goals ┆ Assists ┆ Appearances │
│ ---     ┆ ---             ┆ ---                 ┆ ---   ┆ ---     ┆ ---         │
│ i64     ┆ str             ┆ str                 ┆ i64   ┆ i64     ┆ i64         │
╞═════════╪═════════════════╪═════════════════════╪═══════╪═════════╪═════════════╡
│ 1       ┆ Salah           ┆ Liverpool           ┆ 10    ┆ 7       ┆ 12          │
│ 2       ┆ Haaland         ┆ Manchester City     ┆ 15    ┆ 4       ┆ 11          │
│ 3       ┆ Mbappe          ┆ Paris Saint-Germain ┆ 12    ┆ 6       ┆ 13          │
│ 4       ┆ Bellingham      ┆ Real Madrid         ┆ 7     ┆ 8       ┆ 12          │
│ 5       ┆ Saka            ┆ Arsenal             ┆ 9     ┆ 5       ┆ 11          │
│ …       ┆ …               ┆ …                   ┆ …     ┆ …       ┆ …           │
│ 7       ┆ Valverde        ┆ Real Madrid         ┆ 8     ┆ 6       ┆ 11          │
│ 8       ┆ Van Dijk        ┆ Liverpool           ┆ 3     ┆ 2       ┆ 10          │
│ 9       ┆ Kevin De Bruyne ┆ Manchester City     ┆ 5     ┆ 10      ┆ 13          │
│ 10      ┆ Trent           ┆ Liverpool           ┆ 2     ┆ 4       ┆ 11          │
│ 11      ┆ Yamal           ┆ Barcelona           ┆ 6     ┆ 3       ┆ 10          │
```

**Champions League Top Performing Players based on Key statistics**

```Python
#Adding Additional Columns
ChampionsLeague_Top_players = ChampionsLeague_Top_players.with_columns([
    pl.Series("Minutes Played", [1080, 990, 1170, 1140, 1020, 1110, 1090, 930, 1260, 1020, 900]),
    pl.Series("Pass Accuracy", [84, 76, 89, 91, 78, 87, 86, 92, 88, 83, 81]),  # in percentage
    pl.Series("Tackles", [15, 6, 9, 4, 12, 8, 18, 22, 5, 24, 10]),
    pl.Series("Yellow Cards", [2, 1, 3, 0, 1, 2, 1, 3, 2, 1, 1]),
    pl.Series("Red Cards", [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])
])

print(ChampionsLeague_Top_players)

shape: (11, 11)
┌─────────┬────────────┬─────────────────────┬───────┬───┬──────────┬─────────┬────────┬───────────┐
│ Ranking ┆ Player     ┆ Club Name           ┆ Goals ┆ … ┆ Pass     ┆ Tackles ┆ Yellow ┆ Red Cards │
│ ---     ┆ ---        ┆ ---                 ┆ ---   ┆   ┆ Accuracy ┆ ---     ┆ Cards  ┆ ---       │
│ i64     ┆ str        ┆ str                 ┆ i64   ┆   ┆ ---      ┆ i64     ┆ ---    ┆ i64       │
│         ┆            ┆                     ┆       ┆   ┆ i64      ┆         ┆ i64    ┆           │
╞═════════╪════════════╪═════════════════════╪═══════╪═══╪══════════╪═════════╪════════╪═══════════╡
│ 1       ┆ Salah      ┆ Liverpool           ┆ 10    ┆ … ┆ 84       ┆ 15      ┆ 2      ┆ 0         │
│ 2       ┆ Haaland    ┆ Manchester City     ┆ 15    ┆ … ┆ 76       ┆ 6       ┆ 1      ┆ 0         │
│ 3       ┆ Mbappe     ┆ Paris Saint-Germain ┆ 12    ┆ … ┆ 89       ┆ 9       ┆ 3      ┆ 0         │
│ 4       ┆ Bellingham ┆ Real Madrid         ┆ 7     ┆ … ┆ 91       ┆ 4       ┆ 0      ┆ 0         │
│ 5       ┆ Saka       ┆ Arsenal             ┆ 9     ┆ … ┆ 78       ┆ 12      ┆ 1      ┆ 0         │
│ …       ┆ …          ┆ …                   ┆ …     ┆ … ┆ …        ┆ …       ┆ …      ┆ …         │
│ 7       ┆ Valverde   ┆ Real Madrid         ┆ 8     ┆ … ┆ 86       ┆ 18      ┆ 1      ┆ 0         │
│ 8       ┆ Van Dijk   ┆ Liverpool           ┆ 3     ┆ … ┆ 92       ┆ 22      ┆ 3      ┆ 1         │
│ 9       ┆ Kevin De   ┆ Manchester City     ┆ 5     ┆ … ┆ 88       ┆ 5       ┆ 2      ┆ 0         │
│         ┆ Bruyne     ┆                     ┆       ┆   ┆          ┆         ┆        ┆           │
│ 10      ┆ Trent      ┆ Liverpool           ┆ 2     ┆ … ┆ 83       ┆ 24      ┆ 1      ┆ 0         │
│ 11      ┆ Yamal      ┆ Barcelona           ┆ 6     ┆ … ┆ 81       ┆ 10      ┆ 1      ┆ 0         │
```





