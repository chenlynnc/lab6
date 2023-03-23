"""
A code to shift each number of a string by 3


by moxi kohn
"""

# moxi's encoder
def encoder(raw_data):

    # initialise
    encoded_message = ''

    # loop through each character and add 3, then pass it off to the encoded string
    for character in raw_data:
        encoded_character = int(character) + 3
        encoded_message += encoded_character

    # return
    return encoded_message
def decoder(password):
    res = ""
    for char in password:
        res += str(int(char) - 3)
    return res

#moxi's main
def main():
    while True:

        # get user menu choice
        print("------------- \n1. Encode\n2. Decode\n3. Quit ")
        user_choice = int(input("Please enter an option: "))

        # encode
        if user_choice == 1:
            raw_message = input("Please enter your password to encode: ")
            encoded_message = encoder(raw_message)
            print("Your password has been encoded and stored!")

        # decode
        elif user_choice == 2:
            pass

        # quit
        elif user_choice == 3:
            quit()

        #error case
        else:
            print("Error")
main()