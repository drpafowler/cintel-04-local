import pandas as pd
from palmerpenguins import load_penguins

# Load the original dataset
penguins = load_penguins()

# Replicate the dataset to create 5000 rows
replicated_penguins = pd.concat([penguins] * (5000 // len(penguins)), ignore_index=True)

# If the length is still less than 5000, sample additional rows
if len(replicated_penguins) < 5000:
    additional_rows = penguins.sample(5000 - len(replicated_penguins), replace=True)
    replicated_penguins = pd.concat([replicated_penguins, additional_rows], ignore_index=True)

# Save the new dataset to a CSV file
replicated_penguins.to_csv('palmer_penguins_5000.csv', index=False)

print("New dataset with 5000 rows created: palmer_penguins_5000.csv")