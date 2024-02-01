import random
import string
st = input("Enter message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding=="1") else False
print(coding)
def generate_random_chars():
    return ''.join(random.choices(string.ascii_letters, k=3))
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = generate_random_chars()
            r2 = generate_random_chars()
            stnew = r1+ word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

else:
    nwords = []
    for word in words:
        if(len(word)>=3): 
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
print(" ".join(nwords))






# user_input_start = "abc"
# user_input_end = "xyz"
# latest_encoded_message = None

# def encode(message):
#     if len(message) >= 3:
#         first_char = message[0]
#         message = message[1:] + first_char

#         encoded_message = user_input_start[:3] + message + user_input_end[-3:]
#         return encoded_message
#     else:
#         return message[::-1]

# def decode(message):
#     if len(message) < 3:
#         return message[::-1]
#     else:
#         message = message[3:-3]
#         message = message[-1] + message[:-1]

#         return message

# def person_one():
#     global latest_encoded_message
#     user_choice = input("Person 1: Do you want to encode or decode? Enter 'encode' or 'decode': ").lower()

#     if user_choice == "encode":
#         user_input = input("Person 1 (Encode): Enter a message to encode: ")
#         encoded_message = encode(user_input)
#         print(f"Person 1 (Encode): {encoded_message}")
#         latest_encoded_message = encoded_message
#         return encoded_message

#     elif user_choice == "decode":
#         user_input = input("Person 1 (Decode): Enter a message to decode: ")
#         decoded_message = decode(user_input)
#         print(f"Person 1 (Decode): {decoded_message}")
#         return decoded_message

#     else:
#         print("Invalid choice. Please enter 'encode' or 'decode'.")

# def person_two():
#     global latest_encoded_message
#     user_choice = input("Person 2: Do you want to encode or decode? Enter 'encode' or 'decode': ").lower()

#     if user_choice == "encode":
#         if latest_encoded_message:
#             print(f"Person 2 (Encode): Using Person 1's latest encoded message: {latest_encoded_message}")
#         else:
#             print("Person 2 (Encode): No latest encoded message from Person 1 available.")

#     elif user_choice == "decode":
#         user_input = input("Person 2 (Decode): Enter a message to decode: ")
#         decoded_message = decode(user_input)
#         print(f"Person 2 (Decode): {decoded_message}")
#         return decoded_message

#     else:
#         print("Invalid choice. Please enter 'encode' or 'decode'.")

# while True:
#     person_one_message = person_one()
#     person_two_message = person_two()
