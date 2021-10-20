import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def barplot_missing_data(dataframe):
    missings = dataframe.isnull().sum()  # summarize the n of missing values for each variable
    df = pd.DataFrame({"n_of_missings": missings})  # These series save to a dataframe
    missings_df = df[df["n_of_missings"]>0]  # keep only the variales that have missings
    fig, ax= plt.subplots(dpi=100, figsize=(6,4))
    sns.barplot(data=missings_df, x=missings_df.index, y="n_of_missings")
    ax.set(title="The number of missing values for variables", xlabel="variables", ylabel="number of missings")