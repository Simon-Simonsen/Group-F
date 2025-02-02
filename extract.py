import pandas as pd

df = pd.read_csv("util/data-student.csv")


df_fil = df[df["Group_ID"] == "F"]

df_fil.to_csv("Images_review.csv", index = False)