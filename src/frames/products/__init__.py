from ttkbootstrap import Frame, Label, Button, Treeview, Menu, Toplevel, Entry, StringVar
from tkinter import Tk, CENTER, END
from typing import Optional

from utils.window import center_window

class ProductsFrame(Frame):
    def __init__(self, master: Optional[Tk]=None, **kwargs):
        master.title("Produtos")
        super().__init__(master, **kwargs)
        
        self.data = [
            (1, "Creme para pele", 30, 55),
            (2, "Desodorante Masculino", 25, 15),
            (3, "Shampoo Anticaspa", 40, 22),
            (4, "Condicionador Nutritivo", 35, 28),
            (5, "Sabonete Líquido", 60, 12),
            (6, "Protetor Solar FPS 50", 20, 45),
            (7, "Gel de Barbear", 18, 20),
            (8, "Creme Dental Branqueador", 70, 8),
            (9, "Escova de Dentes Premium", 50, 10),
            (10, "Loção Pós-Barba", 15, 25),
            (11, "Kit Manicure", 12, 35),
            (12, "Perfume Feminino 50ml", 22, 95),
            (13, "Perfume Masculino 100ml", 18, 120),
            (14, "Creme para Mãos", 45, 18),
            (15, "Álcool Gel 70%", 80, 9),
        ]
        
        self.grid_rowconfigure(2, weight=1)
        self.pack(expand=True, fill="both")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self._put_header_bar()
        self._put_search_bar()
        self._put_prdoucts_table()
        
    def _put_header_bar(self) -> None:
        frame = Frame(self)
        frame.grid(row=0, column=0, columnspan=3, pady=(10, 0), sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        heading = Label(frame, text="Gestão de Produtos", font=("TkDefaultFont", 16, "bold"))
        heading.pack(side="left", padx=(20, 0))

        create_product_button = Button(frame, text="Criar produto")
        create_product_button.pack(side="right", padx=(0, 20))
        
    def _put_search_bar(self) -> None:
        frame = Frame(self)
        frame.grid(row=1, column=0, columnspan=3, pady=(10, 10))

        search_label = Label(frame, text="Pesquisar produto:")
        search_label.pack(side="left", padx=(0, 5))

        self.search_var = StringVar()
        search_entry = Entry(frame, textvariable=self.search_var, width=30)
        search_entry.pack(side="left")
        search_entry.bind("<Return>", lambda e: self._filter_products())

        search_btn = Button(frame, text="Pesquisar", command=self._filter_products)
        search_btn.pack(side="left", padx=(5, 0))

    def _put_prdoucts_table(self) -> None:
        columns = ("ID", "Nome", "Estoque", "Preço de Venda")
        self.tree = Treeview(self, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=CENTER)
        
        for row_data in self.data:
            self.tree.insert("", END, values=row_data)

        self.tree.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
        
        self.tree.bind("<Button-3>", self._on_right_click)
        self.tree.bind("<Return>", self._on_enter_key)
        self.tree.bind("<Double-1>", self._on_double_click)
        
    def _filter_products(self):
        term = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())

        if not term:
            filtered_data = self.data
        else:
            filtered_data = [
                p for p in self.data if term in str(p[1]).lower()
            ]

        for row_data in filtered_data:
            self.tree.insert("", END, values=row_data)
        
    def _on_right_click(self, event):
        selected_item = self.tree.identify_row(event.y)
        
        if selected_item:
            self.tree.selection_set(selected_item)
            menu = Menu(self, tearoff=0)
            menu.add_command(label="Ver Produto", command=lambda: self._view_product(selected_item))
            menu.add_command(label="Excluir Produto", command=lambda: self._delete_product(selected_item))
            menu.post(event.x_root, event.y_root)
            
    def _on_enter_key(self, _):
        selected_item = self.tree.focus()
        
        if selected_item:
            self._view_product(selected_item)
            
    def _on_double_click(self, event):
        selected_item = self.tree.identify_row(event.y)
        
        if selected_item:
            self._view_product(selected_item)

    def _view_product(self, item_id):
        values = self.tree.item(item_id, "values")
        print(f"Visualizar produto: {values}")
        self._show_product_popup(values)

    def _delete_product(self, item_id):
        values = self.tree.item(item_id, "values")
        print(f"Excluir produto: {values}")
        self.tree.delete(item_id)
        
    def _show_product_popup(self, values) -> None:
        popup = Toplevel(self)
        popup.title("Editar Produto")
        popup.geometry("350x250")
        popup.resizable(False, False)

        popup.transient(self)
        popup.grab_set()
        
        center_window(popup)

        labels = ["ID", "Nome", "Estoque", "Preço de Venda"]
        entries = []

        for i, (label, value) in enumerate(zip(labels, values)):
            lbl = Label(popup, text=f"{label}:", font=("TkDefaultFont", 10, "bold"))
            lbl.grid(row=i, column=0, sticky="e", padx=10, pady=5)

            entry = Entry(popup)
            entry.insert(0, value)
            entry.grid(row=i, column=1, sticky="w", padx=10, pady=5)
            entries.append(entry)

        def save():
            novos_valores = [entry.get() for entry in entries]
            item_id = self.tree.focus()
            self.tree.item(item_id, values=novos_valores)
            popup.destroy()

        def cancel():
            popup.destroy()
            
        btn_cancel = Button(popup, text="Cancelar", command=cancel, bootstyle="secondary")
        btn_cancel.grid(row=4, column=0, padx=10, pady=15)

        btn_save = Button(popup, text="Salvar", command=save)
        btn_save.grid(row=4, column=1, padx=10, pady=15)
        