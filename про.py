import tkinter
import tkinter.messagebox
import sqlite3

class EmployceDetails:
    def __init__(self):
        #Создать главное окно
        self.main_window = tkinter.Tk()
        #Скомпоновать содержимое главного окна.
        self.__build_main_window()
     #Запустить главный цикл.
        tkinter.mainloop()
        #Скомпоновать главное окно.
    def _＿build_main_window(self) :
        #Создать надпись с подсказкой для пользователя.
        self.＿create_prompt_label()
        #Скомпоновать рамку пиджета
        self.__build_listbox_frame()
        #Создать кнопку Выйти.
        self.__create_quit_button()
        #Создать надпись с подсказкой для пользователя
    def __create_prompt_label(self) :
        self.employee_prompt_label = tkinter.Label(self.main_window, text="Выберите сотрудника")
        self.employee_prompt_label.pack(side="top", padx=5, pady=5)

        #Скомпоновать рамку, содержащую виджеты Listbox и Scrollbar
    def __build_listbox_frame(self):
        #cоздать рамку для виджетов Listbox и Scrollbar.
        self.listbox_frame = tkinter.Frame(self.main_window)
        #Настрить виджет Listbox.
        self.__setup_listbox()
        #Создать полосу прокрутки для просмотра элементов в виджете Listbox.
        self.__create_scrollbar()
        #Заполнить виджет Listbox именами сотрудников.
        self.__populate_listbox()


    def ＿setup_listbox(self):
        #Создать виджет Listbox.
        self.employee_listbox - tkinter.Listbox( self. listbox frame, selectmode tkinter.SINGLE, height=6)
        #Привязать виджет Listbox к функции обратного вызова.
        self. employee_listbox.bindt "<<ListboxSelect>>", self.＿get_details)
        #Создать полосу прокрутки для просмотра элементов в виджете Listbox.
        self.__create_scrollbar()
        #Заполнить виджет Listbox именами сотрудников.
        self.__populate_listbox()
        #Упаковать рамку виджета Listbox.
        self.listbox_frame.pack()
        #Создать виджет Listbox для вывода имен сотрудников на экран.
    def ＿setup listbox(self) :
        #Создать виджет Listbox.
        self.employee_listbox - tkinter.Listboxt
            self.listbox_frame, selectmode=tkinter.SINGLE, height=6)

        #Привязать виджет Listbox к функции обратного вызова.
        self. employee listbox.bindt "<<ListboxSelect>>', self. get_details)
        #Упаковать виджет Listbox.
        self.employee listbox.pack(side="lett", padx=5, pady=5)
        #Создать вертикальный виджет Scrollbar для использования с виджетом Listbox.
    def ＿ create scrollbar(self):
        self.scrollbar tkinter.Scrollbar(self.listbox_frame,
                                          orient=tkinter. VERTICAL)
        self.scrollbar.config (command-self.employee_listbox.yvien)
        self. employee_listbox.configlyscrollcormand-self.scrollbar.set)
        self.scrollbar.pack(side="right", fill=tkinter.Y)
        #Вывести на экран имена сотрудников в виджете Listbox.
    def ＿populate_listbox(self) :
        for employee in self.get employees():
            self.employee listbox.insert(tkinter.END, employee)

        #Создать кнопку выхода из программы.
    def ＿create_quit_button(self) :
        self.quit button - tkinter.Button(
                                    self.main window,
                                    text="Выйти",
                                    command=self.main_window.destroy)
        self.quit button.pack(side="tcp", padx=10, pady=5)

        #Получить список имен сотрудников из базы данных.
    def ＿get_employees(self) :
        employee_list - (1
        conn = None
        try:
            #Подсоединиться к базе данных и получить курсор.
            conn = sqlite3.connect("employees.db")
            cur = conn.cursor()
            #Исполнить запрос SELECT.
            cur. execute ("SELECT Name FFOM Erployees")
            #Получить результаты запроса в виде списка.
            employee_list - In(0] for n in cur.fetchall
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo("Ошибка базы данных', err)
        finally:
            #Если соединение открыто, то закрыть его.
            if conn != None:
                conn. close ()

            return employee list

        #Получить подробную информацию по выбранному сотруднику.
    def _get_details(selr, event) :
        #Получить высранное из вилкета Listbox.
        listbox index - self. employee_listbox.curselection [0]
        selected emp self. employee_listbox.get (listbox index)

        #Запросить в базе данных информацию о выбранном сотруднике.
        conn = None
        try:
            #Подсоединиться к базе данных и получить курсор.
            conn - sqlite3.connect 'employees.db')
            cur - conn.cursor()

            #исполнить запрос SELECT.
            cur. execute (
                '''SELECT
                    Employees. Name,
                    Employees. Position,
                    Departments. Department Name,
                    Locations. City
                FROM
                    Employees, Departments, Locations 
                WHERE
                    Employees. Department ID -- Departments. Department ID AND 
                    Employees. Location ID - Locations. Location tD***, 
                    
                    
            #Получать результаты запроса. 
            results - cur. fetchone()
            #Вывести на экран информацию о сотруднике. 
            self. display_details(name=results[0], position=results[11.
            department-resultal(2), location-results(31)
            oxcopt sqlite3. Error as orr:
tkinter.messagebox.showinto(*Ошика базы данных", err)
finally:
Если соединение открыто, то закрыть его.
if conn I= None: conn. close ()
position

Вывести в диалоговом окне на экран информацию о сотруднике. def _display_details(self, name, position, department, location): tkinter. messagebox. showinto ("Информашия о сотрупнике",
Уп Должность:
Исполнить запрос SELECT. cur. executet SELECT
Employees. Name,

WHERE
Employees, Position, Departments, DepartmentName,
Locations.City FROM
Employees, Departments, Locations
Employees. Name =- ? AND
Employees. DepartmentID -- Departments. Department ID A Employees. LocationID - Locations. LocationID''"
(selected_emp,))
    #Получить результаты запроса.
    results = cur.fetchone()
    #Вывести на экран информацию о сотруднике.
    self.display_details (name=results[01, position=results[11. department-results[2), location-results[3]) except sqlite3.Error as err:
    tkinter.messagebox.showinfo("Ошибка базы данных", err)
finally:

    #Если соединение открыто, то закрыть его. if conn != None:
conn. close()
    #Вывести в диалоговом окне на экран информацию о сотруднике. def ＿display details(self, name, position, department, location): tkinter.messagebox.showinfo("Информация о сотруднике", "Имя: * + name +
"АnДолжность: " + position + "Аnотдел: * + department + "\nМестоположение: + location)
    # Создать экземпляр класса EmployeeDetails.
if ＿namemain

    employee_details = EmployeeDetails()
