import tkinter as tk

from tkinter import ttk, font

from source.core import Currency
from source.data import AVAILABLE_MEALS, update_available_meals, update_available_ingredients


# NOTE: GUI layout hardcoded. Can be made more generic for dynamic enabling/disabling buttons etc.
class PrototypeGui:
    """GUI application for the prototype."""

    def __init__(self):
        # General
        self.indent_size: int = 4
        """Number of spaces for an indent."""
        self.currency: Currency = Currency.EUR
        """Currency type used for price calculation."""

        # Root window
        self.root: tk.Tk = tk.Tk()
        self.root.title('SmartCater Prototype')
        self.root.geometry('1280x720')

        # Grid Layout
        self.root.grid_rowconfigure(0, weight=100)
        self.root.grid_columnconfigure(0, weight=95)
        self.root.grid_columnconfigure(1, weight=5)

        # Overlays
        self.selection_overlay: tk.Frame = tk.Frame(self.root)
        self.selection_overlay.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.selection_overlay.grid_rowconfigure(0, weight=95)
        self.selection_overlay.grid_rowconfigure(1, weight=5)
        self.selection_overlay.grid_columnconfigure(0, weight=99)
        self.selection_overlay.grid_columnconfigure(1, weight=1)
        self.selection_overlay.grid_propagate(False)    # To avoid the selection overlay expanding in x direction over time

        self.button_overlay: tk.Frame = tk.Frame(self.root)
        self.button_overlay.grid(row=0, column=1, sticky='nsew', padx=20, pady=20)
        self.button_overlay.grid_rowconfigure(0, weight=50)
        self.button_overlay.grid_rowconfigure(1, weight=20)
        self.button_overlay.grid_rowconfigure(2, weight=30)
        self.button_overlay.grid_columnconfigure(0, weight=100)

        # Selection view
        self.selection_tree: ttk.Treeview = ttk.Treeview(self.selection_overlay, columns=('Name','Price', 'Description'), show='headings')

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('TkDefaultFont', 10, 'bold'))

        self.selection_tree.heading('Name', text='Meal Name')
        self.selection_tree.column('Name', width=100, stretch=True)
        self.selection_tree.heading('Price', text=f'Price ({self.currency.value})')
        self.selection_tree.column('Price', width=100, stretch=False)
        self.selection_tree.heading('Description', text='Short Description')
        self.selection_tree.column('Description', width=400, stretch=True)

        self.selection_tree.grid(row=0, column=0, sticky='nsew')

        self.scrollbar: ttk.Scrollbar = ttk.Scrollbar(self.selection_overlay, orient='vertical', command=self.selection_tree.yview)
        self.selection_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='nsew')

        # Buttons
        self.button_frame: tk.Frame = tk.Frame(self.button_overlay)
        self.button_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        update_view: tk.Button = tk.Button(
            master=self.button_frame,
            text='Update',
            width=15,
            command=self.update_selection_view
        )
        update_view.pack(padx=5, pady=5)


        # Currency
        self.currency_frame: tk.Frame = tk.Frame(self.button_overlay)
        self.currency_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=20)

        tk.Label(master=self.currency_frame, text='Currency').pack(pady=10)
        self.currency_var = tk.StringVar()

        self.currency_dropdown = ttk.Combobox(
            master=self.currency_frame,
            textvariable=self.currency_var,
            values=[currency.name for currency in Currency],
            state='readonly',
        )
        self.currency_dropdown.set(Currency.EUR.name)
        self.currency_dropdown.pack(pady=10)
        self.currency_dropdown.bind('<<ComboboxSelected>>', lambda event: self.update_selection_view())     # Update interface if currency changes

        self.update_selection_view()
        self.root.mainloop()
        

    def update_selection_view(self) -> None:
        """Add all available meals to the selection view."""
        # Update globals if meals were added / removed
        update_available_ingredients()
        update_available_meals()

        # Update currency
        self.currency = Currency(self.currency_var.get())
        
        # Clear selection view
        for item in self.selection_tree.get_children():
            self.selection_tree.delete(item)

        # Reconstruct selection view
        for meal_name, meal_obj in AVAILABLE_MEALS.items():
            # Add Meal node
            parent_id: str = self.selection_tree.insert(
                parent='',
                index='end',
                values=(
                    meal_name,
                    f'{meal_obj.get_price(Currency(self.currency_var.get())):.2f}',
                    meal_obj.description),
            )

            # Add subsections
            ## Ingredients
            ingredient_section_id: str = self.selection_tree.insert(
                parent=parent_id,
                index='end',
                values=(' ' * self.indent_size + 'Ingredients:',),
                open=True
            )
            for ingredient in meal_obj.ingredients:
                self.selection_tree.insert(
                    parent=ingredient_section_id,
                    index='end',
                    values=(' ' * self.indent_size * 2 + ingredient.name, ingredient.get_cost(self.currency))
                )

            ## Recipe
            recipe_section_id: str = self.selection_tree.insert(
                parent=parent_id,
                index='end',
                values=(' ' * self.indent_size + 'Recipe:',),
                open=True
            )
            recipe_steps: list[str] = meal_obj.recipe.split('\n')
            for step in recipe_steps:
                self.selection_tree.insert(
                    parent=recipe_section_id,
                    index='end',
                    values=('', '', step,)
                )
            # Add new line
            self.selection_tree.insert(
                    parent=recipe_section_id,
                    index='end',
                    values=('',)
                )
