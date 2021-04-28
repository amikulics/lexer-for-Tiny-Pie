# lexer-for-Tiny-Pie
Lexer with GUI written in Python for fake language "TinyPie"

This lexer follows the BNF grammar:
Exp -> float id = math
math -> multi + multi
multi -> int * multi | float

if_exp -> if(companion_exp):
companion_exp -> identifier > identifier

print_exp -> print(Str_literal)

The GUI was made using the tkinter library. There are three boxes: Input, Tokens, and Parse Tree.
The Input box allows the user to type in a line of code. The code will be split into tokens which will be shown in the middle box. Then a text-based parse tree will be made in the third box. 
