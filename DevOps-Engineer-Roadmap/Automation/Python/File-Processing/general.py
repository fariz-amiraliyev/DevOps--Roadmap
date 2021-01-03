fh = open("example.txt", "w")
fh.write("To write or not to write\nthat is the question!\n")
fh.close()

fobj_in = open("ad_lesbiam.txt")
fobj_out = open("ad_lesbiam2.txt","w")
i = 1
for line in fobj_in:
    print(line.rstrip())
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()


poem = open("ad_lesbiam.txt").read()
print(poem[16:34])
VIVAMUS mea Lesbia
type(poem)



poem = open("ad_lesbiam.txt").readlines()
print(poem)
