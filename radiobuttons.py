import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root,
         text="""Choose a Sport:""",
         justify = tk.LEFT,
         padx = 10) .pack()
tk.Radiobutton(root,
               text="Football",
               padx = 20,
               variable=v,
               value=1) .pack(anchor=tk.W)
tk.Radiobutton(root,
               text="Basketball",
               padx = 20,
               variable=v,
               value=2) .pack(anchor=tk.W)
root.mainloop()
