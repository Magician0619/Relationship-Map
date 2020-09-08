# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import re

def parsePDFtoTXT(pdf_path):
    fp = open(pdf_path, 'rb')
    parser = PDFParser(fp)
    document= PDFDocument(parser)
    # parser.set_document(document)
    # document.set_parser(parser)
    # document.initialize()
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr=PDFResourceManager()
        laparams=LAParams()
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        # for page in document.get_pages():
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout=device.get_result()
            # print(layout)
            output=str(layout)
            for x in layout:
                if (isinstance(x,LTTextBoxHorizontal)):
                    text=x.get_text()
                    output+=text
            with open('pdfoutput.txt','a',encoding='utf-8') as f:
                f.write(output)
def sentence():
    restr = 'XXX第四五七医院，创建于1950年12月。位于武汉市江岸区工农兵路15号，占地15万平方米。'
    pattern = re.compile('[，。][^，。]*占地[^，。]*[，。]')
    search = re.search(restr)
    print(search)

def people(txt):
    content = []
    with open(txt, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            content.append(line.replace("\n",""))
    print(content)
    return content

def get_word_page(txt):
    word_list=people(txt)
    f=open('pdfoutput.txt',encoding='utf-8')
    text_list=f.read().split('<LTPage')
    n=len(text_list)
    for w in word_list:
        page_list=[]
        for i in range(1,n):
            if w in text_list[i]:
                # pattern = re.compile('[，。][^，。]*'+w+'[^，。]*[，。]')
                # search = re.search(str(word_list))
                # page_list.append(str(i)+search)
                page_list.append(i)
        with open('result.txt','a',encoding='utf-8') as f:
                f.write(w+str(page_list)+'\n')

if __name__=='__main__':
    # parsePDFtoTXT('ywwq.pdf')
    get_word_page("人名.txt")