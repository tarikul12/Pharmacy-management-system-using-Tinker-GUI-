import tkinter as tk
from PIL import Image,ImageTk

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System") 
        self.root.geometry("1900x800+0+0")  
        
        lbltitle =tk.Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15, relief=tk.RIDGE,bg="White",
                        fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=tk.TOP,fill=tk.X)
        
        image1 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Pharmacy/logo.png")
        image1 =image1.resize((80,80),Image.Resampling.LANCZOS)
        self.photoimage1 =ImageTk.PhotoImage(image1)
        button1 =tk.Button(self.root,image=self.photoimage1,borderwidth=0)
        button1.place(x=70,y=20)
        
        


if __name__ == "__main__":
    root = tk.Tk()  
    obj = PharmacyManagementSystem(root)
    root.mainloop()
