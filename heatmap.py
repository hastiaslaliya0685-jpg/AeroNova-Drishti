
import json
import folium
from folium.plugins import HeatMap
import argparse

def generate_heatmap(preds_file, gps_file, output):
    with open(preds_file) as f:
        preds = json.load(f)
    with open(gps_file) as f:
        gps = json.load(f)

    heat_data = []
    for p, g in zip(preds, gps):
        heat_data.append([g["lat"], g["lon"], p["confidence"]])

    m = folium.Map(location=[gps[0]["lat"], gps[0]["lon"]], zoom_start=12)
    HeatMap(heat_data).add_to(m)
    m.save(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preds", required=True)
    parser.add_argument("--gps", required=True)
    parser.add_argument("--out", default="heatmap.html")
    args = parser.parse_args()
    generate_heatmap(args.preds, args.gps, args.out)
