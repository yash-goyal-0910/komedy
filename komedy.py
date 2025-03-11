import tkinter as tk
import pyjokes
def nxt():
    joke = pyjokes.get_joke()
    label2.config(text=joke)

root = tk.Tk()
root.title('Komedy')
label = tk.Label(root, text='Joke Of The Day', font=('Ariel', 20))
label.pack(anchor='center')
label2 = tk.Label(root, text=pyjokes.get_joke(), wraplength=400, justify='center')  # Wrap text if the joke is long
label2.pack(anchor='center', pady=10)
tk.Button(root, text='next', width=4, height=2, command=nxt).pack(side='right')
root.mainloop()
