from tkinter import *
from PIL import ImageTk,Image
import pyodbc


# TODO DEKLARASI ROOT
root = Tk()
root.title("TOUR GUIDE")
root.geometry("600x345")

# TODO DEKLARASI MENU
my_menu= Menu(root)
root.config(menu=my_menu)

# TODO DEKLARASI DATABASE
#connect DB
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                    'Database=TourGuide;'
                    'Trusted_Connection=yes;')

#Create Cursor
c = conn.cursor()

#!==================================================================================FRAME INSERT TRANSAKSI

def Transaksi():
    hide_all_frame()
    Transaksi_frame.pack()

    # TODO =============================================  SUBMIT TRANSAKSI
    def submit():
        #deklarasi
        IT = IT_transaksi.get()
        PE = PE_transaksi.get()
        GU = GU_transaksi.get()
        PA = PA_transaksi.get()
        TR = TR_transaksi.get()
        Tanggal = Tanggal_transaksi.get()
        JS = Jenis.get()

        #connect DB
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                            'Database=TourGuide;'
                            'Trusted_Connection=yes;')
        #Create Cursor
        c = conn.cursor()

        c.execute("SET DATEFORMAT dmy; INSERT INTO Transaksi VALUES (?,?,?,?,?,?,?)", IT, PE, GU, PA, TR, Tanggal, JS)

        #Commit changes
        conn.commit()
        #Close Connection
        conn.close()

        #clear text box
        IT_transaksi.delete(0, END)
        PE_transaksi.delete(0, END)
        GU_transaksi.delete(0, END)
        PA_transaksi.delete(0, END)
        TR_transaksi.delete(0, END)
        Tanggal_transaksi.delete(0, END)
        Jenis.delete(0, END)

    # TODO =============================================  UPDATE TRANSAKSI
    def update():
        #deklarasi
        IT = IT_transaksi.get()
        PE = PE_transaksi.get()
        GU = GU_transaksi.get()
        PA = PA_transaksi.get()
        TR = TR_transaksi.get()
        Tanggal = Tanggal_transaksi.get()
        JS = Jenis.get()

        #connect DB
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                            'Database=TourGuide;'
                            'Trusted_Connection=yes;')
        #Create Cursor
        c = conn.cursor()

        c.execute("SET DATEFORMAT dmy; EXEC SPtransaksi ?, ?, ?, ?, ?, ?",IT, PE, GU, PA, TR, Tanggal, JS)

        #Commit changes
        conn.commit()
        #Close Connection
        conn.close()

        #clear text box
        IT_transaksi.delete(0, END)
        PE_transaksi.delete(0, END)
        GU_transaksi.delete(0, END)
        PA_transaksi.delete(0, END)
        TR_transaksi.delete(0, END)
        Tanggal_transaksi.delete(0, END)
        Jenis.delete(0, END)

    # TODO ========================================== INTERFACE TRANSAKSI
    # TODO JUDUL HOME ROOT
    judul = Label(Transaksi_frame, text="ADMIN TOUR GUIDE", font=("Open Sans Semibold", 19, "bold"))
    judul.grid(row=0, column=0,pady=5, ipadx=100, columnspan = 4)
    inputlable = Label(Transaksi_frame, text="Input Transaction", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=2, column=0,padx=0, ipadx=0)

    # TODO LABEL DATA TRANSAKSI
    IT_transaksiL = Label(Transaksi_frame, text="ID Transaksi (ITxxx)")
    IT_transaksiL.grid(row=3, column=0, sticky = W, padx=5)
    PE_transaksiL = Label(Transaksi_frame, text="ID Pelanggan (PExxx)")
    PE_transaksiL.grid(row=4, column=0, sticky = W, padx=5)
    GU_transaksiL = Label(Transaksi_frame, text="ID Guide (GUxxx)")
    GU_transaksiL.grid(row=5, column=0, sticky = W, padx=5)
    PA_transaksiL = Label(Transaksi_frame, text="ID Paket (PAxxx)")
    PA_transaksiL.grid(row=6, column=0, sticky = W, padx=5)
    TR_transaksiL = Label(Transaksi_frame, text="ID Transportasi (TRxxx)")
    TR_transaksiL.grid(row=7, column=0, sticky = W, padx=5)
    Tanggal_transaksiL = Label(Transaksi_frame, text="Tanggal Wisata (dd/mm/yyyy)")
    Tanggal_transaksiL.grid(row=8, column=0, sticky = W, padx=5)
    JenisL = Label(Transaksi_frame, text="Jenis Pembayaran")
    JenisL.grid(row=9, column=0, sticky = W, padx=5)

    # TODO INPUT DATA TRANSAKSI
    IT_transaksi = Entry(Transaksi_frame, width=30)
    IT_transaksi.grid(row=3, column=1, padx=30)
    PE_transaksi = Entry(Transaksi_frame, width=30)
    PE_transaksi.grid(row=4, column=1)
    GU_transaksi = Entry(Transaksi_frame, width=30)
    GU_transaksi.grid(row=5, column=1)
    PA_transaksi = Entry(Transaksi_frame, width=30)
    PA_transaksi.grid(row=6, column=1)
    TR_transaksi = Entry(Transaksi_frame, width=30)
    TR_transaksi.grid(row=7, column=1)
    Tanggal_transaksi = Entry(Transaksi_frame, width=30)
    Tanggal_transaksi.grid(row=8, column=1)
    Jenis = Entry(Transaksi_frame, width=30)
    Jenis.grid(row=9, column=1)

    # TODO SUBMIT BUTTON
    submit_btn = Button(Transaksi_frame, text="INPUT", command = submit)
    submit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # TODO UPDATE BUTTON
    update_btn = Button(Transaksi_frame, text="UPDATE", command = update)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#! ==========================================================================FRAME INSERT ALAMAT PELANGGAN
