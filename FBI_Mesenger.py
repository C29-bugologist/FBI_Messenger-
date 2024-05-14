# #The Login Code is **5678346**
import base64

print("*******************************")
print("--------------FBI--------------")
print("*******************************\n")
print("             LOGIN")
Login_id = int(input("         id-"))

while True:
    if Login_id == 5678346:
        Encode_Decode = int(input("Enter '1' if you want to Encrypt a message\nEnter '2' if you want to decode a message\nEnter '3' if you want to Exit\nEnter: "))
        if Encode_Decode == 1:
            To_Encrypt = input("Enter The Message You want to Encrypt:\n")
            Encoded = base64.b64encode(To_Encrypt.encode('utf-8'))
            print("Here is your encrypted message:", Encoded,"\n")
        elif Encode_Decode == 2:
            To_Decode = input("Enter The Message You want to Decode:\n")
            Decoded = base64.b64decode(To_Decode).decode('utf-8')
            print("Here is your decrypted message:", Decoded,"\n")
        elif Encode_Decode == 3:
            print("goodbye")
            break
        else:
            print(Encode_Decode, "is Invalid enter 1 or 2" )
    else:
        print("      YOU ARE INCORRECT")
        break

