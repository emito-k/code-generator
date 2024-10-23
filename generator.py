import re

tokenClassVRegularExpression = r'^V_[a-z]([a-z]|[0-9])*$' # This regular expression accepts variable names
tokenClassFRegularExpression = r'^F_[a-z]([a-z]|[0-9])*$' # This regular expression accepts function names
tokenClassTRegularExpression = r"^\"[A-Z][a-z]{0,7}\"$" # This regular expression accepts strings
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

def pushTab(n):
    global tabs
    tabs += '----'

def popTab(n):
    pass

def getTabs():
    # global tabs
    return '----'

def PROG(n):
    print(getTabs()* n + "> " + "PROG")
    

    global output
    output += "main\n"
    GLOBVARS(n+1)
    ALGO(n+1)
    FUNCTIONS(n+1)

def GLOBVARS(n):
    print(getTabs()* n + "> " + "GLOBVARS")
    

    global output
    rule = getUserInput("Enter GLOBVARS rule: ", r"^[1-2]$")

    if rule == "1":
        return
    elif rule == "2":
        VTYP(n+1)
        VNAME(n+1)
        output += ',\n'
        GLOBVARS(n+1)
    
    

def VTYP(n):
    print(getTabs()* n + "> " + "VTYP")
    
    global output
    rule = getUserInput("Enter VTYPE rule: ", r"^[1-2]$")

    if rule == "1":
        output += "num "
    elif rule == "2":
        output += "text "
    

def VNAME(n):
    print(getTabs()* n + "> " + "VNAME")
    
    global output, tokenClassVRegularExpression
    output += getUserInput("Enter variable name: ", tokenClassVRegularExpression)
    

def ALGO(n):
    print(getTabs()* n + "> " + "ALGO")
    
    global output
    output += "\nbegin\n"
    INSTRUC(n+1)
    output += "\nend\n"
    

def INSTRUC(n):
    print(getTabs()* n + "> " + "INSTRUC")
    
    global output
    rule = getUserInput("Enter INSTRUC rule: ", r"^[1-2]$")

    if rule == "1":
        output += " "
        return 
    elif rule == "2":
        COMMAND(n+1)
        output += "; "
        INSTRUC(n+1)
    

def COMMAND(n):
    print(getTabs()* n + "> " + "COMMAND")
    
    global output
    rule = getUserInput("Enter COMMAND rule: ", r"^[1-7]$")

    if rule == "1":
        output += "skip"
    elif rule == "2":
        output += "halt"
    elif rule == "3":
        output += "print "
        ATOMIC(n+1)
    elif rule == "4":
        ASSIGN(n+1)
    elif rule == "5":
        CALL(n+1)
    elif rule == "6":
        BRANCH(n+1)
    elif rule == "7":
        output += "return "
        ATOMIC(n+1)
    

def ATOMIC(n):
    print(getTabs()* n + "> " + "ATOMIC")
    
    global output
    rule = getUserInput("Enter ATOMIC rule: ", r"^[1-2]$")

    if rule == "1":
        VNAME(n+1)
    elif rule == "2":
        CONST(n+1)
    

def CONST(n):
    print(getTabs()* n + "> " + "CONST")
    
    global output, tokenClassNRegularExpression, tokenClassTRegularExpression
    rule = getUserInput("Enter CONST rule: ", r"^[1-2]$")

    if rule == "1":
        output += getUserInput("Enter a valid number: ", tokenClassNRegularExpression) + " "
    elif rule == "2":
        output += getUserInput("Enter a valid string: ", tokenClassTRegularExpression) + " "
    

def ASSIGN(n):
    print(getTabs()* n + "> " + "ASSIGN")
    
    global output
    rule = getUserInput("Enter ASSIGN rule: ", r"^[1-2]$")

    if rule == "1":
        VNAME(n+1)
        output += " <input"
    elif rule == "2":
        VNAME(n+1)
        output += " = "
        TERM(n+1)
    

def CALL(n):
    print(getTabs()* n + "> " + "CALL")
    
    global output
    
    FNAME(n+1)
    output += "("
    ATOMIC(n+1)
    output += ", "
    ATOMIC(n+1)
    output += ", "
    ATOMIC(n+1)
    output += ") "
    

def BRANCH(n):
    print(getTabs()* n + "> " + "BRANCH")
    
    global output

    output += "if "
    COND(n+1)
    output += "\nthen "
    ALGO(n+1)
    output += "\nelse "
    ALGO(n+1)
    

def TERM(n):
    print(getTabs()* n + "> " + "TERM")
    
    rule = getUserInput("Enter TERM rule: ", r"^[1-3]$")

    if rule == "1":
        ATOMIC(n+1)
    elif rule == "2":
        CALL(n+1)
    elif rule == "3":
        OP(n+1)
    

