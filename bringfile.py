import xlwt
from xlwt import Workbook

#generate workbook
wb = Workbook()

'''creates a sheet and sets the fontstyle'''
sheet = wb.add_sheet('Sheet 1')
style = xlwt.easyxf('font: bold 1')

'''fills the first column'''
sheet.write(0,0, 'Name *', style)
sheet.write(0,1, 'Adress line 1 *', style)
sheet.write(0,2, 'Adress line 2', style)
sheet.write(0,3, 'Postal code *', style)
sheet.write(0,4, 'Contact person', style)
sheet.write(0,5, 'Mobile number *', style)
sheet.write(0,6, 'E-mail *', style)
sheet.write(0,7, "Sender's reference", style)
sheet.write(0,8, "Recipient's reference", style)
sheet.write(0,9, 'Bag on Door (yes/no)', style)

#Saves the test
wb.save('test.xls')
