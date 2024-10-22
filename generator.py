import re

tokenClassVRegularExpression = r'^V_[a-z]([a-z]|[0-9])*$' # This regular expression accepts variable names
tokenClassFRegularExpression = r'^F_[a-z]([a-z]|[0-9])*$' # This regular expression accepts function names
tokenClassTRegularExpression = r"^[A-Z][a-z]{0,7}$" # This regular expression accepts strings
tokenClassNRegularExpression = r"^-?(0|[1-9][0-9]*)(\.[0-9]*[1-9])?$" # This accepts numbers that include
# BUG: This regular expression accepts -0, which is invalid but we'll ignore it for now

output = ""
tabs = ""
# This function is supposed to get user input that matches the regular expression
def getUserInput(prompt: str, regExp):
    while True:
        userInput = input(prompt)

        if re.match(regExp, userInput):
            return userInput
        
        print("Invalid input")

def pushTab():
    global tabs
    tabs += '----'

def popTab():
    global tabs
    tabs = tabs[:len(tabs)-4]

def getTabs():
    global tabs
    return tabs

def PROG():
    print(getTabs() + "> " + "PROG")
    pushTab()

    global output
    output += "main\n"
    GLOBVARS()
    ALGO()
    FUNCTIONS()
    popTab()
    

def GLOBVARS():
    print(getTabs() + "> " + "GLOBVARS")
    pushTab()

    global output
    rule = getUserInput("Enter GLOBVARS rule: ", r"^[1-2]$")

    if rule == "1":
        return
    elif rule == "2":
        VTYP()
        VNAME()
        output += ',\n'
        GLOBVARS()
    
    popTab()

def VTYP():
    print(getTabs() + "> " + "VTYP")
    pushTab()
    global output
    rule = getUserInput("Enter VTYPE rule: ", r"^[1-2]$")

    if rule == "1":
        output += "num "
    elif rule == "2":
        output += "text "
    popTab()

def VNAME():
    print(getTabs() + "> " + "VNAME")
    pushTab()
    global output, tokenClassVRegularExpression
    output += getUserInput("Enter variable name: ", tokenClassVRegularExpression)
    popTab()

def ALGO():
    print(getTabs() + "> " + "ALGO")
    pushTab()
    global output
    output += "\nbegin\n"
    INSTRUC()
    output += "\nend\n"
    popTab()

def INSTRUC():
    print(getTabs() + "> " + "INSTRUC")
    pushTab()
    global output
    rule = getUserInput("Enter INSTRUC rule: ", r"^[1-2]$")

    if rule == "1":
        output += " "
        return 
    elif rule == "2":
        COMMAND()
        output += "; "
        INSTRUC()
    popTab()

def COMMAND():
    print(getTabs() + "> " + "COMMAND")
    pushTab()
    global output
    rule = getUserInput("Enter COMMAND rule: ", r"^[1-6]$")

    if rule == "1":
        output += "skip"
    elif rule == "2":
        output += "halt"
    elif rule == "3":
        output += "return "
        ATOMIC()
    elif rule == "4":
        ASSIGN()
    elif rule == "5":
        CALL()
    elif rule == "6":
        BRANCH()
    popTab()

def ATOMIC():
    print(getTabs() + "> " + "ATOMIC")
    pushTab()
    global output
    rule = getUserInput("Enter ATOMIC rule: ", r"^[1-2]$")

    if rule == "1":
        VNAME()
    elif rule == "2":
        CONST()
    popTab()

def CONST():
    print(getTabs() + "> " + "CONST")
    pushTab()
    global output, tokenClassNRegularExpression, tokenClassTRegularExpression
    rule = getUserInput("Enter CONST rule: ", r"^[1-2]$")

    if rule == "1":
        output += getUserInput("Enter a valid number: ", tokenClassNRegularExpression) + " "
    elif rule == "2":
        output += getUserInput("Enter a valid string: ", tokenClassTRegularExpression) + " "
    popTab()

def ASSIGN():
    print(getTabs() + "> " + "ASSIGN")
    pushTab()
    global output
    rule = getUserInput("Enter ASSIGN rule: ", r"^[1-2]$")

    if rule == "1":
        VNAME()
        output += " <input"
    elif rule == "2":
        VNAME()
        output += " = "
        TERM()
    popTab()

def CALL():
    print(getTabs() + "> " + "CALL")
    pushTab()
    global output
    
    FNAME()
    output += "("
    ATOMIC()
    output += ", "
    ATOMIC()
    output += ", "
    ATOMIC()
    output += ") "
    popTab()

def BRANCH():
    print(getTabs() + "> " + "BRANCH")
    pushTab()
    global output

    output += "if "
    COND()
    output += "\nthen "
    ALGO()
    output += "\nelse "
    ALGO()
    popTab()

