# Principles of Programming Languages

## Giới Thiệu

**Nguyên lý Ngôn ngữ Lập trình (PPL)** là một trong những môn khó nhất trong toàn bộ chương trình đào tạo ngành Khoa học máy tính của Bách Khoa. Mục đích của các bài tập lớn ở môn này chính là xây dựng một trình biên dịch (compiler) cho một ngôn ngữ được đặc tả riêng biệt bởi các giảng viên trong trường và luôn được thay thế sau mỗi kỳ học 😭.

Ở học kỳ này, sinh viên được yêu cầu xây dựng compiler cho ngôn ngữ BKIT được đặc tả theo file BKIT2009 Specification-2.2.pdf.

## Cấu Trúc Thư Mục

Thư mục slides chứa các slide được dùng để giảng dạy môn này.

3 thư mực còn lại gồm 3 phases tương ứng với 3 assignments, bao gồm:

- Phase 1: Xây dựng Lexer và Parser, truy cập ở thư mục assignment1
    - assignment1/initial/src/main/bkit/parser/BKIT.g4
    - assignment1/initial/src/test/LexerSuite.py
    - assignment1/initial/src/test/ParserSuite.py
    
- Phase 2: Xây dựng ASTGenerator, truy cập ở thư mục assignment2
    - assignment2\initial\src\main\bkit\astgen\ASTGeneration.py
    - assignment2\initial\src\test\ASTGenSuite.py
    
- Phase 3: Xây dựng Static Checker, truy cập ở thư mục assignment3
    - assignment3\initial\src\main\bkit\checker\StaticCheck.py
    - assignment3\initial\src\test\CheckSuite.py

- Phase 4: Xây dựng Code Generator (chưa hoàn thành)
## Lưu Ý

Nên sử dụng **PyCharm** để hiện thực assignment 3 vì **VS Code** có thể bị lỗi không so khớp kiểu sử dụng hàm `type` hoặc `isinstance` được vì sự sai khác giữa relative path của **VS Code** (**VS Code** sẽ nhận dạng `bkits.utils.x` và `x` là 2 kiểu khác nhau).
