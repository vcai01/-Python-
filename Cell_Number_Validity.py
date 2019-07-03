"""
Test the validity of a cell phone number
"""

CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
CN_telecom = [133, 153, 180, 181, 189, 177, 1700]

while True:
    cell = input('Enter your number: ')
    num = str(cell)
    ThreeDigits = int(num[0:3])
    FourDigits = int(num[0:4])
    
    if len(cell) == 11:
        if ThreeDigits in CN_telecom or FourDigits in CN_telecom:
            print("Operator: {}\nWe're sending verification code via text to your phone:".format('China Telecom'), cell)
        elif ThreeDigits in CN_mobile or FourDigits in CN_mobile:
            print("Operator: {}\nWe're sending verification code via text to your phone:".format('China Mobile'), cell)
        elif ThreeDigits in CN_union or FourDigits in CN_union:
            print("Operator: {}\nWe're sending verification code via text to your phone:".format('China Union'), cell)
        else:
            print('No such an operator.')
    else:
        print('Invalid length. Your number should be in 11 digits.')
