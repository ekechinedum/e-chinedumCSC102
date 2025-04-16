import tkinter as tk

def calculate_fee():
    location = location_entry.get().strip() # .get grabs the text while .strip removes extra space from beginning or end
    try:
        weight = float(weight_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number for weight.")
        return

    if location == "epe" and weight >= 10:
        fee = 10000
    elif location == "epe" and weight < 10:
        fee = 5000
    elif location == "ibeju-lekki" and weight >= 10:
        fee = 5000
    else:
        fee = 3500

    result_label.config(text=f"Your fee is {fee} naira")


root = tk.Tk()
root.title("Delivery Fee Calculator")

tk.Label(root, text="Enter Location (e.g., Epe, Ibeju-Lekki):").pack()
location_entry = tk.Entry(root)
location_entry.pack()

tk.Label(root, text="Enter Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="Calculate Fee", command=calculate_fee).pack(pady=5)

result_label = tk.Label(root, text="Your fee will appear here.")
result_label.pack()

root.mainloop()






