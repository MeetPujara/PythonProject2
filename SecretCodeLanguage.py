import random
import string

def generate_random_chars():
    return ''.join(random.choices(string.ascii_letters, k=3))

while True:
    st = input("Enter message (type 'exit' to end): ")

    if st.lower() == 'exit':
        print("Exiting the chat.")
        break
    
    words = st.split(" ")

    coding = input("1 for Coding or 0 for Decoding: ")
    coding = True if (coding == "1") else False

    def modify_word(word, coding):
        if len(word) >= 3:
            r1 = generate_random_chars()
            r2 = generate_random_chars()
            if coding:
                stnew = r1 + word[1:] + word[0] + r2  # Encoding
            else:
                stnew = word[3:-3]
                stnew = stnew[-1] + stnew[:-1]  # Decoding
            return stnew
        else:
            return word[::-1]

    nwords = [modify_word(word, coding) for word in words]

    print("Modified Message: ", " ".join(nwords))
