secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Type a number to see if is it the secret number: "))

while number != 777:
    print("Ha ha! You're stuck in my loop!")

print("Well done, muggle! You are free now.")