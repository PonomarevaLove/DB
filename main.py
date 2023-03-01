import tkinter
import tkinter.messagebox
import sqlite3

class EmployeeDetails:
    def __init__(self):
        # Создать главное окно
        self.main_window = tkinter.Tk()

        #Скомпановать содержимое главного окна
        self.__build_main_window()

        #Запустить главный цикл
        tkinter.mainloop()

    def __build_main_window(self):
        #Создать надпись с подсказкой для пользователя
        self.__create_promt_label()

        # Скомпоновать рамку виджета
        self.__build_listbox_frame()

        # Создать кнопку выйти
        self.__reate_quit_button()

    def __create_promt_label(self):
        self.employee_promt_label = tkinter.Label(self.main_window, text=' Выберите сотрудника')
        self.employee_promt_label.pack(side='top', padx=5, pady=5)
    def __build_listbox_frame(self):
        pass
    def __create_quit_button(self):
        pass

    def __build_listbox_frame(self):
        # создание рамки
        self.listbox_frame = tkinter.Frame(self.main_window)
        #настроить виджет
        self.__setup_listbox()
        # создать полосу прокрутки
        self.__create_scrollbar()
        # заполнить виджет
        self.__populate_listbox()
        # упаковать рамку виджета
        self.listbox_frame.pack()

    def __setup_listbox(self):
        #Создать виджет Listbox
        self.employee_listbox = tkinter.Listbox(self.listbox_frame, selectmode=tkinter.SINGLE, height=6)
        #
        self.employee_listboxj



        #
