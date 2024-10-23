# COS 341 Project Code Generator

This script generates test code for the COS 341 Project. Simply run the script, follow the prompts to build your tree, and the code will be generated. When asked for a rule number, input the corresponding number for each production rule listed below.

## Production Rules

### 1. `PROG`
1. `PROG ::= main GLOBVARS ALGO FUNCTIONS`

### 2. `GLOBVARS`
1. `GLOBVARS ::= // nullable`
2. `GLOBVARS ::= VTYP VNAME , GLOBVARS // there can be as many global variables as we like`

### 3. `VTYP`
1. `VTYP ::= num`
2. `VTYP ::= text`

### 4. `VNAME`
1. `VNAME ::= a token of Token-Class V from the Lexer`  
(See the Appendix below)

### 5. `ALGO`
1. `ALGO ::= begin INSTRUC end`

### 6. `INSTRUC`
1. `INSTRUC ::= // nullable`
2. `INSTRUC ::= COMMAND ; INSTRUC`

### 7. `COMMAND`
1. `COMMAND ::= skip // an empty algorithmic step where nothing happens`
2. `COMMAND ::= halt`
3. `COMMAND ::= print ATOMIC`
4. `COMMAND ::= ASSIGN`
5. `COMMAND ::= CALL // call to a void-function that only updates global variables`
6. `COMMAND ::= BRANCH`
7. `COMMAND ::= print ATOMIC`

### 8. `ATOMIC`
1. `ATOMIC ::= VNAME`
2. `ATOMIC ::= CONST`

### 9. `CONST`
1. `CONST ::= a token of Token-Class N from the Lexer`
2. `CONST ::= a token of Token-Class T from the Lexer`

### 10. `ASSIGN`
1. `ASSIGN ::= VNAME < input // user input during run-time`
2. `ASSIGN ::= VNAME = TERM // deep nesting of assignment terms is allowed`

### 11. `CALL`
1. `CALL ::= FNAME( ATOMIC , ATOMIC , ATOMIC ) // un-nested params only`

### 12. `BRANCH`
1. `BRANCH ::= if COND then ALGO else ALGO`

### 13. `TERM`
1. `TERM ::= ATOMIC`
2. `TERM ::= CALL`
3. `TERM ::= OP`

### 14. `OP`
1. `OP ::= UNOP( ARG )`
2. `OP ::= BINOP( ARG , ARG )`

### 15. `ARG`
1. `ARG ::= ATOMIC`
2. `ARG ::= OP // allows deep-nesting of operations`

### 16. `COND`
1. `COND ::= SIMPLE`
2. `COND ::= COMPOSIT`

### 17. `SIMPLE`
1. `SIMPLE ::= BINOP( ATOMIC , ATOMIC )`

### 18. `COMPOSIT`
1. `COMPOSIT ::= BINOP( SIMPLE , SIMPLE )`
2. `COMPOSIT ::= UNOP( SIMPLE )`

### 19. `UNOP`
1. `UNOP ::= not`
2. `UNOP ::= sqrt // square root of real numbers`

### 20. `BINOP`
1. `BINOP ::= or`
2. `BINOP ::= and`
3. `BINOP ::= eq`
4. `BINOP ::= grt // greater than >`
5. `BINOP ::= add`
6. `BINOP ::= sub`
7. `BINOP ::= mul`
8. `BINOP ::= div`

### 21. `FNAME`
1. `FNAME ::= a token of Token-Class F from the Lexer`

### 22. `FUNCTIONS`
1. `FUNCTIONS ::= // nullable`
2. `FUNCTIONS ::= DECL FUNCTIONS`

### 23. `DECL`
1. `DECL ::= HEADER BODY`

### 24. `HEADER`
1. `HEADER ::= FTYP FNAME( VNAME , VNAME , VNAME ) // functions have 3 parameters`

### 25. `FTYP`
1. `FTYP ::= num`
2. `FTYP ::= void`

### 26. `BODY`
1. `BODY ::= PROLOG LOCVARS ALGO EPILOG SUBFUNCS end`

### 27. `PROLOG`
1. `PROLOG ::= { // the prolog`

### 28. `EPILOG`
1. `EPILOG ::= } // the epilog`

### 29. `LOCVARS`
1. `LOCVARS ::= VTYP VNAME , VTYP VNAME , VTYP VNAME`

### 30. `SUBFUNCS`
1. `SUBFUNCS ::= FUNCTIONS // functions can have sub-functions`

---

## Appendix

- **Token-Class V**: Represents variable names, defined by the regular expression: `r'^V_[a-z]([a-z]|[0-9])*$'`
- **Token-Class F**: Represents function names, defined by the regular expression: `r'^F_[a-z]([a-z]|[0-9])*$'`
- **Token-Class N**: Represents numbers, defined by the regular expression: `r"^-?(0|[1-9][0-9]*)(\.[0-9]*[1-9])?$"`
- **Token-Class T**: Represents strings, defined by the regular expression: `r"^\"[A-Z][a-z]{0,7}\"$"`

