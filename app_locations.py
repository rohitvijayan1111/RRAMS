import tkinterweb
import tkinter as tk
root = tk.Tk()
root.attributes('-topmost', 1)
user_query = input("enter: ")
user = ""
for b in user_query.split():
    user = user + "+" + b
user = user[1::]
print(user)
URL = "https://www.google.com/search?q=" + user
print(URL)
frame = tkinterweb.HtmlFrame(root,messages_enabled = False)

frame.load_website(URL)
frame.pack(fill="both", expand=True)
root.mainloop()