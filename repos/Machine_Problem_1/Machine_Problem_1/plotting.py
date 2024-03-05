import matplotlib.pyplot as plt
import pandas as pd

# Load the matrix size timing data
data = pd.read_csv('timing_data_with_errors.csv')

# Plot Home to Device vs Device to Home for different matrix sizes
plt.figure(figsize=(10, 7))
plt.errorbar(data['MatrixSize'], data['HomeToDevice'], yerr=data['HTDError'], label='Home to Device', fmt='-o', capsize=5)
plt.errorbar(data['MatrixSize'], data['DeviceToHome'], yerr=data['DTHError'], label='Device to Home', fmt='-^', capsize=5)
plt.title('Timing vs. Matrix Size')
plt.xlabel('Matrix Size')
plt.ylabel('Timing (ms)')
plt.legend()
plt.grid(True)
plt.show()

# Plot GPU vs CPU for different matrix sizes
plt.figure(figsize=(10, 7))
plt.errorbar(data['MatrixSize'], data['GPU'], yerr=data['GPUError'], label='GPU Runtime', fmt='-o', capsize=5)
plt.errorbar(data['MatrixSize'], data['CPU'], yerr=data['CPUError'], label='CPU Runtime', fmt='-^', capsize=5)
plt.title('GPU vs CPU Runtime vs. Matrix Size')
plt.xlabel('Matrix Size')
plt.ylabel('Runtime (ms)')
plt.legend()
plt.grid(True)
plt.show()


# Load data from CSV
data = pd.read_csv('tile_width_timing_data.csv')

# Unique tile widths for plotting separate lines
tile_widths = data['TileWidth'].unique()

# Setup the plot
plt.figure(figsize=(10, 6))

# Iterate over each tile width to plot its data
for tile_width in tile_widths:
    subset = data[data['TileWidth'] == tile_width]
    plt.errorbar(subset['MatrixSize'], subset['GPUAverage'], yerr=subset['GPUError'], label=f'Tile Width {tile_width}')

# Adding plot title and labels
plt.title('GPU Average Time vs. Matrix Size for Different Tile Widths')
plt.xlabel('Matrix Size')
plt.ylabel('GPU Average Time (ms)')
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()
