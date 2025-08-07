import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(100)

# Generate realistic synthetic data for customer acquisition cost and lifetime value
num_points = 50

# Acquisition cost between $50 and $500
acquisition_cost = np.random.uniform(50, 500, num_points)

# Lifetime value with positive correlation to acquisition cost + noise
lifetime_value = acquisition_cost * np.random.uniform(1.5, 3.0, num_points) + np.random.normal(0, 50, num_points)

# Create DataFrame
df = pd.DataFrame({
    'Acquisition_Cost': acquisition_cost,
    'Lifetime_Value': lifetime_value
})

# Set Seaborn style for professional appearance
sns.set_style('whitegrid')
sns.set_context('talk')  # Presentation-ready text sizes

# FIXED: Use figsize=(5.12, 5.12) with dpi=100 to get exactly 512x512 pixels
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Create scatterplot using sns.scatterplot()
scatter = sns.scatterplot(
    data=df, 
    x='Acquisition_Cost', 
    y='Lifetime_Value',
    color='steelblue',  # Professional blue color
    s=100,  # Marker size
    alpha=0.7  # Slight transparency for professional look
)

# Professional styling and labels
plt.title('Customer Lifetime Value vs. Acquisition Cost', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Acquisition Cost (USD)', fontsize=14)
plt.ylabel('Customer Lifetime Value (USD)', fontsize=14)

# Add grid for better readability
plt.grid(True, alpha=0.3)

# FIXED: Use tight_layout with pad=0 and remove bbox_inches='tight'
plt.tight_layout(pad=0)

# FIXED: Save chart without bbox_inches='tight' to maintain exact dimensions
plt.savefig('chart.png', dpi=100, bbox_inches=None, 
            facecolor='white', edgecolor='none')

# Close the plot to free memory
plt.close()

print("Chart successfully generated as 'chart.png' with exactly 512x512 dimensions")
