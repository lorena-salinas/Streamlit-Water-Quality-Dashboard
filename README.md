# Water Quality Dashboard
**CIS 3590 – Internship Ready Software Development**

**Author:** Lorena Salinas

An interactive web app, built with Streamlit and Plotly, for exploring water-quality readings.

🔗 **Live app:** https://app-water-quality-dashboard-lfyc9j3ohgxpjtizwrduko.streamlit.app/

## Purpose
 
This app turns a raw CSV of sensor readings into tables, charts and a map.

## Dataset
 
File: `biscayneBay_waterquality.csv` (included in this repository) 

Each row is one sensor reading. The main columns used by the app:
 
| Column | Description | Unit |
|---|---|---|
| `Time` | Time the reading was taken | hh:mm:ss |
| `Latitude`, `Longitude` | GPS position of the reading | degrees |
| `Temperature (c)` | Water temperature | °C |
| `Salinity (ppt)` | Amount of dissolved salt in the water | parts per thousand |
| `Total Water Column (m)` | Water depth at that point | meters | | |
 
Users can also **upload their own CSV** with the same column names.
 
## App Sections
 
| Tab | What it shows |
|---|---|
| **Data** | The raw data table and descriptive statistics (count, mean, min, max, etc.). A multiselect lets you choose which columns to display. |
| **Charts** | **Line chart:** any parameter over time, chosen from a dropdown. **Scatter plot:** temperature vs. salinity, colored by depth. **3D plot:** a model of the bay floor built from GPS position and depth. |
| **Maps** | The path where readings were collected, plotted on a street map and colored by water temperature. |
 
## How to Use the App
 
1. **Open the app** using the live link above.
2. **(Optional) Upload data:** in the sidebar, click **Browse files** to upload your own
   water-quality CSV. If you don't upload anything, the app uses the Biscayne Bay dataset.
3. **Data tab:** use **Select columns to display** to choose which columns appear in the descriptive statistics
   table. Click a column header to sort.
4. **Charts tab:** pick a measurement from **Select a parameter** to see how it changed over
   time. Hover over any chart to see exact values, and drag the 3D chart to rotate it.
5. **Maps tab:** zoom and pan the map. Hover over a point to see its temperature.
6. Every Plotly chart has a toolbar in its top-right corner for zooming, resetting, or
   **downloading the chart as a PNG**.

## Project Files
 
```
├── app.py                          # The Streamlit app
├── biscayneBay_waterquality.csv    # Default dataset
├── requirements.txt                # Libraries needed to run the app
├── README.md                       # This file
└── .gitignore                      # Keeps .venv and other local files out of GitHub
```

## Run It on Your Own Computer (Mac)
 
```bash
# 1. Download the project
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
 
# 2. Create and turn on a virtual environment
python3 -m venv .venv
source .venv/bin/activate
 
# 3. Install the required libraries
python3 -m pip install -r requirements.txt
 
# 4. Start the app (it opens in your browser at http://localhost:8501)
streamlit run app.py
```
 
On Windows, use `python` instead of `python3` and `.venv\Scripts\activate` to turn on the
virtual environment.
 
## Requirements
 
Listed in `requirements.txt`:
 
- `streamlit` – builds the web app
- `pandas` – reads and processes the CSV data
- `plotly` – creates the interactive charts and map

## Built With
 
Python · Streamlit · pandas · Plotly · GitHub · Streamlit Community Cloud
