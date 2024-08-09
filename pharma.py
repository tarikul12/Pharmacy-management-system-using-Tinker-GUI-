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
        
        DataFrame=tk.Frame(self.root,bd=15,relief=tk.RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1900,height=400)
        
        DataFrameLeft =tk.LabelFrame(DataFrame,bd=10,relief=tk.RIDGE,padx=20,text="Medicine Information",
                                     fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1100,height=350)
        
        DataFrameRight =tk.LabelFrame(DataFrame,bd=10,relief=tk.RIDGE,padx=20,text="New Medicine Add Department",
                                     fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=1110,y=5,width=700,height=350)
        
        


if __name__ == "__main__":
    root = tk.Tk()  
    obj = PharmacyManagementSystem(root)
    root.mainloop()
