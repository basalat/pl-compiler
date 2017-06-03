import ply.lex as lex

reserved = {
   'op': 'OP',
}

precedence = {
   'xfx',
   'xfy',
   'yfx',
   'fx',
   'fy',
   'xf',
   'yf',
}

operators = {'rdiv', '.', '@>=', '**', '>', '@>', ':<', '\\=@=', '|', '\\==', '^',
             '+', '//', '?-', '*', 'mod', '-->', '=\\=', '=:=', '\\', '@<', '>>',
             '<', 'xor', 'div', '==', ':', '>:<', '\\=', 'rem', '-', '\\/', 'as',
             ':=', '\\+', '->', '$', '/', '>=', 'is', ':-', '?', '=@=', ';', '<<',
             '*->', '=..', '/\\', '=<', '=', '@=<'}

# List of token names.   This is always required
tokens = tuple(list((
   'NUMBER',
   'LPAREN',
   'RPAREN',
   'COMMA',
   'STRING',
   'IMPLY',
   'BAR',
   'RBRACE',
   'LBRACE',
   'DOT',
   'COMMENT_SINGLE_LINE',
   'VAR',
   'ATOM',
   'PRECEDENCE',
   'OPERATOR',
   'PRCUT'))
+ list(reserved.values())
)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_IMPLY = r':-'
t_BAR = r'\|'
t_RBRACE = r'\]'
t_LBRACE = r'\['
t_DOT = r'\.'
t_PRCUT = r'\!'
t_VAR = r'[A-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t


def t_STRING(t):
    r'\"(.|\\")*\"'
    t.value = t.value[1:-1]
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMENT_SINGLE_LINE(t):
    r'(%%|%!)( )(.)*\n'
    pass
    # No return value. Token discarded


def t_ATOM(t):
    r'[a-z0-9@><=\*\\\|\^\+/\?\-/\\:\$\.\;](\S)*'
    if t.value in reserved.keys():
        t.type = reserved.get(t.value)
    elif t.value in precedence:
        t.type = 'PRECEDENCE'
    elif t.value in operators:
        t.type = 'OPERATOR'
    return t


# Build the lexer
lexer = lex.lex()

data = '''
%% 
%! 
op
:-,3.5e1 + 4 * 10 | [ .    ] [   ] "hel\"lo"
  + -20 *2
  ABC
  _Acc
  abc132

msort([],[]).
msort([X],[X]).
msort([H|T], Sx) :- split(H,T,L,R), msort(L, Ls), msort(R, Rs), 
merge(Sxsub, Ls, Rs), merge(Sx, [H], Sxsub).

split(Pivot,[],[],[]).
split(Pivot,[Pivot|T],[Pivot|R],L) :- split(Pivot,T,R,L).
split(Pivot,[H|T],[H|R],L) :- Pivot > H, split(Pivot,T,R,L).
split(Pivot,[H|T],R,[H|L]) :- Pivot < H, split(Pivot,T,R,L).

merge(X,X,[]).
merge(X,[],X).
merge([HL|T],[HL|L],[HR|R]) :- HL =< HR, merge(T,L,[HR|R]).
merge([HR|T],[HL|L],[HR|R]) :- HL >= HR, merge(T,[HL|L],R).
  
  ABC , . ! * :
  
  xfx xfy fx fy
< * --> + hello 1 2 3 3.5 0.99e12  

rdiv  .  @>=  **  >  @>  :<  \\=@=  |  \\==  ^  +  //  ?-  *  mod  -->  
=\\=  =:=  \\  @<  >>  <  xor  div  ==  :  >:<  \\=  rem  -  \\/  
as  :=  \\+  ->  $  /  >=  is  :-  ?  =@=  ;  <<  *->  =..  /\\  =<  =  @=<
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

print(reserved)
print(reserved.keys())
print(reserved.values())
