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

def summarize(dates, flows, sites, filename="streamflow_summary.csv"):
    """Print and save summary statistics for each gauge."""
    rows = []

    for i in range(len(sites)):
        gauge_flows = flows[:, i]
        max_value = np.max(gauge_flows)
        min_value = np.min(gauge_flows)
        avg_value = np.mean(gauge_flows)
        max_row = np.argmax(gauge_flows)
        date_of_max = np.datetime_as_string(dates[max_row], unit="s").replace("T", " ")

        rows.append({
            "Gauge": sites[i],
            "Max (cfs)": max_value,
            "Date of max": date_of_max,
            "Min (cfs)": min_value,
            "Avg (cfs)": avg_value,
        })

    summary = pd.DataFrame(rows).round({
        "Max (cfs)": 1,
        "Min (cfs)": 1,
        "Avg (cfs)": 1,
    })
    summary.to_csv(filename, index=False)

    print(f"{'Gauge':<12}{'Max (cfs)':>10}{'Date of max':>22}"
          f"{'Min (cfs)':>12}{'Avg (cfs)':>12}")

    for row in rows:
        print(f"{row['Gauge']:>12}"
              f"{row['Max (cfs)']:10.1f}"
              f"{row['Date of max']:>22}"
              f"{row['Min (cfs)']:12.1f}"
              f"{row['Avg (cfs)']:12.1f}")


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summarize(dates, flows, sites)
plot_streamflow(dates, flows, sites)