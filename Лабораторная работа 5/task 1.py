# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

dict_int = [{'bin': bin(int), 'dec': int, 'hex': hex(int), 'oct': oct(int)} for int in range (16)]
pprint(dict_int)