def Alamat():
    hide_all_frame()
    Alamat_frame.pack()

    # TODO =============================================  SUBMIT Alamat Pelanggan
    def submit():
        #deklarasi
        ID = ID_Alamat.get()
        JA = Jalan_Alamat.get()
        PO = Pos_Alamat.get()
        KO = Kota_Alamat.get()
        KA = Kabupaten_Alamat.get()


        #connect DB
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                            'Database=TourGuide;'
                            'Trusted_Connection=yes;')
        #Create Cursor
        c = conn.cursor()

        c.execute("INSERT INTO PAlamat VALUES (?,?,?,?,?)", ID, JA, PO, KO, KA)

        #Commit changes
        conn.commit()
        #Close Connection
        conn.close()

        #clear text box
        ID_Alamat.delete(0, END)
        Jalan_Alamat.delete(0, END)
        Pos_Alamat.delete(0, END)
        Kota_Alamat.delete(0, END)
        Kabupaten_Alamat.delete(0, END)

    # TODO =============================================  UPDATE Alamat Pelanggan
    def update():
        #deklarasi
        ID = ID_Alamat.get()
        JA = Jalan_Alamat.get()
        PO = Pos_Alamat.get()
        KO = Kota_Alamat.get()
        KA = Kabupaten_Alamat.get()


        #connect DB
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                            'Database=TourGuide;'
                            'Trusted_Connection=yes;')
        #Create Cursor
        c = conn.cursor()


        c.execute("set nocount on;EXEC SPAlamat ?, ?, ?, ?, ?", ID, JA, PO, KO, KA)


        #Commit changes
        conn.commit()

        #Close Connection
        conn.close()

        #clear text box
        ID_Alamat.delete(0, END)
        Jalan_Alamat.delete(0, END)
        Pos_Alamat.delete(0, END)
        Kota_Alamat.delete(0, END)
        Kabupaten_Alamat.delete(0, END)


    # TODO ======================================================interface Alamat Pelanggan
    inputlable = Label(Alamat_frame, text="Input Alamat Pelanggan", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=2)

    # TODO LABEL DATA  Alamat Pelanggan
    ID_AlamatL = Label(Alamat_frame, text="ID Alamat Pelanggan (ALxxx)")
    ID_AlamatL.grid(row=2, column=0, sticky = W, padx=5)
    Jalan_AlamatL = Label(Alamat_frame, text="Jalan")
    Jalan_AlamatL.grid(row=3, column=0, sticky = W, padx=5)
    Pos_AlamatL = Label(Alamat_frame, text="Kode Pos")
    Pos_AlamatL.grid(row=4, column=0, sticky = W, padx=5)
    Kota_AlamatL = Label(Alamat_frame, text="Kota")
    Kota_AlamatL.grid(row=5, column=0, sticky = W, padx=5)
    Kabupaten_AlamatL = Label(Alamat_frame, text="Kabupaten")
    Kabupaten_AlamatL.grid(row=6, column=0, sticky = W, padx=5)

    # TODO INPUT DATA Alamat Pelanggan
    ID_Alamat = Entry(Alamat_frame, width=30)
    ID_Alamat.grid(row=2, column=1, padx=30)
    Jalan_Alamat = Entry(Alamat_frame, width=30)
    Jalan_Alamat.grid(row=3, column=1)
    Pos_Alamat = Entry(Alamat_frame, width=30)
    Pos_Alamat.grid(row=4, column=1)
    Kota_Alamat = Entry(Alamat_frame, width=30)
    Kota_Alamat.grid(row=5, column=1)
    Kabupaten_Alamat = Entry(Alamat_frame, width=30)
    Kabupaten_Alamat.grid(row=6, column=1)

    # TODO SUBMIT BUTTON
    submit_btn = Button(Alamat_frame, text="INPUT", command = submit)
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # TODO UPDATE BUTTON
    update_btn = Button(Alamat_frame, text="UPDATE", command = update)
    update_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#! ================================================================================FRAME INSERT PELANGGAN

