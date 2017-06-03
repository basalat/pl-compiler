import ply.yacc as yacc
from lexer import tokens


def p_expression_precedence(p):
    'expression : IMPLY OP LPAREN NUMBER COMMA PRECEDENCE COMMA ATOM RPAREN DOT'
    p[0] = p[1] + p[3]
