from web3 import Web3
import requests
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def create_wallet():
    w3 = Web3()
    account = w3.eth.account.create()
    return account.address, account._private_key.hex()

def auto_referral(wallet_address, invitation_code):
    url = "https://points-mainnet.reddio.com/v1/register"
    payload = {
        "wallet_address": wallet_address,
        "invitation_code": invitation_code
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan: {e}")
        return False

def generate_referrals(number_of_wallets, invitation_code):
    successful_referrals = 0
    
    for _ in range(number_of_wallets):
        wallet_address, _ = create_wallet()
        
        if auto_referral(wallet_address, invitation_code):
            successful_referrals += 1
    
    print(f"{Fore.GREEN}Jumlah referral yang berhasil: {successful_referrals}")

def daily_checkin(wallet_address):
    url = f"https://points-mainnet.reddio.com/v1/daily_checkin?wallet_address={wallet_address}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}Daily check-in berhasil untuk {wallet_address}!")
        else:
            print(f"{Fore.RED}Daily check-in gagal untuk {wallet_address} dengan status code: {response.status_code}")
            print(f"Pesan: {response.text}")
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan: {e}")

def main_menu():
    print(f"{Fore.CYAN}=======================================")
    print(f"{Fore.YELLOW}    Reddio Automatic Bot")
    print(f"{Fore.CYAN}=======================================")
    print(f"{Fore.MAGENTA}   Channel: https://t.me/ugdairdrop")
    print(f"{Fore.CYAN}=======================================")

    while True:
        print(f"\n{Fore.CYAN}Menu Utama")
        print(f"{Fore.CYAN}1. {Fore.YELLOW}Generate Referrals")
        print(f"{Fore.CYAN}2. {Fore.YELLOW}Daily Check-in")
        print(f"{Fore.CYAN}3. {Fore.RED}Keluar")
        
        pilihan = input(f"{Fore.CYAN}Pilih opsi (1/2/3): ")
        
        if pilihan == "1":
            number_of_wallets = int(input(f"{Fore.CYAN}Masukkan jumlah wallet yang ingin dibuat: "))
            invitation_code = input(f"{Fore.CYAN}Masukkan kode referral: ")
            generate_referrals(number_of_wallets, invitation_code)
        elif pilihan == "2":
            wallet_address_manual = input(f"{Fore.CYAN}Masukkan wallet address untuk daily check-in: ")
            daily_checkin(wallet_address_manual)
        elif pilihan == "3":
            print(f"{Fore.RED}Keluar dari program.")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid, silakan coba lagi.")

# Jalankan menu utama
main_menu()
