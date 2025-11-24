import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv", header=None)
print(df)

names = df[1].unique().tolist()

print(names)

seclected_rows = df.loc[(df[1] == 'frame_0001') | (df[2]== 'frame_0001')]
print(seclected_rows)

values = seclected_rows.iloc[:, 3:].values  # Assuming columns from index 3 onwards are numerical

# Plot the heatmap
g = sns.heatmap(values, annot=True, cmap='coolwarm')  # Adding annotations for clarity
g.set_yticklabels(g.get_yticklabels(), rotation=0)
g.set_ylabel('Frames')  # Set the y-axis label
cbar = g.collections[0].colorbar  # Get the color bar
cbar.set_label('Percent match', rotation=270, labelpad=15)  # Set label for the color bar
g.set_title('Heatmap of Frame 1')

# Adjust the layout and show the plot
plt.tight_layout()
plt.savefig('heatmap_output.png', format='png')
plt.show()
