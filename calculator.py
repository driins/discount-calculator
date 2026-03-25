import tkinter as tk

def calculate():
    try:
        # Get and clean input (remove accidental spaces)
        raw_price = entry_price.get().strip()
        raw_discount = entry_discount.get().strip()

        price = float(raw_price)
        discount = float(raw_discount)

        # Logic Validate ranges
        if price < 0:
            result_label.config(text="Price cannot be negative!", fg="red")
            return

        if not (0 <= discount <= 100):
            result_label.config(text="Discount must be 0 - 100%", fg="red")
            return

        # Calculate final price
        final_price = price - (price * discount / 100)

        # Display result formatted with Rupiah (Rp)
        result_label.config(text=f"Final Price: Rp {final_price:,.2f}", fg="black")

    except ValueError:
        result_label.config(text="Please enter valid numbers!", fg="red")


# --- UI Setup ---
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("250x250")

# Price Input
tk.Label(root, text="Original Price (Rp):").pack(pady=(10, 0))
entry_price = tk.Entry(root)
entry_price.pack()

# Discount Input
tk.Label(root, text="Discount (%):").pack(pady=(10, 0))
entry_discount = tk.Entry(root)
entry_discount.pack()

# Button
tk.Button(root, text="Calculate", command=calculate).pack(pady=20)

# Result
result_label = tk.Label(root, text="Final Price: -", font=("Arial", 10, "bold"))
result_label.pack()

root.mainloop()