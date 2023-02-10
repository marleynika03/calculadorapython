import re
import math
import tkinter as tk
from typing import List


class Calculator:
    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]]
    ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

    def start(self):
        self.root.mainloop()
        self._config_display()
        self._config_buttons()

    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']
                if self.root.winfo_exists():
                    if button_text == 'C':
                        button.bind('<Button-1>', self.clear)

                    if button_text in '0123456789.+-/*':
                        button.bind('<Button-1>', self.add_text_to_display)

                    if button_text == '=':
                        button.bind('<Button-1>', self.calculate)

    def _config_display(self):
        self.display.bind('<Return>', self.calculate)
        self.display.bind('<KPEnter>', self.calculate)

    def _fix_text(self, text):
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text, 0)
        text = re.sub(r'([.\/\*\-\+\^\])\1+', r'\1', text, 0)
        text = re.sub(r'\?\(\)', '', text)

        return text

    def clear(self, event=None):
        self.display.delete(0, 'end')


def clear(self, event=None):
    self.display.delete(0, 'end')


def add_text_to_display(self, event=None):
    self.display.insert('end', event.widget['text'])


def calculate(self, event=None):
    fixed_text = self._fix_text(self.display.get())
    equations = self._get_equations(fixed_text)

    try:
        if len(equations) == 1:
            result = eval(self._fix_text(equations[0]))
        else:
            result = eval(self._fix_text(equations[0]))
            for equation in equations[1:]:
                result = math.pow(result, eval(self._fix_text(equation)))

        self.display.delete(0, 'end')
        self.display.insert('end', result)
        self.label.config(text=f'{fixed_text} = {result}')

    except OverflowError:
        self.label.config(text='Resultado muito grande')
    except Exception as e:
        self.label.config(text='Conta inválida')

    def _get_equations(self, text):
        return re.split(r'\^', text, 0)
