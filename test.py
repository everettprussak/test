import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
from plotnine import ggplot, aes, geom_point, labs, theme_minimal

glb_cvar = ''

def browse_file():
    print('a')
    df = pd.read_excel("Book1.xlsx")
    print(df)
    convert_hex_to_decimal(df)
    plot_graph(df)

def convert_hex_to_decimal(df):
    print('b')
    df['Column B'] = df['Column B'].apply(lambda x: int(str(x), 16))
    print('c')

def plot_graph(df):
    p = ggplot(df, aes(x='Column A', y='Column B')) + \
        geom_point()

    #print(p)
    glb_cvar = p

# Create the main Tkinter window
root = tk.Tk()
root.title("Excel Data Graph")
root.geometry("400x400")

# Add a button to browse for the Excel file
browse_button = tk.Button(root, text="Browse Excel File", command=browse_file)
browse_button.pack(pady=20)

grpah = tk.Label(text="he")
print(glb_cvar)

# Start the Tkinter event loop
root.mainloop()
