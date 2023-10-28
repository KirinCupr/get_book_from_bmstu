from weasyprint import HTML #for getting .xhtml page and convert it to pdf
from pypdf import PdfMerger #for merging pdf's
from os import remove

def get_string_number(number):
    string_num = '000' + str(number)
    return string_num[-4:]

def convert_to_pdf(first_part, count_of_pages):
    pdfs = []
    prefix = ".xhtml"
    # change first value later
    for i in range(1, count_of_pages+1):
        try:
            pdf = HTML(first_part + get_string_number(i) + prefix).write_pdf()
            open(get_string_number(i) + '.pdf', 'wb').write(pdf)
            pdfs.append(get_string_number(i) + '.pdf')
            print("Itteration - " + str(i))
        except ValueError:        
            print("Oops!  That was no valid number.  Try again... (У меня лапки)")
            print("Itteration - " + str(i) + " failed(( (Не судьба, в следующий раз)")
            continue
    return pdfs
    
def make_merged_pdf(name, pdfs):
    result = PdfMerger()
    for pdf in pdfs:
        result.append(pdf)

    result.write(name + ".pdf")
    result.close()

def delete_temp_files(count_of_pages):
    for i in range(1, count_of_pages+1):
        remove(get_string_number(i) + '.pdf')

first_part = input("Вставьте ссылку в форме 'https:// .. /OEBPS/mybook': ")
name = input("Введите название документа (тип создаваемого файла - .pdf): ")
count_of_pages = int(input("Введите количество страниц (целое, положительное число): "))

pdfs = convert_to_pdf(first_part, count_of_pages)
make_merged_pdf(name, pdfs)
delete_temp_files(count_of_pages)

print("Документ - ", name, ".pdf создан!")
input("Нажмите клавишу для выхода (клавишу, а не кнопку выключения, балда)")
