# Created by: VSCP
# Created on: 10/31/2020
'''
                                   ,-.----.    
              .--.--.     ,----..  \    /  \   
       ,---. /  /    '.  /   /   \ |   :    \  
      /__./||  :  /`. / |   :     :|   |  .\ : 
 ,---.;  ; |;  |  |--`  .   |  ;. /.   :  |: | 
/___/ \  | ||  :  ;_    .   ; /--` |   |   \ : 
\   ;  \ ' | \  \    `. ;   | ;    |   : .   / 
 \   \  \: |  `----.   \|   : |    ;   | |`-'  
  ;   \  ' .  __ \  \  |.   | '___ |   | ;     
   \   \   ' /  /`--'  /'   ; : .'|:   ' |     
    \   `  ;'--'.     / '   | '/  ::   : :     
     :   \ |  `--'---'  |   :    / |   | :     
      '---"              \   \ .'  `---'.|     
                          `---`      `---`     
'''

def decimal_to_binary(decimal_num):
    steps = []
    steps.append("")
    steps.append(f"Start with decimal number {decimal_num}.")
    steps.append("Divide the number by 2.")
    binary_representation = ""
    steps.append("")
    while decimal_num > 0:
        remainder = decimal_num % 2
        steps.append(f"Step: Divide {decimal_num} by 2, quotient is {decimal_num // 2}, remainder is {remainder}.")
        binary_representation = str(remainder) + binary_representation
        decimal_num //= 2
    steps.append("")
    # Add space every 6 bits for better readability
    binary_chunks = [binary_representation[i:i + 6] for i in range(0, len(binary_representation), 6)]
    binary_representation = ' '.join(binary_chunks)
    steps.append("")
    steps.append(f"The binary representation is ∴ {binary_representation}.")
    return steps

def decimal_to_octal(decimal_num):
    steps = []
    steps.append("")
    steps.append(f"Start with decimal number {decimal_num}.")
    steps.append("Divide the number by 8.")
    octal_representation = ""
    steps.append("")
    while decimal_num > 0:
        remainder = decimal_num % 8
        steps.append(f"Step: Divide {decimal_num} by 8, quotient is {decimal_num // 8}, remainder is {remainder}.")
        octal_representation = str(remainder) + octal_representation
        decimal_num //= 8
    steps.append("")
    steps.append(f"The octal representation is ∴ {octal_representation}.")
    return steps

def decimal_to_hexadecimal(decimal_num):
    steps = []
    steps.append("")
    steps.append(f"Start with decimal number {decimal_num}.")
    steps.append("Divide the number by 16.")
    steps.append("")
    hexadecimal_representation = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_digit = str(remainder) if remainder < 10 else chr(ord('A') + remainder - 10)
        steps.append(f"Step: Divide {decimal_num} by 16, quotient is {decimal_num // 16}, remainder is {hex_digit}.")
        hexadecimal_representation = hex_digit + hexadecimal_representation
        decimal_num //= 16
    steps.append("")
    steps.append(f"The hexadecimal representation is ∴ {hexadecimal_representation}.")
    return steps

def binary_to_decimal(binary_num, base):
    steps = []
    decimal_num = int(binary_num, base)
    steps.append("")
    steps.append(f"Start with binary number {binary_num}.")
    steps.append(f"Convert binary to decimal: {binary_num} = {decimal_num} in decimal.")
    steps.append(f"Convert decimal to radix-{base}.")
    steps.append("")
    steps_inside, radial_representation = radial_to_decimal(binary_num, base)
    steps.append(steps_inside)
    steps.append("")
    steps.append(f"The radix-{base} representation is {binary_num}.")
    steps.append(f"The decimal representation is ∴ {radial_representation}.")
    return steps, radial_representation

def octal_to_decimal(octal_num, base):
    steps = []
    decimal_num = int(octal_num, 8)
    steps.append("")
    steps.append(f"Start with octal number {octal_num}.")
    steps.append(f"Convert octal to decimal: {octal_num} = {decimal_num} in decimal.")
    steps.append(f"Convert decimal to radix-{base}.")
    steps.append("")
    steps_inside, radial_representation = radial_to_decimal(octal_num, base)
    steps.append(steps_inside)
    steps.append("")
    steps.append(f"The radix-{base} representation is {octal_num}.")
    steps.append(f"The decimal representation is ∴ {radial_representation}.")
    return steps, radial_representation

def hexadecimal_to_decimal(hex_num, base):
    steps = []
    decimal_num = int(hex_num, 16)
    steps.append("")
    steps.append(f"Start with hexadecimal number {hex_num}.")
    steps.append(f"Convert hexadecimal to decimal: {hex_num} = {decimal_num} in decimal.")
    steps.append(f"Convert decimal to radix-{base}.")
    steps.append("")
    steps_inside, radial_representation = radial_to_decimal(hex_num, base)
    steps.append(steps_inside)
    steps.append("")
    steps.append(f"The radix-{base} representation is {hex_num}.")
    steps.append(f"The decimal representation is ∴ {radial_representation}.")
    steps.append("")
    return steps, radial_representation

