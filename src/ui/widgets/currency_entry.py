from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class CurrencyEntry(ttk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        vcmd = self.register(self._validate_input)
        
        self.config(
            validate="key",
            validatecommand=(vcmd, "%S", "%P")
        )

    def _validate_input(self, inserted_char: str, new_value: str):
        if new_value == "":
            return True

        if inserted_char.isdigit():
            if "," in new_value:
                parts = new_value.split(",")
                
                if len(parts) > 1 and len(parts[1]) > 2:
                    return False
                
            return True

        if inserted_char == ",":
            if new_value.count(",") > 1:
                return False
            
            return True

        return False
