
# Reusable sensor statistics calculations

def calculate_statistics(values):

    # Prevent calculations on an empty dataset
    if not values:
        raise ValueError("Cannot calculate statistics for empty data.")

    # Calculate basic statistics
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)

    # Return the calculated results
    return {
        "minimum": minimum,
        "maximum": maximum,
        "average": average
    }
