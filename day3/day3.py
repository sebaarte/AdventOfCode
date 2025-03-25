import re
import ply.lex as lex


tokens = ("MUL","DO","DONT")

t_MUL = r"mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)"
t_DO = r"do()"
t_DONT = r"don't()"

# def t_MUL(t):
#     r"mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)"
#     m = re.match(t_MUL,t.value)
#     t.value = int(m[0]) * int(m[1])
#     return t

def t_error(t):
    t.lexer.skip(1)

def parse():
    
    with open("day3/data.txt") as file:
        summ = 0
        content = file.read()
        foo = lambda x: int(x[0]) * int(x[1])

    
        lexer = lex.lex()
        lexer.input(content)
        enabled = True
        while True:
            tok = lexer.token()
            
            if not tok:
                return summ
            typ = tok.type
            if enabled:
                match typ:
                    case "MUL":
                        m = re.match(t_MUL,tok.value)
                        summ += int(m[1]) * int(m[2])

                    case "DONT":
                        enabled = False
                    case _:
                        pass
            else:
                match tok.type:
                    case "DO":
                        enabled = True
                    case _:
                        pass
            # print(tok)


if __name__ == "__main__":
    print(parse())