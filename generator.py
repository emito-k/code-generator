import re

tokenClassVRegularExpression = r'^V_[a-z]([a-z]|[0-9])*$' # This regular expression accepts variable names
tokenClassFRegularExpression = r'^F_[a-z]([a-z]|[0-9])*$' # This regular expression accepts function names
tokenClassTRegularExpression = r"^[A-Z][a-z]{0,7}$" # This regular expression accepts strings
tokenClassNRegularExpression = r"^-?(0|[1-9][0-9])*(\.[0-9]*[1-9])?$" # This accepts numbers that include
# BUG: This regular expression accepts -0, which is invalid but we'll ignore it for now

output = ""

# This function is supposed to get user input that matches the regular expression
def getUserInput(prompt: str, regExp):
    while True:
        userInput = input(prompt)

        if re.match(regExp, userInput):
            return userInput
        
        print("Invalid input")

def PROG():
    global output
    output += "main"
    GLOBVARS()
    ALGO()
    FUNCTIONS()
    

def GLOBVARS():
    global output
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        return
    elif rule == "2":
        VTYP()
        VNAME()
        output += ','
        GLOBVARS()

def VTYP():
    global output
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        output += "num"
    elif rule == "2":
        output += "text"

def VNAME():
    global output, tokenClassVRegularExpression
    output += getUserInput("Enter variable name: ", tokenClassVRegularExpression)

def ALGO():
    global output
    output += "begin"
    INSTRUC()
    output += "end"

def INSTRUC():
    global output
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        return
    elif rule == "2":
        COMMAND()
        output += ";"
        INSTRUC()

def COMMAND():
    global output
    rule = getUserInput("Enter rule: ", r"^[1-6]$")

    if rule == "1":
        output += "skip"
    elif rule == "2":
        output += "halt"
    elif rule == "3":
        output += "return"
        ATOMIC()
    elif rule == "4":
        ASSIGN()
    elif rule == "5":
        CALL()
    elif rule == "6":
        BRANCH()

def ATOMIC():
    global output
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        VNAME()
    elif rule == "2":
        CONST()

def CONST():
    global output, tokenClassNRegularExpression, tokenClassTRegularExpression
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        output += getUserInput("Enter a valid number: ", tokenClassNRegularExpression)
    elif rule == "2":
        output +=getUserInput("Enter a valid string: ", tokenClassTRegularExpression)

def ASSIGN():
    global output
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        VNAME()
        output += "<input"
    elif rule == "2":
        VNAME()
        output += "="
        TERM()

def CALL():
    global output
    
    FNAME()
    output += "("
    ATOMIC()
    output += ","
    ATOMIC()
    output += ","
    ATOMIC()
    output += ")"

def BRANCH():
    global output

    output += "if"
    COND()
    output += "then"
    ALGO()
    output += "else"
    ALGO()

def TERM():
    rule = getUserInput("Enter rule: ", r"^[1-3]$")

    if rule == "1":
        ATOMIC()
    elif rule == "2":
        CALL()
    elif rule == "3":
        OP()

def OP():
    global output
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        UNOP()
        output += "("
        ARG()
        output += ")"
    elif rule == "2":
        BINOP()
        output += "("
        ARG()
        output += ","
        ARG()
        output += ")"

def ARG():
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        ATOMIC()
    elif rule == "2":
        OP()

def COND():
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        SIMPLE()
    elif rule == "2":
        COMPOSIT()

def SIMPLE():
    global output

    BINOP()
    output += "("
    ATOMIC()
    output += ","
    ATOMIC()
    output += ")"

def COMPOSIT():
    global output

    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        BINOP()
        output += "("
        ATOMIC()
        output += ","
        ATOMIC()
        output += ")"
    elif rule == "2":
        UNOP()
        output += "("
        SIMPLE()
        output += ")"

def UNOP():
    global output

    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        output += "not"
    elif rule == "2":
        output += "sqrt"

def BINOP():
    global output

    rule = getUserInput("Enter rule: ", r"^[1-8]$")

    if rule == "1":
        output += "or"
    elif rule == "2":
        output += "and"
    elif rule == "3":
        output += "eq"
    elif rule == "4":
        output += "grt"
    elif rule == "5":
        output += "add"
    elif rule == "6":
        output += "sub"
    elif rule == "7":
        output += "mul"
    elif rule == "2":
        output += "div"

def FNAME():
    global output, tokenClassFRegularExpression

    output += getUserInput("Enter function name: ", tokenClassFRegularExpression)

def FUNCTIONS():
    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        return
    elif rule == "2":
        DECL()
        FUNCTIONS()

def DECL():
    HEADER()
    BODY()

def HEADER():
    global output

    FTYP()
    FNAME()
    output += "("
    VNAME()
    output += ","
    VNAME()
    output += ","
    VNAME()
    output += ")"

def FTYP():
    global output

    rule = getUserInput("Enter rule: ", r"^[1-2]$")

    if rule == "1":
        output += "num"
    elif rule == "2":
        output += "void"

def BODY():
    global output

    PROLOG()
    LOCVARS()
    ALGO()
    EPILOG()
    SUBFUNCS()
    output += "end"

def PROLOG():
    global output
    output += "{"

def EPILOG():
    global output
    output += "}"

def LOCVARS():
    global output

    VTYP()
    VNAME()
    output += ","
    VTYP()
    VNAME()
    output += ","
    VTYP()
    VNAME()
    output += ","

def SUBFUNCS():
    FUNCTIONS()

def start():
    global output
    output = ""
    PROG()

    with open("output.txt", "w") as file:
        file.write(output)

start()

