from tkinter import *
from tkinter import ttk
class Calculator:

    def __init__(self, root): # root object to work with interface
        self.result = 0
        self.value = StringVar(root, value='')
        root.title('Calculator!')
        root.geometry('400x400')
        root.resizable(width=False, height=False)
        btn_triggered = False
        self.history = dict()

        style = ttk.Style()
        style.configure("TButton",padding=10)
        style.configure("TEntry",padding=10)


"""Dyan: Developer & Content Maker"""

if __name__ == '__main__':
    Calculator(root=ttk)
