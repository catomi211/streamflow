# Import Statements

import matplotlib.pyplot as plt
import numpy as np

# Functions
def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    array1 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',',dtype=str,skip_header=1)
    dates = array1[:, 0].astype("datetime64")
    flows = array1[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
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


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)