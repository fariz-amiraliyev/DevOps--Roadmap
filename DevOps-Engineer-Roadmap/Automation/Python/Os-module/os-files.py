

>>> import os

>>> os.getcwd()
'/home/cloud_user'

Below are examples for many of the useful file and directory functions:

>>> os.getcwd()

>>> os.chdir('./other_dir') # Will change the current working directory. Relative paths are based on the new current working directory.

>>> os.listdir('.') # List the contents of a directory
['example.txt', 'other.txt']

>>> os.mkdir("sample") # Makes a directory called sample

>>> os.makedirs("sample/foo/bar") # Recursively makes directories `mkdir -p` equivalent

>>> open("sample/foo/bar/baz.txt", 'a').close() # Creates the baz.txt file if it doesn't exist

>>> os.remove("sample/foo/bar/baz.txt") # Remove the baz.txt file

>>> os.rmdir("sample/foo/bar") # Removes the bar directory

>>> os.removedirs("sample/foo") # Recursively removes foo and sample

>>> os.rename("sample.txt", "staple.txt") # Renames the file, equivalent to `mv sample.txt staple.txt`

>>> os.chown('path_to_file.txt', 501, 20)

>>> os.chmod('path_to_file.txt', 0o644)
