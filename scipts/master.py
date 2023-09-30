from IPython.display import HTML
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to embed a YouTube video
def get_video_guide():
    html_code = """
    <iframe width="800" height="450" src="https://www.youtube.com/embed/EJL3cIGQMz0?si=rveyz9SSYs56jp48" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    """
    return HTML(html_code)

# Function to clean and visualize data
def clean_and_visualize_data(input_df):
    input_df.columns = ['age_CE', 'd18O']
    input_df['age_CE'].fillna(input_df['age_CE'].median(), inplace=True)
    d18O_mean = input_df['d18O'].mean()
    d18O_std = input_df['d18O'].std()
    input_df['d18O'] = input_df['d18O'].apply(lambda x: d18O_mean if abs(x - d18O_mean) > 2 * d18O_std else x)

    plt.figure(figsize=(10, 6))
    plt.plot(input_df['age_CE'], input_df['d18O'], marker='o', linestyle='-', color='b')
    plt.title('Temporal Variation of Delta 18 O')
    plt.xlabel('Age (CE)')
    plt.ylabel('Delta 18 O')
    plt.grid(True)
    plt.show()

    return input_df

# Function to check if an array contains negative values
def has_negative(arr):
    return any(element < 0 for element in arr)

# Function to clean data
def clean_the_data(input_df):
    input_df.columns = ['age_CE', 'd18O']
    input_df['age_CE'].fillna(input_df['age_CE'].median(), inplace=True)
    return input_df

# Function to plot data
def plot_data(sheet_key):
    sheet_name = name_dict[sheet_key]
    df = pd.read_excel(github_raw_url, sheet_name=sheet_name, skiprows=1)
    df = clean_the_data(df)
    df_filtered = df[df['age_CE'] <= 5000]
    
    if has_negative(df_filtered['d18O']):
        y_label = 'Proxy: Delta 18 O'
        ylim_low = -2.5
        ylim_up = 3
        title_text = 'Variation of Delta 18 O with Age (CE)'
    else:
        y_label = 'Proxy: Dolomite (%w)'
        ylim_low = 1
        ylim_up = 15
        title_text = 'Variation of Dolomite (%w) with Age (CE)'
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 5))
    plt.plot(df_filtered['age_CE'], df_filtered['d18O'], marker='o', linestyle='-', color='b', label=f'Sheet Key: {sheet_key}')
    plt.xlabel('Age (CE)', fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.title(title_text, fontsize=16)
    plt.text(0.1, 0.95, str(sheet_key), color='red', fontsize=18, transform=plt.gca().transAxes)
    plt.grid(True)
    plt.tight_layout()
    plt.ylim(ylim_low, ylim_up)
    plt.show()

# Function to check event capture
# Initialize flags outside the function
flag_correct = 0
flag_wrong = 0

# Function to check event capture
def check_event_capture():
    names = ['A', 'B', 'C', 'D', 'E']
    name_dict = {i+1: name for i, name in enumerate(names)}
    
    print("Available Plots:")
    for key, name in name_dict.items():
        print(f"{key}")
    
    selected_key = int(input("Enter the number of the plot you want to check: "))
    
    selected_sheet = name_dict.get(selected_key)
 
    if selected_key == 4:
        print(" \n Congratulations! The selected plot ('Gulf_of_Oman') has captured the 4.2 k event.\n ")
        flag_correct = flag_correct + 1
    elif selected_key == 2:
        print(f" \n The selected plot ('Red_sea') has captured the the 4.2 k event. \n ")
        flag_correct = flag_correct + 1
    elif selected_key in [1, 3, 5]:
        print(f" \nThe selected plot ('{selected_key}') has not captured the 4.2 k event.\n ")
        flag_wrong = flag_wrong + 1 
    else:
        print(" \n Invalid selection. Please choose a valid plot. \n ")
    
    user_input = input("Are you done? (Enter 'y' if done, or any other key to continue): ")
    
    if user_input == 'y' or user_input.lower() == 'done':
        if flag_correct == 1:
            print("\n You were on the track but you missed a few. \n")
        elif flag_correct > 1: 
            print("\n Congratulations, you found all the places that captured the 4.2 Ka event! \n")
        print(f'Number of correct attempts: {flag_correct}')
        print(f'Number of failed attempts: {flag_wrong}')
        # Reset flags to zero when the user quits
        flag_correct = 0
        flag_wrong = 0
    else:
        check_event_capture()  # Continue the process
