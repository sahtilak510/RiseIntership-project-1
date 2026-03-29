"""
CLI Currency Converter (All World Currencies)
"""
from forex_python.converter import CurrencyRates

def main():
    c = CurrencyRates()
    print('Currency Converter (CLI) - All World Currencies')
    amount = float(input('Enter amount: '))
    source = input('From currency (e.g., USD): ').upper()
    target = input('To currency (e.g., EUR): ').upper()
    try:
        result = c.convert(source, target, amount)
        print(f'{amount} {source} = {result:.2f} {target}')
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    main()
