# -------------------- Word操作 --------------------
from docx import Document
from docx.shared import Cm, Pt
from docx.document import Document as Doc


def create_doc(filename):
    # 创建Doc对象
    document = Document()
    # 添加标题, 数字0是标题的意思 level
    document.add_heading("Kino's Journey", 0)

    document.save(filename)


def main():
    create_doc('Kino.docx')
    pass


if __name__ == '__main__':
    main()
