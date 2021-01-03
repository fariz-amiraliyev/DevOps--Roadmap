https://www.bogotobogo.com/python/python_interview_questions.php


1. Merging two sorted list
  a = [3, 4, 6, 10, 11, 18]
  b = [1, 5, 7, 12, 13, 19, 21]

print(a+b)

or c.extend(a)
   c.extend(b)


2. Get word frequency - initializing dictionary
 def find_word_frequency (ss):
    words=ss.split()

    d={}.fromkeys(words,0)

    #or # or we can use this to initialize a dict
         #  d = {x:0 for x in words}

    for w in words:
        d[w]+=1
    print (d)

    ds = sorted(d.items(), key=lambda x:x[1], reverse=True)

    # OR
from collections import defaultdict
d = defaultdict(int)
for w in words:
    d[w] += 1
print d


3.Initializing dictionary with list - I

cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

# => {'US':['San Francisco', 'Los Angeles'], 'UK':[,], ...}

from collections import defaultdict
# using collections.defaultdict()
d1 = defaultdict(list) # initialize dict with list
for k,v in cities.items():
    d1[v].append(k)
print d1

# using dict.setdefault(key, default=None)
d2 = {}
for k,v in cities.items():
       d2.setdefault(v,[]).append(k)
print d2


L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

from collections import defaultdict
d = defaultdict(list)
for i in L:
    d[len(str(i))].append(i)
print d
print {k:v for k,v in d.items()}



4. The usage of os.path.dirname() & os.path.basename()
>>> os.path.dirname('/home/k/TEST/PYTHON/p.py')
'/home/k/TEST/PYTHON'

>>> os.path.basename('/home/k/TEST/PYTHON/p.py')
'p.py'

>>> os.path.split('/home/k/TEST/PYTHON/p.py')
('/home/k/TEST/PYTHON', 'p.py')
>>> os.path.join('/home/k/TEST/PYTHON', 'p.py')
'/home/k/TEST/PYTHON/p.py'

5.>>> import os
>>> print(os.getcwd())
C:\Python32
>>> cur_dir = os.curdir
>>> print(cur_dir)
.
>>> scripts_dir = os.path.join(os.curdir, 'Tools\Scripts')
>>> print(scripts_dir)
.\Tools\Scripts
>>> diff_py = os.path.join(scripts_dir, 'diff.py')
>>> print(diff_py)
.\Tools\Scripts\diff.py
>>> os.path.basename(diff_py)
' diff.py'
>>> os.path.splitext(diff_py)
('.\\Tools\\Scripts\\diff', '.py')
print(os.path.expanduser('~'))

6.
