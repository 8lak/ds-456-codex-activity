"""
Visualize Ward Assignment Mismatches
-----------------------------------

Produces an interactive folium map saved to `data/ward_mismatches_map.html`.
Points where the dataset `Ward` differs from the ward computed by spatial join
are shown in red; matches are shown in green. The official ward polygons are
displayed as a base layer.
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium


CSV_PATH = 'data/Snow_Emergency_Victory2_Tags_2023.csv'
WARDS_GEOJSON = 'data/City_Council_Wards.geojson'
OUT_HTML = 'data/ward_mismatches_map.html'


def main():
    df = pd.read_csv(CSV_PATH)

    # build GeoDataFrame from coordinates
    gdf = gpd.GeoDataFrame(df.copy(), geometry=[Point(xy) for xy in zip(df.Longitude, df.Latitude)], crs='EPSG:4326')

    # load ward polygons
    gdf_wards = gpd.read_file(WARDS_GEOJSON)
    # normalize ward id column
    if 'BDNUM' in gdf_wards.columns:
        gdf_wards['WARD'] = gdf_wards['BDNUM'].astype(int)
    elif 'WARD' in gdf_wards.columns:
        gdf_wards['WARD'] = gdf_wards['WARD'].astype(int)

    # spatial join to get ward from geometry
    joined = gpd.sjoin(gdf, gdf_wards[['WARD','geometry']], how='left', predicate='within')
    joined['ward_from_spatial'] = pd.to_numeric(joined['WARD'], errors='coerce').astype('Int64')
    joined['ward_original'] = pd.to_numeric(joined['Ward'], errors='coerce').astype('Int64')
    joined['match'] = joined['ward_from_spatial'] == joined['ward_original']

    # Prepare map
    center = [joined['Latitude'].mean(), joined['Longitude'].mean()]
    m = folium.Map(location=center, zoom_start=11, tiles='cartodbpositron')

    # Add ward polygons as a layer
    folium.GeoJson(
        WARDS_GEOJSON,
        name='Ward boundaries',
        style_function=lambda feat: {
            'fillColor': 'transparent', 'color': '#444444', 'weight': 1
        }
    ).add_to(m)

    # Feature groups for matches/mismatches
    fg_match = folium.FeatureGroup(name='Matches (green)')
    fg_mismatch = folium.FeatureGroup(name='Mismatches (red)')

    # Add points
    for _, row in joined.iterrows():
        lat = row['Latitude']
        lon = row['Longitude']
        addr = row.get('Address', '')
        ward_orig = '' if pd.isna(row['ward_original']) else int(row['ward_original'])
        ward_spat = '' if pd.isna(row['ward_from_spatial']) else int(row['ward_from_spatial'])
        popup = folium.Popup(f"<b>{addr}</b><br>Original Ward: {ward_orig}<br>Spatial Ward: {ward_spat}", max_width=300)

        color = 'green' if row['match'] else 'red'
        fg = fg_match if row['match'] else fg_mismatch

        folium.CircleMarker(
            location=[lat, lon],
            radius=4,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            popup=popup
        ).add_to(fg)

    fg_match.add_to(m)
    fg_mismatch.add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)
    m.save(OUT_HTML)
    print(f"Saved mismatch visualization to {OUT_HTML}")


if __name__ == '__main__':
    main()
