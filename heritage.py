from tkinter import *
root = Tk()
root.title("Jordanian Dishes")
root.geometry("820x560")
root.minsize(700, 500)

lbl = Label(root, text="Jordanian Dishes", 
            font=("Arial", 20 , "bold")
            ,bg="#3e2f1c",fg="#C9A646", pady=12)

lbl.pack(fill=X)

frame_main = Frame(root, bg="#F5E6D3")
frame_main.pack(fill=BOTH, expand=True, padx=10, pady=10)

frame_left = Frame( frame_main, bg="#6e5a3c" ) 
frame_left.pack(side=LEFT, fill=Y)

frame_right = Frame( frame_main, bg="#FFF8E7" ) 
frame_right.pack(side=LEFT, fill=BOTH, expand=True)

jordan_items = [ { "name": "Mansaf", "category": "Food", "desc": "National dish of Jordan made with lamb and jameed." }, 
                { "name": "Zarb", "category": "Food", "desc": "Traditional Bedouin dish cooked underground with meat and vegetables." },
                { "name": "Rashoof", "category": "Food", "desc": "Made with lentils, bulgur or rice, and jameed." },
                { "name": "Maqluba", "category": "Food", "desc": "Upside-down rice and meat dish." },
                { "name": "Knafeh", "category": "Food", "desc": "Sweet cheese pastry dessert." },
                { "name": "Makmora", "category": "Food", "desc": "Made of multiple layers of handmade dough." },
                { "name": "Falafel", "category": "Food", "desc": "Fried chickpea street food." },
                { "name": "Arayes", "category": "Food", "desc": "Grilled bread stuffed with meat." }
                ]

listbox = Listbox( frame_left, width=25, 
                  font=("Arial", 12),
                  bg="#FFF8E7", fg="#3E2723", 
                  selectbackground="#D4AF37", 
                  selectforeground="black" )
listbox.pack(padx=10, pady=10)

for item in jordan_items:
    listbox.insert(END, item["name"])
root.mainloop()