'''
BNF grammer:
Exp -> float id = math
math -> multi + multi
multi -> int * multi | float

if_exp -> if(companion_exp):
companion_exp -> identifier > identifier

print_exp -> print(Str_literal)

'''

from tkinter import *
from tkinter import messagebox

Mytokens = [("empty", "empty"), ("empty", "empty")]
inToken = ("empty", "empty")

def accept_token(self):
    global inToken
    global Mytokens
    self.finalBox.insert(INSERT, "     accept token from the list:" + inToken[1] + '\n')
    inToken = Mytokens.pop(0)

def print_exp(self):
    print("\n----parent node print_exp, finding children nodes:")
    self.finalBox.insert(INSERT, "\n----parent node print_exp, finding children nodes:"+ '\n')
    global inToken
    global Mytokens
    typeT, token = inToken
    if(token=="print"):
        print("child node (internal): keyword")
        self.finalBox.insert(INSERT, "child node (internal): keyword" + '\n')
        print("   keyword has child node (token):" + inToken[1])
        self.finalBox.insert(INSERT, "   keyword has child node (token):" + inToken[1] + '\n')
        accept_token(self)

        if (inToken[1] == "("):
            print("child node (internal): separator")
            self.finalBox.insert(INSERT, "child node (internal): separator" + '\n')
            print("   separator has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   separator has child node (token):" + inToken[1] + '\n')
            accept_token(self)
        else:
            print("Expected separator in print statement!")
            self.finalBox.insert(INSERT, "Expected separator in print statement!" + '\n')
            return

        if (inToken[0] == "string"):
            print("child node (internal): string")
            self.finalBox.insert(INSERT, "child node (internal): string" + '\n')
            print("   string has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   string has child node (token):" + inToken[1] + '\n')
            accept_token(self)
        else:
            print("Expected string in print statement!")
            self.finalBox.insert(INSERT, "Expected string in print statement!" + '\n')
            return

        if (inToken[1] == ")"):
            print("child node (internal): separator")
            self.finalBox.insert(INSERT, "child node (internal): separator" + '\n')
            print("   separator has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   separator has child node (token):" + inToken[1] + '\n')
            accept_token(self)
        else:
            print("Expected separator in print statement!")
            self.finalBox.insert(INSERT, "Expected separator in print statement!" + '\n')
            return

def if_exp(self):
    print("\n----parent node if_exp, finding children nodes:")
    self.finalBox.insert(INSERT, "\n----parent node if_exp, finding children nodes:" + '\n')
    global inToken
    global Mytokens
    typeT, token = inToken
    if(token=="if"):
        print("child node (internal): keyword")
        self.finalBox.insert(INSERT, "child node (internal): keyword" + '\n')
        print("   keyword has child node (token):" + inToken[1])
        self.finalBox.insert(INSERT, "   keyword has child node (token):" + inToken[1] + '\n')
        accept_token(self)
        if(inToken[1]=="("):
            print("child node (internal): separator")
            self.finalBox.insert(INSERT, "child node (internal): separator" + '\n')
            print("   separator has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   separator has child node (token):" + inToken[1] + '\n')
            accept_token(self)
            companion_exp(self)
        else:
            print("Expected separator in if statement!")
            self.finalBox.insert(INSERT, "Expected separator in if statement!" + '\n')
            return
        if (inToken[1] == ")"):
            print("child node (internal): separator")
            self.finalBox.insert(INSERT, "child node (internal): separator" + '\n')
            print("   separator has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   separator has child node (token):" + inToken[1] + '\n')
            accept_token(self)
        else:
            print("Expected separator in if statement!")
            self.finalBox.insert(INSERT, "Expected separator in if statement!" + '\n')
            return

    else:
        print("Expected if statement to start with keyword:if!")
        self.finalBox.insert(INSERT, "Expected if statement to start with keyword:if!" + '\n')
        return

