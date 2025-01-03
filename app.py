import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from random import random

# Import the functions
from formulas.position_size_forex import get_position_sizing_result_forex
from formulas.position_size_futures import get_position_sizing_result_futures


# Main app window
app = tk.Tk()
app.title("Trading Toolbox")
# app.geometry("500x400")
app.resizable(False, False)

# colors
# style = ttk.Style()
# style.configure("TNotebook", background="#161616")
# style.configure("TNotebook.Tab", background="#101010", font=("Arial", 10))
# style.configure("TFrame", background="grey")

# Create a Notebook
notebook = ttk.Notebook(app, style="Vertical.TNotebook") # Create a Notebook with vertical tabs
notebook.pack(expand=True, fill="both")

# Apply a custom style for vertical tabs
style = ttk.Style(app)
style.theme_use("clam")
style.configure("Vertical.TNotebook")
style.configure("Vertical.TNotebook.Tab", padding=(5, 5))

# Add Tabs
position_sizing_forex_tab = ttk.Frame(notebook)
position_sizing_futures_tab = ttk.Frame(notebook)
probability_sim_tab = ttk.Frame(notebook)
rr_required_tab = ttk.Frame(notebook)

notebook.add(position_sizing_forex_tab, text="Position Sizing forex", padding=10)
notebook.add(position_sizing_futures_tab, text="Position Sizing futures")
notebook.add(probability_sim_tab, text="probability simulator")
notebook.add(rr_required_tab, text="RR Required Formula")


# position_size_forex
def calculate_position_size_forex():
    try:
        account_balance = float(entry_account_balance_forex.get())
        risk_dollar = entry_amount_risk_forex.get().strip("$")
        stop_loss_pips = float(entry_stop_loss_pips_forex.get())
        pip_value = float(entry_pip_value_forex.get())

        result = get_position_sizing_result_forex(account_balance, risk_dollar, stop_loss_pips, pip_value)
        label_result_futures_forex.configure(text=result)
    
    except ValueError:
        label_result_futures_forex.configure(text="Error: Please enter valid numbers.")

# position_size_forex GUI
ttk.Label(position_sizing_forex_tab, text="Position Sizing (Forex)", font=("Arial", 20)).grid(column=2, row=0, sticky="", columnspan=2, padx=10, pady=10)

ttk.Label(position_sizing_forex_tab, text="Account Balance:").grid(column=0, row=1, padx=10, pady=10)
entry_account_balance_forex = ttk.Entry(position_sizing_forex_tab)
entry_account_balance_forex.grid(column=1, row=1,  padx=10, pady=10)

ttk.Label(position_sizing_forex_tab, text="Dollar Risk $:").grid(column=0, row=2, padx=10, pady=10)
entry_amount_risk_forex = ttk.Entry(position_sizing_forex_tab)
entry_amount_risk_forex.grid(column=1, row=2,  padx=10, pady=10)

ttk.Label(position_sizing_forex_tab, text="Stop Loss (pips):").grid(column=0, row=3,  padx=10, pady=10)
entry_stop_loss_pips_forex = ttk.Entry(position_sizing_forex_tab)
entry_stop_loss_pips_forex.grid(column=1, row=3,  padx=10, pady=10)

ttk.Label(position_sizing_forex_tab, text="Pip value: (eurusd=10$)").grid(column=0, row=4,  padx=10, pady=10)
entry_pip_value_forex = ttk.Entry(position_sizing_forex_tab)
entry_pip_value_forex.grid(column=1, row=4,  padx=10, pady=10)

button_calculate = ttk.Button(position_sizing_forex_tab, text="Calculate", command=calculate_position_size_forex)
button_calculate.grid(column=1, row=5, columnspan=2, padx=10, pady=10)

label_result_futures_forex = ttk.Label(position_sizing_forex_tab)
label_result_futures_forex.grid(column=1, row=6,padx=10, pady=10)


# position_size_futures
def calculate_position_size_futures():
    try:
        account_balance = float(entry_account_balance_futures.get())
        risk_dollar = entry_amount_risk_futures.get().strip("$")
        stop_loss_points = float(entry_stop_loss_points_futures.get())
        point_value = float(entry_point_value_futures.get())

        result = get_position_sizing_result_futures(account_balance, risk_dollar, stop_loss_points, point_value)
        label_result_futures.configure(text=result)

    except ValueError:
        label_result_futures.configure(text="Error: Please enter valid numbers.")

# position_size_futures GUI
ttk.Label(position_sizing_futures_tab, text="Position Sizing (Futures)", font=("Arial", 20)).grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(position_sizing_futures_tab, text="Account Balance:").grid(column=0, row=0,  padx=10, pady=10)
entry_account_balance_futures = ttk.Entry(position_sizing_futures_tab)
entry_account_balance_futures.grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(position_sizing_futures_tab, text="Dollar Risk $:").grid(column=0, row=0,  padx=10, pady=10)
entry_amount_risk_futures = ttk.Entry(position_sizing_futures_tab)
entry_amount_risk_futures.grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(position_sizing_futures_tab, text="Stop Loss (points):").grid(column=0, row=0,  padx=10, pady=10)
entry_stop_loss_points_futures = ttk.Entry(position_sizing_futures_tab)
entry_stop_loss_points_futures.grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(position_sizing_futures_tab, text="P value: MNQ=2$ MES=5$").grid(column=0, row=0,  padx=10, pady=10)
entry_point_value_futures = ttk.Entry(position_sizing_futures_tab)
entry_point_value_futures.grid(column=0, row=0,  padx=10, pady=10)

