def excel(duong dan)
    import xlrd
    book = xlrd.open_workbook(duongdan)
    first_sheet = book.sheet_by_index(0)
    dauvao_list=[]
    for i in ran
