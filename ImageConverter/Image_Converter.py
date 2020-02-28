from tkinter import *
from ImageConverterFunctions import convert


window = Tk(screenName='Image Converter',
            baseName='Image Converter', className='Image Converter')
window.geometry('800x250')
Title_label1 = Label(window, text='******Image Converter is a tool for taking several image files located in a folder(.jpg, .png, .tiff, etc)******\n and combining them into a single word document(docx) file.',
                     justify=CENTER)


Title_label2 = Label(window, text='''Simply enter the path to the folder containing the image files you wish transcriped and Image\n Converter will take each image file and write the name of the file as well as\n paste the image to a single page of the word doc per image file.''', justify=CENTER)


Title_label3 = Label(
    window, text='The .docx end product will be placed in the output path location. The file name will include the the current date and will default to it if no name is given.''', justify=CENTER)

Path_label = Label(window, text='Path')
Path_entry = Entry(window)

File_Name = Label(window, text='File Name')
File_Name_Entry = Entry(window)


def Convert_Button():
    PathFile = Path_entry.get()
    FileName = File_Name_Entry.get()
    convert(PathFile, FileName)


Convert_Button = Button(
    window, text='Convert Images to docx', command=Convert_Button)


Title_label1.pack()
Title_label2.pack()
Title_label3.pack()

Path_label.pack()
Path_entry.pack(fill=X)

File_Name.pack()
File_Name_Entry.pack(fill=X)

Convert_Button.pack()
window.mainloop()