def Pelanggan():
    hide_all_frame()
    Pelanggan_frame.pack()

    # TODO =============================================  SUBMIT Pelanggan
    def submit():
        #deklarasi
        ID = ID_Pelanggan.get()
        NA = Nama_Pelanggan.get()
        PO = Phone_Pelanggan.get()
        SX = Sex_Pelanggan.get()
        TA = Tanggal_Pelanggan.get()
        AL = Alamat_Pelanggan.get()

        #connect DB
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                            'Database=TourGuide;'
                            'Trusted_Connection=yes;')
        #Create Cursor
        c = conn.cursor()

        c.execute("SET DATEFORMAT dmy; INSERT INTO Pelanggan VALUES (?,?,?,?,?,?)", ID, NA, PO, SX, TA, AL)

        #Commit changes
        conn.commit()
        #Close Connection
        conn.close()

        #cleare text box
        ID_Pelanggan.delete(0, END)
        Nama_Pelanggan.delete(0, END)
        Phone_Pelanggan.delete(0, END)
        Sex_Pelanggan.delete(0, END)
        Tanggal_Pelanggan.delete(0, END)
        Alamat_Pelanggan.delete(0, END)

    # TODO =============================================  UPDATE Pelanggan
    def update():
        #deklarasi
        ID = ID_Pelanggan.get()
        NA = Nama_Pelanggan.get()
        PO = Phone_Pelanggan.get()
        SX = Sex_Pelanggan.get()
        TA = Tanggal_Pelanggan.get()
        AL = Alamat_Pelanggan.get()

        #connect DB
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                            'Database=TourGuide;'
                            'Trusted_Connection=yes;')
        #Create Cursor
        c = conn.cursor()

        c.execute("SET DATEFORMAT dmy; EXEC SPPelanggan ?,?,?,?,?,?", ID, NA, PO, SX, TA, AL)

        #Commit changes
        conn.commit()
        #Close Connection
        conn.close()

        #cleare text box
        ID_Pelanggan.delete(0, END)
        Nama_Pelanggan.delete(0, END)
        Phone_Pelanggan.delete(0, END)
        Sex_Pelanggan.delete(0, END)
        Tanggal_Pelanggan.delete(0, END)
        Alamat_Pelanggan.delete(0, END)



    # TODO ======================================================interface Pelanggan
    inputlable = Label(Pelanggan_frame, text="Input Pelanggan", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=2)

    # TODO LABEL DATA Pelanggan
    ID_PelangganL = Label(Pelanggan_frame, text="ID Pelanggan (PExxx)")
    ID_PelangganL.grid(row=2, column=0, sticky = W, padx=5)
    Nama_PelangganL = Label(Pelanggan_frame, text="Nama ")
    Nama_PelangganL.grid(row=3, column=0, sticky = W, padx=5)
    Phone_PelangganL = Label(Pelanggan_frame, text="Phone ")
    Phone_PelangganL.grid(row=4, column=0, sticky = W, padx=5)
    Sex_PelangganL = Label(Pelanggan_frame, text="Sex (Pria/Wanita)")
    Sex_PelangganL.grid(row=5, column=0, sticky = W, padx=5)
    Tanggal_PelangganL = Label(Pelanggan_frame, text="Tangal lahir (dd/mm/yyyy)")
    Tanggal_PelangganL.grid(row=6, column=0, sticky = W, padx=5)
    Alamat_PelangganL = Label(Pelanggan_frame, text="ID Alamat (ALxxx)")
    Alamat_PelangganL.grid(row=7, column=0, sticky = W, padx=5)

    # TODO INPUT DATA Pelanggan
    ID_Pelanggan = Entry(Pelanggan_frame, width=30)
    ID_Pelanggan.grid(row=2, column=1, padx=30)
    Nama_Pelanggan = Entry(Pelanggan_frame, width=30)
    Nama_Pelanggan.grid(row=3, column=1)
    Phone_Pelanggan = Entry(Pelanggan_frame, width=30)
    Phone_Pelanggan.grid(row=4, column=1)
    Sex_Pelanggan = Entry(Pelanggan_frame, width=30)
    Sex_Pelanggan.grid(row=5, column=1)
    Tanggal_Pelanggan = Entry(Pelanggan_frame, width=30)
    Tanggal_Pelanggan.grid(row=6, column=1)
    Alamat_Pelanggan = Entry(Pelanggan_frame, width=30)
    Alamat_Pelanggan.grid(row=7, column=1)

    # TODO SUBMIT BUTTON
    submit_btn = Button(Pelanggan_frame, text="INPUT", command = submit)                                                              
    submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # TODO UPDATE BUTTON
    update_btn = Button(Pelanggan_frame, text="UPDATE", command = update)
    update_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)





