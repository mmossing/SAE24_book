# strava_gpx_utils.py

def func_0():
    print(ACCESS_TOKEN)

    !ls *.csv


def func_1():
    gpx_filename = "GPX_files/activity_13185040780.json"

    # Open the file and print first 500 characters
    with open(gpx_filename, "r") as file:
        raw_data = file.read()

    print(raw_data[:500])  # Print the first few lines of the file


def func_2():
    # test with a single example last ride 
    # elevation_profile, distances_km defined in the block above
    plt.figure(figsize=(10, 5))
    plt.plot(distances_km, elevation_profile, color="blue", label=f'Activity {activity_id}')

    plt.title("Elevation Profile")
    plt.xlabel("Distance (km)")
    plt.ylabel("Elevation (m)")
    plt.grid(True)
    plt.legend()
    plt.show()
    # looks perfect!


def func_3():
    # import pandas as pd
    # import numpy as np
    # import matplotlib.pyplot as plt
    # import ast
    # import itertools  # <-- Missing import added

    # # Already done above # -----------------------------
    # # # STEP 1: Read CSV and Extract Block Information
    # # # -----------------------------
    # # df = pd.read_csv('exped_blocks.csv')

    # # # Convert 'start_date_local' to datetime and extract the date part
    # # df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    # # df['date'] = df['start_date_local'].dt.date

    # -----------------------------
    # # STEP 2: Generate Elevation vs. Distance Plots by Block
    # # -----------------------------

    # # Define a cycle of colors for consistency with mapping
    # color_cycle = itertools.cycle(['red', 'blue', 'green', 'purple', 'orange', 'darkred'])

    # # Group rides by Block
    # blocks = df.groupby('Block')

    # for block, group in blocks:
    #     color = next(color_cycle)  # Assign a color to this block

    #     plt.figure(figsize=(12, 6))

    #     for _, row in group.iterrows():
    #         activity_id = row["id"]
    #         gpx_filename = f"GPX_files/activity_{activity_id}.json"

    #         try:
    #             # Read the GPX JSON file
    #             with open(gpx_filename, "r") as file:
    #                 data = ast.literal_eval(file.read())  # Parse JSON-like data

    #             if "altitude" in data and "distance" in data:
    #                 elevation = np.array(data["altitude"]["data"])  # Elevation in meters
    #                 distances = np.array(data["distance"]["data"]) / 1000  # Convert to km

    #                 # Plot elevation profile with the assigned block color
    #                 plt.plot(distances, elevation, color=color, alpha=0.7, label=f'Activity {activity_id}')

    #         except (FileNotFoundError, SyntaxError, ValueError) as e:
    #             print(f"❌ Skipping Activity {activity_id} due to error: {e}")

    #     # Format the elevation plot
    #     plt.title(f"Elevation Profile - Block {block}")
    #     plt.xlabel("Distance (km)")
    #     plt.ylabel("Elevation (m)")
    #     plt.legend(fontsize="small")
    #     plt.grid(True)

    #     # Save elevation plot
    #     elevation_filename = f"block_{block}_elevation.png"
    #     plt.savefig(elevation_filename, dpi=300, bbox_inches='tight')
    #     plt.close()

    #     print(f"✅ Elevation profile for Block {block} saved as {elevation_filename}")


