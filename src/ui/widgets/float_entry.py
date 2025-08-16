from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class FloatEntry(ttk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        vcmd = self.register(self._validate_input)
        self.config(
            validate="key",
            validatecommand=(vcmd, "%S", "%P")
        )

    def _validate_input(self, text: str, new_value: str):
        if text == "":
            return True

        if text.isdigit():
            return True

        if text in (".", ","):
            if new_value.count(".") <= 1 and new_value.count(",") <= 1:
                return True
        
        return False