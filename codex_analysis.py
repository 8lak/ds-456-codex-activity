import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium  # for interactive maps
import numpy as np

# Load data
df = pd.read_csv('data/Snow_Emergency_Victory2_Tags_2023.csv')

# Display basic info
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nBasic statistics:")
print(df.describe())

# ============ EXPLORATION VISUALIZATIONS ============

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Ordinance code distribution (top violations)
ax1 = axes[0, 0]
ordinance_counts = df['Ordinance_'].value_counts().head(10)
ordinance_counts.plot(kind='barh', ax=ax1, color='steelblue')
ax1.set_title('Top 10 Ordinance Violations', fontsize=12, fontweight='bold')
ax1.set_xlabel('Count')

# 2. Violations by Ward
ax2 = axes[0, 1]
ward_counts = df['Ward'].value_counts().sort_index()
ward_counts.plot(kind='bar', ax=ax2, color='coral')
ax2.set_title('Violations by Ward', fontsize=12, fontweight='bold')
ax2.set_xlabel('Ward')
ax2.set_ylabel('Count')
ax2.tick_params(axis='x', rotation=45)

# 3. Violations by Neighborhood
ax3 = axes[1, 0]
neighborhood_counts = df['Neighborho'].value_counts().head(10)
neighborhood_counts.plot(kind='barh', ax=ax3, color='seagreen')
ax3.set_title('Top 10 Neighborhoods with Violations', fontsize=12, fontweight='bold')
ax3.set_xlabel('Count')

# 4. Day of week distribution
ax4 = axes[1, 1]
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_counts = df['Day'].value_counts().reindex(day_order)
day_counts.plot(kind='bar', ax=ax4, color='mediumpurple')
ax4.set_title('Violations by Day of Week', fontsize=12, fontweight='bold')
ax4.set_xlabel('Day')
ax4.set_ylabel('Count')
ax4.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('data/exploration_1_categorical.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: exploration_1_categorical.png")

# ============ GEOGRAPHIC VISUALIZATION ============

# 2D scatter plot of violations
fig, ax = plt.subplots(figsize=(14, 10))
scatter = ax.scatter(df['Longitude'], df['Latitude'], 
                     c=df['Ward'].astype('category').cat.codes, 
                     cmap='tab20', alpha=0.6, s=30, edgecolors='none')
ax.set_xlabel('Longitude', fontsize=11)
ax.set_ylabel('Latitude', fontsize=11)
ax.set_title('Geographic Distribution of Snow Emergency Violations\nMinneapolis 2023', 
             fontsize=13, fontweight='bold')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Ward')
plt.tight_layout()
plt.savefig('data/exploration_2_geographic_scatter.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exploration_2_geographic_scatter.png")

# ============ DENSITY HEATMAP ============

fig, ax = plt.subplots(figsize=(14, 10))
h = ax.hexbin(df['Longitude'], df['Latitude'], gridsize=25, cmap='YlOrRd', mincnt=1)
ax.set_xlabel('Longitude', fontsize=11)
ax.set_ylabel('Latitude', fontsize=11)
ax.set_title('Violation Density Heatmap - Minneapolis\n(Hexbin aggregation)', 
             fontsize=13, fontweight='bold')
cb = plt.colorbar(h, ax=ax)
cb.set_label('Number of Violations')
plt.tight_layout()
plt.savefig('data/exploration_3_density_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: exploration_3_density_heatmap.png")

# ============ INTERACTIVE MAP ============

# Create folium map centered on Minneapolis
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=11, tiles='OpenStreetMap')

# Add violation points with color coding by ward
ward_colors = {ward: f'#{np.random.randint(0, 0xFFFFFF):06x}' for ward in df['Ward'].unique()}

for idx, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=4,
        popup=f"Ward: {row['Ward']}<br>Address: {row['Address']}<br>Ordinance: {row['Ordinance_']}",
        color=ward_colors.get(row['Ward'], 'blue'),
        fill=True,
        fillOpacity=0.7
    ).add_to(m)

m.save('data/exploration_4_interactive_map.html')
print("✓ Saved: exploration_4_interactive_map.html")
print("\nOpen this file in your browser to explore the interactive map!")

# ============ CORRELATION & SUMMARY ============

print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)
print(f"Total violations: {len(df)}")
print(f"Number of wards: {df['Ward'].nunique()}")
print(f"Number of neighborhoods: {df['Neighborho'].nunique()}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Most common ordinance: {df['Ordinance_'].value_counts().index[0]}")
print(f"Most cited neighborhood: {df['Neighborho'].value_counts().index[0]}")
print(f"Most cited ward: {df['Ward'].value_counts().index[0]}")

# ============ TIME-OF-DAY ANALYSIS ============

print('\n\n=== Time-of-day analysis ===')

# Parse Time column; handle cases like '10:10:00' or '2023-02-24 10:10:00'
if 'Time' in df.columns:
    # try parse as time
    df['time_parsed'] = pd.to_datetime(df['Time'], errors='coerce').dt.time
    # fallback: if parse failed, try extracting hour from DateTime in 'Date' column
    if df['time_parsed'].isnull().all() and 'Date' in df.columns:
        df['time_parsed'] = pd.to_datetime(df['Date'], errors='coerce').dt.time
    # Extract hour (0-23)
    df['hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
    # if still null, try Date
    df.loc[df['hour'].isnull(), 'hour'] = pd.to_datetime(df['Date'], errors='coerce').dt.hour
else:
    df['hour'] = pd.NA

# Replace NaN hours with a sentinel and drop rows where hour is NA for plotting
hour_counts = df['hour'].value_counts(dropna=True).sort_index()
hour_counts_df = hour_counts.reset_index()
hour_counts_df.columns = ['hour', 'count']
hour_counts_df.to_csv('data/time_of_day_counts.csv', index=False)

print('\nSaved: data/time_of_day_counts.csv')

# Plot histogram of counts by hour
plt.figure(figsize=(12,6))
sns.barplot(x='hour', y='count', data=hour_counts_df, color='steelblue')
plt.title('Violations by Hour of Day')
plt.xlabel('Hour (0-23)')
plt.ylabel('Number of Violations')
plt.tight_layout()
plt.savefig('data/exploration_time_of_day_hist.png', dpi=300)
print('Saved: data/exploration_time_of_day_hist.png')

# Plot by hour stacked/colored by Ward (top wards)
top_wards = df['Ward'].value_counts().nlargest(6).index.tolist()
df_top = df[df['Ward'].isin(top_wards) & df['hour'].notna()].copy()
if not df_top.empty:
    pivot = df_top.pivot_table(index='hour', columns='Ward', values='Address', aggfunc='count', fill_value=0)
    pivot = pivot.reindex(range(0,24), fill_value=0)
    pivot.plot(kind='bar', stacked=True, figsize=(14,7), colormap='tab20')
    plt.title('Hourly Violations by Top Wards')
    plt.xlabel('Hour')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('data/exploration_time_of_day_by_ward.png', dpi=300)
    print('Saved: data/exploration_time_of_day_by_ward.png')
else:
    print('No hourly data available for top wards to plot.')

print('\nTime-of-day analysis complete.')

print('\nFinal Research Question (chosen):')
print('How are snow-emergency parking violations distributed by time of day during Feb 24–25, 2023?')