def func_4():
    # # -----------------------------
    # # STEP 2: Generate Elevation vs. Distance Plots with Cumulative Distance
    # # -----------------------------

    # # Reset color cycle to ensure consistent coloring across plots
    # color_cycle = itertools.cycle(['red', 'blue', 'green', 'purple', 'orange', 'darkred'])

    # # Group rides by Block
    # blocks = df.groupby('Block')

    # for block, group in blocks:
    #     color = next(color_cycle)  # Assign a color to this block

    #     plt.figure(figsize=(12, 6))

    #     cumulative_distance = 0  # Track cumulative distance for correct positioning

    #     for _, row in group.iterrows():
    #         # activity_id = row["id"]
    #         gpx_filename = f"GPX_files/activity_{activity_id}.json"

    #         try:
    #             # Read the GPX JSON file
    #             with open(gpx_filename, "r") as file:
    #                 data = ast.literal_eval(file.read())  # Parse JSON-like data

    #             if "altitude" in data and "distance" in data:
    #                 elevation = np.array(data["altitude"]["data"])  # Elevation in meters
    #                 distances = np.array(data["distance"]["data"]) / 1000  # Convert to km

    #                 # Adjust distances to be cumulative
    #                 distances += cumulative_distance
    #                 cumulative_distance = distances[-1]  # Update cumulative distance

    #                 # Plot elevation profile with the assigned block color
    #                 plt.plot(distances, elevation, color=color, alpha=0.7, label=f'Activity {activity_id}')

    #         except (FileNotFoundError, SyntaxError, ValueError) as e:
    #             print(f"❌ Skipping Activity {activity_id} due to error: {e}")

    #     # Format the elevation plot
    #     plt.title(f"Elevation Profile - Block {block}")
    #     plt.xlabel("Cumulative Distance (km)")
    #     plt.ylabel("Elevation (m)")
    #     plt.legend(fontsize="small")
    #     plt.grid(True)

    #     # Save elevation plot
    #     elevation_filename = f"block_{block}_elevation_cumulative.png"
    #     plt.savefig(elevation_filename, dpi=300, bbox_inches='tight')
    #     plt.close()

    #     print(f"✅ Cumulative Elevation profile for Block {block} saved as {elevation_filename}")


def func_5():
    # -----------------------------
    # STEP 1: Read CSV and Extract First Block Only
    # -----------------------------
    df = pd.read_csv('exped_blocks.csv')

    # Convert 'start_date_local' to datetime and extract the date part
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['date'] = df['start_date_local'].dt.date

    # Extract only the first block for practice
    first_block = df[df["Block"] == df["Block"].min()]

    # -----------------------------
    # STEP 2: Generate Elevation vs. Distance Plot for First Block
    # -----------------------------

    plt.figure(figsize=(12, 6))
    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred']  # Unique colors for each ride

    cumulative_distance = 0  # Track cumulative distance

    for idx, row in enumerate(first_block.itertuples()):
        activity_id = row.id
        gpx_filename = f"GPX_files/activity_{activity_id}.json"
        color = color_list[idx % len(color_list)]  # Assign a different color to each ride

        try:
            # Read the GPX JSON file
            with open(gpx_filename, "r") as file:
                data = ast.literal_eval(file.read())  # Parse JSON-like data

            if "altitude" in data and "distance" in data:
                elevation = np.array(data["altitude"]["data"])  # Elevation in meters
                distances = np.array(data["distance"]["data"]) / 1000  # Convert to km

                # Adjust distances to be cumulative
                distances += cumulative_distance
                cumulative_distance = distances[-1]  # Update cumulative distance

                # Plot each ride with a different color
                plt.plot(distances, elevation, color=color, alpha=0.7, label=f'Ride {idx + 1} (ID {activity_id})')

        except (FileNotFoundError, SyntaxError, ValueError) as e:
            print(f"❌ Skipping Activity {activity_id} due to error: {e}")

    # Format the elevation plot
    plt.title("Elevation Profile - First Block (Practice)")
    plt.xlabel("Cumulative Distance (km)")
    plt.ylabel("Elevation (m)")
    plt.legend(fontsize="small")
    plt.grid(True)

    # Save and display the plot
    elevation_filename = "block_1_elevation_practice.png"
    plt.savefig(elevation_filename, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"✅ Practice Elevation profile for Block 1 saved as {elevation_filename}")


