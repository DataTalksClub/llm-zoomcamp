import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = pd.read_csv("LLMZoomcamp_registrations_processed.csv")
    data["Country"].str.strip().reset_index()["Country"].str.lower()

    # Count registrations per country
    country_counts = data['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Counts']

    country_mapping = {
        "united states": "united states of america",
        "usa": "united states of america",
        "singapore": "",
        "us": "united states of america",
        "uk": "united kingdom",
        "brasil": "brazil",
        "türkiye": "turkey",
        "méxico": "mexico",
        "perú": "peru",
        "españa": "spain",
        "deutschland": "germany",
        "uae": "united arab emirates",
        "the netherlands": "netherlands"
    }

    country_counts["Country"] = country_counts["Country"].replace(country_mapping)
    country_counts = country_counts.groupby('Country', as_index=False)['Counts'].sum()
    country_counts["Counts_log"] = np.log1p(country_counts["Counts"])

    # Load world geometry from geopandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world["name"] = world["name"].str.lower()

    # Merge the country counts with the world geometry 'name' in world corresponds to the country names
    world = world.merge(country_counts, how="left", left_on="name", right_on="Country")
    world["Counts_log"] = world["Counts_log"].fillna(1.3)

    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    world.plot(column='Counts_log', ax=ax, legend=True, cmap="Blues")


if __name__ == "__main__":
    main()
