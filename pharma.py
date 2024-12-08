from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")
        
        lbltitle = Label(self.root, text=" PHARMACY MANAGEMENT SYSTEM ", 
                         bd=15, relief=RIDGE, bg='white', fg="darkgreen", 
                         font=("times new roman", 40, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)
        
        # Load and resize the image
        img1 = Image.open(r"C:\Users\Glady Manyama\Desktop\pharma\logo.png")
        img1 = img1.resize((65, 65), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create a button and place it
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=65, y=20)
        #=============================DataFrame===================================
        DataFrame=Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1280, height=400)
        
        
        # Left DataFrame (adjust width and positioning)
        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information", 
                           fg="darkgreen", font=("Arial", 12, "bold"))
        DataFrameLeft.place(x=10, y=5, width=720, height=350)  # Slightly increased width and added left margin

        # Right DataFrame (adjust width and positioning)
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", 
                            fg="darkgreen", font=("Arial", 12, "bold"))
        DataFrameRight.place(x=750, y=5, width=470, height=350)  # Positioned it right next to DataFrameLeft with small spacing
        
        #=======================ButtonFrame=========================================
        ButtonFrame=Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1280, height=65)
        
        #================MainFrame==================================================
        btnAddData=Button(ButtonFrame, text="Medicine Add", font=("arial", 12, "bold"), bg="darkgreen", fg="white")
        btnAddData.grid(row=0, column=0)
        
        btnUpdateMed=Button(ButtonFrame, text="UPDATE", font=("arial", 12, "bold"), width=10, bg="darkgreen", fg="white")
        btnUpdateMed.grid(row=0, column=1)
        
        btnDeleteMed=Button(ButtonFrame, text="DELETE", font=("arial", 12, "bold"), width=10,bg="red", fg="white")
        btnDeleteMed.grid(row=0, column=2)
        
        btnRestMed=Button(ButtonFrame, text="RESET", font=("arial", 12, "bold"), width=10,bg="darkgreen", fg="white")
        btnRestMed.grid(row=0, column=3)
        
        btnExitMed=Button(ButtonFrame, text="EXIT", font=("arial", 12, "bold"), width=10,bg="red", fg="white")
        btnExitMed.grid(row=0, column=4)
        
        
        #==============search By=====================
        lblSearch=Label(ButtonFrame, font=("arial", 17, "bold"), text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)
        
        search_combo=ttk.Combobox(ButtonFrame, width=12, font=("arial", 17, "bold"), state="readonly")
        search_combo["values"]=("Ref", "Medname", "Lot")
        search_combo.grid(row=0, column=6)
        search_combo.current(0)
        
        
        txtSearch=Entry(ButtonFrame, bd=3, relief=RIDGE, width=10, font=("arial", 17, "bold"))
        txtSearch.grid(row=0, column=7)
        
        searchBtn=Button(ButtonFrame, text="SEARCH", font=("arial", 13, "bold"), width=10, bg="darkgreen", fg="white")
        searchBtn.grid(row=0, column=8)
        
        showAll=Button(ButtonFrame, text="SHOW ALL", font=("arial", 13, "bold"), width=10, bg="darkgreen", fg="white")
        showAll.grid(row=0, column=9)
        
        #================labels and Entries=================
        lblrefno= Label(DataFrameLeft,font=("arial", 10, "bold"), text="Reference No", padx=2, bg="red", fg="white" )
        lblrefno.grid(row=0, column=0, sticky=W)
        
        ref_combo=ttk.Combobox(DataFrameLeft, width=18, font=("arial", 10, "bold"), state="readonly")
        ref_combo["values"]=("Ref", "Medname", "Lot")
        ref_combo.grid(row=0, column=1, padx=5, pady=5)
        ref_combo.current(0)
        
        # Company Name Entry
        tk.Label(DataFrameLeft,text="Company Name:",font=("arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W)
        company_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=18)
        company_entry.grid(row=1, column=1, padx=5, pady=5)

        # Type of Medicine Dropdown (Combobox)
        tk.Label(DataFrameLeft, text="Type of Medicine:", font=("arial", 10, "bold")).grid(row=1, column=0, sticky=tk.W)
        type_of_medicine_combo = ttk.Combobox(
            DataFrameLeft, 
            values=[
                "Tablet", 
                "Capsule", 
                "Syrup", 
                "Injection", 
                "Inhaler", 
                "Ointment", 
                "Powder", 
                "Cream", 
                "Drops", 
                "Suppository", 
                "Gel", 
                "Spray", 
                "Lozenge", 
                "Patch", 
                "Solution", 
                "Granules", 
                "Pill", 
                "Lotion", 
                "Suspension", 
                "Emulsion"
                ], 
            font=("arial", 10), 
            width=18,
            state="readonly"
            )
        type_of_medicine_combo.grid(row=1, column=1, padx=5, pady=5)
        type_of_medicine_combo.current(0)  # Set default selection to "Tablet"
        
        # Medicine Name Dropdown (Combobox)
        tk.Label(DataFrameLeft, text="Medicine Name:", font=("arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W)
        medicine_name_combo = ttk.Combobox(
            DataFrameLeft, 
            values=[
                "Paracetamol", 
                "Ibuprofen", 
                "Amoxicillin", 
                "Ciprofloxacin", 
                "Metformin",
                "Aspirin", 
                "Omeprazole", 
                "Azithromycin", 
                "Doxycycline", 
                "Clarithromycin", 
                "Prednisolone", 
                "Diclofenac", 
                "Losartan", 
                "Atorvastatin", 
                "Ranitidine", 
                "Cetirizine", 
                "Levothyroxine", 
                "Insulin", 
                "Salbutamol"
                ], 
            font=("arial", 10), 
            width=18,
            state="readonly"
            )
        medicine_name_combo.grid(row=2, column=1,padx=5, pady=5)
        medicine_name_combo.current(0)  # Set default selection to "Paracetamol"


        # Lot No Entry
        tk.Label(DataFrameLeft, text="Lot No:", font=("arial", 10, "bold")).grid(row=3, column=0, sticky=tk.W)
        lot_no_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        lot_no_entry.grid(row=3, column=1,padx=5, pady=5)

        # Issue Date Entry
        tk.Label(DataFrameLeft, text="Issue Date:", font=("arial", 10, "bold")).grid(row=4, column=0, sticky=tk.W)
        issue_date_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        issue_date_entry.grid(row=4, column=1,padx=5, pady=5)

        # Expiry Date Entry
        tk.Label(DataFrameLeft, text="Expiry Date:", font=("arial", 10, "bold")).grid(row=5, column=0, sticky=tk.W)
        exp_date_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        exp_date_entry.grid(row=5, column=1,padx=5, pady=5)

        # Uses Entry
        tk.Label(DataFrameLeft, text="Uses:", font=("arial", 10, "bold")).grid(row=6, column=0, sticky=tk.W)
        uses_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        uses_entry.grid(row=6, column=1,padx=5, pady=5)

        # Side Effects Entry
        tk.Label(DataFrameLeft, text="Side Effects:", font=("arial", 10, "bold")).grid(row=7, column=0, sticky=tk.W)
        side_effects_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        side_effects_entry.grid(row=7, column=1,padx=5, pady=5)
        
        # New fields on the right side within the same DataFrame
        tk.Label(DataFrameLeft, text="Precautions & Warnings:", font=("arial", 10, "bold")).grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)
        prec_warnings_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        prec_warnings_entry.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(DataFrameLeft, text="Dosage:", font=("arial", 10, "bold")).grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)
        dosage_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        dosage_entry.grid(row=1, column=3, padx=10, pady=5)

        tk.Label(DataFrameLeft, text="Tablet Price:", font=("arial", 10, "bold")).grid(row=2, column=2, sticky=tk.W, padx=10, pady=5)
        tablet_price_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        tablet_price_entry.grid(row=2, column=3, padx=10, pady=5)

        tk.Label(DataFrameLeft, text="Product Quantity:", font=("arial", 10, "bold")).grid(row=3, column=2, sticky=tk.W, padx=10, pady=5)
        product_quantity_entry = ttk.Entry(DataFrameLeft, font=("arial", 10, "bold"), width=20)
        product_quantity_entry.grid(row=3, column=3, padx=10, pady=5)
        
        
        
        img2 = Image.open(r"C:\Users\Glady Manyama\Desktop\pharma\tab.jpg")
        img2 = img2.resize((150, 135), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image=self.photoimg2, borderwidth=0)
        b1.place(x=720, y=330)
        
        img3 = Image.open(r"C:\Users\Glady Manyama\Desktop\pharma\tab.jpg")
        img3 = img3.resize((150, 135), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=620, y=330)
        

if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
