numero_base_decimal = int(input("Enter a decimal number: "))

# Initialize an empty string to store the binary digits
numero_base_binaria = ""

# Convert the decimal number to binary using a for loop
while numero_base_decimal > 0:
    # Get the remainder of the decimal number divided by 2
    resto = numero_base_decimal % 2

    # Add the remainder to the binary string
    numero_base_binaria = str(resto) + numero_base_binaria

    # Divide the decimal number by 2
    numero_base_decimal = numero_base_decimal // 2

# Print the decimal number and its binary representation
print(f"Número na base decimal: {numero_base_decimal}")
print(f"Conversão para base binária: {numero_base_binaria}")