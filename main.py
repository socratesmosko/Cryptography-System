def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1] + keys[0:-1]

    # Create encryption dictionary
    encrypt_dict = dict(zip(keys, value))

    # Create decryption dictionary
    decrypt_dict = dict(zip(value, keys))

    while True:
        # Get input from user
        message = input("Please enter a password: ")
        mode = input("Please select an encryption mode: Encode(E) or Decode(D): ")

        # Process user input
        if mode.upper() == 'E':
            # Encrypt message using encryption dictionary
            encrypted_message = ''
            for letter in message.lower():
                if letter in encrypt_dict:
                    encrypted_message += encrypt_dict[letter]
                else:
                    encrypted_message += letter
            new_message = encrypted_message

        elif mode.upper() == 'D':
            # Decrypt message using decryption dictionary
            decrypted_message = ''
            for letter in message.lower():
                if letter in decrypt_dict:
                    decrypted_message += decrypt_dict[letter]
                else:
                    decrypted_message += letter
            new_message = decrypted_message

        else:
            print('Please enter a valid choice, Decrypt(D) or Encrypt(E)')
            continue

        # Print the result
        print(new_message)

        # Ask the user if they want to add another password
        answer = input("Do you want to add another password? (Y/N)")
        if answer.upper() == 'N':
            break

# Call the machine function
machine()
