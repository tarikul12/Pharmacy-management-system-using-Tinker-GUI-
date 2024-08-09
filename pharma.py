import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk

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
        
        #==============================DataFrame====================================
        
        DataFrame=tk.Frame(self.root,bd=15,relief=tk.RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1900,height=400)
        
        DataFrameLeft =tk.LabelFrame(DataFrame,bd=10,relief=tk.RIDGE,padx=20,text="Medicine Information",
                                     fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1100,height=350)
        
        DataFrameRight =tk.LabelFrame(DataFrame,bd=10,relief=tk.RIDGE,padx=20,text="New Medicine Add Department",
                                     fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=1110,y=5,width=700,height=350)
        
        #+++++++++++++++++++++++++++++ButtonFrame++++++++++++++++++++++++++++++++++===
        
        ButtonFrame =tk.Frame(self.root,bd=15,relief=tk.RIDGE,padx=20)
        ButtonFrame.place(x=1,y=520,width=1900,height=65)
        
           #+++++++++++++++++++++++++++++MainButton++++++++++++++++++++++++++++++++++===
        for i in range(50):  # Adjust the number to cover your columns
            ButtonFrame.grid_columnconfigure(i, weight=1)

  
        btnAddData = tk.Button(ButtonFrame, text="Medicine Add", bg="darkgreen", font=("arial", 13, "bold"), fg="white")
        btnAddData.grid(row=0, column=0, columnspan=5, sticky=tk.W+tk.E, padx=5, pady=5)

        btnUpdateData = tk.Button(ButtonFrame, text="UPDATE", bg="darkgreen", font=("arial", 13, "bold"), fg="white")
        btnUpdateData.grid(row=0, column=5, columnspan=5, sticky=tk.W+tk.E, padx=5, pady=5)

        btnDeleteData = tk.Button(ButtonFrame, text="DELETE", bg="red", font=("arial", 13, "bold"), fg="white")
        btnDeleteData.grid(row=0, column=10, columnspan=5, sticky=tk.W+tk.E, padx=5, pady=5)

        btnResetData = tk.Button(ButtonFrame, text="RESET", bg="darkgreen", font=("arial", 13, "bold"), fg="white")
        btnResetData.grid(row=0, column=15, columnspan=5, sticky=tk.W+tk.E, padx=5, pady=5)

        btnExitData = tk.Button(ButtonFrame, text="EXIT", bg="darkgreen", font=("arial", 13, "bold"), fg="white")
        btnExitData.grid(row=0, column=20, columnspan=5, sticky=tk.W+tk.E, padx=5, pady=5)

       
        lblSearch = tk.Label(ButtonFrame, text="Search By", bg="red", font=("arial", 17, "bold"), fg="white")
        lblSearch.grid(row=0, column=25, sticky=tk.W, padx=5, pady=5)

        serch_combo = ttk.Combobox(ButtonFrame, width=12, font=("arial", 17, "bold"), state="readonly")
        serch_combo["values"] = ("Ref", "Medname", "Lot")
        serch_combo.grid(row=0, column=30, sticky=tk.W, padx=5, pady=5)
        serch_combo.current(0)

        txtSerch = tk.Entry(ButtonFrame, bd=3, relief=tk.RIDGE, width=12, font=("arial", 17, "bold"))
        txtSerch.grid(row=0, column=35, sticky=tk.W, padx=5, pady=5)

        btnSearchData = tk.Button(ButtonFrame, text="SEARCH", bg="darkgreen", font=("arial", 13, "bold"), fg="white")
        btnSearchData.grid(row=0, column=40, columnspan=5, sticky=tk.W+tk.E, padx=5, pady=5)

        btnShowAllData = tk.Button(ButtonFrame, text="SHOW ALL", bg="darkgreen", font=("arial", 13, "bold"), fg="white")
        btnShowAllData.grid(row=0, column=45, columnspan=5, sticky=tk.W+tk.E, padx=5, pady=5)
        
         #+++++++++++++++++++++++++++++Label and entry ++++++++++++++++++++++++++++++++++===
        


if __name__ == "__main__":
    root = tk.Tk()  
    obj = PharmacyManagementSystem(root)
    root.mainloop()
