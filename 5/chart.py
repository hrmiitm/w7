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
# Higher acquisition costs generally lead to higher value customers
lifetime_value = acquisition_cost * np.random.uniform(1.5, 3.0, num_points) + np.random.normal(0, 50, num_points)

# Create DataFrame
df = pd.DataFrame({
    'Acquisition_Cost': acquisition_cost,
    'Lifetime_Value': lifetime_value
})

# Set Seaborn style for professional appearance
sns.set_style('whitegrid')
sns.set_context('talk')  # Presentation-ready text sizes

# Create figure with specific size for 512x512px at 64 dpi
plt.figure(figsize=(8, 8))

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

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save chart with exact specifications
plt.savefig('chart.png', dpi=64, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

# Close the plot to free memory
plt.close()

print("Chart successfully generated as 'chart.png' with 512x512 dimensions")
