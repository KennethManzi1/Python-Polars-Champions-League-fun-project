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
```







