import os
import re



# Regex used to match relevant loglines: in this case IP address

log_regex= re.compile(r".*fwd=\"12.23.34.23\".*$")

#output file where the matched lines will be attached

output_file = os.path.normpath("parsed_lines.log")


with open(output_file, "w") as file_out:
    file_out.write("")


    #opne output file in a append mode


    with open (output_file, "a") as in file_out:
        with open ("system.log", "r") as in_file:
            for line in in_file:
                if (line.regex.search(line)):
                    print(line)
                    file_out.write(line)



                    
