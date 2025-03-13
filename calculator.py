# Python 3.12.3
import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Simple Calculator')

        self.expression = ""

        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black",
                                    highlightcolor="black", highlightthickness=1)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'),
                                    width=50, bd=0, bg="#eee", justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)  # padx=10, pady=10

        self.buttons_frame = tk.Frame(self.root, width=312, height=272.5, bg="grey")
        self.buttons_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                      command=action).grid(row=row_val, column=col_val, padx=1, pady=1)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += button
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
