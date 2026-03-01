import pandas as pd
import matplotlib.pyplot as plt

# 1. Verified Real-World Data (Volume: UN Comtrade, Intensity: CEEW, Price: EU ETS)
data = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Export_Volume_Tonnes': [320000, 380000, 350000, 264600, 260000],
    'EU_Carbon_Price_EUR': [53, 81, 85, 70, 80], 
    'Avg_Emission_Intensity': [20.88, 20.88, 20.88, 20.88, 20.88] 
}

df = pd.DataFrame(data)

# 2. Calculate the Theoretical CBAM Liability
df['Theoretical_CBAM_Liability_Millions_EUR'] = (
    df['Export_Volume_Tonnes'] * df['Avg_Emission_Intensity'] * df['EU_Carbon_Price_EUR']
) / 1_000_000

# 3. Visualize the Financial Risk
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Year'], df['Theoretical_CBAM_Liability_Millions_EUR'], color='#2c3e50')

plt.title('EU CBAM Liability on Indian Aluminum Exports (2021-2025)', fontsize=14)
plt.suptitle('Based on CEEW Emission Intensity (20.88 tCO2/tonne)', fontsize=10, color='gray')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Estimated Carbon Tax Exposure (Million €)', fontsize=12)
plt.xticks(df['Year'])
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'€{round(yval)}M', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()