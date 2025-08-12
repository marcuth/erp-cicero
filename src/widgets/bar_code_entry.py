from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class BarCodeEntry(ttk.Entry):
    def __init__(self, master, max_length=13, **kwargs):
        super().__init__(master, **kwargs)
        self.max_length = max_length

        vcmd = self.register(self._validate_input)
        
        self.config(
            validate="key",
            validatecommand=(vcmd, "%P", "%S")
        )

    def _validate_input(self, new_value: str, char: str):
        if new_value == "":
            return True

        if not char.isdigit():
            return False

        if len(new_value) > self.max_length:
            self.delete(0, "end")
            self.insert(0, char)
            return False

        return True

    def get_barcode(self):
        return self.get()

    def is_complete(self):
        return len(self.get()) == self.max_length