def func_6():
    # -----------------------------
    # STEP 1: Read CSV and Extract First Block Only
    # -----------------------------
    df = pd.read_csv('exped_blocks.csv')

    # Convert 'start_date_local' to datetime and extract the date part
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['date'] = df['start_date_local'].dt.date

    # Extract only the first block for practice
    first_block = df[df["Block"] == df["Block"].min()]

    # -----------------------------
    # STEP 2: Generate Elevation vs. Distance Plot for First Block
    # -----------------------------

    plt.figure(figsize=(12, 6))
    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred']  # Unique colors for each ride

    cumulative_distance = 0  # Track cumulative distance

    for idx, row in enumerate(first_block.itertuples()):
        activity_id = row.id
        ride_name = row.name  # Get ride name from dataframe
        gpx_filename = f"GPX_files/activity_{activity_id}.json"
        color = color_list[idx % len(color_list)]  # Assign a different color to each ride

        try:
            # Read the GPX JSON file
            with open(gpx_filename, "r") as file:
                data = ast.literal_eval(file.read())  # Parse JSON-like data

            if "altitude" in data and "distance" in data:
                elevation = np.array(data["altitude"]["data"])  # Elevation in meters
                distances = np.array(data["distance"]["data"]) / 1000  # Convert to km

                # Adjust distances to be cumulative
                distances += cumulative_distance
                cumulative_distance = distances[-1]  # Update cumulative distance

                # Plot each ride with a different color
                plt.plot(distances, elevation, color=color, alpha=0.7, label=f'{ride_name}')

        except (FileNotFoundError, SyntaxError, ValueError) as e:
            print(f"❌ Skipping Activity {activity_id} due to error: {e}")

    # Format the elevation plot with larger labels and title
    plt.title(f"Elevation Profile - Block 1", fontsize=16)
    plt.xlabel("Cumulative Distance (km)", fontsize=14)
    plt.ylabel("Elevation (m)", fontsize=14)
    plt.legend(fontsize="large", loc="upper right")
    plt.grid(True)

    # Save and display the plot
    elevation_filename = "block_1_elev_practice.png"
    plt.savefig(elevation_filename, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"✅ Practice Elevation profile for Block 1 saved as {elevation_filename}")


def func_7():
    # -----------------------------
    # STEP 1: Read CSV and Extract First Block Only
    # -----------------------------
    df = pd.read_csv('exped_blocks.csv')

    # Convert 'start_date_local' to datetime and extract the date part
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['date'] = df['start_date_local'].dt.date

    # Extract only the first block for practice
    first_block = df[df["Block"] == df["Block"].min()]

    # -----------------------------
    # STEP 2: Generate Elevation vs. Distance Plot for First Block
    # -----------------------------

    plt.figure(figsize=(12, 6))
    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred']  # Unique colors for each ride

    cumulative_distance = 0  # Track cumulative distance

    for idx, row in enumerate(first_block.itertuples()):
        activity_id = row.id
        ride_name = row.name  # Get ride name from dataframe
        gpx_filename = f"GPX_files/activity_{activity_id}.json"
        color = color_list[idx % len(color_list)]  # Assign a different color to each ride

        try:
            # Read the GPX JSON file
            with open(gpx_filename, "r") as file:
                data = ast.literal_eval(file.read())  # Parse JSON-like data

            if "altitude" in data and "distance" in data:
                elevation = np.array(data["altitude"]["data"])  # Elevation in meters
                distances = np.array(data["distance"]["data"]) / 1000  # Convert to km

                # Adjust distances to be cumulative
                distances += cumulative_distance
                cumulative_distance = distances[-1]  # Update cumulative distance

                # Plot each ride with a different color
                plt.plot(distances, elevation, color=color, alpha=0.7, label=f'{ride_name}')

        except (FileNotFoundError, SyntaxError, ValueError) as e:
            print(f"❌ Skipping Activity {activity_id} due to error: {e}")

    # Format the elevation plot with larger labels and title
    plt.title(f"Elevation Profile - Block 1", fontsize=16)
    plt.xlabel("Cumulative Distance (km)", fontsize=14)
    plt.ylabel("Elevation (m)", fontsize=14)
    plt.legend(fontsize="large", loc="upper right")
    plt.grid(True)

    # Save and display the plot
    elevation_filename = "block_1_elevation_practice.png"
    plt.savefig(elevation_filename, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"✅ Practice Elevation profile for Block 1 saved as {elevation_filename}")


