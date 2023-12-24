
from window import Window 
from tkinter import Tk
from tkinter import ttk

if __name__ == "__main__":

   app = Tk()
   style = ttk.Style()
   style.theme_use("clam")
   window = Window(app)
   app.mainloop()