def companion_exp(self):
    print("\n----parent node companion_exp, finding children nodes:")
    self.finalBox.insert(INSERT, "\n----parent node companion_exp, finding children nodes:" + '\n')
    global inToken
    global Mytokens
    if (inToken[0] == "identifier"):
        print("child node (internal): identifier")
        self.finalBox.insert(INSERT, "child node (internal): identifier" + '\n')
        print("   identifier has child node (token):" + inToken[1])
        self.finalBox.insert(INSERT, "   identifier has child node (token):" + inToken[1] + '\n')
        accept_token(self)
        if (inToken[1] == ">"):
            print("child node (internal): operator")
            self.finalBox.insert(INSERT, "child node (internal): operator" + '\n')
            print("   operator has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   operator has child node (token):" + inToken[1] + '\n')
            accept_token(self)
        else:
            print("Expected > in companion statement!")
            self.finalBox.insert(INSERT, "Expected > in companion statement!" + '\n')
            return
        if (inToken[0] == "identifier"):
            print("child node (internal): identifier")
            self.finalBox.insert(INSERT, "child node (internal): identifier" + '\n')
            print("   identifier has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   identifier has child node (token):" + inToken[1] + '\n')
            accept_token(self)
        else:
            print("Expected identifier in companion statement!")
            self.finalBox.insert(INSERT, "Expected identifier in companion statement!" + '\n')
            return
    else:
        print("Expected companion statement to start with identifier!")
        self.finalBox.insert(INSERT, "Expected companion statement to start with identifier!" + '\n')
        return

