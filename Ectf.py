#Retail Store Daily Revenue vs Customer Count Analysis
#● From: Minor 1 – EDA
#● Extension: Analyze revenue vs footfall correlation.
#● Add-ons: Scatter plots, line charts.
#● Difficulty: Medium

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry


def load_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        messagebox.showinfo("Success", f"Loaded {file_path}")


def plot_data():
    if df is None:
        messagebox.showerror("Error", "Please load a CSV file first!")
        return
    
    start = start_cal.get_date()
    end = end_cal.get_date()
    filtered_df = df[(df['Date'] >= pd.to_datetime(start)) & (df['Date'] <= pd.to_datetime(end))]

    choice = chart_var.get()
    
    if choice == "Scatter":
        plt.figure(figsize=(8,5))
        sns.scatterplot(x="Customer_Count", y="Revenue", data=filtered_df)
        plt.title("Revenue vs Customer Count")
        plt.xlabel("Customer Count")
        plt.ylabel("Revenue")
        plt.show()
        
        correlation = filtered_df["Customer_Count"].corr(filtered_df["Revenue"])
        messagebox.showinfo("Correlation", f"Correlation between Customer Count and Revenue: {correlation:.2f}")
    
    elif choice == "Line":
        plt.figure(figsize=(10,5))
        plt.plot(filtered_df['Date'], filtered_df['Revenue'], label='Revenue', marker='o')
        plt.plot(filtered_df['Date'], filtered_df['Customer_Count'], label='Customer Count', marker='x')
        plt.title("Daily Revenue and Customer Count Trend")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    elif choice == "Revenue per Customer":
        filtered_df['Revenue_per_Customer'] = filtered_df['Revenue'] / filtered_df['Customer_Count']
        messagebox.showinfo("Revenue per Customer", filtered_df[['Date', 'Revenue_per_Customer']].to_string(index=False))


df = None
root = tk.Tk()
root.title("Retail Store Analysis")
root.geometry("400x300")


load_btn = tk.Button(root, text="Load CSV File", command=load_csv)
load_btn.pack(pady=10)

tk.Label(root, text="Start Date:").pack()
start_cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
start_cal.pack(pady=5)

tk.Label(root, text="End Date:").pack()
end_cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end_cal.pack(pady=5)


chart_var = tk.StringVar(value="Scatter")
tk.Radiobutton(root, text="Scatter Plot", variable=chart_var, value="Scatter").pack()
tk.Radiobutton(root, text="Line Chart", variable=chart_var, value="Line").pack()
tk.Radiobutton(root, text="Revenue per Customer", variable=chart_var, value="Revenue per Customer").pack()

plot_btn = tk.Button(root, text="Generate Chart / Table", command=plot_data)
plot_btn.pack(pady=15)

root.mainloop()
