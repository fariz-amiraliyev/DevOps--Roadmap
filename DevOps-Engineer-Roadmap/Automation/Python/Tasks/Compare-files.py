file1 = open('some_file_1.txt', 'r')
file2 = open('some_file_2.txt', 'r')
FO = open('some_output_file.txt', 'w')

for line1 in file1:
    for line2 in file2:
        if line1 == line2:
            FO.write("%s\n" %(line1))

FO.close()
file1.close()
file2.close()
