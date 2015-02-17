"""
Challenge C: (Fibonacci word )
The word a4z47 makes a Fibonacci 
word sum of 1 + 5 + 196418 + 5 + 21 = 196450  
by replacing all the alphabets with their 
equivalent positions in the alphabetical 
chart and taking their Fibonacci equivalent 
for example f is equivalent to 6 and Fibonacci(6) is 13.
The file hexa.txt contains over 6000 words. 
Find the total Fibonacci word sum in the file.
(Right click on the file and click Save Link As...)
[Source: Sci CodeJam Team]

"""
import time

#alphabet chart
alph_chart = {'a': 1, 'b':2, 'c':3,
              'A': 1, 'B':2, 'C':3,
              'd': 4, 'e':5, 'f':6,
              'D': 4, 'E':5, 'F':6,
              'g': 7, 'h':8, 'i':9,
              'G': 7, 'H':8, 'I':9,
              'j': 10, 'k':11, 'l':12,
              'J': 10, 'K':11, 'L':12,
              'm': 13, 'n':14, 'o':15,
              'M': 13, 'N':14, 'O':15,
              'p': 16, 'q':17, 'r':18,
              'P': 16, 'Q':17, 'R':18,
              's': 19, 't':20, 'u':21,
              'S': 19, 'T':20, 'U':21,
              'v': 22, 'w':23, 'x':24,
              'V': 22, 'W':23, 'X':24,
              'y': 25, 'z':26,
              'Y': 25, 'Z':26}
num = 6
start_time1 = time.clock()
def Fib(n):
  if n + 1 == 0: return 0
  elif n + 1 == 1: return 1
  else: return Fib(n-1)+Fib(n-2)

def Fib_word(string):
  word_sum = 0
  if not string.isalnum(): 
    print "\n\t--Invalid input--\n"
    return
  for i in string:
    if i.isalpha():
      word_sum += Fib(alph_chart[i])
    else:
      word_sum += Fib(int(i))
  print word_sum 

test_string = 'a4z47'

with open ("hexa.txt", "r") as myfile:
    file_str=myfile.read().replace('\n', '').replace(' ','')
      
Fib_word(file_str)
print("--- %s seconds ---" % str(time.clock() - start_time1))
