import os
import glob
import netCDF4 as nc
import matplotlib.pyplot as plt
def load_datasets(base_dir):
    data = []

    # Iterate over all subdirectories of base_dir
    for subdir in os.listdir(base_dir):
        subdir_path = os.path.join(base_dir, subdir)
        if os.path.isdir(subdir_path):
            # Iterate over all subdirectories of subdir
            for subdir2 in os.listdir(subdir_path):
                subdir2_path = os.path.join(subdir_path, subdir2)
                if os.path.isdir(subdir2_path):
                    # Find all .nc files in subdir2
                    files = glob.glob(os.path.join(subdir2_path, '*.nc'))
                    if len(files) == 0:
                        print(f'Warning: Found 0 NetCDF files in {subdir2_path}. Expected exactly one.')
                    elif len(files) > 1:
                        print(f'Warning: Found {len(files)} NetCDF files in {subdir2_path}. Expected exactly one.')
                    else:
                        # Load NetCDF data
                        dataset = nc.Dataset(files[0])
                        # Store 'LST' data and close dataset
                        lst_data = dataset.variables['LST'][:]
                        data.append(lst_data)
                        dataset.close()

    return data


# Load all datasets
datasets = load_datasets('/home/master1/gis/2017')


# Plot the 'LST' data from each dataset
for i, lst in enumerate(datasets):

    # Create a new matplotlib figure
    plt.figure(figsize=(10, 10))

    # Plot the 'LST' data
    plt.imshow(lst, cmap='hot', interpolation='nearest')
    plt.colorbar()

    # Show the plot
    plt.show()

