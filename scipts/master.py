def get_video_guide():
  from IPython.display import HTML
  # Create an HTML iframe element to embed the YouTube video
  html_code = f"""
  <iframe width="800" height="450" src="https://www.youtube.com/embed/EJL3cIGQMz0?si=rveyz9SSYs56jp48" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""
  
  # Display the embedded YouTube video
  return HTML(html_code)
!pip3 install pandas
import pandas as pd
!pip3 install matplotlib
import matplotlib.pyplot as plt

def clean_and_visualize_data(input_df):
    # Rename columns based on their positions
    input_df.columns = ['age_CE', 'd18O']

    # Data Cleaning
    # Handle missing values (replace with the median for demonstration)
    input_df['age_CE'].fillna(input_df['age_CE'].median(), inplace=True)

    # Handle outliers (replace with the mean for demonstration)
    d18O_mean = input_df['d18O'].mean()
    d18O_std = input_df['d18O'].std()
    input_df['d18O'] = input_df['d18O'].apply(lambda x: d18O_mean if abs(x - d18O_mean) > 2 * d18O_std else x)

    # Visualization
    # Line Plot to visualize temporal variation of d18O over age_CE
    plt.figure(figsize=(10, 6))
    plt.plot(input_df['age_CE'], input_df['d18O'], marker='o', linestyle='-', color='b')
    plt.title('Temporal Variation of Delta 18 O')
    plt.xlabel('Age (CE)')
    plt.ylabel('Delta 18 O')
    plt.grid(True)
    plt.show()

    return input_df

import seaborn as sns
# Specify the raw file URL on GitHub
github_raw_url = 'https://raw.githubusercontent.com/atiwary17/TemporalTales-Delta18OAnalysis/main/data/Data.xlsx'

# Dictionary of sheet names
# List of names
names = ['Red_sea', 'Gulf_of_Oman', 'F1', 'F2', 'F3']

# Create a dictionary with integer keys
name_dict = {i+1: name for i, name in enumerate(names)}

# Display the dictionary
print(name_dict)

def has_negative(arr):
    for element in arr:
        if element < 0:
            return True
    return False

#Clean the data
def clean_the_data(input_df):
    # Rename columns based on their positions
    input_df.columns = ['age_CE', 'd18O']

    # Data Cleaning
    # Handle missing values (replace with the median for demonstration)
    input_df['age_CE'].fillna(input_df['age_CE'].median(), inplace=True)

    # Handle outliers (replace with the mean for demonstration)
    d18O_mean = input_df['d18O'].mean()
    d18O_std = input_df['d18O'].std()
    #input_df['d18O'] = input_df['d18O'].apply(lambda x: d18O_mean if abs(x - d18O_mean) > 2 * d18O_std else x)
    return input_df


def plot_data(sheet_key):
    # Get the sheet name based on the key from name_dict
    sheet_name = name_dict[sheet_key]
    #print(sheet_name)

    # Load the data from the specified sheet into a Pandas DataFrame
    df = pd.read_excel(github_raw_url, sheet_name=sheet_name, skiprows=1)
    df = clean_the_data(df)
    # Check the first few rows of the DataFrame
    #print(df.head())

    # Filter the data to include only values up to 5000 on the x-axis (age_CE)
    df_filtered = df[df['age_CE'] <= 5000]
    if has_negative(df_filtered['d18O']):
        #print("The array contains negative values.")
        y_label = 'Proxy : Delta 18 O'
        ylim_low = -2.5
        ylim_up = 3
        title_text = 'Variation of Delta 18 O with Age (CE)'
    else:
        #print("The array does not contain negative values.")
        y_label = 'Proxy : Dolomite (%w)'
        ylim_low = 1
        ylim_up = 15
        title_text = 'Variation of Dolomite (%w) with Age (CE)'

    # Set plot style to a clean and compact style
    # Set the seaborn style to whitegrid
    sns.set_style("whitegrid")
    # Create a simple line plot to visualize raw δ18O variations
    plt.figure(figsize=(10, 5))
    plt.plot(df_filtered['age_CE'], df_filtered['d18O'], marker='o', linestyle='-', color='b',label=f'Sheet Key: {sheet_key}')

    # Set plot labels and title
    plt.xlabel('Age (CE)', fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.title(title_text, fontsize=16)
    # Add sheet key to the title with red color
    plt.text(0.1, 0.95, str(sheet_key), color='red', fontsize=18, transform=plt.gca().transAxes)
    #plt.legend(fontsize=12)

    # Show the plot
    plt.grid(True)
    # Adjust the layout for better spacing
    plt.tight_layout()
    plt.ylim(ylim_low, ylim_up)  # Set the y-axis limits to [0, 7]
    plt.show()
  def check_event_capture():
    # Dictionary of sheet names
    names = ['Red_sea', 'Gulf_of_Oman', 'F1', 'F2', 'F3']

    # Create a dictionary with integer keys
    name_dict = {i+1: name for i, name in enumerate(names)}

    # Display available options to the user
    print("Available Plots:")
    for key, name in name_dict.items():
        print(f"{key}")

    # Prompt the user to select a plot
    selected_key = int(input("Enter the number of the plot you want to check: "))
    flag = 0
    # Check if the selected plot captures the 4.2 k event
    selected_sheet = name_dict.get(selected_key)
    if selected_key == 1:
        print(" \n Congratulations! The selected plot ('Gulf_of_Oman') has captured the 4.2 k event.\n ")
        flag = flag+1
    elif selected_key == 2:
        print(f" \n The selected plot ('Red_sea') has captured the the 4.2 k event. \n ")
        flag = flag+1
    elif selected_key in [3,4,5]:
        print(f" \nThe selected plot ('{selected_key}') has not captured the the 4.2 k event.\n ")
    else:
        print(" \n Invalid selection. Please choose a valid plot. \n ")

    # Ask if the user is done
    user_input = input("Are you done? (Enter 'y' if done, or any other key to continue): ")

    # Check if the user is done and provide a greeting message
    if user_input == 'y' or user_input.lower() == 'done':
        if flag ==1:

        print("\n Thank you for using the plot checker! \n")
    else:
        # Recursively call the function to continue checking
        check_event_capture()



