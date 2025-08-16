from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class IntEntry(ttk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        vcmd = self.register(self._validate_input)
        
        self.config(
            validate="key",
            validatecommand=(vcmd, '%S')
        )

    def _validate_input(self, text: str):
        return text.isdigit() or text == ""