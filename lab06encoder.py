
def encoder(password):
    res = ""
    for char in password:
        res += str(int(char) + 3)
    return res

def decoder(password):
    res = ""
    for char in password:
        res += str(int(char) - 3)
    return res

if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            raw = input("Please enter your password to encode: ")
            encoded = encoder(raw)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        elif option == 3:
            break