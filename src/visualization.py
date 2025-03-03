
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def show_boxplots(columns: list, df: pd.DataFrame) -> None:
  """
  Creates boxplots for float-type features in the given DataFrame.

    Args:
        columns (list): List of feature names that are of float type.
        df (pd.DataFrame): The DataFrame containing the features.

    Returns:
        None: Displays the boxplots in a grid with up to 3 columns per row.
  """
  row = max(1, np.ceil(len(columns) / 3).astype(int))
  fig, axes = plt.subplots(row, 3, figsize=(15, 5 * row))

  if row == 1:
      axes = np.array(axes).reshape(1, -1) 

  for index, name in enumerate(columns): 
      r, c = divmod(index, 3)
      sns.boxplot(y=name, data=df, ax=axes[r, c])

  plt.tight_layout()
  plt.show()
