# Generated from e:\ppl\assignment2\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0213\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\5\2\u009e\n\2\3\3\3\3\3\4\3\4\7\4\u00a4")
        buf.write("\n\4\f\4\16\4\u00a7\13\4\3\5\3\5\3\5\3\5\7\5\u00ad\n\5")
        buf.write("\f\5\16\5\u00b0\13\5\3\6\3\6\3\6\3\6\7\6\u00b6\n\6\f\6")
        buf.write("\16\6\u00b9\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u00c5\n\7\3\b\6\b\u00c8\n\b\r\b\16\b\u00c9\3\t")
        buf.write("\3\t\7\t\u00ce\n\t\f\t\16\t\u00d1\13\t\3\n\3\n\5\n\u00d5")
        buf.write("\n\n\3\n\6\n\u00d8\n\n\r\n\16\n\u00d9\3\13\3\13\5\13\u00de")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00ee\n\f\3\r\3\r\3\r\3\r\5\r\u00f4\n\r\3")
        buf.write("\16\3\16\7\16\u00f8\n\16\f\16\16\16\u00fb\13\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\7\17\u0104\n\17\f\17\16\17")
        buf.write("\u0107\13\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3")
        buf.write(":\3;\3;\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\7G\u01e8\nG\fG\16G\u01eb")
        buf.write("\13G\3H\6H\u01ee\nH\rH\16H\u01ef\3H\3H\3I\3I\7I\u01f6")
        buf.write("\nI\fI\16I\u01f9\13I\3I\3I\3I\3I\3I\3J\3J\7J\u0202\nJ")
        buf.write("\fJ\16J\u0205\13J\3J\3J\3K\3K\3K\3K\7K\u020d\nK\fK\16")
        buf.write("K\u0210\13K\3L\3L\4\u0105\u020e\2M\3\3\5\2\7\2\t\2\13")
        buf.write("\2\r\4\17\2\21\2\23\2\25\5\27\2\31\2\33\6\35\7\37\b!\t")
        buf.write("#\n%\13\'\f)\r+\16-\17/\20\61\21\63\22\65\23\67\249\25")
        buf.write(";\26=\27?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"U#W$Y%")
        buf.write("[&]\'_(a)c*e+g,i-k.m/o\60q\61s\62u\63w\64y\65{\66}\67")
        buf.write("\1778\u00819\u0083:\u0085;\u0087<\u0089=\u008b>\u008d")
        buf.write("?\u008f@\u0091A\u0093B\u0095C\u0097D\3\2\21\3\2\63;\3")
        buf.write("\2\62;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2")
        buf.write("\629\4\2GGgg\4\2--//\7\2\f\f\17\17$$))^^\3\2c|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\t\2))^^ddhhppttvv\2\u0225")
        buf.write("\2\3\3\2\2\2\2\r\3\2\2\2\2\25\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\3\u009d\3\2\2\2\5\u009f\3\2\2\2\7\u00a1\3\2\2\2\t\u00a8")
        buf.write("\3\2\2\2\13\u00b1\3\2\2\2\r\u00c4\3\2\2\2\17\u00c7\3\2")
        buf.write("\2\2\21\u00cb\3\2\2\2\23\u00d2\3\2\2\2\25\u00dd\3\2\2")
        buf.write("\2\27\u00ed\3\2\2\2\31\u00f3\3\2\2\2\33\u00f5\3\2\2\2")
        buf.write("\35\u00ff\3\2\2\2\37\u010d\3\2\2\2!\u0112\3\2\2\2#\u0117")
        buf.write("\3\2\2\2%\u011e\3\2\2\2\'\u0121\3\2\2\2)\u0125\3\2\2\2")
        buf.write("+\u012b\3\2\2\2-\u0131\3\2\2\2/\u0138\3\2\2\2\61\u0141")
        buf.write("\3\2\2\2\63\u014b\3\2\2\2\65\u0151\3\2\2\2\67\u015a\3")
        buf.write("\2\2\29\u0162\3\2\2\2;\u0166\3\2\2\2=\u016d\3\2\2\2?\u0172")
        buf.write("\3\2\2\2A\u0175\3\2\2\2C\u017b\3\2\2\2E\u0184\3\2\2\2")
        buf.write("G\u0189\3\2\2\2I\u018f\3\2\2\2K\u0191\3\2\2\2M\u0194\3")
        buf.write("\2\2\2O\u0196\3\2\2\2Q\u0199\3\2\2\2S\u019b\3\2\2\2U\u019e")
        buf.write("\3\2\2\2W\u01a0\3\2\2\2Y\u01a3\3\2\2\2[\u01a5\3\2\2\2")
        buf.write("]\u01a7\3\2\2\2_\u01aa\3\2\2\2a\u01ad\3\2\2\2c\u01b0\3")
        buf.write("\2\2\2e\u01b3\3\2\2\2g\u01b5\3\2\2\2i\u01b7\3\2\2\2k\u01ba")
        buf.write("\3\2\2\2m\u01bd\3\2\2\2o\u01c1\3\2\2\2q\u01c4\3\2\2\2")
        buf.write("s\u01c7\3\2\2\2u\u01cb\3\2\2\2w\u01cf\3\2\2\2y\u01d1\3")
        buf.write("\2\2\2{\u01d3\3\2\2\2}\u01d5\3\2\2\2\177\u01d7\3\2\2\2")
        buf.write("\u0081\u01d9\3\2\2\2\u0083\u01db\3\2\2\2\u0085\u01dd\3")
        buf.write("\2\2\2\u0087\u01df\3\2\2\2\u0089\u01e1\3\2\2\2\u008b\u01e3")
        buf.write("\3\2\2\2\u008d\u01e5\3\2\2\2\u008f\u01ed\3\2\2\2\u0091")
        buf.write("\u01f3\3\2\2\2\u0093\u01ff\3\2\2\2\u0095\u0208\3\2\2\2")
        buf.write("\u0097\u0211\3\2\2\2\u0099\u009e\5\5\3\2\u009a\u009e\5")
        buf.write("\7\4\2\u009b\u009e\5\t\5\2\u009c\u009e\5\13\6\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009a\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\4\3\2\2\2\u009f\u00a0\7\62")
        buf.write("\2\2\u00a0\6\3\2\2\2\u00a1\u00a5\t\2\2\2\u00a2\u00a4\t")
        buf.write("\3\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\b\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a8\u00a9\7\62\2\2\u00a9\u00aa\t\4\2\2\u00aa")
        buf.write("\u00ae\t\5\2\2\u00ab\u00ad\t\6\2\2\u00ac\u00ab\3\2\2\2")
        buf.write("\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3")
        buf.write("\2\2\2\u00af\n\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2")
        buf.write("\7\62\2\2\u00b2\u00b3\t\7\2\2\u00b3\u00b7\t\b\2\2\u00b4")
        buf.write("\u00b6\t\t\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\f\3\2\2")
        buf.write("\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb\5\17\b\2\u00bb\u00bc")
        buf.write("\5\21\t\2\u00bc\u00bd\5\23\n\2\u00bd\u00c5\3\2\2\2\u00be")
        buf.write("\u00bf\5\17\b\2\u00bf\u00c0\5\21\t\2\u00c0\u00c5\3\2\2")
        buf.write("\2\u00c1\u00c2\5\17\b\2\u00c2\u00c3\5\23\n\2\u00c3\u00c5")
        buf.write("\3\2\2\2\u00c4\u00ba\3\2\2\2\u00c4\u00be\3\2\2\2\u00c4")
        buf.write("\u00c1\3\2\2\2\u00c5\16\3\2\2\2\u00c6\u00c8\t\3\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\20\3\2\2\2\u00cb\u00cf\7\60")
        buf.write("\2\2\u00cc\u00ce\t\3\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\22\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d4\t\n\2\2\u00d3")
        buf.write("\u00d5\t\13\2\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2")
        buf.write("\2\u00d5\u00d7\3\2\2\2\u00d6\u00d8\t\3\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\24\3\2\2\2\u00db\u00de\5=\37\2\u00dc")
        buf.write("\u00de\5G$\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\26\3\2\2\2\u00df\u00e0\7^\2\2\u00e0\u00ee\7)\2\2\u00e1")
        buf.write("\u00e2\7^\2\2\u00e2\u00ee\7^\2\2\u00e3\u00e4\7^\2\2\u00e4")
        buf.write("\u00ee\7d\2\2\u00e5\u00e6\7^\2\2\u00e6\u00ee\7h\2\2\u00e7")
        buf.write("\u00e8\7^\2\2\u00e8\u00ee\7p\2\2\u00e9\u00ea\7^\2\2\u00ea")
        buf.write("\u00ee\7t\2\2\u00eb\u00ec\7^\2\2\u00ec\u00ee\7v\2\2\u00ed")
        buf.write("\u00df\3\2\2\2\u00ed\u00e1\3\2\2\2\u00ed\u00e3\3\2\2\2")
        buf.write("\u00ed\u00e5\3\2\2\2\u00ed\u00e7\3\2\2\2\u00ed\u00e9\3")
        buf.write("\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\30\3\2\2\2\u00ef\u00f4")
        buf.write("\n\f\2\2\u00f0\u00f4\5\27\f\2\u00f1\u00f2\7)\2\2\u00f2")
        buf.write("\u00f4\7$\2\2\u00f3\u00ef\3\2\2\2\u00f3\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f4\32\3\2\2\2\u00f5\u00f9\7$\2")
        buf.write("\2\u00f6\u00f8\5\31\r\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\7$\2\2")
        buf.write("\u00fd\u00fe\b\16\2\2\u00fe\34\3\2\2\2\u00ff\u0100\7,")
        buf.write("\2\2\u0100\u0101\7,\2\2\u0101\u0105\3\2\2\2\u0102\u0104")
        buf.write("\13\2\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0108\u0109\7,\2\2\u0109\u010a\7")
        buf.write(",\2\2\u010a\u010b\3\2\2\2\u010b\u010c\b\17\3\2\u010c\36")
        buf.write("\3\2\2\2\u010d\u010e\7D\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7f\2\2\u0110\u0111\7{\2\2\u0111 \3\2\2\2\u0112\u0113")
        buf.write("\7G\2\2\u0113\u0114\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116")
        buf.write("\7g\2\2\u0116\"\3\2\2\2\u0117\u0118\7G\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7f\2\2\u011a\u011b\7H\2\2\u011b\u011c")
        buf.write("\7q\2\2\u011c\u011d\7t\2\2\u011d$\3\2\2\2\u011e\u011f")
        buf.write("\7K\2\2\u011f\u0120\7h\2\2\u0120&\3\2\2\2\u0121\u0122")
        buf.write("\7X\2\2\u0122\u0123\7c\2\2\u0123\u0124\7t\2\2\u0124(\3")
        buf.write("\2\2\2\u0125\u0126\7G\2\2\u0126\u0127\7p\2\2\u0127\u0128")
        buf.write("\7f\2\2\u0128\u0129\7F\2\2\u0129\u012a\7q\2\2\u012a*\3")
        buf.write("\2\2\2\u012b\u012c\7D\2\2\u012c\u012d\7t\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e\u012f\7c\2\2\u012f\u0130\7m\2\2\u0130,\3")
        buf.write("\2\2\2\u0131\u0132\7G\2\2\u0132\u0133\7n\2\2\u0133\u0134")
        buf.write("\7u\2\2\u0134\u0135\7g\2\2\u0135\u0136\7K\2\2\u0136\u0137")
        buf.write("\7h\2\2\u0137.\3\2\2\2\u0138\u0139\7G\2\2\u0139\u013a")
        buf.write("\7p\2\2\u013a\u013b\7f\2\2\u013b\u013c\7Y\2\2\u013c\u013d")
        buf.write("\7j\2\2\u013d\u013e\7k\2\2\u013e\u013f\7n\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\60\3\2\2\2\u0141\u0142\7R\2\2\u0142\u0143")
        buf.write("\7c\2\2\u0143\u0144\7t\2\2\u0144\u0145\7c\2\2\u0145\u0146")
        buf.write("\7o\2\2\u0146\u0147\7g\2\2\u0147\u0148\7v\2\2\u0148\u0149")
        buf.write("\7g\2\2\u0149\u014a\7t\2\2\u014a\62\3\2\2\2\u014b\u014c")
        buf.write("\7Y\2\2\u014c\u014d\7j\2\2\u014d\u014e\7k\2\2\u014e\u014f")
        buf.write("\7n\2\2\u014f\u0150\7g\2\2\u0150\64\3\2\2\2\u0151\u0152")
        buf.write("\7E\2\2\u0152\u0153\7q\2\2\u0153\u0154\7p\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155\u0156\7k\2\2\u0156\u0157\7p\2\2\u0157\u0158")
        buf.write("\7w\2\2\u0158\u0159\7g\2\2\u0159\66\3\2\2\2\u015a\u015b")
        buf.write("\7G\2\2\u015b\u015c\7p\2\2\u015c\u015d\7f\2\2\u015d\u015e")
        buf.write("\7D\2\2\u015e\u015f\7q\2\2\u015f\u0160\7f\2\2\u0160\u0161")
        buf.write("\7{\2\2\u01618\3\2\2\2\u0162\u0163\7H\2\2\u0163\u0164")
        buf.write("\7q\2\2\u0164\u0165\7t\2\2\u0165:\3\2\2\2\u0166\u0167")
        buf.write("\7T\2\2\u0167\u0168\7g\2\2\u0168\u0169\7v\2\2\u0169\u016a")
        buf.write("\7w\2\2\u016a\u016b\7t\2\2\u016b\u016c\7p\2\2\u016c<\3")
        buf.write("\2\2\2\u016d\u016e\7V\2\2\u016e\u016f\7t\2\2\u016f\u0170")
        buf.write("\7w\2\2\u0170\u0171\7g\2\2\u0171>\3\2\2\2\u0172\u0173")
        buf.write("\7F\2\2\u0173\u0174\7q\2\2\u0174@\3\2\2\2\u0175\u0176")
        buf.write("\7G\2\2\u0176\u0177\7p\2\2\u0177\u0178\7f\2\2\u0178\u0179")
        buf.write("\7K\2\2\u0179\u017a\7h\2\2\u017aB\3\2\2\2\u017b\u017c")
        buf.write("\7H\2\2\u017c\u017d\7w\2\2\u017d\u017e\7p\2\2\u017e\u017f")
        buf.write("\7e\2\2\u017f\u0180\7v\2\2\u0180\u0181\7k\2\2\u0181\u0182")
        buf.write("\7q\2\2\u0182\u0183\7p\2\2\u0183D\3\2\2\2\u0184\u0185")
        buf.write("\7V\2\2\u0185\u0186\7j\2\2\u0186\u0187\7g\2\2\u0187\u0188")
        buf.write("\7p\2\2\u0188F\3\2\2\2\u0189\u018a\7H\2\2\u018a\u018b")
        buf.write("\7c\2\2\u018b\u018c\7n\2\2\u018c\u018d\7u\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018eH\3\2\2\2\u018f\u0190\7-\2\2\u0190J\3\2\2")
        buf.write("\2\u0191\u0192\7-\2\2\u0192\u0193\7\60\2\2\u0193L\3\2")
        buf.write("\2\2\u0194\u0195\7/\2\2\u0195N\3\2\2\2\u0196\u0197\7/")
        buf.write("\2\2\u0197\u0198\7\60\2\2\u0198P\3\2\2\2\u0199\u019a\7")
        buf.write(",\2\2\u019aR\3\2\2\2\u019b\u019c\7,\2\2\u019c\u019d\7")
        buf.write("\60\2\2\u019dT\3\2\2\2\u019e\u019f\7^\2\2\u019fV\3\2\2")
        buf.write("\2\u01a0\u01a1\7^\2\2\u01a1\u01a2\7\60\2\2\u01a2X\3\2")
        buf.write("\2\2\u01a3\u01a4\7\'\2\2\u01a4Z\3\2\2\2\u01a5\u01a6\7")
        buf.write("#\2\2\u01a6\\\3\2\2\2\u01a7\u01a8\7(\2\2\u01a8\u01a9\7")
        buf.write("(\2\2\u01a9^\3\2\2\2\u01aa\u01ab\7~\2\2\u01ab\u01ac\7")
        buf.write("~\2\2\u01ac`\3\2\2\2\u01ad\u01ae\7?\2\2\u01ae\u01af\7")
        buf.write("?\2\2\u01afb\3\2\2\2\u01b0\u01b1\7#\2\2\u01b1\u01b2\7")
        buf.write("?\2\2\u01b2d\3\2\2\2\u01b3\u01b4\7>\2\2\u01b4f\3\2\2\2")
        buf.write("\u01b5\u01b6\7@\2\2\u01b6h\3\2\2\2\u01b7\u01b8\7>\2\2")
        buf.write("\u01b8\u01b9\7?\2\2\u01b9j\3\2\2\2\u01ba\u01bb\7@\2\2")
        buf.write("\u01bb\u01bc\7?\2\2\u01bcl\3\2\2\2\u01bd\u01be\7?\2\2")
        buf.write("\u01be\u01bf\7\61\2\2\u01bf\u01c0\7?\2\2\u01c0n\3\2\2")
        buf.write("\2\u01c1\u01c2\7>\2\2\u01c2\u01c3\7\60\2\2\u01c3p\3\2")
        buf.write("\2\2\u01c4\u01c5\7@\2\2\u01c5\u01c6\7\60\2\2\u01c6r\3")
        buf.write("\2\2\2\u01c7\u01c8\7>\2\2\u01c8\u01c9\7?\2\2\u01c9\u01ca")
        buf.write("\7\60\2\2\u01cat\3\2\2\2\u01cb\u01cc\7@\2\2\u01cc\u01cd")
        buf.write("\7?\2\2\u01cd\u01ce\7\60\2\2\u01cev\3\2\2\2\u01cf\u01d0")
        buf.write("\7?\2\2\u01d0x\3\2\2\2\u01d1\u01d2\7*\2\2\u01d2z\3\2\2")
        buf.write("\2\u01d3\u01d4\7+\2\2\u01d4|\3\2\2\2\u01d5\u01d6\7]\2")
        buf.write("\2\u01d6~\3\2\2\2\u01d7\u01d8\7_\2\2\u01d8\u0080\3\2\2")
        buf.write("\2\u01d9\u01da\7<\2\2\u01da\u0082\3\2\2\2\u01db\u01dc")
        buf.write("\7\60\2\2\u01dc\u0084\3\2\2\2\u01dd\u01de\7.\2\2\u01de")
        buf.write("\u0086\3\2\2\2\u01df\u01e0\7=\2\2\u01e0\u0088\3\2\2\2")
        buf.write("\u01e1\u01e2\7}\2\2\u01e2\u008a\3\2\2\2\u01e3\u01e4\7")
        buf.write("\177\2\2\u01e4\u008c\3\2\2\2\u01e5\u01e9\t\r\2\2\u01e6")
        buf.write("\u01e8\t\16\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2")
        buf.write("\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u008e")
        buf.write("\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ee\t\17\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2")
        buf.write("\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\b")
        buf.write("H\3\2\u01f2\u0090\3\2\2\2\u01f3\u01f7\7$\2\2\u01f4\u01f6")
        buf.write("\5\31\r\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2")
        buf.write("\u01f9\u01f7\3\2\2\2\u01fa\u01fb\7^\2\2\u01fb\u01fc\n")
        buf.write("\20\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\bI\4\2\u01fe\u0092")
        buf.write("\3\2\2\2\u01ff\u0203\7$\2\2\u0200\u0202\5\31\r\2\u0201")
        buf.write("\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0206\u0207\bJ\5\2\u0207\u0094\3\2\2\2\u0208\u0209")
        buf.write("\7,\2\2\u0209\u020a\7,\2\2\u020a\u020e\3\2\2\2\u020b\u020d")
        buf.write("\13\2\2\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u020f\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0096\3\2\2\2")
        buf.write("\u0210\u020e\3\2\2\2\u0211\u0212\13\2\2\2\u0212\u0098")
        buf.write("\3\2\2\2\26\2\u009d\u00a5\u00ae\u00b7\u00c4\u00c9\u00cf")
        buf.write("\u00d4\u00d9\u00dd\u00ed\u00f3\u00f9\u0105\u01e9\u01ef")
        buf.write("\u01f7\u0203\u020e\6\3\16\2\b\2\2\3I\3\3J\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_LIT = 1
    FLOAT_LIT = 2
    BOOL_LIT = 3
    STRING_LIT = 4
    COMMENT = 5
    BODY = 6
    ELSE = 7
    ENDFOR = 8
    IF = 9
    VAR = 10
    ENDDO = 11
    BREAK = 12
    ELSEIF = 13
    ENDWHILE = 14
    PARAM = 15
    WHILE = 16
    CONTINUE = 17
    ENDBODY = 18
    FOR = 19
    RETURN = 20
    TRUE = 21
    DO = 22
    ENDIF = 23
    FUNC = 24
    THEN = 25
    FALSE = 26
    ADD = 27
    FADD = 28
    SIGN = 29
    FSIGN = 30
    MUL = 31
    FMUL = 32
    DIV = 33
    FDIV = 34
    MOD = 35
    NOT = 36
    AND = 37
    OR = 38
    ISEQUAL = 39
    ISDIF = 40
    SMALLER = 41
    BIGGER = 42
    EQUALORSMALLER = 43
    EQUALORBIGGER = 44
    FISDIF = 45
    FSMALLER = 46
    FBIGGER = 47
    FEQUALORSMALLER = 48
    FEQUALORBIGGER = 49
    ASSIGN = 50
    LB = 51
    RB = 52
    LS = 53
    RS = 54
    COLON = 55
    DOT = 56
    COMMA = 57
    SEMI = 58
    LC = 59
    RC = 60
    ID = 61
    WS = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    UNTERMINATED_COMMENT = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
            "'EndIf'", "'Function'", "'Then'", "'False'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'='", "'('", "')'", 
            "'['", "']'", "':'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "COMMENT", 
            "BODY", "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", 
            "ENDWHILE", "PARAM", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
            "RETURN", "TRUE", "DO", "ENDIF", "FUNC", "THEN", "FALSE", "ADD", 
            "FADD", "SIGN", "FSIGN", "MUL", "FMUL", "DIV", "FDIV", "MOD", 
            "NOT", "AND", "OR", "ISEQUAL", "ISDIF", "SMALLER", "BIGGER", 
            "EQUALORSMALLER", "EQUALORBIGGER", "FISDIF", "FSMALLER", "FBIGGER", 
            "FEQUALORSMALLER", "FEQUALORBIGGER", "ASSIGN", "LB", "RB", "LS", 
            "RS", "COLON", "DOT", "COMMA", "SEMI", "LC", "RC", "ID", "WS", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "INT_LIT", "ZERO", "DEC", "HEX", "OCT", "FLOAT_LIT", "FINT", 
                  "FDEC", "FEXP", "BOOL_LIT", "ESCAPE_SEQUENCE", "CHAR_LIT", 
                  "STRING_LIT", "COMMENT", "BODY", "ELSE", "ENDFOR", "IF", 
                  "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAM", 
                  "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", 
                  "DO", "ENDIF", "FUNC", "THEN", "FALSE", "ADD", "FADD", 
                  "SIGN", "FSIGN", "MUL", "FMUL", "DIV", "FDIV", "MOD", 
                  "NOT", "AND", "OR", "ISEQUAL", "ISDIF", "SMALLER", "BIGGER", 
                  "EQUALORSMALLER", "EQUALORBIGGER", "FISDIF", "FSMALLER", 
                  "FBIGGER", "FEQUALORSMALLER", "FEQUALORBIGGER", "ASSIGN", 
                  "LB", "RB", "LS", "RS", "COLON", "DOT", "COMMA", "SEMI", 
                  "LC", "RC", "ID", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.STRING_LIT_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.strip('"')
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('"','',1)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('"','',1)
     


