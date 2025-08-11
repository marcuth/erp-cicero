from ttkbootstrap import Frame
from tkinter import Tk

class CouponFrame(Frame):
    def __init__(self, master: Tk, **kwargs):
        master.title("Cupom")
        super().__init__(master, **kwargs)