Zip file compressor implemented in Python.

To run it: 

$python compress.py zip 'example.txt'

The compressed file will be generated. The output on terminal will be the content in the example.txt

compressor.py:
To see the compressed binary strings, modify the compress.py, and add 'print binString'.
To see the huffman code of each character, modify the compress.py, and add 'print codes'.

heap.py:
The min heap structure and priority queue is implemented in this file.

read.py:
Read in the txt file to be compressed.

decompress.py:
Read in the compressed file and convert it to binary strings to be used in compress.py.

swap.py:
Simply swap two element in the heap.

test.txt:
contains test case for the huffman codes. To test, run:
$ python compress.py test
