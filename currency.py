# exchange rates for currency pairs
exchange_rates = {
    'USD to EUR': 0.95,
    'EUR to USD': 1.05,
    'USD to DOP': 60.62,
    'DOP to USD': 0.016,
}


def display_options():
    print("Available currency conversions:")
    for i, pair in enumerate(exchange_rates.keys(), 1):
        print(f"{i}. {pair}")


def currency_converter():
    try:
        # Display options
        display_options()
        choice = int(input("\nChoose a conversion option by number: "))

        # check if the option valid
        if choice < 1 or choice > len(exchange_rates):
            raise ValueError("Invalid choice.")

        # Get the selected currency pair from the dictionary
        selected_pair = list(exchange_rates.keys())[choice - 1]
        rate = exchange_rates[selected_pair]

        # Input the currency amount
        amount = float(input(f"Enter amount in {selected_pair.split(' ')[0]}: "))

        # Convert the amount using the chosen rate
        converted_amount = amount * rate

        # Output the converted amount
        print(
            f"{amount:.2f} {selected_pair.split(' ')[0]} is equivalent to {converted_amount:.2f} {selected_pair.split(' ')[-1]}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}. Please enter a valid number.")


if __name__ == "__main__":
    currency_converter()