def OP(n):
    print(getTabs()* n + "> " + "OP")
    
    global output
    rule = getUserInput("Enter OP rule: ", r"^[1-2]$")

    if rule == "1":
        UNOP(n+1)
        output += "("
        ARG(n+1)
        output += ")"
    elif rule == "2":
        BINOP(n+1)
        output += "("
        ARG(n+1)
        output += ", "
        ARG(n+1)
        output += ")"
    

def ARG(n):
    print(getTabs()* n + "> " + "ARG")
    
    rule = getUserInput("Enter ARG rule: ", r"^[1-2]$")

    if rule == "1":
        ATOMIC(n+1)
    elif rule == "2":
        OP(n+1)
    

def COND(n):
    print(getTabs()* n + "> " + "COND")
    
    rule = getUserInput("Enter COND rule: ", r"^[1-2]$")

    if rule == "1":
        SIMPLE(n+1)
    elif rule == "2":
        COMPOSIT(n+1)
    

def SIMPLE(n):
    print(getTabs()* n + "> " + "SIMPLE")
    
    global output

    BINOP(n+1)
    output += "("
    ATOMIC(n+1)
    output += ", "
    ATOMIC(n+1)
    output += ")"
    

def COMPOSIT(n):
    print(getTabs()* n + "> " + "COMPOSIT")
    
    global output

    rule = getUserInput("Enter COMPOSIT rule: ", r"^[1-2]$")

    if rule == "1":
        BINOP(n+1)
        output += "("
        ATOMIC(n+1)
        output += ", "
        ATOMIC(n+1)
        output += ")"
    elif rule == "2":
        UNOP(n+1)
        output += "("
        SIMPLE(n+1)
        output += ")"
    

def UNOP(n):
    print(getTabs()* n + "> " + "UNOP")
    
    global output

    rule = getUserInput("Enter UNOP rule: ", r"^[1-2]$")

    if rule == "1":
        output += "not"
    elif rule == "2":
        output += "sqrt"
    

def BINOP(n):
    print(getTabs()* n + "> " + "BINOP")
    
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
    

def FNAME(n):
    print(getTabs()* n + "> " + "FNAME")
    
    global output, tokenClassFRegularExpression

    output += getUserInput("Enter function name: ", tokenClassFRegularExpression)
    

def FUNCTIONS(n):
    print(getTabs()* n + "> " + "FUNCTIONS")
    
    rule = getUserInput("Enter FUNCTIONS rule: ", r"^[1-2]$")

    if rule == "1":
        return
    elif rule == "2":
        DECL(n+1)
        FUNCTIONS(n+1)
    

def DECL(n):
    print(getTabs()* n + "> " + "DECL")
    
    HEADER(n+1)
    BODY(n+1)
    

def HEADER(n):
    print(getTabs()* n + "> " + "HEADER")
    
    global output

    FTYP(n+1)
    FNAME(n+1)
    output += "("
    VNAME(n+1)
    output += ", "
    VNAME(n+1)
    output += ", "
    VNAME(n+1)
    output += ")"
    

def FTYP(n):
    print(getTabs()* n + "> " + "FTYP")
    
    global output

    rule = getUserInput("Enter FTYP rule: ", r"^[1-2]$")

    if rule == "1":
        output += "num "
    elif rule == "2":
        output += "void "
    

def BODY(n):
    print(getTabs()* n + "> " + "BODY")
    
    global output

    PROLOG(n+1)
    LOCVARS(n+1)
    ALGO(n+1)
    EPILOG(n+1)
    SUBFUNCS(n+1)
    output += "\nend"
    

def PROLOG(n):
    print(getTabs()* n + "> " + "PROLOG")
    
    global output
    output += "{\n"
    

def EPILOG(n):
    print(getTabs()* n + "> " + "EPILOG")
    
    global output
    output += "\n}\n"
    

def LOCVARS(n):
    print(getTabs()* n + "> " + "LOCVARS")
    
    global output

    VTYP(n+1)
    VNAME(n+1)
    output += ",\n"
    VTYP(n+1)
    VNAME(n+1)
    output += ",\n"
    VTYP(n+1)
    VNAME(n+1)
    output += ",\n"
    

def SUBFUNCS(n):
    print(getTabs()* n + "> " + "SUBFUNCS")
    
    FUNCTIONS(n+1)
    

def start():
    global output
    output = ""
    PROG(0)

    with open(input("Output file name (please add .txt): "), "w") as file:
        file.write(output)

start()

