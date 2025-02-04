def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            result += new_char
        else:
            result += char

    return result

def get_input():
    message = input("Please enter the message: ")

    while True:
        try:
            shift = int(input("Please enter the shift value (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")

    while True:
        mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
        if mode in ["encrypt", "decrypt"]:
            break
        else:
            print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

    return message, shift, mode

def main():
    print("Welcome to the Caesar Cipher Program!")

    while True:
        message, shift, mode = get_input()

        result = caesar_cipher(message, shift, mode)

        print(f"The resulting message is: {result}")

        continue_choice = input("Do you want to continue? Type 'exit' to finish or press Enter to continue: ").lower()
        if continue_choice == "exit":
            print("Thank you for using the Caesar Cipher Program!")
            break

# Correct the condition to check __name__ and __main__
if __name__ == "__main__":
    main()

