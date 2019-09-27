Python 3.7.3 (default, Aug 20 2019, 17:04:43) 
[GCC 8.3.0] on linux
>>> from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))
Number of words in the file : Counter({'what': 7, 'orange': 5, 'text.': 5, 'text.orange': 2, 'surprise': 1, 'to
': 1, 'never': 1}) 