def func_8():
    # # getting closer, colors correct but legends overlap. lines too skinny, 1000m min 
    # # -----------------------------
    # # STEP 1: Read CSV and Extract Block Information
    # # -----------------------------
    # df = pd.read_csv('exped_blocks.csv')

    # # Convert 'start_date_local' to datetime and extract the date part
    # df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    # df['date'] = df['start_date_local'].dt.date

    # # -----------------------------
    # # STEP 2: Generate Elevation vs. Distance Plots for All Blocks
    # # -----------------------------

    # # Define a cycle of colors for consistency across blocks
    # color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred']

    # # Group rides by Block
    # blocks = df.groupby('Block')

    # for block, group in blocks:
    #     plt.figure(figsize=(12, 6))

    #     cumulative_distance = 0  # Track cumulative distance

    #     for idx, row in enumerate(group.itertuples()):
    #         activity_id = row.id
    #         ride_name = row.name  # Get ride name from dataframe
    #         gpx_filename = f"GPX_files/activity_{activity_id}.json"
    #         color = color_list[idx % len(color_list)]  # Assign a different color to each ride

    #         try:
    #             # Read the GPX JSON file
    #             with open(gpx_filename, "r") as file:
    #                 data = ast.literal_eval(file.read())  # Parse JSON-like data

    #             if "altitude" in data and "distance" in data:
    #                 elevation = np.array(data["altitude"]["data"])  # Elevation in meters
    #                 distances = np.array(data["distance"]["data"]) / 1000  # Convert to km

    #                 # Adjust distances to be cumulative
    #                 distances += cumulative_distance
    #                 cumulative_distance = distances[-1]  # Update cumulative distance

    #                 # Plot each ride with a different color
    #                 plt.plot(distances, elevation, color=color, alpha=0.7, label=f'{ride_name}')

    #         except (FileNotFoundError, SyntaxError, ValueError) as e:
    #             print(f"❌ Skipping Activity {activity_id} due to error: {e}")

    #     # Format the elevation plot with larger labels and title
    #     plt.title(f"Elevation Profile - Block {block}", fontsize=16)
    #     plt.xlabel("Cumulative Distance (km)", fontsize=14)
    #     plt.ylabel("Elevation (m)", fontsize=14)
    #     plt.legend(fontsize="large", loc="upper right")
    #     plt.grid(True)

    #     # Save and display the plot
    #     elevation_filename = f"block_{block}_elevation.png"
    #     plt.savefig(elevation_filename, dpi=300, bbox_inches='tight')
    #     plt.close()

    #     print(f"✅ Elevation profile for Block {block} saved as {elevation_filename}")


def func_9():
    # legends best. lines fatter, 1000m min

    # -----------------------------
    # STEP 1: Read CSV and Extract Block Information
    # -----------------------------
    df = pd.read_csv('exped_blocks.csv')

    # Convert 'start_date_local' to datetime and extract the date part
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['date'] = df['start_date_local'].dt.date

    # -----------------------------
    # STEP 2: Generate Elevation vs. Distance Plots for All Blocks
    # -----------------------------

    # Define a cycle of colors for consistency across blocks
    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred']

    # Group rides by Block
    blocks = df.groupby('Block')

    for block, group in blocks:
        plt.figure(figsize=(12, 6))

        cumulative_distance = 0  # Track cumulative distance
        all_elevations = []  # Store all elevations to determine y-axis limits

        for idx, row in enumerate(group.itertuples()):
            activity_id = row.id
            ride_name = row.name  # Get ride name from dataframe
            gpx_filename = f"GPX_files/activity_{activity_id}.json"
            color = color_list[idx % len(color_list)]  # Assign a different color to each ride

            try:
                # Read the GPX JSON file
                with open(gpx_filename, "r") as file:
                    data = ast.literal_eval(file.read())  # Parse JSON-like data

                if "altitude" in data and "distance" in data:
                    elevation = np.array(data["altitude"]["data"])  # Elevation in meters
                    distances = np.array(data["distance"]["data"]) / 1000  # Convert to km

                    # Adjust distances to be cumulative
                    distances += cumulative_distance
                    cumulative_distance = distances[-1]  # Update cumulative distance

                    # Store elevation data for setting y-axis limits
                    all_elevations.extend(elevation)

                    # Plot each ride with a thicker line
                    plt.plot(distances, elevation, color=color, alpha=0.7, linewidth=3, label=f'{ride_name}')

            except (FileNotFoundError, SyntaxError, ValueError) as e:
                print(f"❌ Skipping Activity {activity_id} due to error: {e}")

        # Set elevation y-axis limit if max elevation is below 1000m
        if all_elevations and max(all_elevations) < 1000:
            plt.ylim(0, 1000)

        # Format the elevation plot with larger labels and title
        plt.title(f"Elevation Profile - Block {block}", fontsize=16)
        plt.xlabel("Cumulative Distance (km)", fontsize=14)
        plt.ylabel("Elevation (m)", fontsize=14)

        # Automatically place the legend in the best location
        plt.legend(fontsize="large", loc="best")
        plt.grid(True)

        # Save and close the plot
        elevation_filename = f"block_{block}_elevation.png"
        plt.savefig(elevation_filename, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"✅ Elevation profile for Block {block} saved as {elevation_filename}")
