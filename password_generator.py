#Write a program to create password generator using 3d arrays


import random

def generate_password(length):

    chars = [
        [ # Layer 1: Lowercase letters
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
            ['u', 'v', 'w', 'x', 'y', 'z']
        ],
        [ # Layer 2: Uppercase letters
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y', 'Z']
        ],
        [ # Layer 3: Digits
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ],
        [ # Layer 4: Special characters
            ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        ]
    ]

    password = ""

    for _ in range(length):

        layer = random.randint(0, 3)

        row = random.randint(0, len(chars[layer]) - 1)

        col = random.randint(0, len(chars[layer][row]) - 1)

        password += chars[layer][row][col]


    return password


lenght = int(input("Enter the length of the password: "))
password_length = lenght
generated_password = generate_password(password_length)
print("Generated Password: ",generated_password)
