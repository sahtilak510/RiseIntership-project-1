"""
Tkinter GUI Currency Converter (All World Currencies)
"""
import tkinter as tk
from tkinter import ttk, messagebox
from forex_python.converter import CurrencyRates

def get_currency_list():
    # forex-python does not provide a direct list, so use a common set or extend as needed
    return [
        'USD', 'EUR', 'GBP', 'JPY', 'INR', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD',
        'SGD', 'HKD', 'NOK', 'KRW', 'TRY', 'RUB', 'BRL', 'ZAR', 'DKK', 'PLN', 'TWD',
        'THB', 'MYR', 'IDR', 'CZK', 'HUF', 'ILS', 'PHP', 'AED', 'SAR', 'MXN', 'QAR',
        'PKR', 'EGP', 'KWD', 'NGN', 'BDT', 'LKR', 'VND', 'UAH', 'COP', 'ARS', 'CLP',
        'MAD', 'KES', 'GHS', 'TZS', 'UGX', 'RON', 'HRK', 'BGN', 'ISK', 'JOD', 'OMR',
        'BHD', 'QAR', 'KZT', 'AZN', 'GEL', 'BYN', 'MZN', 'AOA', 'DZD', 'TND', 'LBP',
        'SDG', 'SYP', 'IQD', 'YER', 'AFN', 'MNT', 'UZS', 'TMT', 'AMD', 'MKD', 'ALL',
        'MDL', 'BAM', 'RSD', 'MOP', 'BND', 'LAK', 'KHR', 'MMK', 'KPW', 'MVR', 'BTN',
        'NPR', 'SRD', 'GYD', 'BBD', 'TTD', 'JMD', 'XCD', 'BSD', 'BZD', 'HTG', 'DOP',
        'HNL', 'NIO', 'CRC', 'PAB', 'PYG', 'UYU', 'BOB', 'VEF', 'GMD', 'SLL', 'GNF',
        'MWK', 'ZMW', 'SZL', 'LSL', 'BWP', 'MUR', 'SCR', 'MGA', 'KMF', 'DJF', 'SOS',
        'ETB', 'SDG', 'SSP', 'CDF', 'RWF', 'BIF', 'XOF', 'XAF', 'XPF', 'XAG', 'XAU'
    ]

CURRENCIES = get_currency_list()

c = CurrencyRates()

def on_convert():
    try:
        amount = float(amount_var.get())
        source = source_var.get()
        target = target_var.get()
        result = c.convert(source, target, amount)
        result_var.set(f'{amount} {source} = {result:.2f} {target}')
    except Exception as e:
        messagebox.showerror('Error', str(e))

root = tk.Tk()
root.title('Currency Converter')

amount_var = tk.StringVar()
source_var = tk.StringVar(value=CURRENCIES[0])
target_var = tk.StringVar(value=CURRENCIES[1])
result_var = tk.StringVar()

tk.Label(root, text='Amount:').grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=amount_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text='From:').grid(row=1, column=0, padx=5, pady=5)
ttk.Combobox(root, textvariable=source_var, values=CURRENCIES, state='readonly').grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text='To:').grid(row=2, column=0, padx=5, pady=5)
ttk.Combobox(root, textvariable=target_var, values=CURRENCIES, state='readonly').grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text='Convert', command=on_convert).grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(root, textvariable=result_var, font=('Arial', 12)).grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
