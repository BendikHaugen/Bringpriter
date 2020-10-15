import xlwt
from xlwt import Workbook

#generate workbook
wb = Workbook()

#Create a sheet, with the first row in the same way as Bring's 'pakke i postkassen'
sheet = wb.add_sheet('Sheet 1')
sheet.write(0,0, 'Name *')
sheet.write(0,1, 'Adress line 1 *')
sheet.write(0,2, 'Adress line 2')
sheet.write(0,3, 'Postal code *')
sheet.write(0,4, 'Contact person')
sheet.write(0,5, 'Mobile number *')
sheet.write(0,6, 'E-mail *')
sheet.write(0,7, "Sender's reference")
sheet.write(0,8, "Recipient's reference")
sheet.write(0,9, 'Bag on Door (yes/no)')

#Saves the test
wb.save('test.xls')
