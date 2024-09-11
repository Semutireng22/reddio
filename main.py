import requests
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Display the title and channel link
print(Fore.CYAN + "=" * 41)
print(Fore.GREEN + "           Reddio Automatic Bot       ")
print(Fore.CYAN + "=" * 41)
print(Fore.YELLOW + "   Channel: https://t.me/ugdairdrop   ")
print(Fore.CYAN + "=" * 41)

# Prompt the user to input multiple wallet addresses, separated by commas
addresses_input = input(Fore.BLUE + "Enter your wallet addresses (separated by commas): ")

# Split the input into a list of wallet addresses
wallet_addresses = [address.strip() for address in addresses_input.split(',')]

while True:
    for wallet_address in wallet_addresses:
        # Define the check-in URL for each address
        url = f"https://points-mainnet.reddio.com/v1/daily_checkin?wallet_address={wallet_address}"

        # Send the request and get the response
        response = requests.get(url)

        # Check the response status
        if response.status_code == 200:
            print(Fore.GREEN + f"Check-in successful for {wallet_address}!")
        else:
            print(Fore.RED + f" Already check-in for {wallet_address}. Please try again.")

    # Wait for 24 hours (86400 seconds) before checking in again
    print(Fore.YELLOW + "Silahkan tunggu 24 Jam sebelum mencoba lagi.")
    time.sleep(86400)
