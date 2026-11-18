# Import Statements

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Functions
def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    array1 = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
    dates = array1[:, 0].astype("datetime64")
    flows = array1[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

    for i in range(len(sites)):
        plt.plot(dates, flows[:, i], label=sites[i])

    # creates a legend
    plt.legend(title = "Site Numbers", loc = "upper right")
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")
    plt.title("Provo River Streamflow Data (2021)")

    # rotates the x labels 45 degrees
    plt.xticks(rotation = 45)
    plt.ylabel("Flowrate (cfs)")

    plt.title("Provo River Streamflow Data (2021)")

    plt.grid()
    plt.show()

### Values I got from excel Gauge	Max (cfs)	Date of max	Min (cfs)	Avg (cfs)
# 10163000	131	6/1/2021 8:15	35.6	57
# 10155200	215	6/27/2021 17:00	125	166.4
# 10155500	259	6/24/2021 20:15	182	213.3
# 10154200	406	6/2/2021 5:15	50.4	139.6
# 10155000	754	6/3/2021 5:45	23.2	187.8


def summarize(dates, flows, sites, filename="streamflow_summary.csv"):
    """Print and save summary statistics for each gauge."""
    rows = []

    # this goes through each site to calculate max,min,avd, and date.
    for i in range(len(sites)):
        gauge_flows = flows[:, i]
        max_value = np.max(gauge_flows)
        min_value = np.min(gauge_flows)
        avg_value = np.mean(gauge_flows)
        max_row = np.argmax(gauge_flows)
        date_of_max = np.datetime_as_string(dates[max_row], unit="s").replace("T", " ")

        # this appends dictionaries to ones list. 
        rows.append({
            "Gauge": sites[i],
            "Max (cfs)": max_value,
            "Date of max": date_of_max,
            "Min (cfs)": min_value,
            "Avg (cfs)": avg_value,
        })

    # This create a pandas dataframe from each row based on dictionaries. 
    summary = pd.DataFrame(rows).round({
        "Max (cfs)": 1,
        "Min (cfs)": 1,
        "Avg (cfs)": 1,
    })
    # this saves everything to an excel file.
    summary.to_csv(filename, index=False) 


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summarize(dates, flows, sites)

# asks the user to input a threshold value.
threshold = float(input("Enter a flow threshold in cfs: "))

# loops through each site.
for i in range(len(sites)):
  # this calculates the number of cases that are above the threshold
    readings_above_threshold = np.sum(flows[:, i] > threshold)

    # converts to hours 
    hours_above_threshold = readings_above_threshold * 0.25
    
    # prints out the number of hours above the given threshold
    print(f"Gauge {sites[i]}: {hours_above_threshold} hours above {threshold} cfs")

plot_streamflow(dates, flows, sites)