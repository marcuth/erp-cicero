from ttkbootstrap import Frame

class CouponFrame(Frame):
    def __init__(self, master=None, **kwargs):
        master.title("Cupom")
        super().__init__(master, **kwargs)