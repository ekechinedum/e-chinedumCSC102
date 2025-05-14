import tkinter as tk
from tkinter import messagebox
class Zenith:
    def __init__(self, employee_name):
        self.employee_name = employee_name
    def get_services(self):
        return []
class RetailBanking(Zenith):
    def get_services(self):
        return [
            "Lines of Credit",
            "Investment Management and Accounts",
            "Insurance",
            "Retirement and Education Accounts",
            "Loans and Mortgages",
            "Checking and Saving"
        ]
class GlobalBanking(Zenith):
    def get_services(self):
        return [
            "Multi-currency Management Services and Products",
            "Foreign Currency Accounts",
            "Foreign Currency Credit Cards",
            "Transborder Advisory Services and Products",
            "Liquidity Management"
        ]
class CommercialBanking(Zenith):
    def get_services(self):
        return [
            "Lines of Credit",
            "Investment Management and Accounts",
            "Insurance",
            "Advisory Services"
        ]
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zenith Bank - Division Services")

        tk.Label(root, text="Employee Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Select Division:").pack()
        self.division_var = tk.StringVar()
        self.division_var.set("Retail Banking")
        tk.OptionMenu(root, self.division_var, "Retail Banking", "Global Banking", "Commercial Banking").pack()

        tk.Button(root, text="Get Services", command=self.show_services).pack(pady=10)

        self.output_text = tk.Text(root, height=10, width=60)
        self.output_text.pack()

    def show_services(self):
        name = self.name_entry.get().strip()
        division = self.division_var.get()

        if not name:
            messagebox.showerror("Input Error", "Please enter the employee's name.")
            return

        if division == "Retail Banking":
            obj = RetailBanking(name)
        elif division == "Global Banking":
            obj = GlobalBanking(name)
        elif division == "Commercial Banking":
            obj = CommercialBanking(name)
        else:
            messagebox.showerror("Division Error", "Unknown division selected.")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, f"Employee: {name}\nDivision: {division}\n\nServices:\n")
        for service in obj.get_services():
            self.output_text.insert(tk.END, f"• {service}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
