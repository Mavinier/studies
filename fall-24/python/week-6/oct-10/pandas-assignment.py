import pandas as pd
csv_file_path = "fall-24/python/week-6/oct-10/assignments.csv"

df = pd.read_csv(csv_file_path)
print("---Only the firts 5 rows---")
print(df.head())

name_score = df[["Name", "Score"]]
print(f"\n---Only Name and Score columns---\n {name_score}")

print("\n---Only the rows where Score is above 85---")
print(df[df["Score"] > 85])

average_age = df["Age"].aggregate("mean")
print(f"\n---Average age: {average_age}---")

max_score = df["Score"].aggregate("max")
filtered = df.loc[df.Score == max_score]
print(f"\n---Individual with the highest score---\n {filtered}")

cities = ["Chicago", "Huston"]
filtered_city = df.loc[df["City"].isin(cities)]
print(f"\n---Individuals living in Chicago or Huston---\n {filtered_city}")

sorted_by_age = df.sort_values(by="Age", ascending=False)
print(f"\n---Individuals sorted by age (DESC)---\n {sorted_by_age}")

df["Passed"] = df["Score"].apply(lambda x: "Yes" if x >= 80 else "No")
print(f"\n---Table showing if the individuals passed or not---\n {df}")