#! ================================================================================ VIEW Alamat PELANGGAN
def VAlamat():
    ViewA = Tk()
    ViewA.title("TOUR GUIDE - Data Alamat Pelanggan")
    ViewA.geometry("600x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show alamat pelanggan
    #execute show
    c.execute("SELECT * FROM ViewCustomerAlamat")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''
    print_records4 = ''

    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += str(record[2]) + "\n"
        print_records3 += str(record[3]) + "\n"
        print_records4 += str(record[4]) + "\n"

    inputlable = Label(ViewA, text="DATA ALAMAT PELANGGAN", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=5)

    ID_AlamatL = Label(ViewA, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    ID_AlamatL.grid(row=2, column=0, sticky = W, pady=5)
    Jalan_AlamatL = Label(ViewA, text="Jalan", font=("Open Sans Semibold",10,"bold"),width = 20)
    Jalan_AlamatL.grid(row=2, column=1, sticky = W, pady=5)
    Pos_AlamatL = Label(ViewA, text="Kode Pos", font=("Open Sans Semibold",10,"bold"),width = 10)
    Pos_AlamatL.grid(row=2, column=2, sticky = W, pady=5)
    Kota_AlamatL = Label(ViewA, text="Kota", font=("Open Sans Semibold",10,"bold"),width = 20)
    Kota_AlamatL.grid(row=2, column=3, sticky = W, pady=5)
    Kabupaten_AlamatL = Label(ViewA, text="Kabupaten", font=("Open Sans Semibold",10,"bold"),width = 20)
    Kabupaten_AlamatL.grid(row=2, column=4, sticky = W, pady=5)

    query_label = Label(ViewA, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(ViewA, text= print_records1, width = 20)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(ViewA, text= print_records2, width = 10)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(ViewA, text= print_records3, width = 20)
    query_label.grid(row = 3, column=3, pady=2)
    query_label = Label(ViewA, text= print_records4, width = 20)
    query_label.grid(row = 3, column=4, pady=2)

    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    ViewA.mainloop()



#! =======================================================================================  VIEW PELANGGAN
def VPlenggan():
    ViewP = Tk()
    ViewP.title("TOUR GUIDE - Data Pelanggan")
    ViewP.geometry("625x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show pelanggan
    #execute show
    c.execute("SELECT * FROM ViewPelanggan")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''
    print_records4 = ''
    print_records5 = ''

    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += "0"+str(record[2]) + "\n"
        print_records3 += str(record[3]) + "\n"
        print_records4 += str(record[4]) + "\n"
        print_records5 += str(record[5]) + "\n"

    inputlable = Label(ViewP, text="DATA PELANGGAN", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=6)

    ID_PelangganL = Label(ViewP, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    ID_PelangganL.grid(row=2, column=0, sticky = W, pady=5)
    Nama_PelangganL = Label(ViewP, text="Nama", font=("Open Sans Semibold",10,"bold"),width = 20)
    Nama_PelangganL.grid(row=2, column=1, sticky = W, pady=5)
    Phone_PelangganL = Label(ViewP, text="Phone ", font=("Open Sans Semibold",10,"bold"),width = 18)
    Phone_PelangganL.grid(row=2, column=2, sticky = W, pady=5)
    Sex_PelangganL = Label(ViewP, text="Sex", font=("Open Sans Semibold",10,"bold"),width = 5)
    Sex_PelangganL.grid(row=2, column=3, sticky = W, pady=5)
    Tanggal_PelangganL = Label(ViewP, text="Tangal lahir", font=("Open Sans Semibold",10,"bold"),width = 15)
    Tanggal_PelangganL.grid(row=2, column=4, sticky = W, pady=5)
    Alamat_PelangganL = Label(ViewP, text="ID Alamat", font=("Open Sans Semibold",10,"bold"),width = 10)
    Alamat_PelangganL.grid(row=2, column=5, sticky = W, pady=5)

    query_label = Label(ViewP, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(ViewP, text= print_records1, width = 20)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(ViewP, text= print_records2, width = 18)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(ViewP, text= print_records3, width = 5)
    query_label.grid(row = 3, column=3, pady=2)
    query_label = Label(ViewP, text= print_records4, width = 10)
    query_label.grid(row = 3, column=4, pady=2)
    query_label = Label(ViewP, text= print_records5, width = 5)
    query_label.grid(row = 3, column=5, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    ViewP.mainloop()


#! ==================================================================================  VIEW TRANSPORTASI
def VTransportasi():
    View = Tk()
    View.title("TOUR GUIDE - Data Transportasi")
    View.geometry("875x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show Transportasi
    #execute show
    c.execute("SELECT * FROM ViewTransportasi")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''
    print_records4 = ''
    print_records5 = ''

    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += str(record[2]) + "\n"
        print_records3 += "0"+str(record[3]) + "\n"
        print_records4 += str(record[4]) + "\n"
        print_records5 += str(record[5]) + "\n"

    inputlable = Label(View, text="DATA TRANSPORTASI", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=6)

    ID_TransportasiL = Label(View, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    ID_TransportasiL.grid(row=2, column=0, sticky = W, pady=5)
    Nama_TransportasiL = Label(View, text="Nama", font=("Open Sans Semibold",10,"bold"),width = 20)
    Nama_TransportasiL.grid(row=2, column=1, sticky = W, pady=5)
    Klasifikasi_TransportasiL = Label(View, text="Klasifikasi", font=("Open Sans Semibold",10,"bold"),width = 15)
    Klasifikasi_TransportasiL.grid(row=2, column=2, sticky = W, pady=5)
    Phone_TransportasiL = Label(View, text="Phone", font=("Open Sans Semibold",10,"bold"),width = 18)
    Phone_TransportasiL.grid(row=2, column=3, sticky = W, pady=5)
    ALamat_TransportasiL = Label(View, text="Alamat", font=("Open Sans Semibold",10,"bold"),width = 30)
    ALamat_TransportasiL.grid(row=2, column=4, sticky = W, pady=5)
    Harga_TransportasiL = Label(View, text="Harga", font=("Open Sans Semibold",10,"bold"),width = 15)
    Harga_TransportasiL.grid(row=2, column=5, sticky = W, pady=5)

    query_label = Label(View, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 20)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(View, text= print_records2, width = 15)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(View, text= print_records3, width = 18)
    query_label.grid(row = 3, column=3, pady=2)
    query_label = Label(View, text= print_records4, width = 30)
    query_label.grid(row = 3, column=4, pady=2)
    query_label = Label(View, text= print_records5, width = 15)
    query_label.grid(row = 3, column=5, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()


#! =======================================================================================  VIEW GUIDE
def VGuide():
    View = Tk()
    View.title("TOUR GUIDE - Data Guide")
    View.geometry("760x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show Guide
    #execute show
    c.execute("SELECT * FROM ViewGuide")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''
    print_records4 = ''
    print_records5 = ''
    print_records6 = ''

    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += "0"+str(record[2]) + "\n"
        print_records3 += str(record[3]) + "\n"
        print_records4 += str(record[4]) + "\n"
        print_records5 += str(record[5]) + "\n"
        print_records6 += str(record[6]) + "\n"

    inputlable = Label(View, text="DATA GUIDE", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=7)

    ID_GuideL = Label(View, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    ID_GuideL.grid(row=2, column=0, sticky = W, pady=5)
    Nama_GuideL = Label(View, text="Nama", font=("Open Sans Semibold",10,"bold"),width = 20)
    Nama_GuideL.grid(row=2, column=1, sticky = W, pady=5)
    Phone_GuideL = Label(View, text="Phone", font=("Open Sans Semibold",10,"bold"),width = 18)
    Phone_GuideL.grid(row=2, column=2, sticky = W, pady=5)
    Sex_GuideL = Label(View, text="Sex", font=("Open Sans Semibold",10,"bold"),width = 5)
    Sex_GuideL.grid(row=2, column=3, sticky = W, pady=5)
    Tanggal_GuideL = Label(View, text="Tanggal Lahir", font=("Open Sans Semibold",10,"bold"),width = 15)
    Tanggal_GuideL.grid(row=2, column=4, sticky = W, pady=5)
    Alamat_GuideL = Label(View, text="Alamat", font=("Open Sans Semibold",10,"bold"),width = 30)
    Alamat_GuideL.grid(row=2, column=5, sticky = W, pady=5)
    Gaji_GuideL = Label(View, text="Gaji", font=("Open Sans Semibold",10,"bold"),width = 15)
    Gaji_GuideL.grid(row=2, column=6, sticky = W, pady=5)

    query_label = Label(View, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 20)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(View, text= print_records2, width = 18)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(View, text= print_records3, width = 5)
    query_label.grid(row = 3, column=3, pady=2)
    query_label = Label(View, text= print_records4, width = 15)
    query_label.grid(row = 3, column=4, pady=2)
    query_label = Label(View, text= print_records5, width = 30)
    query_label.grid(row = 3, column=5, pady=2)
    query_label = Label(View, text= print_records6, width = 15)
    query_label.grid(row = 3, column=6, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()


#! ==================================================================================  VIEW Wisata
def VWisata():
    View = Tk()
    View.title("TOUR GUIDE - Data Wisata")
    View.geometry("575x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show wisata
    #execute show
    c.execute("SELECT * FROM ViewWisata")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''

    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += str(record[2]) + "\n"
        print_records3 += str(record[3]) + "\n"


    inputlable = Label(View, text="DATA WISATA", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=4)

    ID_WisataL = Label(View, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    ID_WisataL.grid(row=2, column=0, sticky = W, pady=5)
    Nama_WisataL = Label(View, text="Nama", font=("Open Sans Semibold",10,"bold"),width = 20)
    Nama_WisataL.grid(row=2, column=1, sticky = W, pady=5)
    Alamat_WisataL = Label(View, text="Alamat", font=("Open Sans Semibold",10,"bold"),width = 30)
    Alamat_WisataL.grid(row=2, column=2, sticky = W, pady=5)
    Harga_WisataL = Label(View, text="Harga", font=("Open Sans Semibold",10,"bold"),width = 15)
    Harga_WisataL.grid(row=2, column=3, sticky = W, pady=5)


    query_label = Label(View, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 20)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(View, text= print_records2, width = 30)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(View, text= print_records3, width = 15)
    query_label.grid(row = 3, column=3, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()

#! ==================================================================================  VIEW Penginapan
def VPenginapan():
    View = Tk()
    View.title("TOUR GUIDE - Data Penginapan")
    View.geometry("625x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show Penginapan
    #execute show
    c.execute("SELECT * FROM ViewPenginapan")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''
    print_records4 = ''


    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += str(record[2]) + "\n"
        print_records3 += "0"+str(record[3]) + "\n"
        print_records4 += str(record[4]) + "\n"

    inputlable = Label(View, text="DATA PENGINAPAN", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=5)

    ID_PenginapanL = Label(View, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    ID_PenginapanL.grid(row=2, column=0, sticky = W, pady=5)
    Nama_PenginapanL = Label(View, text="Nama", font=("Open Sans Semibold",10,"bold"),width = 20)
    Nama_PenginapanL.grid(row=2, column=1, sticky = W, pady=5)
    Alamat_PenginapanL = Label(View, text="Alamat", font=("Open Sans Semibold",10,"bold"),width = 30)
    Alamat_PenginapanL.grid(row=2, column=2, sticky = W, pady=5)
    Phone_PenginapanL = Label(View, text="Phone", font=("Open Sans Semibold",10,"bold"),width = 18)
    Phone_PenginapanL.grid(row=2, column=3, sticky = W, pady=5)
    Harga_PenginapanL = Label(View, text="Harga", font=("Open Sans Semibold",10,"bold"),width = 15)
    Harga_PenginapanL.grid(row=2, column=4, sticky = W, pady=5)

    query_label = Label(View, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 20)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(View, text= print_records2, width = 30)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(View, text= print_records3, width = 18)
    query_label.grid(row = 3, column=3, pady=2)
    query_label = Label(View, text= print_records4, width = 15)
    query_label.grid(row = 3, column=4, pady=2)

    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()

#! ==================================================================================  VIEW Paket
def VPaket():
    View = Tk()
    View.title("TOUR GUIDE - Data Paket")
    View.geometry("425x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show Paket
    #execute show
    c.execute("SELECT * FROM ViewPaket")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''


    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += str(record[2]) + "\n"
        print_records3 += str(record[3]) + "\n"

    inputlable = Label(View, text="DATA PAKET", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=5)

    ID_PaketL = Label(View, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    ID_PaketL.grid(row=2, column=0, sticky = W, pady=5)
    IDWisata_PaketL = Label(View, text="Wisata", font=("Open Sans Semibold",10,"bold"),width = 15)
    IDWisata_PaketL.grid(row=2, column=1, sticky = W, pady=5)
    IDPenginapan_PaketL = Label(View, text="Penginapan", font=("Open Sans Semibold",10,"bold"),width = 15)
    IDPenginapan_PaketL.grid(row=2, column=2, sticky = W, pady=5)
    Harga_PaketL = Label(View, text="Harga", font=("Open Sans Semibold",10,"bold"),width = 15)
    Harga_PaketL.grid(row=2, column=3, sticky = W, pady=5)

    query_label = Label(View, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 10)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(View, text= print_records2, width = 10)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(View, text= print_records3, width = 15)
    query_label.grid(row = 3, column=3, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()

#! =======================================================================================  VIEW Transaksi
def VTransaksi():
    View = Tk()
    View.title("TOUR GUIDE - Data Transaksi")
    View.geometry("780x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show transaksi
    #execute show
    c.execute("SELECT * FROM ViewTransaksi")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''
    print_records4 = ''
    print_records5 = ''
    print_records6 = ''

    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += str(record[2]) + "\n"
        print_records3 += str(record[3]) + "\n"
        print_records4 += str(record[4]) + "\n"
        print_records5 += str(record[5]) + "\n"
        print_records6 += str(record[6]) + "\n"

    inputlable = Label(View, text="DATA TRANSAKSI", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=7)

    IT_transaksiL = Label(View, text="ID", font=("Open Sans Semibold",10,"bold"),width = 5)
    IT_transaksiL.grid(row=2, column=0, sticky = W, pady=5)
    PE_transaksiL = Label(View, text="ID Pelanggan", font=("Open Sans Semibold",10,"bold"),width = 15)
    PE_transaksiL.grid(row=2, column=1, sticky = W, pady=5)
    GU_transaksiL = Label(View, text="ID Guide", font=("Open Sans Semibold",10,"bold"),width = 15)
    GU_transaksiL.grid(row=2, column=2, sticky = W, pady=5)
    PA_transaksiL = Label(View, text="ID Paket", font=("Open Sans Semibold",10,"bold"),width = 15)
    PA_transaksiL.grid(row=2, column=3, sticky = W, pady=5)
    TR_transaksiL = Label(View, text="ID Transportasi", font=("Open Sans Semibold",10,"bold"),width = 15)
    TR_transaksiL.grid(row=2, column=4, sticky = W, pady=5)
    Tanggal_transaksiL = Label(View, text="Tanggal Wisata", font=("Open Sans Semibold",10,"bold"),width = 15)
    Tanggal_transaksiL.grid(row=2, column=5, sticky = W, pady=5)
    PembayaranL = Label(View, text="Pembayaran", font=("Open Sans Semibold",10,"bold"),width = 15)
    PembayaranL.grid(row=2, column=6, sticky = W, pady=5)

    query_label = Label(View, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 15)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(View, text= print_records2, width = 15)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(View, text= print_records3, width = 15)
    query_label.grid(row = 3, column=3, pady=2)
    query_label = Label(View, text= print_records4, width = 15)
    query_label.grid(row = 3, column=4, pady=2)
    query_label = Label(View, text= print_records5, width = 15)
    query_label.grid(row = 3, column=5, pady=2)
    query_label = Label(View, text= print_records6, width = 15)
    query_label.grid(row = 3, column=6, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()

#! =======================================================================================  VIEW PENDAPATAN
def VPendapatan():
    View = Tk()
    View.title("TOUR GUIDE - Pendapatan Bulanan")
    View.geometry("1100x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show pendapatan
    #execute show
    c.execute("SELECT * FROM KeuntunganBulan")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''
    print_records2 = ''
    print_records3 = ''
    print_records4 = ''
    print_records5 = ''
    print_records6 = ''
    print_records7 = ''

    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"
        print_records2 += str(record[2]) + "\n"
        print_records3 += str(record[3]) + "\n"
        print_records4 += str(record[4]) + "\n"
        print_records5 += str(record[5]) + "\n"
        print_records6 += str(record[6]) + "\n"
        print_records7 += str(record[7]) + "\n"

    inputlable = Label(View, text="DATA PENDAPATAN BULANAN", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=7)

    IT_transasiL = Label(View, text="Tahun", font=("Open Sans Semibold",10,"bold"),width = 5)
    IT_transasiL.grid(row=2, column=0, sticky = W, pady=5)
    IT_transaksiL = Label(View, text="Bulan", font=("Open Sans Semibold",10,"bold"),width = 5)
    IT_transaksiL.grid(row=2, column=1, sticky = W, pady=5)
    PE_transaksiL = Label(View, text="Gaji Pegawai", font=("Open Sans Semibold",10,"bold"),width = 20)
    PE_transaksiL.grid(row=2, column=2, sticky = W, pady=5)
    GU_transaksiL = Label(View, text="Pengeluaran Transportasi", font=("Open Sans Semibold",10,"bold"),width = 20)
    GU_transaksiL.grid(row=2, column=3, sticky = W, pady=5)
    PA_transaksiL = Label(View, text="Pengeluaran Wisata", font=("Open Sans Semibold",10,"bold"),width = 20)
    PA_transaksiL.grid(row=2, column=4, sticky = W, pady=5)
    TR_transaksiL = Label(View, text="Pengeluaran Penginapan", font=("Open Sans Semibold",10,"bold"),width = 20)
    TR_transaksiL.grid(row=2, column=5, sticky = W, pady=5)
    Tanggal_transaksiL = Label(View, text="Pendapatan Kotor", font=("Open Sans Semibold",10,"bold"),width = 20)
    Tanggal_transaksiL.grid(row=2, column=6, sticky = W, pady=5)
    PendapatanBersih = Label(View, text="Pendapatan Bersih", font=("Open Sans Semibold",10,"bold"),width = 20)
    PendapatanBersih.grid(row=2, column=7, sticky = W, pady=5)

    query_label = Label(View, text= print_records, width = 5)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 5)
    query_label.grid(row = 3, column=1, pady=2)
    query_label = Label(View, text= print_records2, width = 20)
    query_label.grid(row = 3, column=2, pady=2)
    query_label = Label(View, text= print_records3, width = 20)
    query_label.grid(row = 3, column=3, pady=2)
    query_label = Label(View, text= print_records4, width = 20)
    query_label.grid(row = 3, column=4, pady=2)
    query_label = Label(View, text= print_records5, width = 20)
    query_label.grid(row = 3, column=5, pady=2)
    query_label = Label(View, text= print_records6, width = 20)
    query_label.grid(row = 3, column=6, pady=2)
    query_label = Label(View, text= print_records7, width = 20)
    query_label.grid(row = 3, column=7, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()



#! =======================================================================================  VIEW Guide Populer
def VGuideP():
    View = Tk()
    View.title("TOUR GUIDE - Guide Populer")
    View.geometry("250x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show pendapatan
    #execute show
    c.execute("EXEC GuideP")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''


    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"


    inputlable = Label(View, text="DATA GUIDE POPULER", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=2)

    IT_transasiL = Label(View, text="IdGuide", font=("Open Sans Semibold",10,"bold"),width = 10)
    IT_transasiL.grid(row=2, column=0, pady=5)
    IT_transaksiL = Label(View, text="Kepopuleran", font=("Open Sans Semibold",10,"bold"),width = 10)
    IT_transaksiL.grid(row=2, column=1, pady=5)


    query_label = Label(View, text= print_records, width = 10)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 10)
    query_label.grid(row = 3, column=1, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()




#! =======================================================================================  VIEW Pelanggan Populer
def VPelangganP():
    View = Tk()
    View.title("TOUR GUIDE - Pelanggan Populer")
    View.geometry("280x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show pendapatan
    #execute show
    c.execute("EXEC PelangganP")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''


    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"


    inputlable = Label(View, text="DATA PELANGGAN POPULER", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=2)

    IT_transasiL = Label(View, text="IdPelanggan", font=("Open Sans Semibold",10,"bold"),width = 10)
    IT_transasiL.grid(row=2, column=0, pady=5)
    IT_transaksiL = Label(View, text="Kepopuleran", font=("Open Sans Semibold",10,"bold"),width = 10)
    IT_transaksiL.grid(row=2, column=1, pady=5)


    query_label = Label(View, text= print_records, width = 10)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 10)
    query_label.grid(row = 3, column=1, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()




#! =======================================================================================  VIEW Transportasi Populer
def VTransportasiP():
    View = Tk()
    View.title("TOUR GUIDE - Transportasi Populer")
    View.geometry("300x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show pendapatan
    #execute show
    c.execute("EXEC TransportasiP")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''


    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"


    inputlable = Label(View, text="DATA TRANSPORTASI POPULER", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=2)

    IT_transasiL = Label(View, text="IdTransportasi", font=("Open Sans Semibold",10,"bold"),width = 15)
    IT_transasiL.grid(row=2, column=0, pady=5)
    IT_transaksiL = Label(View, text="Kepopuleran", font=("Open Sans Semibold",10,"bold"),width = 10)
    IT_transaksiL.grid(row=2, column=1, pady=5)


    query_label = Label(View, text= print_records, width = 15)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 10)
    query_label.grid(row = 3, column=1, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()




#! =======================================================================================  VIEW Paket Populer
def VPaketP():
    View = Tk()
    View.title("TOUR GUIDE - Paket Populer")
    View.geometry("250x400")

    #connect DB
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D81NMIB\SQLEXPRESS;'
                        'Database=TourGuide;'
                        'Trusted_Connection=yes;')
    #Create Cursor
    c = conn.cursor()

    #TODO show pendapatan
    #execute show
    c.execute("EXEC PaketP")
    records = c.fetchall()

    print_records = ''
    print_records1 = ''


    for record in records:
        print_records += str(record[0]) + "\n"
        print_records1 += str(record[1]) + "\n"


    inputlable = Label(View, text="DATA PAKET POPULER", font=("Open Sans Semibold", 15, "bold"))
    inputlable.grid(row=1, column=0,padx=0, ipadx=0, columnspan=2)

    IT_transasiL = Label(View, text="IdPaket", font=("Open Sans Semibold",10,"bold"),width = 10)
    IT_transasiL.grid(row=2, column=0, pady=5)
    IT_transaksiL = Label(View, text="Kepopuleran", font=("Open Sans Semibold",10,"bold"),width = 10)
    IT_transaksiL.grid(row=2, column=1, pady=5)


    query_label = Label(View, text= print_records, width = 10)
    query_label.grid(row = 3, column=0, pady=2)
    query_label = Label(View, text= print_records1, width = 10)
    query_label.grid(row = 3, column=1, pady=2)


    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()
    #akhir GUI
    View.mainloop()





def hide_all_frame():
    Transaksi_frame.pack_forget()
    Pelanggan_frame.pack_forget()
    Alamat_frame.pack_forget()


# ! =======================================================================================    MENU
insert_menu = Menu(my_menu)
my_menu.add_cascade(label="INSERT", menu=insert_menu)
insert_menu.add_command(label="Transaksi", command=Transaksi)
insert_menu.add_command(label="Alamat Pelanggan", command=Alamat)
insert_menu.add_command(label="Pelanggan", command=Pelanggan)

view_menu = Menu(my_menu)
my_menu.add_cascade(label="VIEW", menu=view_menu)
view_menu.add_command(label="Alamat Pelanggan", command=VAlamat)
view_menu.add_command(label="Pelanggan", command=VPlenggan)
view_menu.add_command(label="Transportasi", command=VTransportasi)
view_menu.add_command(label="Guide", command=VGuide)
view_menu.add_command(label="Wisata", command=VWisata)
view_menu.add_command(label="Penginapan", command=VPenginapan)
view_menu.add_command(label="Paket", command=VPaket)
view_menu.add_command(label="Transaksi", command=VTransaksi)

repot_menu = Menu(my_menu)
my_menu.add_cascade(label="REPORT", menu=repot_menu)
repot_menu.add_command(label="Pendapatan", command=VPendapatan)
repot_menu.add_command(label="Guide Populer", command=VGuideP)
repot_menu.add_command(label="Pelanggan Populer", command=VPelangganP)
repot_menu.add_command(label="Transportasi Populer", command=VTransportasiP)
repot_menu.add_command(label="Paket Populer", command=VPaketP)

# ! =======================================================================================    FRAME
Transaksi_frame = Frame(root)
Alamat_frame = Frame(root)
Pelanggan_frame = Frame(root)




Transaksi()

#Commit changes
conn.commit()
#Close Connection
conn.close()
#akhir GUI
root.mainloop()