from tkinter import *
from db import *


class Gui:

    def __init__(self):
        self.window = Tk()
        self.window.title('BookStore by Maciek')
        self.backend = Backend()

    def get_selected_row(self, event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def create_label(self, text, row, column):
        name = Label(self.window, text=text)
        name.grid(row=row, column=column)
        return name

    def create_entry(self, variable, row, column):
        name = Entry(self.window, textvariable=variable)
        name.grid(row=row, column=column)
        return name

    def create_button(self, text, row, column, cmd=None):
        name = Button(self.window, text=text, width=12, command=cmd)
        name.grid(row=row, column=column)
        return name

    def view_command(self):
        self.list1.delete(0, END)
        [self.list1.insert(END, row) for row in self.backend.view()]

    def search_command(self):
        self.list1.delete(0, END)
        [self.list1.insert(END, row) for row in
         self.backend.search(self.title_text.get(), self.author_text.get(),
                             self.year_text.get(), self.isbn_text.get())]

    def add_command(self):
        self.backend.insert(self.title_text.get(), self.author_text.get(),
                            self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(),
                                self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        self.backend.delete(self.selected_tuple[0])
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

    def update_command(self):
        self.backend.update(self.selected_tuple[0], self.title_text.get(),
                            self.author_text.get(), self.year_text.get(),
                            self.isbn_text.get())

    def main(self):
        l1 = self.create_label('Title', 0, 0)
        l2 = self.create_label('Author', 0, 2)
        l3 = self.create_label('Year', 1, 0)
        l4 = self.create_label('ISBN', 1, 2)
        self.title_text = StringVar()
        self.author_text = StringVar()
        self.year_text = StringVar()
        self.isbn_text = StringVar()
        self.e1 = self.create_entry(self.title_text, 0, 1)
        self.e2 = self.create_entry(self.author_text, 0, 3)
        self.e3 = self.create_entry(self.year_text, 1, 1)
        self.e4 = self.create_entry(self.isbn_text, 1, 3)

        b1 = self.create_button('View all', 2, 3, self.view_command)
        b2 = self.create_button('Search entry', 3, 3, self.search_command)
        b3 = self.create_button('Add entry', 4, 3, self.add_command)
        b4 = self.create_button('Update selected', 5, 3, self.update_command)
        b5 = self.create_button('Delete selected', 6, 3, self.delete_command)
        b6 = self.create_button('Close', 7, 3, self.window.destroy)

        self.list1 = Listbox(self.window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)
        sb1 = Scrollbar(self.window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)
        self.window.mainloop()


if __name__ == '__main__':
    Gui().main()
