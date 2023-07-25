import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        convert_hex_to_decimal(df)
        plot_graph(df)

def convert_hex_to_decimal(df):
    df['Column_B'] = df['Column_B'].apply(lambda x: int(str(x), 16))

def plot_graph(df):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.plot(df['Column_A'], df['Column_B'], marker='o')
    ax.set_xlabel('Time')
    ax.set_ylabel('Column B (Decimal)')
    plt.xticks(rotation=45)
    plt.title('Excel Data in Graph Form')
    plt.tight_layout()
    plt.show()

# Create the main Tkinter window
root = tk.Tk()
root.title("Excel Data Graph")

# Add a button to browse for the Excel file
browse_button = tk.Button(root, text="Browse Excel File", command=browse_file)
browse_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()