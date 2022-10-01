//grammar BKIT;
//
//@lexer::header {
//from lexererr import *
//}
//
//@lexer::members {
//def emit(self):
//    tk = self.type
//    result = super().emit()
//    if tk == self.UNCLOSE_STRING:
//        raise UncloseString(result.text)
//    elif tk == self.ILLEGAL_ESCAPE:
//        raise IllegalEscape(result.text)
//    elif tk == self.ERROR_CHAR:
//        raise ErrorToken(result.text)
//    elif tk == self.UNTERMINATED_COMMENT:
//        raise UnterminatedComment()
//    else:
//        return result;
//}
//
//options {
//	language = Python3;
//}
//
//program: var_decl* func_decl* EOF;
//
//// 7. Program
//
//var_decl: VAR COLON variable_list SEMI;
//variable: ID (LS INT_LIT RS)*;
//full_variable: variable (ASSIGN literal)?;
//variable_list: full_variable (COMMA full_variable)*;
//
//func_decl: func_name func_param? func_body;
//func_name: FUNC COLON ID;
//func_param: PARAM COLON param_list;
//func_body: BODY COLON stmts ENDBODY DOT;
//param_list: variable (COMMA variable)*;
//
//// 5. Expressions
//
//expr_list: expr (COMMA expr)*;
//
//expr:
//	logic_expr (
//		ISEQUAL
//		| ISDIF
//		| SMALLER
//		| BIGGER
//		| EQUALORBIGGER
//		| EQUALORSMALLER
//		| FISDIF
//		| FSMALLER
//		| FBIGGER
//		| FEQUALORBIGGER
//		| FEQUALORSMALLER
//	) logic_expr
//	| logic_expr;
//
//logic_expr: logic_expr (AND | OR) add_expr | add_expr;
//
//add_expr:
//	add_expr (ADD | FADD | SIGN | FSIGN) mul_expr
//	| mul_expr;
//
//mul_expr:
//	mul_expr (MUL | FMUL | DIV | FDIV | MOD) not_expr
//	| not_expr;
//
//not_expr: NOT not_expr | sign_expr;
//
//sign_expr: (SIGN | FSIGN) sign_expr | element_expr;
//
////element_expr: element_expr index_operators | func_expr;
//
//element_expr: array_element | func_expr;
//
//func_expr: func_call | parenthesed_expr;
//
//parenthesed_expr: LB expr RB | literal | ID;
//
//func_call: ID LB expr_list? RB;
//index_operators: LS expr RS | LS expr RS index_operators;
//
////array_element: (ID | func_call) index_operators;
//
//array_element: func_expr index_operators;
//
//// 6. Statements
//
//stmts: vardecl_stmt* other_stmt*;
//other_stmt:
//	assign_stmt
//	| if_stmt
//	| for_stmt
//	| while_stmt
//	| do_while_stmt
//	| break_stmt
//	| continue_stmt
//	| call_stmt
//	| return_stmt;
//
//vardecl_stmt: var_decl;
//
//assign_stmt: (ID | array_element) ASSIGN expr SEMI;
//
//if_stmt:
//	IF expr THEN stmts (ELSEIF expr THEN stmts)* (ELSE stmts)? ENDIF DOT;
//
//for_stmt:
//	FOR LB (ID ASSIGN expr) (COMMA expr) (COMMA expr) RB DO stmts ENDFOR DOT;
//
//while_stmt: WHILE expr DO stmts ENDWHILE DOT;
//
//do_while_stmt: DO stmts WHILE expr ENDDO DOT;
//
//break_stmt: BREAK SEMI;
//
//continue_stmt: CONTINUE SEMI;
//
//call_stmt: func_call SEMI;
//
//return_stmt: RETURN expr? SEMI;
//
//// 4. Literals
//
//INT_LIT: ZERO | DEC | HEX | OCT;
//fragment ZERO: '0';
//fragment DEC: [1-9][0-9]*;
//fragment HEX: '0' [xX] [1-9A-F][0-9A-F]*;
//fragment OCT: '0' [oO] [1-7][0-7]*;
//
//FLOAT_LIT: (FINT FDEC FEXP) | (FINT FDEC) | (FINT FEXP);
//fragment FINT: [0-9]+;
//fragment FDEC: '.' [0-9]*;
//fragment FEXP: [eE][-+]? [0-9]+;
//
//BOOL_LIT: TRUE | FALSE;
//
//fragment ESCAPE_SEQUENCE:
//	'\\\''
//	| '\\\\'
//	| '\\b'
//	| '\\f'
//	| '\\n'
//	| '\\r'
//	| '\\t';
//
//fragment CHAR_LIT: ~["\\\r\n'] | ESCAPE_SEQUENCE | '\'"';
//
//STRING_LIT: '"' CHAR_LIT* '"' {self.text = self.text.strip('"')};
//
//array: LC literal_element RC;
//literal_element: literal (COMMA literal)*;
//
//literal: INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT | array;
//
//// 8. Comment
//
//COMMENT: ('**' .*? '**') -> skip; // <- need to check whether it is greedy or not
//
//// 1. Keywords
//
//BODY: 'Body';
//
//ELSE: 'Else';
//
//ENDFOR: 'EndFor';
//
//IF: 'If';
//
//VAR: 'Var';
//
//ENDDO: 'EndDo';
//
//BREAK: 'Break';
//
//ELSEIF: 'ElseIf';
//
//ENDWHILE: 'EndWhile';
//
//PARAM: 'Parameter';
//
//WHILE: 'While';
//
//CONTINUE: 'Continue';
//
//ENDBODY: 'EndBody';
//
//FOR: 'For';
//
//RETURN: 'Return';
//
//TRUE: 'True';
//
//DO: 'Do';
//
//ENDIF: 'EndIf';
//
//FUNC: 'Function';
//
//THEN: 'Then';
//
//FALSE: 'False';
//
//// 3. Operators
//
//ADD: '+';
//
//FADD: '+.';
//
//SIGN: '-';
//
//FSIGN: '-.';
//
//MUL: '*';
//
//FMUL: '*.';
//
//DIV: '\\';
//
//FDIV: '\\.';
//
//MOD: '%';
//
//NOT: '!';
//
//AND: '&&';
//
//OR: '||';
//
//ISEQUAL: '==';
//
//ISDIF: '!=';
//
//SMALLER: '<';
//
//BIGGER: '>';
//
//EQUALORSMALLER: '<=';
//
//EQUALORBIGGER: '>=';
//
//FISDIF: '=/=';
//
//FSMALLER: '<.';
//
//FBIGGER: '>.';
//
//FEQUALORSMALLER: '<=.';
//
//FEQUALORBIGGER: '>=.';
//
//ASSIGN: '=';
//
//// 3. Seperators
//
//LB: '(';
//
//RB: ')';
//
//LS: '[';
//
//RS: ']';
//
//COLON: ':';
//
//DOT: '.';
//
//COMMA: ',';
//
//SEMI: ';';
//
//LC: '{';
//
//RC: '}';
//
//// 2. Indentifiers
//
//ID: [a-z][a-zA-Z0-9_]*;
//
//// 9. Others
//
//WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
//
//ILLEGAL_ESCAPE:
//	'"' CHAR_LIT* ('\\' ~([bfnrt\\] | '\'')) {self.text = self.text.replace('"','',1)};
//
//UNCLOSE_STRING:
//	'"' CHAR_LIT* {self.text = self.text.replace('"','',1)};
//
//UNTERMINATED_COMMENT: '**' .*?;
//
//ERROR_CHAR: .;

// -> Below is the exam test
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

program:  EOF;

test_aa: AA;
AA: CONTENT+ | CONTENT+ 'a' | CONTENT+ 'aa' | 'a' | 'aa';
fragment CONTENT: ('a' | 'aa')? 'b'+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines