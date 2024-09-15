#!/usr/bin/env python
# coding: utf-8

# In[19]:


get_ipython().system('pip install Polars')
get_ipython().system('pip install pyarrow')


# ### Testing some Polars features with a Dummy Dataframe

# In[63]:


import polars as pl

##Getting Data of Champions League Players 2021-2022

# List of file paths for CSVs
csv_files_champions_league_2022 = ['/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/attacking.csv', '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/disciplinary.csv', '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/distributon.csv', 
                                   '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/key_stats.csv', '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/goals.csv', 
                                   '/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/defending.csv','/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/goalkeeping.csv']


#test it out by reading the first file which is the attacking csv file

combined_df = pl.read_csv(csv_files_champions_league_2022[0], encoding='ISO-8859-1', infer_schema_length=10000, ignore_errors=True )

print(combined_df)


# In[67]:


## Now we will loop through the champions league 2022 files and join them using the player name


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



#Looks like the join only got very few matched results because the player name field is pretty dirty. Will take work to clean up the strings so let's look into key champions league stats for now


# In[55]:


##Champions League top stats

Champions_League_2022_top_stats = pl.read_csv(csv_files_champions_league_2022[3], encoding='ISO-8859-1', infer_schema_length=10000, ignore_errors=True )
print(Champions_League_2022_top_stats)


# In[57]:


##SQL QUERY Test
result = pl.sql("""
    SELECT "*"
    FROM Champions_League_2022_top_stats
    ORDER BY goals DESC
""").collect()

print(result)


# In[81]:


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


# In[87]:


##Ranking the clubs with highest Total Goals and Assists

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


# In[ ]:




