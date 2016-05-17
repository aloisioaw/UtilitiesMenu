from Tkinter import *

class popupWindow(object):

	def __init__(self,master):
		self.master = master
		self.master.resizable(width=FALSE, height=FALSE)
		self.master.minsize(width=160, height=80)
		self.master.title("Senha de Root")
		self.lblSenha = Label(master,text = "Senha:")
		self.lblSenha.grid(row = 0, column = 0, columnspan=2)
		self.txtSenha = Entry(master, show="*")
		self.txtSenha.bind("<Return>", self.pressionou_enter)
		self.txtSenha.grid(row = 1, column = 0, columnspan=2)
		self.btnOk = Button(master,text = 'Ok',command = self.cleanup).grid(row = 2, column = 0)
		self.btnCancelar = Button(master,text = 'Cancelar',command = self.cancelar).grid(row = 2, column = 1)

	def cleanup(self):
		self.senha = self.txtSenha.get()
		self.master.destroy()

	def cancelar(self):
		self.master.destroy()

	def pressionou_enter(self, event):
		self.senha = self.txtSenha.get()
		self.master.destroy()


if __name__ == "__main__":
	root = Tk()
	m = popupWindow(root)
	root.mainloop()