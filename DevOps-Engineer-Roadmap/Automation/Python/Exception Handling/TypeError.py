geeky_list = ["Geeky", "GeeksforGeeks", "SuperGeek", "Geek"]
indices = [0, 1, "2", 3]
for i in range(len(indices)):
    try:
        print(geeky_list[indices[i]])
    except TypeError:
        print("TypeError: Check list of indices")


        
