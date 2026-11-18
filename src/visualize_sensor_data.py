import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Define the sensor dataset location
filename = "data/sensor_data.csv"

# Read CSV data into a Pandas DataFrame
df = pd.read_csv(filename, parse_dates=["timestamp"])

# Display basic dataset information
print("Industrial Sensor Data Visualization")
print("------------------------------------")

# Display the first five measurements
print("\nFirst 5 measurements:")
print(df.head())

# Display the number of rows and columns
print("\nDataset shape:", df.shape)

# Display data types
print("\nColumn data types:")
print(df.dtypes)

# Reusable function for industrial sensor visualization
def plot_sensor(
    data,
    column,
    title,
    ylabel,
    color,
    filename,
    lower_limit=None,
    upper_limit=None
):

    # Identify abnormal measurements
    anomaly_mask = pd.Series(False, index=data.index)

    if lower_limit is not None:
        anomaly_mask = anomaly_mask | (data[column] < lower_limit)

    if upper_limit is not None:
        anomaly_mask = anomaly_mask | (data[column] > upper_limit)

    anomalies = data[anomaly_mask]

    # Create figure
    plt.figure(figsize=(10, 5))

    # Plot sensor measurements
    plt.plot(
        data["timestamp"],
        data[column],
        marker="o",
        linestyle="-",
        color=color,
        label="Sensor Measurements"
    )

    # Add lower threshold if specified
    if lower_limit is not None:
        plt.axhline(
            y=lower_limit,
            color="red",
            linestyle="--",
            label=f"Lower Threshold ({lower_limit})"
        )

    # Add upper threshold if specified
    if upper_limit is not None:
        plt.axhline(
            y=upper_limit,
            color="red",
            linestyle="--",
            label=f"Upper Threshold ({upper_limit})"
        )

    # Highlight abnormal measurements
    if not anomalies.empty:
        plt.scatter(
            anomalies["timestamp"],
            anomalies[column],
            color="red",
            marker="x",
            s=100,
            linewidths=2,
            label="Detected Anomalies",
            zorder=5
        )

    # Configure graph appearance
    plt.title(title)
    plt.xlabel("Timestamp")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend(loc="best")

    # Format and save
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()

    print(f"{column} anomalies detected:", len(anomalies))
    print("Graph saved to:", filename)



# Ensure reports directory exists
Path("reports").mkdir(exist_ok=True)

# Generate temperature graph
plot_sensor(
    data=df,
    column="temperature_C",
    title="Industrial Motor Temperature Monitoring",
    ylabel="Temperature (°C)",
    color="blue",
    filename="reports/temperature_plot.png",
    upper_limit=75
)

# Generate voltage graph
plot_sensor(
    data=df,
    column="voltage_V",
    title="Industrial Motor Voltage Monitoring",
    ylabel="Voltage (V)",
    color="orange",
    filename="reports/voltage_plot.png",
    lower_limit=207,
    upper_limit=253
)

# Generate current graph
plot_sensor(
    data=df,
    column="current_A",
    title="Industrial Motor Current Monitoring",
    ylabel="Current (A)",
    color="green",
    filename="reports/current_plot.png",
    upper_limit=8
)







