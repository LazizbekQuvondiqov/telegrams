from tkinter import *

window = Tk()
window.title('My App')
window.geometry('430x330')
window.configure(background='green')
def change_text():
    my_label.config(text=str(int(txt.get())**4) )
def change1_text():
    my_label.config(text=str(int(txt.get())**(1/2)))
my_label=Label(window, width=60,
height=5, bg='white', text='Javob ')
my_label.grid(row=0, column=0)

txt = Entry(window, width=60, bg='white',)
txt.grid(column=0, row=1)


my_button=Button(window, text="press me!", width=10, command=change_text)
my_button.grid(row=2, column=0)

my_button1=Button(window, text="press me!", width=10, command=change1_text)
my_button1.grid(row=3, column=0)
window.mainloop()

