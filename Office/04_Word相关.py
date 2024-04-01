# -------------------- Word操作 --------------------
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.document import Document as Doc


# -------------------- 写操作 --------------------
def create_doc(filename):
    # 创建Doc对象
    document = Document()
    # 添加标题, 数字0是标题的意思 level
    document.add_heading("Kino's Journey", 0)

    # 添加段落
    p = document.add_paragraph("無理矢理他の人と")
    # 声明一个列表
    bold_list = []
    # 往段落中追加内容,并返回追加的对象 我们可以通过修改该对象的属性值来决定文本的样式
    run = p.add_run("同じように")
    # 因为我想要这些文本的样式都统一是 加粗 + 绿色; 如果每次都逐个设置的话就会出现很多重复代码
    # 所以先将他们收集到列表中,最后统一进行修改
    bold_list.append(run)
    p.add_run('大人になるのではなく、')
    # 将需要修改的对象加入列表
    bold_list.append(p.add_run('速度'))
    p.add_run('や')
    bold_list.append(p.add_run('順番'))
    p.add_run('はバラバラでも、')
    bold_list.append(p.add_run('自分自身'))
    p.add_run('納得する方法で、自分自身納得する、納得できる')
    bold_list.append(p.add_run('大人になる'))
    p.add_run('。')

    # 遍历bold_list 对每一个对象都进行 加粗 + 修改颜色的操作
    for run in bold_list:
        run.font.bold = True
        run.font.color.rgb = RGBColor(46, 139, 87)

    document.save(filename)

    # 添加一级标题
    document.add_heading('人の痛みが分かる国')
    document.add_paragraph()
    document.add_paragraph('',style='Intense Quote')


def main():
    create_doc('./testFile/Kino.docx')
    pass


if __name__ == '__main__':
    main()
