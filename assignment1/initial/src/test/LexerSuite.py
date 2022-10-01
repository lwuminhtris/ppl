import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier_0(self):
        """lower"""
        input=r'''thisissomeid'''
        expect=r'''thisissomeid,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,100))

    def test_identifier_1(self):
        input=r'''slowDancingINtHEDark'''
        expect=r'''slowDancingINtHEDark,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('fOOlzZZ','fOOlzZZ,<EOF>',101))

    def test_identifier_2(self):
        input=r'''inthe_dark'''
        expect=r'''inthe_dark,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('under__score','under__score,<EOF>',102))

    def test_identifier_3(self):
        input=r'''the1toloveyou'''
        expect=r'''the1toloveyou,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('the1andon1y','the1andon1y,<EOF>',103))

    def test_identifier_4(self):
        input=r'''show_thatILoveY'''
        expect=r'''show_thatILoveY,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('parser_RULE','parser_RULE,<EOF>',104))

    def test_identifier_5(self):
        input=r'''show_D1LoveY123'''
        expect=r'''show_D1LoveY123,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('vaRIAb1e567','vaRIAb1e567,<EOF>',105))

    def test_identifier_6(self):
        input=r'''tothe____moonAndB4ackstillLoveYou'''
        expect=r'''tothe____moonAndB4ackstillLoveYou,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('x__221','x__221,<EOF>',106))

    def test_identifier_7(self):
        input=r'''i_tlikeNothingHASchanged123560'''
        expect=r'''i_tlikeNothingHASchanged123560,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('mIxed13_andYoUxx__','mIxed13_andYoUxx__,<EOF>',107))

    def test_identifier_8(self):
        input=r'''s1235__justLIKETHIS'''
        expect=r'''s1235__justLIKETHIS,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('lOVrE_99_YOUr3000','lOVrE_99_YOUr3000,<EOF>',108))

    def test_identifier_9(self):
        input=r'''aBBBFFWQETYx123_5869'''
        expect=r'''aBBBFFWQETYx123_5869,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('aBBBBBx999rr0','aBBBBBx999rr0,<EOF>',109))

    def test_identifier_10(self):
        input=r'''Flywithme'''
        expect=r'''Error Token F'''
        self.assertTrue(TestLexer.checkLexeme('Aa','Error Token A',110))

    def test_identifier_11(self):
        input=r'''isthisthereal?life'''
        expect=r'''isthisthereal,Error Token ?'''
        self.assertTrue(TestLexer.checkLexeme('aaaaa?bbbbb','aaaaa,Error Token ?',111))

    def test_identifier_12(self):
        input="withyou\n"
        expect="withyou,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,112))

    def test_identifier_13(self):
        input=r'''1234huh'''
        expect=r'''1234,huh,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('1233what','1233,what,<EOF>',113))

    def test_comment_14(self):
        """single line"""
        input=r'''**just a glimpse of us**'''
        expect=r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,114))

    def test_comment_15(self):
        """multi-line"""
        input=r'''**hoping you will \n find \n a glimpse of us**'''
        expect=r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,115))

    def test_comment_16(self):
        """unterminated single"""
        input=r'''** not finished ......'''
        expect=r'''Unterminated Comment'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,116))

    def test_comment_17(self):
        """unterminated multi"""
        input=r'''** not finished me \n don't care much ..'''
        expect=r'''Unterminated Comment'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,117))

    def test_keyword_18(self):
        input=r'''Body EndBody If EndIf Do EndDo While EndWhile'''
        expect=r'''Body,EndBody,If,EndIf,Do,EndDo,While,EndWhile,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('Body Break Continue Do Else ElseIf EndBody EndIf','Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,<EOF>',118))

    def test_keyword_19(self):
        input=r'''For EndFor Return Then If Function Var Parameter'''
        expect=r'''For,EndFor,Return,Then,If,Function,Var,Parameter,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('EndFor EndWhile For Function If Parameter Return Then','EndFor,EndWhile,For,Function,If,Parameter,Return,Then,<EOF>',119))

    def test_keyword_20(self):
        input=r'''True False'''
        expect=r'''True,False,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('Var While True False EndDo','Var,While,True,False,EndDo,<EOF>',120))

    def test_keyword_21(self):
        input=r'''If i was you i would EndIf Else'''
        expect=r'''If,i,was,you,i,would,EndIf,Else,<EOF>'''
        """mix keyword and identifier"""
        self.assertTrue(TestLexer.checkLexeme('If if Else else','If,if,Else,else,<EOF>',121))

    def test_keyword_22(self):
        input=r'''While this do True Else Return'''
        expect=r'''While,this,do,True,Else,Return,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('Do a whiLe b Return','Do,a,whiLe,b,Return,<EOF>',122))

    def test_keyword_23(self):
        input=r'''Whileiwasyou'''
        expect=r'''While,iwasyou,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('DoNothing','Do,Error Token N',123))

    def test_keyword_24(self):
        input=r'''Function?Parameter'''
        expect=r'''Function,Error Token ?'''
        self.assertTrue(TestLexer.checkLexeme('Do?While','Do,Error Token ?',124))

    def test_operator_25(self):
        """int operators"""
        input=r'''+-*\\==!=><>=<='''
        expect=r'''+,-,*,\,==,!=,>,<,>=,<=,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('+-*\\==!=><>=<=','+,-,*,\,==,!=,>,<,>=,<=,<EOF>',125))

    def test_operator_26(self):
        """float operators"""
        input=r'''+.-.*.\\.=/=<.>.<=.>=.'''
        expect=r'''+.,-.,*.,\.,=/=,<.,>.,<=.,>=.,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme('+.-.*.\\.=/=<.>.<=.>=.','+.,-.,*.,\.,=/=,<.,>.,<=.,>=.,<EOF>',126))

    def test_operator_27(self):
        """bool operators"""
        input=r'''!&&||'''
        expect=r'''!,&&,||,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,127))

    def test_mix_28(self):
        input=r'''If True Then dothis();'''
        expect=r'''If,True,Then,dothis,(,),;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,128))

    def test_mix_29(self):
        input="Function: a\n Parameter: b\n Body EndBody."
        expect="Function,:,a,Parameter,:,b,Body,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,129))

    def test_mix_30(self):
        """Some non-operator symbols"""
        input=r'''1+2==3 ? Return True'''
        expect=r'''1,+,2,==,3,Error Token ?'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,130))

    def test_mix_31(self):
        """Non-operator symbols"""
        input=r'''Var: s = lala'''
        expect=r'''Var,:,s,=,lala,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,131))

    def test_mix_32(self):
        input=r'''&&&'''
        expect=r'''&&,Error Token &'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,132))

    def test_mix_33(self):
        input=''
        expect='<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input,expect,133))

    def test_number_34(self):
        input=r'''07685'''
        expect=r'''0,7685,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,134))

    def test_number_35(self):
        """ hexa x and X"""
        input=r'''0x123 0X12345'''
        expect=r'''0x123,0X12345,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,135))

    def test_number_36(self):
        """octo o and O"""
        input=r'''0o034 0O555'''
        expect=r'''0,o034,0O555,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,136))

    def test_number_37(self):
        """all types"""
        input=r'''0o1111 0X69 69'''
        expect=r'''0o1111,0X69,69,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,137))

    def test_number_38(self):
        """hex, oct and identifier"""
        input=r'''0x1111 x1111 1111'''
        expect=r'''0x1111,x1111,1111,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,138))

    def test_number_39(self):
        """wrong format hex"""
        input=r'''12x32BCD'''
        expect=r'''12,x32BCD,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,139))

    def test_number_40(self):
        """wrong format oct"""
        input=r'''10p43'''
        expect=r'''10,p43,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,140))

    def test_number_41(self):
        input=r'''000'''
        expect=r'''0,0,0,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,141))

    def test_number_42(self):
        input=r'''0o11111'''
        expect=r'''0o11111,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,142))

    def test_number_43(self):
        input=r'''0xXX123'''
        expect=r'''0,xXX123,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,143))

    def test_number_44(self):
        """float"""
        input=r'''123E456'''
        expect=r'''123E456,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,144))

    def test_number_45(self):
        """float"""
        input=r'''123e+4'''
        expect=r'''123e+4,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,145))

    def test_number_46(self):
        """float"""
        input=r'''123.456'''
        expect=r'''123.456,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,146))

    def test_number_47(self):
        """float"""
        input=r'''1.'''
        expect=r'''1.,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,147))

    def test_number_48(self):
        """float"""
        input=r'''169.E+419'''
        expect=r'''169.E+419,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,148))

    def test_number_49(self):
        """float"""
        input=r'''123.4E567'''
        expect=r'''123.4E567,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,149))

    def test_complex_50(self):
        """float"""
        input=r'''1,11e23'''
        expect=r'''1,,,11e23,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,150))

    def test_number_51(self):
        """float"""
        input=r'''12e+202.5E-123.12345.0'''
        expect=r'''12e+202,.,5E-123,.,12345.0,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,151))

    def test_number_52(self):
        """float"""
        input=r'''12E'''
        expect=r'''12,Error Token E'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,152))

    def test_number_53(self):
        """float"""
        input=r'''11..111e222'''
        expect=r'''11.,.,111e222,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,153))

    def test_number_54(self):
        """float"""
        input=r'''.11-E11'''
        expect=r'''.,11,-,Error Token E'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,154))

    def test_number_55(self):
        """float"""
        input=r'''123.45F67'''
        expect=r'''123.45,Error Token F'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,155))

    def test_number_56(self):
        """float"""
        input=r'''0000.0000E+0000'''
        expect=r'''0000.0000E+0000,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,156))

    def test_complex_57(self):
        input=r'''Var: a_B=0E90, do = 0X90;'''
        expect=r'''Var,:,a_B,=,0E90,,,do,=,0X90,;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,157))

    def test_complex_58(self):
        input=r'''hh + 0000 >= 12.E00 - True;'''
        expect=r'''hh,+,0,0,0,0,>=,12.E00,-,True,;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,158))

    def test_complex_59(self):
        input=r'''True False true false TRUE FALSE '''
        expect=r'''True,False,true,false,Error Token T'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,159))

    def test_string_60(self):
        input=r'''" just a normal string"'''
        expect=r''' just a normal string,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,160))

    def test_string_61(self):
        """escape string"""
        input=r'''" \\n Hello \\n \\f \\t"'''
        expect=r''' \\n Hello \\n \\f \\t,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,161))

    def test_string_62(self):
        input='" Boundme \'" please \'" "'
        expect=r''' Boundme '" please '" ,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,162))

    def test_string_63(self):
        input=r'''""'''
        expect=r''',<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,163))

    def test_string_64(self):
        input=r'''"""wtf"'''
        expect=r''',wtf,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,164))

    def test_string_65(self):
        """string"""
        input=r''''''
        expect=r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,165))

    def test_string_66(self):
        """string"""
        input=r''''''
        expect=r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,166))

    def test_string_67(self):
        input=r'''" something just like this \\t huh!!'''
        expect=r'''Unclosed String:  something just like this \\t huh!!'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,167))

    def test_string_68(self):
        input=r'''"""im not fvcking completed!""'''
        expect=r''',im not fvcking completed!,Unclosed String: '''
        self.assertTrue(TestLexer.checkLexeme(input,expect,168))

    def test_string_69(self):
        input='"multi \n string";'
        expect='Unclosed String: multi '
        self.assertTrue(TestLexer.checkLexeme(input,expect,169))

    def test_string_70(self):
        input='"Wrong escape: \\x";'
        expect=r'''Illegal Escape In String: Wrong escape: \x'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,170))

    def test_string_71(self):
        input = '"Escapes: \\b \\t \\g \\"'
        expect = r'''Illegal Escape In String: Escapes: \b \t \g'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,171))

    def test_string_72(self):
        input = r'''"w **t** f"'''
        expect = r'''w **t** f,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,172))

    def test_string_73(self):
        input = r'''**w "t" f**'''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,173))

    def test_string_74(self):
        input = '"Wrong Escape: \\"'
        expect = 'Illegal Escape In String: Wrong Escape: \\"'
        self.assertTrue(TestLexer.checkLexeme(input,expect,174))

    def test_string_75(self):
        input = r''''''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,175))

    def test_string_76(self):
        input = r'''abc^'''
        expect = r'''abc,Error Token ^'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,176))

    def test_complex_77(self):
        input = r'''Var: s="haha","qweqweqwe",0O1234,True;'''
        expect = r'''Var,:,s,=,haha,,,qweqweqwe,,,0O1234,,,True,;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,177))

    def test_string_78(self):
        input = '"Who\'re you"'
        expect = 'Unclosed String: Who'
        self.assertTrue(TestLexer.checkLexeme(input,expect,178))

    def test_complex_79(self):
        input = 'writeLn("bokura wa \n");'
        expect = 'writeLn,(,Unclosed String: bokura wa '
        self.assertTrue(TestLexer.checkLexeme(input,expect,179))

    def test_complex_80(self):
        input = r''''''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,180))

    def test_complex_81(self):
        input = r''''''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,181))

    def test_complex_82(self):
        input = r''''''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,182))

    def test_complex_83(self):
        input = 'me("and") + you("are", not) && 111;'
        expect = 'me,(,and,),+,you,(,are,,,not,),&&,111,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input,expect,183))

    def test_complex_84(self):
        input = r'''me = you = someone * 123 - 3.14'''
        expect = r'''me,=,you,=,someone,*,123,-,3.14,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,184))

    def test_complex_85(self):
        """for loop"""
        input = 'For (i=0, i<69,1) Do \n j = j + 1; \n EndFor.'
        expect = 'For,(,i,=,0,,,i,<,69,,,1,),Do,j,=,j,+,1,;,EndFor,.,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input,expect,185))

    def test_complex_86(self):
        input = r'''a[4[5]] = b[c[6][7][8]];'''
        expect = r'''a,[,4,[,5,],],=,b,[,c,[,6,],[,7,],[,8,],],;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,186))

    def test_complex_87(self):
        input = ''
        expect = '<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input,expect,187))

    def test_complex_88(self):
        input = r'''Var: a, b = 1,2,3,4;'''
        expect = r'''Var,:,a,,,b,=,1,,,2,,,3,,,4,;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,188))

    def test_complex_89(self):
        input = 'abc123\\n;'
        expect = 'abc123,\\,n,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input,expect,189))

    def test_complex_90(self):
        input = '  \t  \t'
        expect = '<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input,expect,190))

    def test_complex_91(self):
        input = r'''123123_2591029WEQSD1.45E2'''
        expect = r'''123123,Error Token _'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,191))

    def test_complex_92(self):
        input = r'''5sadqwrE8.1E4GG1392ASdjwoiqjr'''
        expect = r'''5,sadqwrE8,.,1E4,Error Token G'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,192))

    def test_complex_93(self):
        input = r'''1ytr=1234xxx;'''
        expect = r'''1,ytr,=,1234,xxx,;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,193))

    def test_complex_94(self):
        input = r'''2..3467.22'''
        expect = r'''2.,.,3467.22,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,194))

    def test_complex_95(self):
        input = r'''[1][2][3][[4][5]]'''
        expect = r'''[,1,],[,2,],[,3,],[,[,4,],[,5,],],<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,195))

    def test_complex_96(self):
        input = r''''''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,196))

    def test_complex_97(self):
        input = r''''''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,197))

    def test_complex_98(self):
        input = r'''-1,-1.111'''
        expect = r'''-,1,,,-,1.111,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,198))

    def test_complex_99(self):
        input = r''''''
        expect = r'''<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input,expect,199))

