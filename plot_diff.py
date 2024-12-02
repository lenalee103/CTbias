import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_combined_violin_plot(folder_path):
    # Find all CSV files in the target folder that begin with 'patient1'
    methods = ['Original', 'GS-IMR', 'CycleGAN-IMR','DM-IMR']
    csv_files = [f'{method}.csv' for method in methods]  # Files will be in same order as methods array

    # Create lists to store data
    all_data_ssim = []
    all_data_psnr = []
    methods = []

    # Read and reshape data for seaborn
    for csv_file in csv_files:
        df = pd.read_csv(os.path.join(folder_path, csv_file))
        method = os.path.splitext(csv_file)[0]
        
        # Add data for SSIM
        all_data_ssim.extend(df['SSIM Score'].values)
        methods.extend([method] * len(df['SSIM Score']))
        
        # Add data for PSNR
        all_data_psnr.extend(df['PSNR Score'].values)

    # Create DataFrames in the format Seaborn expects
    df_ssim = pd.DataFrame({
        'Method': methods,
        'Score': all_data_ssim,
    })
    
    df_psnr = pd.DataFrame({
        'Method': methods,
        'Score': all_data_psnr,
    })

    # Set the style
    sns.set_style("whitegrid")
    
    # Create two separate figures
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    fig2, ax2 = plt.subplots(figsize=(10, 6))

    # Create violin plots combined with box plots with enhanced box plots
    sns.violinplot(data=df_ssim, x='Method', y='Score', ax=ax1, 
                  inner='box', color='lightblue', scale='width', width=0.8,
                  boxprops={'zorder': 2, 'facecolor': 'white', 'alpha': 0.7, 'linewidth' : 2})
    sns.violinplot(data=df_psnr, x='Method', y='Score', ax=ax2,
                  inner='box', color='lightgreen', scale='width', width=0.8, 
                  boxprops={'zorder': 2, 'facecolor': 'white', 'alpha': 0.7, 'linewidth' : 2})

    # Customize the plots
    ax1.set_title('SSIM Scores Distribution of in-modality', fontsize=14)
    ax1.set_xlabel('Similarity Check of Methods', fontsize=12)
    ax1.set_ylabel('SSIM Values', fontsize=12)
    ax1.tick_params(axis='x', rotation=45)

    ax2.set_title('PSNR Scores Distribution of in-modality', fontsize=14)
    ax2.set_xlabel('Data Quality Check of Methods', fontsize=12)
    ax2.set_ylabel('PSNR Values', fontsize=12)
    ax2.tick_params(axis='x', rotation=45)

    # Adjust layouts
    fig1.tight_layout()
    fig2.tight_layout()
    
    plt.show()

# Specify the folder path containing the CSV files
folder_path = './results'

# Call the function to create the combined violin plots
create_combined_violin_plot(folder_path)