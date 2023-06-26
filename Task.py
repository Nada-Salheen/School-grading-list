import tkinter as tk
import tkinter.messagebox
window1 = tk.Tk()
window1.title("PYTHON International School")
window1.geometry("300x500")



l1 = tk.Label(text="Name")
l2 = tk.Label(text="Bench number")
l3 = tk.Label(text="Maths Mark")
l4 = tk.Label(text="Science Mark")
l5 = tk.Label(text="Arabic Mark")

l1.place(x=20 , y=30)
l2.place(x=20 , y=60)
l3.place(x=20 , y=90)
l4.place(x=20 , y=120)
l5.place(x=20 , y=150)

e1 = tk.Entry()
e2 = tk.Entry()
e3 = tk.Entry()
e4 = tk.Entry()
e5 = tk.Entry()

e1.place(x=150, y=30)
e2.place(x=150, y=60)
e3.place(x=150, y=90)
e4.place(x=150, y=120)
e5.place(x=150, y=150)


def b1_click():
     name = e1.get()
     bench = e2.get()
     maths = e3.get()
     sc = e4.get()
     arab = e5.get()
     file = open("student.txt", "a")
     if not bench.isdigit() and not maths.isdigit() and not arab.isdigit() and not sc.isdigit() :
         tk.messagebox.showerror("Caution", "Please enter numbers")
         return
     k = ((int(maths) + int(sc) + int(arab)) / 300)* 100

     file.write(str(name) +"," +str(bench)+"," + str(maths)+"," + str(sc) +","+ str(arab)+"," + str(k)+"\n")
     if k < 50.0:
         tk.messagebox.showinfo("Caution", "This Student has failed")
     e1.delete(0, tk.END)
     e2.delete(0, tk.END)
     e3.delete(0, tk.END)
     e4.delete(0, tk.END)
     e5.delete(0, tk.END)
     file.close()
b1 = tk.Button(text="Export Data", command=b1_click)
b1.place(x=110 , y=400)























window1.mainloop()