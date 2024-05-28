

import matplotlib.pyplot as plt

age_bins = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60']
populations = [15, 8, 30, 5, 3, 25]

# Create histogram
plt.bar(age_bins, populations, color='orange', edgecolor='black')

# Add title and labels
plt.title('Distribution of Ages in a Population')
plt.xlabel('Age Group')
plt.ylabel('Population')

# Show plot
plt.show()
