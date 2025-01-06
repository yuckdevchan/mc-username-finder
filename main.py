import requests
import nltk
import time
import os
from nltk.corpus import words

def is_username_taken(username):
    found = False
    while not found:
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        if response.status_code == 429:
            time.sleep(2) # Rate wait
        else:
            break
    return response.status_code == 200, response.status_code

def find_usernames_of_length(length):
    word_list = words.words()
    word_list = [word.lower() for word in word_list]
    with open("usernames.txt", "r") as file:
        last_name = file.readlines()[-1].strip()
    word_list = word_list[word_list.index(last_name) + 1:]

    for word in word_list:
        if len(word) == length:
            taken, status = is_username_taken(word)
            if not taken:
                print(f"Username '{word}' is available ({status})")
                if os.path.exists("usernames.txt"):
                    with open("usernames.txt", "a") as file:
                        file.write(word + "\n")
                else:
                    with open("usernames.txt", "w") as file:
                        file.write(word + "\n")
            time.sleep(0.4) # Avoid rate limit

if __name__ == "__main__":
    nltk.download('words')
    length = int(input("Enter the length of the username: "))
    find_usernames_of_length(length)
