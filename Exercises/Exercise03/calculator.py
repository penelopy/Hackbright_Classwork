from arithmetic  import *



def do_calc():
    while True:
        usr_input = raw_input("> ")
        tok_input = usr_input.split()

        if tok_input[0] == "q":
            break
        
        elif tok_input[0] == "+": 
            print add(int(tok_input[1]), int(tok_input[2]))
        elif tok_input[0] == "-": 
            print subtract(int(tok_input[1]), int(tok_input[2]))
        elif tok_input[0] == "*": 
            print multiply(int(tok_input[1]), int(tok_input[2]))
        elif tok_input[0] == "/": 
            print divide(int(tok_input[1]), float(tok_input[2]))

        elif tok_input[0] == "square": 
            print square(int(tok_input[1]))

        elif tok_input[0] == "cube": 
            print cube(int(tok_input[1]))

        elif tok_input[0] == "power": 
            print power(int(tok_input[1]), int(tok_input[2]))

        elif tok_input[0] == "mod": 
            print mod(int(tok_input[1]), int(tok_input[2]))
        
        else:
            print "What language is that?"

print "name is ", __name__

if __name__ == "__main__": 
    do_calc()