from tkinter import*
from tkinter import messagebox
from tkinter import ttk


class Ventana(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master = master
        self.pack
        self.create_widgets()
        
    def create_widgets(self):
        pass
    

def main():
    root = Tk()
    root.wm_title("CRUD Python MySQL")
    app = Ventana(root)
    app.mainloop()
    
if __name__ == "__main__":
    main()