def radial_to_decimal(radial_num, base):
    decimal_num = 0
    power = len(radial_num) - 1
    steps = []
    steps.append("")
    for digit in radial_num:
        if digit.isdigit():
            value = int(digit) * (base ** power)
            steps.append(f"Step: Multiply {digit} by {base}^{power} = {value}")
            decimal_num += value
        else:
            value = (ord(digit.upper()) - ord('A') + 10) * (base ** power)
            steps.append(f"Step: Multiply {digit} by {base}^{power} = {value}")
            decimal_num += value
        power -= 1
    steps.append("")
    steps.append(f"Step: Add all the values. {radial_num} = {decimal_num} in decimal.")
    return steps, decimal_num

def binary_to_octal(binary_num):
    while len(binary_num) % 3 != 0:
        binary_num = '0' + binary_num
    
    steps = []
    steps.append("")
    steps.append(f"Start with binary number {binary_num}.")
    steps.append("Divide the binary number into groups of 3 bits.")
    binary_chunks = [binary_num[i:i + 3] for i in range(0, len(binary_num), 3)]
    steps.append("")
    
    octal_representation = ""
    for chunk in binary_chunks:
        radial_to_decimal_steps, decimal_value = radial_to_decimal(chunk, 2)
        octal_digit = oct(decimal_value)[2:]
        octal_representation += octal_digit
        steps.append(f"Step: Convert {chunk} to decimal: {chunk} = {decimal_value} in decimal.")
        steps.append(radial_to_decimal_steps)
        steps.append(f"Step: Convert {decimal_value} to octal: {decimal_value} = {octal_digit} in octal.")
        steps.append("")

    return steps, octal_representation

def binary_to_hexadecimal(binary_num):
    while len(binary_num) % 4 != 0:
        binary_num = '0' + binary_num
    
    steps = []
    steps.append("")
    steps.append(f"Start with binary number {binary_num}.")
    steps.append("Divide the binary number into groups of 4 bits.")
    binary_chunks = [binary_num[i:i + 4] for i in range(0, len(binary_num), 4)]
    steps.append("")
    
    hexadecimal_representation = ""
    for chunk in binary_chunks:
        radial_to_decimal_steps, decimal_value = radial_to_decimal(chunk, 2)
        hex_digit = hex(decimal_value)[2:].upper()
        hexadecimal_representation += hex_digit
        steps.append(f"Step: Convert {chunk} to decimal: {chunk} = {decimal_value} in decimal.")
        steps.append(radial_to_decimal_steps)
        steps.append(f"Step: Convert {decimal_value} to hexadecimal: {decimal_value} = {hex_digit} in hexadecimal.")
        steps.append("")
    steps.append("")
    return steps, hexadecimal_representation

def octal_to_binary(octal_num):
    octal_to_binary_dict = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }
    
    steps = []
    steps.append("")
    steps.append(f"Start with octal number {octal_num}.")
    steps.append("")
    binary_representation = ""
    for digit in octal_num:
        binary_digit = octal_to_binary_dict[digit]
        binary_representation += binary_digit
        steps.append(f"Step: Convert octal digit '{digit}' to binary: '{digit}' = {binary_digit} in binary.")
    steps.append("")
    return steps, binary_representation

def octal_to_hexadecimal(octal_num):
    steps = []
    steps.append("")
    steps.append(f"Start with octal number {octal_num}.")
    steps.append("")
    radial_to_decimal_steps, decimal_num = radial_to_decimal(octal_num, 8)
    steps.append(f"Convert octal to decimal: {octal_num} = {decimal_num} in decimal.")
    steps.append(radial_to_decimal_steps)
    steps.append("")
    
    hexadecimal_representation = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_digit = str(remainder) if remainder < 10 else chr(ord('A') + remainder - 10)
        steps.append(f"Step: Divide {decimal_num} by 16, quotient is {decimal_num // 16}, remainder is {hex_digit}.")
        hexadecimal_representation = hex_digit + hexadecimal_representation
        decimal_num //= 16
    steps.append("")
    return steps, hexadecimal_representation

def hexadecimal_to_binary(hex_num):
    hex_to_bin_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    steps = []
    steps.append("")
    steps.append(f"Start with hexadecimal number {hex_num}.")
    steps.append("")
    binary_representation = ""
    for digit in hex_num:
        binary_equivalent = hex_to_bin_dict[digit]
        steps.append(f"Convert {digit} to binary: {binary_equivalent}.")
        binary_representation += binary_equivalent
    steps.append("")
    return steps, binary_representation

