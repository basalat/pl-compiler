import ply.yacc as yacc
from lexer import tokens

class OperatorInfo:
    precedence_values = {}
    precedence_type = {}



def p_expression_precedence(p):
    'expression : OP LPAREN NUMBER COMMA PRECEDENCE COMMA ATOM RPAREN DOT'
    print('number = ' + p[2] + ', precedence = ' + p[4] + ', op = ' + p[6])

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
op(700, xfx, )@<.
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
