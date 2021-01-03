# imported the requests library
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:

    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)


# Download large files

import requests
file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"

r = requests.get(file_url, stream = True)

with open("python.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):

         # writing one chunk at a time to pdf file
         if chunk:
             pdf.write(chunk)
