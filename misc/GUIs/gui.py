from tkinter import *

#cria uma nova janela
window = Tk()

#seta o título da janela
window.title("Meu programa")

entry_text = Entry(window, width=30)
entry_text.pack()
entry_text.focus_set()

def click_button():
	
	x = int(entry_text.get())
	print(x*2)

btn = Button(window, text='Clique Aqui', width=20, command=click_button)
btn.pack()

window.geometry('300x150')
window.mainloop()