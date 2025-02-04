Caesar Cipher Program
This program encrypts and decrypts text using the Caesar Cipher algorithm, a simple substitution cipher that shifts characters in a message by a specified amount.

Features:
Encrypt Messages: Converts plaintext into encrypted text by shifting characters.
Decrypt Messages: Converts encrypted text back into the original message.
Handles uppercase and lowercase letters.
Ignores non-alphabetic characters (punctuation, numbers, spaces remain unchanged).

How It Works:
Input a Message: Provide the text to be encrypted or decrypted.
Choose a Shift Value: Enter an integer to define the shift amount.
Select Mode: Choose encrypt to encode or decrypt to decode the message.

Running the Program:
1.Save the program code in a file named caesar_cipher.py.
2.Run the script in a Python environment:
   python caesar_cipher.py
3.Follow the on-screen prompts to encrypt or decrypt messages.

Requirements:
Python 3.x is required to run this program.
Program Structure
caesar_cipher(): Performs the encryption or decryption logic.
get_input(): Collects user input for the message, shift value, and mode.
main(): The entry point of the program, allowing users to perform multiple operations.
