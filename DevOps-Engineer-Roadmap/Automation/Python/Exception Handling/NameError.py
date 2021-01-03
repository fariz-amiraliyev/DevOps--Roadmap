def geek_message():
    try:
        geek = "GeeksforGeeks"
        return geeksforgeeks
    except NameError:
        return "NameError occured. Some variable isn't defined."

print(geek_message())
