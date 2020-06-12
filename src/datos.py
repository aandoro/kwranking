import openpyxl

def exportar_resultados_a_xlsx(keywords):
    wb = openpyxl.Workbook()
    hoja = wb.active
    hoja.append(('Keywords', 'Posición'))
    
    for keyword in keywords:
        hoja.append(keyword)
    
    wb.save('keywords.xlsx')