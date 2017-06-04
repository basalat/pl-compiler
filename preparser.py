import ply.yacc as yacc
from lexer import tokens

class OperatorInfo:
    precedence_values = {}
    precedence_type = {}


def p_expression_precedence_list(p):
    '''precedence_list : precedence precedence_list
                       | precedence'''
    pass

def p_expression_precedence(p):
    'precedence : OP LPAREN NUMBER COMMA PRECEDENCE COMMA ATOM RPAREN DOT'
    print('precedence = ' + p[5] + ', op = ' + p[7])
    p[0] = p[7]


standardOperators = '''
op(700, xfx, <).
op(700, xfx, =).
op(700, xfx, =..).
op(700, xfx, =@=).
op(700, xfx, \=@=).
op(700, xfx, =:=).
op(700, xfx, =<).
op(700, xfx, ==).
op(700, xfx, =/=).
op(700, xfx, >).
op(700, xfx, >=).
op(700, xfx, @<).
op(700, xfx, @=<).
op(700, xfx, @>).
op(700, xfx, @>=).
op(700, xfx, \=).
op(700, xfx, \==).
op(700, xfx, as).
op(700, xfx, is).
op(700, xfx, >:<).
op(700, xfx, :<).
op(1200, xfx, -->).
op(1200, xfx, :-).
op(1200, fx, :-).
op(1200, fx, ?-).
op(1100, xfy, ;).
op(1100, xfy, |).
op(1050, xfy, ->).
op(1050, xfy, *->).
op(990, xfx, :=).
op(900, xfx, \+).
op(600, yfx, :).
op(500, yfx, +).
op(500, yfx, -).
op(500, yfx, /\).
op(500, yfx, \/).
op(500, yfx, xor).
op(500, fx, ?).
op(400, yfx, *).
op(400, yfx, /).
op(400, yfx, //).
op(400, yfx, div).
op(400, yfx, rdiv).
op(400, yfx, <<).
op(400, yfx, >>).
op(400, yfx, mod).
op(400, yfx, rem).
op(200, xfx, **).
op(200, xfy, ^).
op(200, fy, +).
op(200, fy, -).
op(200, fy, \).
op(1, fx, $).
'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   s = standardOperators
   result = parser.parse(s)
   if result == None:
       break
   print(result)