button_calculate = ttk.Button(position_sizing_futures_tab, text="Calculate", command=calculate_position_size_futures)
button_calculate.grid(column=0, row=0,  padx=10, pady=10)

label_result_futures = ttk.Label(position_sizing_futures_tab)
label_result_futures.grid(column=0, row=0,  padx=10, pady=10)


# probability simulator func
def probability_simulator():
    try:
        # Get user inputs
        initial_balance = float(balance_entry.get())
        risk_percent = float(risk_entry.get())
        rr_ratio = float(rr_entry.get())
        num_trades = int(trades_entry.get())

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0:
            sim_label.configure(text="Error: All inputs must be positive numbers.")

        # Simulation logic
        balance = initial_balance
        balance_history = [initial_balance]
        wins = 0
        for _ in range(num_trades):
            risk_amount = balance * (risk_percent / 100)
            if random() > 0.5:
                balance += risk_amount * rr_ratio
                wins += 1
            else:
                balance -= risk_amount
            balance_history.append(balance)

        # Calculate results
        win_rate = (wins / num_trades) * 100
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Display results
        messagebox.showinfo(message=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nWin Rate: {win_rate:.2f}%")

        # Plot the balance history
        plt.style.use("ggplot")
        plt.plot(balance_history)
        plt.title("Trading Simulation Results")
        plt.xlabel("Number of Trades")
        plt.ylabel("Balance ($)")
        plt.grid(True)
        plt.savefig("Simulation.png")
        plt.show()

    except ValueError:
        sim_label.configure(text="Error: Please enter valid numbers.")


# probability_simulator GUI
ttk.Label(probability_sim_tab, text="Trading Simulator", font=("Arial", 24)).grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(probability_sim_tab, text="Initial Balance:").grid(column=0, row=0,  padx=10, pady=10)
balance_entry = ttk.Entry(probability_sim_tab)
balance_entry.grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(probability_sim_tab, text="Risk Percentage:").grid(column=0, row=0,  padx=10, pady=10)
risk_entry = ttk.Entry(probability_sim_tab)
risk_entry.grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(probability_sim_tab, text="Risk-Reward Ratio:").grid(column=0, row=0,  padx=10, pady=10)
rr_entry = ttk.Entry(probability_sim_tab)
rr_entry.grid(column=0, row=0,  padx=10, pady=10)

ttk.Label(probability_sim_tab, text="Number of Trades:").grid(column=0, row=0,  padx=10, pady=10)
trades_entry = ttk.Entry(probability_sim_tab)
trades_entry.grid(column=0, row=0,  padx=10, pady=10)

ttk.Button(probability_sim_tab, text="Run Simulation", command=probability_simulator).grid(column=0, row=0,  padx=10, pady=10)

sim_label = ttk.Label(probability_sim_tab, text="")
sim_label.grid(column=0, row=0,  padx=10, pady=10)


# Min Risk-Reward Required func
def calculate_min_rr_required():
    try:
        win_wate = float(win_rate_input.get())
        # Formula
        rr_result = (1 - win_wate) / win_wate
        # Validate inputs
        if win_wate >= 1:
            rr_result_label.configure(text="Please enter a risk-reward ratio in decimal form.")
        else:
            messagebox.showinfo(title="R-R Required", message=(f"Min Risk-Reward required is: {rr_result:.1f}R"))
            rr_result_label.configure(text=(f"Min Risk-Reward Required is: {rr_result}"))

    except ValueError:
        rr_result_label.configure(text="Error: Please enter valid numbers.")


ttk.Label(rr_required_tab, text='"Calculate the minimum Risk-Reward ratio required based on your system\'s Win-Rate:"', font=("Arial", 11)).grid(column=0, row=0,  padx=10, pady=10)

rr_label = ttk.Label(rr_required_tab, text="Win-Rate: (0.5 = 50%)")
rr_label.grid(column=0, row=0,  padx=10, pady=10)

win_rate_input = ttk.Entry(rr_required_tab)
win_rate_input.grid(column=0, row=0,  padx=10, pady=10)

ttk.Button(rr_required_tab, text="Calculate", command=calculate_min_rr_required).grid(column=0, row=0,  padx=10, pady=10)

rr_result_label = ttk.Label(rr_required_tab)
rr_result_label.grid(column=0, row=0,  padx=10, pady=10)


# popup after closing
def on_closing(): 
    messagebox.showwarning(title="DON'T FORGET", message="accept the loss before it happens")
    app.destroy()
app.protocol("WM_DELETE_WINDOW", on_closing)


app.mainloop() # Run App
