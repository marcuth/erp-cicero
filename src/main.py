from ttkbootstrap import Style, Notebook
from tkinter import messagebox
from tkinter import Tk

from frames.products import ProductsFrame
from frames.coupon import CouponFrame
from utils.window import clear_window
from frames.login import LoginFrame

style = Style("cosmo")
root: Tk = style.master
root.title("ERP")

def handle_submit_login_credentials(username: str, password: str) -> None:
    clean_username = username.strip()
    clean_password = password.strip()
    
    if not clean_username:
        messagebox.showerror("ERP - Erro ve validação", "Você deve preencher o campo de 'Usuário'!")
        return
    
    if not clean_password:
        messagebox.showerror("ERP - Erro ve validação", "Você deve preencher o campo de 'Senha'!")
        return
    
    handle_valid_login()
    
def handle_valid_login() -> None:
    clear_window(root)
    
    root.state("zoomed")
    
    notebook = Notebook(root)
    
    tabs_cls = [
        (CouponFrame, "Cupom"),
        (ProductsFrame, "Produtos"),
        (CouponFrame, "Clientes"),
        (CouponFrame, "Relatórios"),
        (CouponFrame, "Usuários")
    ]
    
    for tab_cls, text in tabs_cls:
        tab = tab_cls(root)
        notebook.add(tab, text=text)
        
    notebook.pack(expand=True, fill="both")

def main() -> None:
    login_frame = LoginFrame(root, on_submit=handle_submit_login_credentials)
    login_frame.pack()
    root.mainloop()

if __name__ == "__main__":
    main()