def hexadecimal_to_octal(hex_num):
    hex_to_bin_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    steps = []
    steps.append("")
    steps.append(f"Start with hexadecimal number {hex_num}.")
    steps.append("")

    binary_representation = ""
    for digit in hex_num:
        binary_equivalent = hex_to_bin_dict[digit]
        steps.append(f"Convert {digit} to binary: {binary_equivalent}.")
        binary_representation += binary_equivalent

    steps.append("")
    steps.append(f"The binary representation is: {binary_representation}.")
    steps.append("Divide the binary number into groups of 3 bits.")
    steps.append("")
    while len(binary_representation) % 3 != 0:
        binary_representation = '0' + binary_representation

    octal_representation = ""
    for i in range(0, len(binary_representation), 3):
        octal_digit = binary_representation[i:i + 3]
        octal_equivalent = int(octal_digit, 2)
        steps.append(f"Convert {octal_digit} to octal: {octal_equivalent}.")
        octal_representation += str(octal_equivalent)
    steps.append("")
    return steps, octal_representation

def print_steps(steps):
    for step in steps:
        if isinstance(step, list):
            print_steps(step)
        else:
            print(step)

print("Select the type of calculation:")
print("1. Decimal to Radial")
print("2. Radial to Decimal")
print("3. Other Calculations")

choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    print("Select the type of radial conversion:")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    radial_choice = int(input("Enter your choice (1, 2, or 3): "))
    decimal_num = int(input("Enter a decimal number: "))
    if radial_choice == 1:
        steps = decimal_to_binary(decimal_num)
        print_steps(steps)
    elif radial_choice == 2:
        steps = decimal_to_octal(decimal_num)
        print_steps(steps)
    elif radial_choice == 3:
        steps = decimal_to_hexadecimal(decimal_num)
        print_steps(steps)
    else:
        print("Invalid choice.")
elif choice == 2:
    print("Select the type of radial conversion:")
    print("1. Binary to Decimal")
    print("2. Octal to Decimal")
    print("3. Hexadecimal to Decimal")
    radial_choice = int(input("Enter your choice (1, 2, or 3): "))
    radial_num = input("Enter a radial number: ")

    if radial_choice == 1:
        steps = binary_to_decimal(radial_num, 2)
        print_steps(steps)
    elif radial_choice == 2:
        steps = octal_to_decimal(radial_num, 8)
        print_steps(steps)
    elif radial_choice == 3:
        steps = hexadecimal_to_decimal(radial_num, 16)
        print_steps(steps)
    else:
        print("Invalid choice.")
elif choice == 3:
    print("Select the type of conversion:")
    print("1. Binary to Octal")
    print("2. Binary to Hexadecimal")
    print("3. Octal to Binary")
    print("4. Octal to Hexadecimal")
    print("5. Hexadecimal to Binary")
    print("6. Hexadecimal to Octal")
    conversion_choice = int(input("Enter your choice (1, 2, 3, 4, 5, or 6): "))
    num = input("Enter a number: ")
    if conversion_choice == 1:
        steps, result = binary_to_octal(num)
        print_steps(steps)
        print(f"The octal representation is ∴ {result}.")
    elif conversion_choice == 2:
        steps, result = binary_to_hexadecimal(num)
        print_steps(steps)
        print(f"The hexadecimal representation is ∴ {result}.")
    elif conversion_choice == 3:
        steps, result = octal_to_binary(num)
        print_steps(steps)
        print(f"The binary representation is ∴ {result}.")
    elif conversion_choice == 4:
        steps, result = octal_to_hexadecimal(num)
        print_steps(steps)
        print(f"The hexadecimal representation is ∴ {result}.")
    elif conversion_choice == 5:
        steps, result = hexadecimal_to_binary(num)
        print_steps(steps)
        print(f"The binary representation is ∴ {result}.")
    elif conversion_choice == 6:
        steps, result = hexadecimal_to_octal(num)
        print_steps(steps)
        print(f"The octal representation is ∴ {result}.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice. Please select 1, 2, or 3.")

# Created by: VSCP
# Created on: 10/31/2020
'''
                                   ,-.----.    
              .--.--.     ,----..  \    /  \   
       ,---. /  /    '.  /   /   \ |   :    \  
      /__./||  :  /`. / |   :     :|   |  .\ : 
 ,---.;  ; |;  |  |--`  .   |  ;. /.   :  |: | 
/___/ \  | ||  :  ;_    .   ; /--` |   |   \ : 
\   ;  \ ' | \  \    `. ;   | ;    |   : .   / 
 \   \  \: |  `----.   \|   : |    ;   | |`-'  
  ;   \  ' .  __ \  \  |.   | '___ |   | ;     
   \   \   ' /  /`--'  /'   ; : .'|:   ' |     
    \   `  ;'--'.     / '   | '/  ::   : :     
     :   \ |  `--'---'  |   :    / |   | :     
      '---"              \   \ .'  `---'.|     
                          `---`      `---`     
'''