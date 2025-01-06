from main import is_username_taken

taken = is_username_taken("abey")

if taken:
    print("Username is taken.")
else:
    print("Username is available.")
