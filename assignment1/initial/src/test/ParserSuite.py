import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_number_0(self):
        input = r"""
            Var: a;
        """
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,output, 200))

    def test_number_1(self):
        input = r"""
            Var: a,b,c;
        """
        output = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,output, 201))

    def test_number_2(self):
        input = r"""
            Var: a,b,c,d=4,e;
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(input,output, 202)
        )

    def test_number_3(self):
        input = r"""
        Var: x,y,z,a[1][2];
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 203
            )
        )

    def test_number_4(self):
        input = r"""
        Var: a={1,2,{1},{2,3}};
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                204,
            )
        )

    def test_number_5(self):
        input = r"""Var: a=a[2],b,c="hihi";"""
        output = r"""Error on line 1 col 7: a"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                205,
            )
        )

    def test_number_6(self):
        input = r"""Var: x"""
        output = r"""Error on line 1 col 6: <EOF>"""
        self.assertTrue(
            TestParser.checkParser(input,output, 206)
        )

    def test_number_7(self):
        input = r"""Var: array[1][1] = {1,2,3,4,5}"""
        output = r"""Error on line 1 col 30: <EOF>"""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 207
            )
        )

    def test_number_8(self):
        input = r"""Var: v=;"""
        output = r"""Error on line 1 col 7: ;"""
        self.assertTrue(
            TestParser.checkParser(input,output, 208)
        )

    def test_number_9(self):
        input = r"""Var: c[1][2 ;"""
        output = r"""Error on line 1 col 12: ;"""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 209
            )
        )

    def test_number_10(self):
        input = r"""Var: ar[1][2] = {3,{4,5};"""
        output = r"""Error on line 1 col 24: ;"""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 210
            )
        )

    def test_number_11(self):
        input = r"""Var: a,b c;"""
        output = r"""Error on line 1 col 9: c"""
        self.assertTrue(
            TestParser.checkParser(input,output, 211)
        )

    def test_number_12(self):
        input = r"""Var: a,b,c,;"""
        output = r"""Error on line 1 col 11: ;"""
        self.assertTrue(
            TestParser.checkParser(input,output, 212)
        )

    def test_number_13(self):
        input = r"""
            Function: empty
                Body:
                    genesis(1,2,a[2][-True])[5+6] = ive[1][!!2];
                EndBody.
        """
        output = "successful"
        self.assertTrue(TestParser.checkParser(input, output, 213))

    def test_number_14(self):
        input = r"""
            Function: empty 
                Body: 
                
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(input,output, 214)
        )

    def test_number_15(self):
        input = r"""
            Function: main
                Parameter: a,b,c
                Body: 
                
                EndBody.    
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 215
            )
        )

    def test_number_16(self):
        input = r"""
            Function: lovedive
                Body:
                    x = "haha";
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                216,
            )
        )

    def test_number_17(self):
        input = r"""
            Function: main
                Parameter: a[1]
                Body:
                    narcist = a[1];
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                217,
            )
        )

    def test_number_18(self):
        input = r"""
            Function: main 
                Parameter: n 
                Body: 
                    Var: a,b,c; 
                    writeln(a,b,c); 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                218,
            )
        )

    def test_number_19(self):
        input = r"""
            Function: main 
                Parameter: a,b[1][2],c 
                Body: 
                    
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                219,
            )
        )

    def test_number_20(self):
        input = r"""
            Function: selena 
                Parameter: n, a[2][3] 
                Body: 
                    age=22;
                EndBody.
                
            Function: justin 
                Parameter: n, a[2][3] 
                Body: 
                    age=23;
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                220,
            )
        )

    def test_number_21(self):
        input = r"""
            Function: main 
                Parameter: a=51
                Body:
                
                EndBody.
        """
        output = r"""Error on line 3 col 28: ="""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 221
            )
        )

    def test_number_22(self):
        input = r"""
            Function: main 
                Body: 
                
                EndBody. 
                
            Var: a,b,c;
        """
        output = r"""Error on line 7 col 12: Var"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                222,
            )
        )

    def test_number_23(self):
        input = r"""
            Function: main 
                Body: 
                    Return; 
                    Var: a;  
                EndBody.
        """
        output = r"""Error on line 5 col 20: Var"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                223,
            )
        )

    def test_number_24(self):
        input = r"""
            Function: Main 
                Body: 
                
                EndBody.
        """
        output = r"""M"""
        self.assertTrue(
            TestParser.checkParser(input,output, 224)
        )

    def test_number_25(self):
        input = r"""
            Function: main 
                Parameter: 
                Body:
                 
                EndBody.
        """
        output = r"""Error on line 4 col 16: Body"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                225,
            )
        )

    def test_number_26(self):
        input = r"""
            Function: main 
                Parameter: 1,2.5
                Body: 
                
                EndBody.
        """
        output = r"""Error on line 3 col 27: 1"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                226,
            )
        )

    def test_number_27(self):
        input = r"""
            Function: main 
                Parameter: 
                Body: 
                    Return; 
        """
        output = r"""Error on line 4 col 16: Body"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                227,
            )
        )

    def test_number_28(self):
        input = r"""
            Function: func 
                Parameter x,y,z 
                Body: 
                
                EndBody.
        """
        output = r"""Error on line 3 col 26: x"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                228,
            )
        )

    def test_number_29(self):
        input = r"""
            Function: main 
                Parameter: n,c,y 
                Body: 
                
                EndBody
        """
        output = r"""Error on line 7 col 8: <EOF>"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                229,
            )
        )

    def test_number_30(self):
        input = r"""
            Function: main 
                Body: 
                    If x>3 Then 
                        n=10;   
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                230,
            )
        )

    def test_number_31(self):
        input = r"""
            Function: main 
                Body: 
                    If a==b Then 
                        a=1; 
                    ElseIf a!=b Then 
                        Return a; 
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                231,
            )
        )

    def test_number_32(self):
        input = r"""
            Function: main 
                Body: 
                    If 1+2==3 Then 
                        Return; 
                    ElseIf "hihi" Then 
                        Break; 
                    Else 
                        Return; 
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                232,
            )
        )

    def test_number_33(self):
        input = r"""
            Function: main 
                Body: 
                    If 7e3 *. "5" 
                        Then a=""; 
                    Else 
                        b(); 
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                233,
            )
        )

    def test_number_34(self):
        input = r"""
            Function: main 
                Body: 
                    If something Then 
                        Return; 
                    ElseIf nothing Then 
                        Return; 
                    ElseIf maybe Then 
                        Var: a=2; 
                    Else 
                        Return; 
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                234,
            )
        )

    def test_number_35(self):
        input = r"""
            Function: main 
                Body: 
                    If (a+b)>2 Then 
                        Return; 
                    Else 
                        Break; 
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                235,
            )
        )

    def test_number_36(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                236,
            )
        )

    def test_number_37(self):
        input = r"""
            Function: main 
                Body: 
                    If a Then 
                        a=x; 
                    ElseIf b Then 
                        b=x; 
                        If c Then 
                            c=x;  
                        ElseIf d Then  
                            d=x; 
                        EndIf. 
                    Else 
                        Continue; 
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                237,
            )
        )

    def test_number_38(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                238,
            )
        )

    def test_number_39(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                239,
            )
        )

    def test_number_40(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                240,
            )
        )

    def test_number_41(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                241,
            )
        )

    def test_number_42(self):
        input = r"""Var: a=;"""
        output = r"""Error on line 1 col 7: ;"""
        self.assertTrue(
            TestParser.checkParser(input,output, 242)
        )

    def test_number_43(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                243,
            )
        )

    def test_number_44(self):
        input = r"""
            Function: empty 
                Body: 
                    For(i=1>2, i < 100, 1) Do 
                    
                    EndFor. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                244,
            )
        )

    def test_number_45(self):
        input = """
            Function: empty 
                Body: 
                    For(i = 2, i!=100, i+1) Do 
                        If (a+b)>(c+d) Then 
                            Return "Something\'"Just Like This\\n\'""; 
                        EndIf. 
                    EndFor. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                245,
            )
        )

    def test_number_46(self):
        input = r"""
            Function: empty 
                Body: 
                    For(i=1,i<=100,1) Do 
                        For(j=i,j<=100,2) Do 
                            writeln(j);  
                        EndFor. 
                        Continue; 
                    EndFor. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                246,
            )
        )

    def test_number_47(self):
        input = r"""
            Function: empty 
                Body: 
                    i = 15; 
                    For(,i,-1) Do 
                    
                    EndFor. 
                EndBody.
        """
        output = r"""Error on line 5 col 24: ,"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                247,
            )
        )

    def test_number_48(self):
        input = r"""
            Function: empty 
                Body: 
                    For(i = 2, 1>2,  ) Do 
                    
                    EndFor. 
                EndBody.
        """
        output = r"""Error on line 4 col 37: )"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                248,
            )
        )

    def test_number_49(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                249,
            )
        )

    def test_number_50(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                250,
            )
        )


    def test_number_51(self):
        input = r"""
            Function: empty 
                Body: 
                    For(i=2;i<100;i++) Do 
                    
                    EndFor. 
                EndBody.
        """
        output = r"""Error on line 4 col 27: ;"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                251,
            )
        )

    def test_number_52(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                252,
            )
        )

    def test_number_53(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                253,
            )
        )

    def test_number_54(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                254,
            )
        )

    def test_number_55(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                255,
            )
        )

    def test_number_56(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                256,
            )
        )

    def test_number_57(self):
        input = r"""
            Function: empty
                Body:
                    While a!=b Do
                        writeln();
                    EndWhile.
                EndBody.
        """
        output = "successful"
        self.assertTrue(TestParser.checkParser(input,output, 257))

    def test_number_58(self):
        input = r"""
            Function: main
                Body: 
                    While a>b Do
                        While b<c Do 
                            b=b+1; 
                        EndWhile. 
                        Break; 
                    EndWhile. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                258,
            )
        )

    def test_number_59(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                259,
            )
        )

    def test_number_60(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                260,
            )
        )

    def test_number_61(self):
        input = r"""
            Function: main 
                Body: 
                    Do 

                    While x<100 EndDo. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                261,
            )
        )

    def test_number_62(self):
        input = r"""
            Function: empty 
                Body: 
                    Do 
                        Do 
                            a=(a-b)+c*2; 
                        While x>50 EndDo. 
                    While x<100 EndDo. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                262,
            )
        )

    def test_number_63(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                263,
            )
        )

    def test_number_64(self):
        input = r"""
            Function: empty 
                Body: 
                    Do 
                    
                    While a<1 EndDo. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                264,
            )
        )

    def test_number_65(self):
        input = r"""
            Var: bb_me; 
            Function: main 
                Body: 
                    Var: a,b,c; 
                    If a>b Then 
                        Var: d; 
                        Return; 
                    EndIf. 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                265,
            )
        )

    def test_number_66(self):
        input = r"""
            Function: main 
                Body: 
                    a(1); 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                266,
            )
        )

    def test_number_67(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                267,
            )
        )

    def test_number_68(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                268,
            )
        )

    def test_number_69(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                269,
            )
        )

    def test_number_70(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                270,
            )
        )


    def test_number_71(self):
        input = r"""
            Function: main 
                Body: 
                    Return(1+2*3); 
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 271
            )
        )

    def test_number_72(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                272,
            )
        )

    def test_number_73(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                273,
            )
        )

    def test_number_74(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                274,
            )
        )

    def test_number_75(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                275,
            )
        )

    def test_number_76(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                276,
            )
        )

    def test_number_77(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                277,
            )
        )

    def test_number_78(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                278,
            )
        )

    def test_number_79(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                279,
            )
        )

    def test_number_80(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                280
            )
        )

    def test_number_81(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                281,
            )
        )

    def test_number_82(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                282,
            )
        )

    def test_number_83(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                283,
            )
        )

    def test_number_84(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                284,
            )
        )

    def test_number_85(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                285,
            )
        )

    def test_number_86(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                286,
            )
        )

    def test_number_87(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                287
            )
        )

    def test_number_88(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                288,
            )
        )

    def test_number_89(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                289
            )
        )

    def test_number_90(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                290,
            )
        )

    def test_number_91(self):
        input = r"""
            Function: main 
                Body: 
                    f(a-b++d); 
                EndBody.
        """
        output = r"""Error on line 4 col 26: +"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                291,
            )
        )

    def test_number_92(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                292,
            )
        )

    def test_number_93(self):
        input = r"""
            Function: main 
                Body: 
                    a=b[True==False+2] + a + "aaa";  
                EndBody.
        """
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                293,
            )
        )

    def test_number_94(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,output, 294
            )
        )

    def test_number_95(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                295,
            )
        )

    def test_number_96(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                296,
            )
        )

    def test_number_97(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                297,
            )
        )

    def test_number_98(self):
        input = r""""""
        output = r"""successful"""
        self.assertTrue(
            TestParser.checkParser(
                input,
                output,
                298,
            )
        )

    def test_number_99(self):
        input = r"""
            Var: a; 
            Function: main 
                Body: 
                    a = {}; 
                EndBody.
        """
        output = r"""Error on line 5 col 25: }"""
        self.assertTrue(
            TestParser.checkParser(
                input, output,
                299,
            )
        )