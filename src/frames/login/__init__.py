from ttkbootstrap import Frame, Label, Entry, Button
from typing import Optional, Mapping, Any
from ttkbootstrap.constants import *
from tkinter import Tk

from utils.window import center_window

class LoginFrame(Frame):
    def __init__(self, master: Optional[Tk]=None, on_submit=None, **kwargs):
        master.title("ERP - Login")
        master.resizable(False, False)
        
        super().__init__(master, width=300, height=250, **kwargs)
        
        self.pack_propagate(False)
        self.on_submit = on_submit
        self._put_heading()
        self._put_form()
        self._put_button()
    
    def _put_heading(self) -> None:
        heading = Label(self, text="Login", font=("TkDefaultFont", 16, "bold"))
        heading.pack(pady=(10, 20))

    def _put_form(self) -> None:
        self.username_label = Label(self, text="Usuário:")
        self.username_label.pack(anchor="w", padx=20)

        self.username_entry = Entry(self)
        self.username_entry.pack(fill="x", padx=20, pady=5)

        self.password_label = Label(self, text="Senha:")
        self.password_label.pack(anchor="w", padx=20)

        self.password_entry = Entry(self, show="•")
        self.password_entry.pack(fill="x", padx=20, pady=5)

    def _put_button(self) -> None:
        login_button = Button(self, text="Entrar", bootstyle=PRIMARY, command=self._handle_submit)
        login_button.pack(pady=15)

    def _handle_submit(self) -> None:
        user = self.username_entry.get()
        password = self.password_entry.get()

        if self.on_submit:
            self.on_submit(user, password)
            
    def pack(self, cnf: Optional[Mapping[str, Any]] = None, **kwargs) -> None:
        if cnf is None:
            cnf = {}
            
        super().pack(cnf, **kwargs)
        center_window(self.master)