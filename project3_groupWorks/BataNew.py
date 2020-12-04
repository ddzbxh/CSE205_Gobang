import tkinter as tk
import tkinter.filedialog as fd


class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.var = tk.StringVar()
        self.initUI()

    def initUI(self):
        group_top = tk.LabelFrame(self, padx=15, pady=10)
        group_top.pack(padx=10, pady=5)

        tk.Button(group_top, text="浏览", width=10, command=self.choose_file).grid(row=0, column=1)

        self.path_entry = tk.Entry(group_top, width=30)
        self.path_entry.grid(row=0, column=0, pady=5, padx=5)

        tk.Button(group_top, text="开始执行", width=10, command=self.func).grid(row=1, column=1, sticky=tk.E)
        tk.Button(group_top, text="停止", width=10, command=self.destroy).grid(row=1, column=0, sticky=tk.W)

        console_frame = tk.Frame(group_top).grid(row=2, column=0, columnspan=2)
        self.console_text = tk.Text(
            console_frame, fg="green", bg="black", width=40, height=20, state=tk.DISABLED)
        scrollbar = tk.Scrollbar(console_frame, command=self.console_text.yview)
        scrollbar.pack(side="right", fill=tk.Y)
        self.console_text.pack(expand=1, fill=tk.BOTH)
        self.console_text['yscrollcommand'] = scrollbar.set

    def output_to_console(self, new_text):
        self.console_text.config(state=tk.NORMAL)
        self.console_text.insert(tk.END, new_text)
        self.console_text.see(tk.END)
        self.console_text.config(state=tk.DISABLED)

    def choose_file(self):
        filetypes = (("Plain text files", "*.txt"),
                     ("Images", "*.jpg *.gif *.png"),
                     ("All files", "*"))
        filename = fd.askopenfilename(title="Open file", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            self.path_entry.delete("0", tk.END)
            self.path_entry.insert(tk.END, filename)
            self.output_to_console(f"{filename}\n")

    def func(self):
        path = self.path_entry.get()
        self.output_to_console(f"{path}\n")


if __name__ == '__main__':
    app = App()
    app.resizable(height=False)
    app.mainloop()