def multi(self):
    print("\n----parent node multi, finding children nodes:")
    self.finalBox.insert(INSERT, "\n----parent node multi, finding children nodes:" + '\n')
    global inToken
    global Mytokens
    if (inToken[0] == "float"):
        print("child node (internal): float")
        self.finalBox.insert(INSERT, "child node (internal): float" + '\n')
        print("   float has child node (token):" + inToken[1])
        self.finalBox.insert(INSERT,"   float has child node (token):" + inToken[1] + '\n')
        accept_token(self)
    elif (inToken[0] == "integer"):
        print("child node (internal): int")
        self.finalBox.insert(INSERT, "child node (internal): int" + '\n')
        print("   int has child node (token):" + inToken[1])
        self.finalBox.insert(INSERT, "   int has child node (token):" + inToken[1] + '\n')
        accept_token(self)

        if (inToken[1] == "*"):
            print("child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "child node (token):" + inToken[1] + '\n')
            accept_token(self)

            print("child node (internal): multi")
            self.finalBox.insert(INSERT, "child node (internal): multi" + '\n')
            multi(self)
        else:
            print("error, you need * after the int in the multi")
            self.finalBox.insert(INSERT, "error, you need * after the int in the multi" + '\n')

    else:
        print("error, multi expects float or int")
        self.finalBox.insert(INSERT, "error, multi expects float or int" + '\n')

def math(self):
    print("\n----parent node math, finding children nodes:")
    self.finalBox.insert(INSERT, "\n----parent node math, finding children nodes:" + '\n')
    global inToken
    global Mytokens
    typeT, token = inToken
    print("child node (internal): multi")
    self.finalBox.insert(INSERT, "child node (internal): multi" + '\n')
    multi(self)
    if(inToken[1]=="+"):
        print("child node (token):" + inToken[1])
        self.finalBox.insert(INSERT, "child node (token):" + inToken[1] + '\n')
        accept_token(self)
    else:
        print("error, you need + between multi")
        self.finalBox.insert(INSERT, "error, you need + between multi" + '\n')
        return
    print("child node (internal): multi")
    self.finalBox.insert(INSERT, "child node (internal): multi" + '\n')
    multi(self)

def exp(self):
    print("\n----parent node exp, finding children nodes:")
    self.finalBox.insert(INSERT,"\n----parent node exp, finding children nodes:" + '\n')
    global inToken
    global Mytokens
    typeT, token = inToken
    if (typeT == "keyword" and token == "float"):
        print("child node (internal): keyword")
        self.finalBox.insert(INSERT, "child node (internal): keyword"+'\n')
        print("   keyword has child node (token):" + token)
        self.finalBox.insert(INSERT, "   keyword has child node (token):" + token + '\n')
        accept_token(self)
    else:
        print("expect keyword:float as the first element of the expression!\n")
        self.finalBox.insert(INSERT, "expect keyword:float as the first element of the expression!\n" + '\n')
        return

    typeT, token = inToken
    if (typeT == "identifier"):
        print("child node (internal): identifier")
        self.finalBox.insert(INSERT, "child node (internal): identifier" + '\n')
        print("   identifier has child node (token):" + token)
        self.finalBox.insert(INSERT, "   identifier has child node (token):" + token + '\n')
        accept_token(self)
    else:
        print("expect identifier as the next element of the expression!\n")
        self.finalBox.insert(INSERT, "expect identifier as the next element of the expression!\n" + '\n')
        return

    if (inToken[1] == "="):
        print("child node (token):" + inToken[1])
        self.finalBox.insert(INSERT, "child node (token):" + inToken[1] + '\n')
        accept_token(self)
    else:
        print("expect = as the next element of the expression!")
        self.finalBox.insert(INSERT, "expect = as the next element of the expression!" + '\n')
        return

    print("Child node (internal): math")
    self.finalBox.insert(INSERT, "Child node (internal): math" + '\n')
    math(self)

def parse(self):
    global inToken
    global Mytokens
    inToken = Mytokens.pop(0)
    typeT, token = inToken
    if (token == "float"): exp(self)
    elif (token == "if"):
        if_exp(self)
        if (inToken[1] == ":"):
            print("child node (internal): separator")
            self.finalBox.insert(INSERT, "child node (internal): separator" + '\n')
            print("   separator has child node (token):" + inToken[1])
            self.finalBox.insert(INSERT, "   separator has child node (token):" + inToken[1] + '\n')
            print("     accept token from the list:" + inToken[1])
            self.finalBox.insert(INSERT, "     accept token from the list:" + inToken[1] + '\n')
            print("\nparse tree building success!")
            self.finalBox.insert(INSERT, "\nparse tree building success!" + '\n')
        else:
            print("Expected separator in if statement!")
            self.finalBox.insert(INSERT, "Expected separator in if statement!" + '\n')
            return

    elif (token == "print"): print_exp(self)
    if (inToken[1] == ";"):
        print("\nparse tree building success!")
        self.finalBox.insert(INSERT, "\nparse tree building success!" + '\n')

class lexerGUI:

    def __init__(self, root):
        self.currentLine = 0
        self.master = root
        self.master.title("Lexer for TinyPie - HW5")

        self.inputLabel = Label(self.master, text="Source Code Input:")  # entry text
        self.inputLabel.grid(row=0, column=1)
        self.inputBox = Text(self.master, height=35, width=50)  # entry box
        self.inputBox.grid(row=1, column=1, padx=20, columnspan=2)

        self.outputLabel = Label(self.master, text="Tokens:")  # output text
        self.outputLabel.grid(row=0, column=3)
        self.outputBox = Text(self.master, height=35, width=50)  # output box
        self.outputBox.grid(row=1, column=3, padx=20, columnspan=2)

        self.finalLabel = Label(self.master, text="Parse Tree:")  # final text
        self.finalLabel.grid(row=0, column=5)
        self.finalBox = Text(self.master, height=35, width=50)  # final box
        self.finalBox.grid(row=1, column=5, padx=20, columnspan=2)

        self.lineNumberDisplay = Entry(self.master, width=3)  # line number counter
        self.lineNumberDisplay.grid(row=2, column=2)
        self.numberLabel = Label(self.master, text="Current Processing Line:")
        self.numberLabel.grid(row=2, column=1)

        self.nextButton = Button(self.master, text="Next Line", command=self.nextLine)  # next line button
        self.nextButton.grid(row=3, column=2, pady=5)

        self.quitButton = Button(self.master, text="Quit", command=self.master.destroy)  # quit button
        self.quitButton.grid(row=2, column=5, padx=5, pady=5)

    def nextLine(self):
        global inToken
        global Mytokens
        inputText = self.inputBox.get("1.0", "end")
        strList = []
        strList = inputText.rstrip().split('\n')
        tokenList = []
        if (self.currentLine + 1 <= len(strList)):
            Mytokens = cutOneLineTokens(strList[self.currentLine])

            self.lineNumberDisplay.delete(0, 'end')
            self.currentLine += 1
            self.lineNumberDisplay.insert(1, self.currentLine)
            for i in Mytokens:
                self.outputBox.insert(INSERT, '<')
                self.outputBox.insert(INSERT, i[0])
                self.outputBox.insert(INSERT, ',')
                self.outputBox.insert(INSERT, i[1])
                self.outputBox.insert(INSERT, '>')
                self.outputBox.insert(INSERT, '\n')
            parse(self)
        else:
            messagebox.showerror("Error", "No more lines to print!")

def cutOneLineTokens(line):
    print("Test input string:", line)
    resultList = []
    while (line != ""):
        line = line.lstrip()
        test1 = re.match(r'\b(if|else|int|float|print)\b', line)  # keyword
        if (test1 != None):
            # resultList.append("<keyword, " + test1.group() + ">")
            tempToken = ("keyword", test1.group())
            resultList.append(tempToken)
            line = removeFromStr(line, test1.group())
            line = line.lstrip()
            continue

        test2 = re.match(r'[=+>*]', line)  # operator
        if (test2 != None):
            # resultList.append("<operator, " + test2.group() + ">")
            tempToken = ("operator", test2.group())
            resultList.append(tempToken)
            line = removeFromStr(line, test2.group())
            line = line.lstrip()
            continue

        test3 = re.match(r'[():";\]\[]', line)  # seperators
        if (test3 != None):
            # resultList.append("<seperators, " + test3.group() + ">")
            tempToken = ("seperators", test3.group())
            resultList.append(tempToken)
            line = removeFromStr(line, test3.group())
            line = line.lstrip()
            continue

        test4 = re.match(r'([A-Z]+|[a-z]+)([A-Z]+|[a-z]+)*[0-9]*', line)  # identifers
        if (test4 != None):
            # resultList.append("<Identifiers, " + test4.group() + ">")
            tempToken = ("identifier", test4.group())
            resultList.append(tempToken)
            line = removeFromStr(line, test4.group())
            line = line.lstrip()
            continue

        test5 = re.match(r'\d+[.]\d+', line)  # float
        if (test5 != None):
            # resultList.append("<Float, " + test5.group() + ">")
            tempToken = ("float", test5.group())
            resultList.append(tempToken)
            line = removeFromStr(line, test5.group())
            line = line.lstrip()
            continue

        test6 = re.match(r'\d+', line)  # integers
        if (test6 != None):
            # resultList.append("<Integer, " + test6.group() + ">")
            tempToken = ("integer", test6.group())
            resultList.append(tempToken)
            line = removeFromStr(line, test6.group())
            line = line.lstrip()
            continue

        test7 = re.match(r'(["].+["])|([“].+[”])', line)  # string
        if (test7 != None):
            # resultList.append("<String, " + test7.group() + ">")
            tempToken = ("string", test7.group())
            resultList.append(tempToken)
            line = removeFromStr(line, test7.group())
            line = line.lstrip()
            continue

    print("Output <type, token> list:", resultList)
    return resultList

def removeFromStr(fullLine, str):  # removes str from fullline, returns result
    length = len(str)
    return fullLine[(length):]

if __name__ == '__main__':
    mainRoot = Tk()
    mainGUI = lexerGUI(mainRoot)
    mainRoot.mainloop()