def TERM():
    print(getTabs() + "> " + "TERM")
    pushTab()
    rule = getUserInput("Enter TERM rule: ", r"^[1-3]$")

    if rule == "1":
        ATOMIC()
    elif rule == "2":
        CALL()
    elif rule == "3":
        OP()
    popTab()

def OP():
    print(getTabs() + "> " + "OP")
    pushTab()
    global output
    rule = getUserInput("Enter OP rule: ", r"^[1-2]$")

    if rule == "1":
        UNOP()
        output += "("
        ARG()
        output += ")"
    elif rule == "2":
        BINOP()
        output += "("
        ARG()
        output += ", "
        ARG()
        output += ")"
    popTab()

def ARG():
    print(getTabs() + "> " + "ARG")
    pushTab()
    rule = getUserInput("Enter ARG rule: ", r"^[1-2]$")

    if rule == "1":
        ATOMIC()
    elif rule == "2":
        OP()
    popTab()

def COND():
    print(getTabs() + "> " + "COND")
    pushTab()
    rule = getUserInput("Enter COND rule: ", r"^[1-2]$")

    if rule == "1":
        SIMPLE()
    elif rule == "2":
        COMPOSIT()
    popTab()

def SIMPLE():
    print(getTabs() + "> " + "SIMPLE")
    pushTab()
    global output

    BINOP()
    output += "("
    ATOMIC()
    output += ", "
    ATOMIC()
    output += ")"
    popTab()

def COMPOSIT():
    print(getTabs() + "> " + "COMPOSIT")
    pushTab()
    global output

    rule = getUserInput("Enter COMPOSIT rule: ", r"^[1-2]$")

    if rule == "1":
        BINOP()
        output += "("
        ATOMIC()
        output += ", "
        ATOMIC()
        output += ")"
    elif rule == "2":
        UNOP()
        output += "("
        SIMPLE()
        output += ")"
    popTab()

def UNOP():
    print(getTabs() + "> " + "UNOP")
    pushTab()
    global output

    rule = getUserInput("Enter UNOP rule: ", r"^[1-2]$")

    if rule == "1":
        output += "not"
    elif rule == "2":
        output += "sqrt"
    popTab()

def BINOP():
    print(getTabs() + "> " + "BINOP")
    pushTab()
    global output

    rule = getUserInput("Enter BINOP rule: ", r"^[1-8]$")

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
    popTab()

def FNAME():
    print(getTabs() + "> " + "FNAME")
    pushTab()
    global output, tokenClassFRegularExpression

    output += getUserInput("Enter function name: ", tokenClassFRegularExpression)
    popTab()

def FUNCTIONS():
    print(getTabs() + "> " + "FUNCTIONS")
    pushTab()
    rule = getUserInput("Enter FUNCTIONS rule: ", r"^[1-2]$")

    if rule == "1":
        return
    elif rule == "2":
        DECL()
        FUNCTIONS()
    popTab()

def DECL():
    print(getTabs() + "> " + "DECL")
    pushTab()
    HEADER()
    BODY()
    popTab()

def HEADER():
    print(getTabs() + "> " + "HEADER")
    pushTab()
    global output

    FTYP()
    FNAME()
    output += "("
    VNAME()
    output += ", "
    VNAME()
    output += ", "
    VNAME()
    output += ")"
    popTab()

def FTYP():
    print(getTabs() + "> " + "FTYP")
    pushTab()
    global output

    rule = getUserInput("Enter FTYP rule: ", r"^[1-2]$")

    if rule == "1":
        output += "num "
    elif rule == "2":
        output += "void "
    popTab()

def BODY():
    print(getTabs() + "> " + "BODY")
    pushTab()
    global output

    PROLOG()
    LOCVARS()
    ALGO()
    EPILOG()
    SUBFUNCS()
    output += "\nend"
    popTab()

def PROLOG():
    print(getTabs() + "> " + "PROLOG")
    pushTab()
    global output
    output += "{\n"
    popTab()

def EPILOG():
    print(getTabs() + "> " + "EPILOG")
    pushTab()
    global output
    output += "\n}\n"
    popTab()

def LOCVARS():
    print(getTabs() + "> " + "LOCVARS")
    pushTab()
    global output

    VTYP()
    VNAME()
    output += ",\n"
    VTYP()
    VNAME()
    output += ",\n"
    VTYP()
    VNAME()
    output += ",\n"
    popTab()

def SUBFUNCS():
    print(getTabs() + "> " + "SUBFUNCS")
    pushTab()
    FUNCTIONS()
    popTab()

def start():
    global output
    output = ""
    PROG()

    with open("./samples/output.txt", "w") as file:
        file.write(output)

start()

