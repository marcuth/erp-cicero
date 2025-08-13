from ttkbootstrap import Frame, Label, Button, Treeview, Menu, Toplevel, Entry, StringVar, Text
from tkinter import Tk, CENTER, END, StringVar
from typing import Optional, Tuple
from datetime import datetime

from widgets.currency_entry import CurrencyEntry
from widgets.bar_code_entry import BarCodeEntry
from widgets.int_entry import IntEntry
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
        frame.grid(row=0, column=0, columnspan=3, pady=(10, 10), padx=20, sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        heading = Label(frame, text="Gestão de Produtos", font=("TkDefaultFont", 16, "bold"))
        heading.pack(side="left", padx=(20, 0))

        create_product_button = Button(frame, text="Criar produto", command=self._show_create_product_popup)
        create_product_button.pack(side="right", padx=(0, 20))
    
    def _show_create_product_popup(self) -> None:
        popup = Toplevel(self)
        popup.title("Criar Produto")
        popup.geometry("700x380")
        popup.resizable(False, False)

        popup.transient(self)
        popup.grab_set()
        
        center_window(popup)
        
        container = Frame(master=popup)
        
        name_label = Label(master=container, text="Nome*:")
        name_entry = Entry(master=container)
        
        buy_price_label = Label(master=container, text="Preço de custo (R$)*:")
        buy_price_entry = CurrencyEntry(master=container)
        
        sell_price_label = Label(master=container, text="Preço de venda (R$)*:")
        sell_price_entry = CurrencyEntry(master=container)
        
        description_label = Label(master=container, text="Descrição:")
        description_text = Text(master=container, height=3)
        
        stock_label = Label(master=container, text="Itens em estoque*:")
        stock_entry = IntEntry(master=container)
        
        barcodes_label = Label(master=container, text="EANs*:")
        
        barcode1_entry = BarCodeEntry(master=container)
        barcode2_entry = BarCodeEntry(master=container)
        barcode3_entry = BarCodeEntry(master=container)
        
        button_frame = Frame(master=container)
        button_frame.grid(row=6, column=0, columnspan=5, sticky="e", padx=10, pady=(10,15))
        
        cancel_button = Button(master=button_frame, text="Cancelar", command=popup.destroy, bootstyle="secondary")
        create_button = Button(master=button_frame, text="Criar produto", command=lambda: print("Criar clicado"))
        
        create_button.pack(side="right")
        cancel_button.pack(side="right", padx=10)
        
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.columnconfigure(4, weight=1)

        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=(15,5))
        name_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(15,5))

        description_label.grid(row=2, column=0, sticky="nw", padx=10, pady=(10,5))
        description_text.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=(0,15))

        buy_price_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        buy_price_entry.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

        sell_price_label.grid(row=4, column=1, sticky="w", padx=10, pady=5)
        sell_price_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=5)
        
        barcodes_label.grid(row=0, column=4, sticky="w", padx=10, pady=(0,5))
        
        barcode1_entry.grid(row=1, column=4, padx=10, pady=(0,1))
        barcode2_entry.grid(row=2, column=4, padx=10, pady=1)
        barcode3_entry.grid(row=3, column=4, padx=10, pady=(1,15))
        
        stock_label.grid(row=4, column=4, sticky="w", padx=10, pady=(10,15))
        stock_entry.grid(row=5, column=4, sticky="ew", padx=10, pady=(10,15))
        
        button_frame.grid(row=6, column=0, columnspan=5, sticky="e", padx=10, pady=(10,15))
        
        container.pack(fill="both", expand=True, padx=15, pady=15)
        
    def _handle_create_product(self) -> None: ...
        
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
        
        self.tree.bind("<Button-3>", self._on_item_right_click)
        self.tree.bind("<Return>", self._on_item_enter_key)
        self.tree.bind("<Double-1>", self._on_item_double_click)
        
    def _filter_products(self) -> None:
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
        
    def _on_item_right_click(self, event):
        selected_item = self.tree.identify_row(event.y)
        
        if selected_item:
            self.tree.selection_set(selected_item)
            menu = Menu(self, tearoff=0)
            menu.add_command(label="Ver Produto", command=lambda: self._view_product(selected_item))
            menu.add_command(label="Excluir Produto", command=lambda: self._delete_product(selected_item))
            menu.post(event.x_root, event.y_root)
            
    def _on_item_enter_key(self, _):
        selected_item = self.tree.focus()
        
        if selected_item:
            self._view_product(selected_item)
            
    def _on_item_double_click(self, event):
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
        
    def _show_product_popup(self, values: Tuple[str, str, str, str]) -> None:
        id, name, buy_price, sell_price = values
        
        print(values)

        popup = Toplevel(self)
        popup.title("Editar Produto")
        popup.geometry("720x450")
        popup.resizable(False, False)
        
        name_var = StringVar(popup, name)
        buy_price_var = StringVar(popup, str(buy_price))
        sell_price_var = StringVar(popup, str(sell_price))
        created_at = datetime.now()
        updated_at = datetime.now()

        popup.transient(self)
        popup.grab_set()
        
        center_window(popup)
        
        container = Frame(master=popup)
        
        id_label = Label(master=container, text=f"ID #{id}")
        created_at_label = Label(master=container, text=created_at.strftime("Criado em %d/%m/%Y às %H:%m:%S"))
        updated_at_label = Label(master=container, text=updated_at.strftime("Atualizado em %d/%m/%Y às %H:%m:%S"))
        
        name_label = Label(master=container, text="Nome*:")
        name_entry = Entry(master=container, textvariable=name_var)
        
        buy_price_label = Label(master=container, text="Preço de custo (R$)*:")
        buy_price_entry = CurrencyEntry(master=container, textvariable=buy_price_var)
        
        sell_price_label = Label(master=container, text="Preço de venda (R$)*:")
        sell_price_entry = CurrencyEntry(master=container, textvariable=sell_price_var)
        
        description_label = Label(master=container, text="Descrição:")
        description_text = Text(master=container, height=3)
        
        stock_label = Label(master=container, text="Itens em estoque*:")
        stock_entry = IntEntry(master=container)
        
        barcodes_label = Label(master=container, text="EANs*:")
        
        barcode1_entry = BarCodeEntry(master=container)
        barcode2_entry = BarCodeEntry(master=container)
        barcode3_entry = BarCodeEntry(master=container)
        
        button_frame = Frame(master=container)
        button_frame.grid(row=6, column=0, columnspan=5, sticky="e", padx=10, pady=(10,15))
        
        cancel_button = Button(master=button_frame, text="Cancelar", command=popup.destroy, bootstyle="secondary")
        create_button = Button(master=button_frame, text="Atualizar produto", command=lambda: print("Criar clicado"))
        
        create_button.pack(side="right")
        cancel_button.pack(side="right", padx=10)
        
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.columnconfigure(4, weight=1)
        
        id_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(15,5))

        name_label.grid(row=1, column=0, sticky="w", padx=10, pady=(15,5))
        name_entry.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(15,5))

        description_label.grid(row=3, column=0, sticky="nw", padx=10, pady=(10,5))
        description_text.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=(0,15))

        buy_price_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        buy_price_entry.grid(row=6, column=0, sticky="ew", padx=10, pady=5)

        sell_price_label.grid(row=5, column=1, sticky="w", padx=10, pady=5)
        sell_price_entry.grid(row=6, column=1, sticky="ew", padx=10, pady=5)
        
        created_at_label.grid(row=0, column=4)
        updated_at_label.grid(row=1, column=4,)
        
        barcodes_label.grid(row=2, column=4, sticky="w", padx=10, pady=(0,5))
        
        barcode1_entry.grid(row=3, column=4, padx=10, pady=(0,1))
        barcode2_entry.grid(row=4, column=4, padx=10, pady=1)
        barcode3_entry.grid(row=5, column=4, padx=10, pady=(1,15))
        
        stock_label.grid(row=6, column=4, sticky="w", padx=10, pady=(10,15))
        stock_entry.grid(row=7, column=4, sticky="ew", padx=10, pady=(10,15))
        
        button_frame.grid(row=9, column=0, columnspan=5, sticky="e", padx=10, pady=(10,15))
        
        container.pack(fill="both", expand=True, padx=15, pady=15)
        