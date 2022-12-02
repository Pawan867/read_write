
import xlwt
from xlwt import Workbook


wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, '1')
sheet1.write(2, 0, '2')
sheet1.write(3, 0, '3')
sheet1.write(4, 0, '4')

sheet1.write(0, 1, 'name')
sheet1.write(0, 2, 'job')
sheet1.write(0, 3, 'salary')
sheet1.write(0, 4, 'age')

sheet1.write(1, 1, 'pawan')
sheet1.write(2, 1, 'air')
sheet1.write(3, 1, 'sameer')
sheet1.write(4, 1, 'hawa')

wb.save('salary1.xls')
