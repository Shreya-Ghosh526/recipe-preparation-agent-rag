import pandas as pd
import ast

df = pd.read_csv("RAW_recipes.csv")
df = df.head(100)

with open("recipes.txt", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():

        try:
            ingredients = ast.literal_eval(row["ingredients"])
        except:
            ingredients = []

        try:
            steps = ast.literal_eval(row["steps"])
        except:
            steps = []

        f.write(f"Recipe: {row['name']}\n\n")

        f.write("Ingredients:\n")
        for item in ingredients:
            f.write(f"- {item}\n")

        f.write("\nSteps:\n")
        for i, step in enumerate(steps, 1):
            f.write(f"{i}. {step}\n")

        f.write("\n" + "=" * 80 + "\n\n")

print("recipes.txt created successfully")