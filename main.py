# 1. Import pandas
import pandas as pd

# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data

critic = pd.read_csv("metacritic2.csv", index_col = 0)
print(critic)


# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)

mario = critic[critic.index.str.contains("Mario")]
print(mario)

# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)

mario = mario.sort_values(by = ["Release Year"])
print(mario)


# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?


groups = critic.groupby("Release Year").count()
print(groups)


# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?

print(critic.groupby("Platform").count())
print(critic.groupby("Platform").mean())
print(critic.groupby("Platform").median())

# 7. Create a new dataframe from the HunterAMC.csv file.
amc = pd.read_csv("HunterAMC.csv", sep = '\t')
print(amc)

# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.

ten = amc.loc[amc["contest"] == 0]
print(ten)
twe = amc.loc[amc["contest"]== 2]
print(twe)

# 9. Find the average scores for each contest.

print(ten["TotalScore"].mean())
print(twe["TotalScore"].mean())

# 10. For each column, count how often each answer choice was selected.

for column in amc.columns[6:]:
  print(column)
  print(amc[column].value_counts())