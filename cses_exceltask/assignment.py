import openpyxl
import re
#Open "train.xlsx" file and open "train" sheet
open_workbook=openpyxl.load_workbook('./train.xlsx')
work_sheet=open_workbook['train']

#Make new excel file and create 4 sheets
new_workbook=openpyxl.Workbook()
new_worksheet_Mr=new_workbook.active
new_worksheet_Mr.title='남성'
for i in range(1,12+1):
    new_worksheet_Mr.cell(row=1,column=i).value=work_sheet.cell(row=1,column=i).value

new_worksheet_Miss=new_workbook.create_sheet('미혼여성')
for i in range(1,12+1):
    new_worksheet_Miss.cell(row=1,column=i).value=work_sheet.cell(row=1,column=i).value

new_worksheet_Mrs=new_workbook.create_sheet('기혼여성')
for i in range(1,12+1):
    new_worksheet_Mrs.cell(row=1,column=i).value=work_sheet.cell(row=1,column=i).value

new_worksheet_Others=new_workbook.create_sheet('기타')
for i in range(1,12+1):
    new_worksheet_Others.cell(row=1,column=i).value=work_sheet.cell(row=1,column=i).value


#Classify the gender data in "train.xlsx" and push each data(row) to the corresponding sheet in the new excel file
pattern=re.compile('[A-Za-z]+\.')
for each_row in work_sheet.rows:
    if len(pattern.findall(each_row[3].value))>0:
        if pattern.findall(each_row[3].value)[0]=='Mr.':
            new_worksheet_Mr.append([cell.value for cell in each_row])
        elif pattern.findall(each_row[3].value)[0]=='Miss.':
            new_worksheet_Miss.append([cell.value for cell in each_row])
        elif pattern.findall(each_row[3].value)[0]=='Mrs.':
            new_worksheet_Mrs.append([cell.value for cell in each_row])
        else:
            new_worksheet_Others.append([cell.value for cell in each_row])

open_workbook.close()
new_workbook.save('./assginment.xlsx')
