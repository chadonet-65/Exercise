if __name__ == '__main__':
 import sys
 import  os
 """try:
     f = open('my_file.txt')
     s = f.readline()
     i = int(s.strip())
 except OSError as err:
     print('Os error: ',err)
 except ValueError:
     print("Could not convert data to an integer")
 except Exception as err:
     print(f"Unexcepected {err=}, {type(err)=}")
     raise"""
 """for arg in sys.argv[2:3]:
     try:
         f=open(arg, 'r')
     except OSError:
         print('cannot open ',arg)
     else:
         print(arg, 'has', len(f.readline()),'lines')
         f.close()"""
 """def this_fails():
     x = 1/0
 try:
     this_fails()
 except ZeroDivisionError as err:
     print('Handling run-time error:', err)"""
 """try:
     raise KeyboardInterrupt
 finally:
     print('Goodbye, world!')
 def divid(a, b):
     try:
         result = a/b
     except ZeroDivisionError:
         print("divide by zero!")
     except TypeError as err:
         print("Impossible ",err)
     else:
         print("result is: ",result)
     finally:
         print("exucte finally")
divid("1","2")"""

 if os.path.exists("file2.txt"):
  os.remove("file2.txt")
 else:
  print("file doesn't exist")