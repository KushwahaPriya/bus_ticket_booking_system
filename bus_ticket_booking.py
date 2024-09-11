from tkinter import *
from tkinter.messagebox import *
import sqlite3
import datetime
currentDateTime = datetime.datetime.now()
con=sqlite3.connect("ticket_database", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
# con=sqlite3.connect("ticket_database")
cur=con.cursor()
# cur.execute("create table user(user_id int primary key,pass text)")9
# cur.execute("create table bus_details(bid int primary key ,type varchar(20),capacity int ,fare int,opid int ,route_id int)")
# cur.execute("create table operator(operid int primary key ,opname varchar(20),adress varchar(20),phoneno int ,email varchar(30),foreign key(operid) references bus_details(opid))")
# cur.execute("create table route(rid int ,sid int primary key,sname varchar(20),foreign key(rid) references bus_details(route_id))")
# cur.execute("create table runs(busid int primary key,rdate timestamp,seat_av int,foreign key(busid) references bus_details(bid))")
# cur.execute("create table booking_histr(ref_no int primary key ,pass_name varchar(20),age int,booked_seat int,bidd int,booking_date timestamp,trav_date text,frome varchar(16),too varchar(15),foreign key(bidd) references bus_datails(bid))")
# cur.execute("create table route(rid int primary key ,sid int,sname varchar(20),foreign key(rid) references bus_datails(route_id))")
# cur.execute("create table runs(busid int,date timestamp,seat_aval int,foreign key(busid) references bus_datails(bid),primary key(busid,date))")
# cur.execute("drop table booking_histr")
# cur.execute("drop table user")
# con.commit()
class test:
    def __init__(self,a,b):
        self.age=a
        self.name=b      
    def screen1(self):
        root=Tk()
        root.title("first page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Name: Priya kushwaha",fg="blue",font="Arial 10 bold").grid(row=4,column=1,padx=w//3)
        ##fr2=Frame(root)
        ##fr2.grid(row=5,column=1,columnspan=10)
        Label(fr1,text="\n").grid(row=5,column=1)
        count=6
        Label(fr1,text="Er: 221b502",fg="blue",font="Arial 10 bold").grid(row=count,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=7,column=1)
        Label(fr1,text="Mobile: 9770290716",fg="blue",font="Arial 10 bold").grid(row=8,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=9,column=1)
        Label(fr1,text="Submitted to: Dr.mahesh kumar",bg="light blue",fg="red1",font="Arial 14 bold").grid(row=10,column=1,padx=w//3)
        Label(fr1,text="Project Based Learning",fg="red1",font="Arial 10 bold").grid(row=11,column=1,padx=w//3)
        def close1(e=1):
            root.destroy()
            sel.screen2()
        root.after(2000,close1)
        root.mainloop()
        
    def screen2(self):
        root=Tk()
        root.title("Second page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        fr2=Frame(root)
        fr2.grid(row=3,column=1,columnspan=10)
        Label(fr2,text="\n").grid(row=3,column=1)
        def close2():
            root.destroy()
            sel.users()
        def close3():
            root.destroy()
            sel.screen5()
        def close4():
            root.destroy()
            sel.screen6()
        Button(fr2,text="Seat Booking",command=close2,bg="light green",fg="black",font="Arial 12 bold").grid(row=4,column=1)
        Label(fr2,text="         ").grid(row=4,column=2)
        Button(fr2,text="Check Booked Seat",command=close3,bg="green2",fg="black",font="Arial 12 bold").grid(row=4,column=3)
        Label(fr2,text="         ").grid(row=4,column=4)
        Button(fr2,text="Add Bus Details",command=close4,bg="green3",fg="black",font="Arial 12 bold").grid(row=4,column=5)
        Label(fr2,text="\n").grid(row=5,column=1)
        Label(fr2,text="For Admin Only",fg="red1",font="arial 8 bold").grid(row=6,column=5)
        
        root.mainloop()


    def users(self):
        root=Tk()
        root.title("sign up or log in page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=0,column=0,columnspan=10)
        sign_upp=PhotoImage(file="log_in_page_image.png")
        Label(fr1,image=sign_upp).grid(row=0,column=0,padx=w//2.5)
        Label(fr1,text="\n").grid(row=1,column=0)
        def close1():
            root.destroy()
            sel.sign_up()
        def close2():
            root.destroy()
            sel.sign_in()
        fr1=Frame(root)
        fr1.grid(row=5,column=0,columnspan=10)
        sign_up=PhotoImage(file="sign_up1.png")
        Button(fr1,text="sign up",command=close1,bg="light blue",fg="red",font="arial 13 bold").grid(row=5,column=0)
        Label(fr1,text="          ").grid(row=5,column=1)
        Button(fr1,text="sign in",command=close2,bg="light blue",fg="red",font="arial 13 bold").grid(row=5,column=2)
        def hom():
            root.destroy()
            sel.screen2()
        fr2=Frame(root)
        fr2.grid(row=7,column=0,columnspan=10)
        # Label(fr3,text="    ").grid(row=,column=10)
        Label(fr1,text="\n").grid(row=6,column=0)

        home=PhotoImage(file="home.png")
        Button(fr2,image=home,command=hom).grid(row=7,column=0,padx=w//3)
        
        root.mainloop()

    def sign_up(self):
        # from tkinter.messagebox import *
        # import sqlite3
        # conn=sqlite3.connect("sign_up")
        # cur=conn.cursor()
        # cur.execute("create table users(user_id int primary key,pass text)")
        root=Tk()
        root.title("sign up page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=0,column=0,columnspan=10)
        sign_upp=PhotoImage(file="log_in_page_image.png")
        Label(fr1,image=sign_upp).grid(row=0,column=0,padx=w//2.5)
        Label(fr1,text="\n").grid(row=1,column=0)

        fr2=Frame(root)
        fr2.grid(row=1,column=0,columnspan=10)
        Label(fr2,text="Enter User Id-",fg="black",font="Arial 12 bold").grid(row=1,column=0)
        Label(fr2,text="      ").grid(row=1,column=1)
        us_name=Entry(fr2)
        us_name.grid(row=1,column=2)
        Label(fr2,text="\n").grid(row=2,column=0)


        fr3=Frame(root)
        fr3.grid(row=3,column=0,columnspan=10)
        Label(fr3,text="Enter  Password-",fg="black",font="Arial 12 bold").grid(row=3,column=0)
        Label(fr3,text="      ").grid(row=3,column=1)
        us_pass=Entry(fr3,show="*")
        us_pass.grid(row=3,column=2)
        Label(fr3,text="\n").grid(row=4,column=0)

        def sign_up1():
            if(len(us_name.get())<10 or us_name.get()==""):
                showerror("entry error","user name sould be m.n. or email id")
            elif(len(us_pass.get())<9 or us_pass.get()==""):
                showerror("entry error","password should be of atlist 8 digit")
            # elif((isnumeric(us_pass))):
            #     showerror("entry error","password should be alphanumeric value")
            else:
                cur.execute("insert into users values(?,?)",(us_name.get(),us_pass.get()))
                con.commit()
                showinfo("account","account created successfully")
        def back():
            root.destroy()
            sel.users()
        fr4=Frame(root)
        fr4.grid(row=5,column=0,columnspan=10)
        sign_up=PhotoImage(file="sign_up1.png")
        Button(fr4,text="sign up",command=sign_up1,bg="light blue",fg="red",font="arial 13 bold").grid(row=5,column=0)
        Label(fr4,text="             ").grid(row=5,column=1)
        Button(fr4,text="back",command=back,bg="light blue",fg="red",font="arial 13 bold").grid(row=5,column=2)



        root.mainloop()
    def sign_in(self):
        # from tkinter.messagebox import *
        # import sqlite3
        # conn=sqlite3.connect("sign_up")
        # cur=conn.cursor()
        # cur.execute("create table users(user_id int primary key,pass text)")
        root=Tk()
        root.title("sign up page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=0,column=0,columnspan=10)
        sign_upp=PhotoImage(file="log_in_page_image.png")
        Label(fr1,image=sign_upp).grid(row=0,column=0,padx=w//2.5)
        Label(fr1,text="\n").grid(row=1,column=0)

        fr2=Frame(root)
        fr2.grid(row=1,column=0,columnspan=10)
        Label(fr2,text="Enter User Id-",fg="black",font="Arial 12 bold").grid(row=1,column=0)
        Label(fr2,text="      ").grid(row=1,column=1)
        us_name=Entry(fr2)
        us_name.grid(row=1,column=2)
        Label(fr2,text="\n").grid(row=2,column=0)


        fr3=Frame(root)
        fr3.grid(row=3,column=0,columnspan=10)
        Label(fr3,text="Enter  Password-",fg="black",font="Arial 12 bold").grid(row=3,column=0)
        Label(fr3,text="      ").grid(row=3,column=1)
        us_pass=Entry(fr3,show="*")
        us_pass.grid(row=3,column=2)
        Label(fr3,text="\n").grid(row=4,column=0)

        def sign_in():
            if len(us_name.get())<10 or us_name.get()=="":
                showerror("entry error","user name sould be m.n. or email id")
            elif(len(us_pass.get())<9 or us_pass.get()==""):
                showerror("entry error","password should be of atlist 8 digit")
            # elif((isnumeric(us_pass))):
            #     showerror("entry error","password should be alphanumeric value")
            elif(cur.execute("select user_id from user where user_id=? and pass=?",(us_name.get(),us_pass.get()),)):
                root.destroy()
                sel.screen3()
                # showinfo("account","account created successfully")
        def back():
            root.destroy()
            sel.users()
        fr4=Frame(root)
        fr4.grid(row=5,column=0,columnspan=10)
        sign_up=PhotoImage(file="sign_up1.png")
        Button(fr4,text="sign in",command=sign_in,bg="light blue",fg="red",font="arial 13 bold").grid(row=5,column=0)
        Label(fr4,text="             ").grid(row=5,column=1)
        Button(fr4,text="back",command=back,bg="light blue",fg="red",font="arial 13 bold").grid(row=5,column=2)


        root.mainloop()

        
          

    def screen3(self):
        root=Tk()
        root.title("fourth page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Enter journey Details",bg="green1",fg="green",font="Arial 10 bold").grid(row=4,column=1,padx=w//3)
        fr2=Frame(root)
        fr2.grid(row=5,column=1,columnspan=10)
        Label(fr2,text="\n").grid(row=5,column=1)
        Label(fr2,text="To",font="Arial 8 bold").grid(row=6,column=1)
        a=Entry(fr2)
        a.grid(row=6,column=2)
        Label(fr2,text="from",font="Arial 8 bold").grid(row=6,column=3)
        b=Entry(fr2)
        b.grid(row=6,column=4)
        Label(fr2,text="Journey Date",font="Arial 8 bold").grid(row=6,column=5)
        c=Entry(fr2)
        c.grid(row=6,column=6)
        
        def showing_bus():
            fr3=Frame(root)
            fr3.grid(row=7,column=1,columnspan=10)
            Label(fr3,text="\n").grid(row=7,column=1)
            Label(fr3,text="Select Bus        ",fg="green",font="Arial 10 bold").grid(row=8,column=1)
            Label(fr3,text="Operator            ",fg="green",font="Arial 10 bold").grid(row=8,column=2)
            Label(fr3,text="Bus type         ",fg="green",font="Arial 10 bold").grid(row=8,column=3)
            Label(fr3,text="Availablecapacity         ",fg="green",font="Arial 10 bold").grid(row=8,column=4)
            Label(fr3,text="Fare           ",fg="green",font="Arial 10 bold").grid(row=8,column=5)
            Label(fr3,text="\n").grid(row=9,column=1)

            cur.execute("select distinct rid from route")
            res1=cur.fetchall()
            # print(res1[1][0])

            
            def func(res):
                count=0
                for row in res:
                    count+=1
                row2=-1
                flag=False
                print("count",count)
                
                for rows in res:
                    #print(res[row2][0])
                    row2=row2+1
                    row3=row2+1
                    if row3<count:
                        for rowss in res:
                            # print("manohar")
                            # print(row3)
                            # print(res[row3][0])
                            if res[row2][2]==b.get() and res[row3][2]==a.get():
                                flag=True
                            row3+=1
                            if row3>=count:
                                break
                    else:
                        break
                if flag:
                    return res[0][0]
                else:
                    return -1
            i=0
            L=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
            for row in res1:
                # print(row)
                cur.execute("select * from route where rid=?",(row))
                result=cur.fetchall()
                # print(result[0][1])
                L[i]=func(result)
                i=i+1
            print("list",L)
            # for row1 in result:
            #print(L)
            to=StringVar()
            frome=StringVar()
            to=a.get()
            frome=b.get()
            dt=StringVar()
            dt=c.get()

            for id in L:
                print("bid",id)
                if id!=-1:
                    print("bid",id)
                    cur.execute("select bus_details.bid,bus_details.type,bus_details.capacity,bus_details.fare,operator.opname from bus_details inner join route on bus_details.route_id=route.rid inner join runs on  bus_details.bid=runs.busid inner join operator on  bus_details.opid=operator.operid  where route.rid=? and runs.date=? and route.sname=?  ",(id,dt,to,))
                    bd=cur.fetchall()

                    
                    # for row in bd:
                    #print(bd[0][0])
            print("rid",bd)
            rc=10
            fr4=Frame(root)
            fr4.grid(row=10,column=1,columnspan=10)
            sel_bus=IntVar()
            # sel_bus=1
            count=1
            for row in bd:
                # var=IntVar()
                print("row",rc)
                var=row
                # print(var)
                # break
                # rc=10
                # break
                # bus1=IntVar()
                # fr4=Frame(root)
                # fr4.grid(row=10,column=1,columnspan=10)
                # bus1=IntVar()
                Radiobutton(fr4,text="bus"+str(count)+"                ",variable=sel_bus,value=row[0]).grid(row=rc,column=1)
                Label(fr4,text= var[4],fg="blue",font="Arial 8 bold").grid(row=rc,column=2)
                Label(fr4,text= "                         ",fg="blue",font="Arial 8 bold").grid(row=rc,column=3)
                Label(fr4,text=var[1],fg="blue",font="Arial 8 bold").grid(row=rc,column=4)
                Label(fr4,text= "                      ",fg="blue",font="Arial 8 bold").grid(row=rc,column=5)
                Label(fr4,text=var[2],fg="blue",font="Arial 8 bold").grid(row=rc,column=6)                                                                 
                Label(fr4,text= "                       ",fg="blue",font="Arial 8 bold").grid(row=rc,column=7)
                Label(fr4,text=var[3],fg="blue",font="Arial 8 bold").grid(row=rc,column=8)
                Label(fr4,text="                         ",fg="blue",font="Arial 8 bold").grid(row=rc,column=9)
                # Button(fr4,text="Proceed to book",font="Arial 8 bold",bg="light green",command=edit).grid(row=17,column=11)
                Label(fr4,text="\n").grid(row=18,column=12)
                # Button(fr4,text="Proceed to book",font="Arial 8 bold",bg="light green",command=edit).grid(row=17,column=11)

                rc+=1
                print("var value",sel_bus)
                print("bid",row[0])
                count+=1
                # fr5=Frame(root)
                fr6=Frame(root)
                d=Entry(fr6)
                gender=StringVar()
                gender.set("select gender")
                option=["Male","female","other"]
                menu=OptionMenu(fr6,gender,*option)
                g=IntVar()
                g=Entry(fr6)
                h=Entry(fr6)
                i=Entry(fr6)
                
            def editing():
                print("busid",sel_bus.get())
                fr5=Frame(root)
                fr5.grid(row=17,column=1,columnspan=10)
                Label(fr5,text="Fill Passenger Details to Book the Bus Ticket",bg="light blue",fg="red",font="Arial 14 bold").grid(row=17,column=1,padx=w//3)
                Label(fr5,text="\n").grid(row=18,column=1)
                # Label(root,text="\n").grid(row=7,column=1)
                # fr6=Frame(root)
                fr6.grid(row=19,column=1,columnspan=10)
                Label(fr6,text="Name",font="Arial 8 bold").grid(row=19,column=1)
                # d=Entry(fr6)
                d.grid(row=19,column=2)
                Label(fr6,text="Gender",font="Arial 8 bold").grid(row=19,column=3)
                # gender=StringVar()
                # gender.set("select gender")
                # option=["Male","female","other"]
                # menu=OptionMenu(fr6,gender,*option)
                menu.grid(row=19,column=4)
                Label(fr6,text="No of seats",font="Arial 8 bold").grid(row=19,column=5)
                # g=Entry(fr6)
                g.grid(row=19,column=6)
                Label(fr6,text="Mobile No?: ",font="Arial 8 bold").grid(row=19,column=7)
                # h=Entry(fr6)
                h.grid(row=19,column=8)
                Label(fr6,text="Age",font="Arial 8 bold").grid(row=19,column=9)
                # i=Entry(fr6)
                i.grid(row=19,column=10)
                
                Button(fr6,text="Book seat",font="Arial 8 bold",bg="green1",command=booking).grid(row=19,column=11)
            def booking():
                print("booking busid",sel_bus.get())
                print(g.get())
                cur.execute("select fare,capacity from bus_details where bid=?",(sel_bus.get(),))
                fare=cur.fetchone()
                print("fare",fare)
                tf=fare[0]*int(g.get())
                # print(tf)
                # print(a.get())
                flag=askyesno("Fare confirmed","Total amount to be fare Rs:"+str(tf))
                # if d.get==()'' or g.get()=='' or h.get()=='' i.get()=='' :
                #     Showerror("entry error","please fill all entries")
                if flag and fare[0]:
                    if d.get()=='' or g.get()=='' or h.get()=='' or i.get()=='' :
                        showerror("entry error","please fill all entries")
                    else:
                        cur.execute("insert into booking_histr  values(?,?,?,?,?,?,?,?,?)",(h.get(),d.get(),i.get(),g.get(),sel_bus.get(),currentDateTime,c.get(),b.get(),a.get())) 
                        con.commit()
                        cap=fare[1]-int(g.get())
                        cur.execute("update bus_details set capacity=? where bid=?",(cap,sel_bus.get(),))
                        con.commit()
                    if flag:
                        scr2()
            Button(fr4,text="Proceed to book",font="Arial 8 bold",bg="light green",command=editing).grid(row=17,column=11)
   


        Button(fr2,text="Show Bus",font="Arial 8 bold",bg="green1",command=showing_bus).grid(row=6,column=7)
        Label(fr2,text="     ").grid(row=6,column=8)
        home=PhotoImage(file="home.png")
        def scr2():
            root.destroy()
            sel.screen5()
            
            
        Button(fr2,image=home,font="Arial 8 bold",bg="green1",command=scr2).grid(row=6,column=9)
        def close5(e=1):
            root.destroy()
        
        root.mainloop() 
        


    def screen5(self):
        root=Tk()
        root.title("sixsth page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        fr2=Frame(root)
        fr2.grid(row=6,column=1,columnspan=10)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Check your booking",bg="green1",fg="green",font="Arial 10 bold").grid(row=4,column=1)
        Label(fr1,text="\n").grid(row=5,column=1)
        Label(fr2,text="Enter your mobile no:",font="Arial 10 bold").grid(row=6,column=1)
        a=Entry(fr2)
        a.grid(row=6,column=2)

        def pass_d():
            # print(type(int(a.get())))
            cur.execute("select ref_no,pass_name,age,booked_seat,bidd,frome,too,booking_date,trav_date from booking_histr where ref_no=?",(a.get(),))
            info=cur.fetchall()
            print(info)
            fr3=Frame(root,relief="groove",bd=10)
            fr3.grid(row=7,column=1,columnspan=10)
            Label(fr3,text="passengers:"+info[0][1],font="Arial 12 bold").grid(row=7,column=1)
            Label(fr3,text="Gender: Male",font="Arial 12 bold").grid(row=7,column=2)
            Label(fr3,text="No of Seets:"+str(info[0][3]),font="Arial 12 bold").grid(row=8,column=1)
            Label(fr3,text="phone:"+str(info[0][0]),font="Arial 12 bold").grid(row=8,column=2)
            Label(fr3,text="Age:"+str(info[0][2]),font="Arial 12 bold").grid(row=9,column=1)
            Label(fr3,text="Travel On:"+str(info[0][8]),font="Arial 12 bold").grid(row=10,column=1)
            Label(fr3,text="Boarding point:"+info[0][5],font="Arial 12 bold").grid(row=11,column=2)
            Label(fr3,text="Dest:"+info[0][6],font="Arial 12 bold").grid(row=12,column=1)
            Label(fr3,text="booking date:"+str(info[0][7]),font="Arial 12 bold").grid(row=11,column=1)

    
        Button(fr2,text="Check booking",command=pass_d,font="Arial 8 bold").grid(row=6,column=3)
        home=PhotoImage(file="home.png")
        Label(fr2,text="     ").grid(row=6,column=4)
        home=PhotoImage(file="home.png")
        def scr3():
            root.destroy()
            sel.screen2()
            
        Button(fr2,image=home,font="Arial 8 bold",bg="green1",command=scr3).grid(row=6,column=5)

        root.mainloop()
    def screen6(self):
        root=Tk()
        root.title("sixsth page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Add New Details to Database",fg="green",font="Arial 12 bold").grid(row=4,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=5,column=1)
        fr2=Frame(root)
        fr2.grid(row=6,column=1,columnspan=10)
        def close6():#for new opretor deatails
            root.destroy()
            sel.screen7()
        def close7():#for new bus details
            root.destroy()
            sel.screen8()
        def close8():#for new route details
            root.destroy()
            sel.screen9()
        def close9():#for new run details
            root.destroy()
            sel.screen10()       
        Button(fr2,text="new operator",command=close6,bg="light green",fg="green",font="Arial 8 bold").grid(row=6,column=1)
        Label(fr2,text="        ").grid(row=5,column=2)
        Button(fr2,text="New Bus",command=close7,bg="red1",fg="black",font="Arial 8 bold").grid(row=6,column=3)
        Label(fr2,text="        ").grid(row=5,column=4)
        Button(fr2,text="New Route",command=close8,bg="light blue",fg="black",font="Arial 8 bold").grid(row=6,column=5)
        Label(fr2,text="         ").grid(row=5,column=6)
        Button(fr2,text="new Run",command=close9,bg="purple",fg="black",font="Arial 8 bold").grid(row=6,column=7)
        root.mainloop()
        
                

    def screen7(self):
        root=Tk()
        root.title("Eightth page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Add Bus operator Details\n",fg="green",font="Arial 12 bold").grid(row=4,column=1,padx=w//3)
        fr2=Frame(root)
        fr2.grid(row=5,column=1,columnspan=10)
        Label(fr2,text="Operator Id").grid(row=5,column=1)
        a=Entry(fr2)
        a.grid(row=5,column=2)
        Label(fr2,text="Name",bg="white",font="Arial 10 bold").grid(row=5,column=3)
        B=Entry(fr2)
        B.grid(row=5,column=4)
        Label(fr2,text="Adress",bg="white",font="Arial 10 bold").grid(row=5,column=5)
        c=Entry(fr2)
        c.grid(row=5,column=6)
        Label(fr2,text="Phone no:",bg="white",font="Arial 10 bold").grid(row=5,column=7)
        D=Entry(fr2)
        D.grid(row=5,column=8)
        Label(fr2,text="Email",bg="white",font="Arial 10 bold").grid(row=5,column=9)
        E=Entry(fr2)
        E.grid(row=5,column=10)
        def add():
            if a.get()=='' or B.get()=='' or c.get()==''or D.get()=='' or E.get()=='':
                showerror("entry error","please fill all entries")
            else:
                cur.execute("insert into operator values(?,?,?,?,?)",(a.get(),B.get(),c.get(),D.get(),E.get()))
                con.commit()
                showinfo("operator entry","operator details aded successfully")
                fr3=Frame(root)
                fr3.grid(row=6,column=1,columnspan=10)
        def edit():
            if a.get()=='' or B.get()=='' or c.get()==''or D.get()=='' or E.get()=='':
                showerror("entry error","please fill all entries")
            else:
                cur.execute("update operator set operid=? ,opname=?,adress=?,phoneno=?,email=? where operid=?",(a.get(),B.get(),c.get(),D.get(),E.get(),a.get()))
                con.commit()
                showinfo("operator details entry","operator details edited successfully")
        Button(fr2,text="Add",command=add,bg="light green",fg="green",font="Arial 8 bold").grid(row=5,column=11)
        Label(fr2,text="      ").grid(row=5,column=12)
        Button(fr2,text="Edit",command=edit,bg="light green",fg="green",font="Arial 8 bold").grid(row=5,column=13)
        home=PhotoImage(file="home.png")
        Label(fr2,text="     ").grid(row=5,column=14)
        home=PhotoImage(file="home.png")
        def scr4():
            root.destroy()
            sel.screen2()
            
        Button(fr2,image=home,font="Arial 8 bold",bg="green1",command=scr4).grid(row=5,column=15)
        root.mainloop()

    def screen8(self):
        root=Tk()
        root.title("Ninth page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Add Bus Details",fg="green",font="Arial 12 bold").grid(row=4,column=1,padx=w//3)
        fr2=Frame(root)
        fr2.grid(row=5,column=1,columnspan=10)
        Label(fr2,text="\n").grid(row=5,column=1)
        Label(fr2,text="Bus Id",font="Arial 10 bold").grid(row=5,column=1)
        A=Entry(fr2)
        A.grid(row=5,column=2)
        Label(fr2,text="Bus Type",font="Arial 10 bold").grid(row=5,column=3)
        bus_type=StringVar()
        option=["Ac 2x2","Ac 3x2","Non Ac 2x2","non Ac 3x2","Ac sleeper 2x1","Non Ac sleeper 2x1"]
        menu=OptionMenu(fr2,bus_type,*option)
        menu.grid(row=5,column=4)
        Label(fr2,text="Capacity",font="Arial 10 bold").grid(row=5,column=5)
        C=Entry(fr2)
        C.grid(row=5,column=6)
        Label(fr2,text="Fare Rs",font="Arial 10 bold").grid(row=5,column=7)
        d=Entry(fr2)
        d.grid(row=5,column=8)
        Label(fr2,text="Operator Id",font="Arial 10 bold").grid(row=5,column=9)
        e=Entry(fr2)
        e.grid(row=5,column=10)
        Label(fr2,text="Route Id",font="Arial 10 bold").grid(row=5,column=11)
        f=Entry(fr2)
        f.grid(row=5,column=12)

        fr3=Frame(root)
        fr3.grid(row=6,column=1,columnspan=10)
        fr4=Frame(root)
        fr4.grid(row=8,column=1,columnspan=10)
        Label(fr3,text="\n").grid(row=6,column=1)
        def add_bus():
            if A.get()=='' or bus_type.get()=='' or C.get()=='' or d.get()=='' or e.get()=='' or f.get()=='' :
                showerror("entry error","please fill all entries")
            else:
                cur.execute("insert into bus_details values(?,?,?,?,?,?) ",(A.get(),bus_type.get(),C.get(),d.get(),e.get(),f.get()))
                con.commit()
                showinfo("bus details entry","bus details aded successfully")
        def edit_bus():
            if A.get()=='' or bus_type.get()=='' or C.get()=='' or d.get()=='' or e.get()=='' or f.get()=='' :
                showerror("entry error","please fill all entries")
            else:
                cur.execute("update bus_details set bid=? ,type=?,capacity=?,fare=?,opid=?,route_id=? where bid=?",(A.get(),bus_type.get(),C.get(),d.get(),e.get(),f.get(),A.get()))
                con.commit()
                showinfo("bus details entry","bus details edited successfully")
        Button(fr3,text="Add Bus",command=add_bus,bg="light green",fg="green",font="Arial 8 bold").grid(row=7,column=7,padx=10)
        Label(fr3,text="    ").grid(row=7,column=8)
        Button(fr3,text="Edit Bus",command=edit_bus,bg="light green",font="Arial 8 bold").grid(row=7,column=9)
        
        home=PhotoImage(file="home.png")
        def scr5():
            root.destroy()
            sel.screen2()
        
        Label(fr3,text="    ").grid(row=7,column=10)
        home=PhotoImage(file="home.png")
        Button(fr3,image=home,command=scr5).grid(row=7,column=11)
       
        root.mainloop()

    def screen9(self):
        root=Tk()
        root.title("tenth page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Add Bus route Details",fg="green",font="Arial 12 bold").grid(row=4,column=1,padx=w//3)
        ##Label(fr1,text="\n").grid(row=4,column=1)
        fr2=Frame(root)
        fr2.grid(row=5,column=1,columnspan=10)
        Label(fr2,text="\n").grid(row=5,column=1)
        Label(fr2,text="Route Id",font="Arial 10 bold").grid(row=5,column=1)
        A=Entry(fr2)
        A.grid(row=5,column=2)
        Label(fr2,text="Station Name",font="Arial 10 bold").grid(row=5,column=3)
        B=Entry(fr2)
        B.grid(row=5,column=4)
        Label(fr2,text="Station Id",font="Arial 10 bold").grid(row=5,column=5)
        C=Entry(fr2)
        C.grid(row=5,column=6)
        #Label(root,text="\n").grid(row=5,column=1)
        def add_route():
            if A.get()==''  or C.get()=='' or B.get()=='':
                showerror("entry error","please fill all entries")
            else:
                cur.execute("insert into route values(?,?,?)",(A.get(),C.get(),B.get()))
                con.commit()
                showinfo("roue entry","route details aded")
        def delete_route():
            if A.get()=='':
                showerror("entry error","please enter route id in route id column")
            else:
                cur.execute("delete from route where rid=?",(A.get()))
                con.commit()
                showinfo("route entry","route details deleted successfully")
        Button(fr2,text="Add Route",command=add_route,bg="light green",fg="green",font="Arial 8 bold").grid(row=5,column=7)
        Label(fr2,text="  ").grid(row=5,column=8)
        Button(fr2,text="Delete Route",command=delete_route,bg="light green",fg="red1",font="Arial 8 bold").grid(row=5,column=9)
        #Label(root,text="* suthij Travels Delhi 223433342 email ").grid(row=5,column=6)
        fr3=Frame(root)
        fr3.grid(row=6,column=3,columnspan=10)
        def scr6():
            root.destroy()            
            sel.screen2()
        Label(fr2,text="\n\n").grid(row=6,column=1)
        home=PhotoImage(file="home.png")
        Button(fr3,image=home,command=scr6).grid(row=8,column=1,padx=450)
        root.mainloop()
    def screen10(self):
        root=Tk()
        root.title("eleventh page")
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry("%dx%d+0+0"%(w,h))
        fr1=Frame(root)
        fr1.grid(row=1,column=1,columnspan=10)
        bus=PhotoImage(file="1.png")
        Label(fr1,image=bus).grid(row=1,column=1,padx=w//3)
        Label(fr1,text="Online Bus Booking System",bg="light blue",fg="red",font="Arial 14 bold").grid(row=2,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=3,column=1)
        Label(fr1,text="Add Bus Running Details",fg="green",font="Arial 12 bold").grid(row=4,column=1,padx=w//3)
        Label(fr1,text="\n").grid(row=5,column=1)
        fr2=Frame(root)
        fr2.grid(row=6,column=1,columnspan=10)
        Label(fr2,text="Bus Id",font="Arial 10 bold").grid(row=6,column=1)
        A=Entry(fr2)
        A.grid(row=6,column=2)
        Label(fr2,text="Running date",font="Arial 10 bold").grid(row=6,column=3)
        B=Entry(fr2)
        B.grid(row=6,column=4)
        Label(fr2,text="Seat Available",font="Arial 10 bold").grid(row=6,column=5)
        C=Entry(fr2)
        C.grid(row=6,column=6)
        #Label(root,text="\n").grid(row=5,column=1)
        def add_runs():
            if A.get()==''  or C.get()=='' or B.get()=='':
                showerror("entry error","please fill all entries")
            else:
                cur.execute("insert into runs values(?,?,?)",(A.get(),B.get(),C.get()))
                con.commit()
                showinfo("roue entry","route details aded")
        def delete_runs():
            if A.get()=='':
                showerror("entry error","please enter bus Id in entry column")
            else:
                cur.execute("delete from runs where busid=?",(A.get()))
                con.commit()
                showinfo("runs entry","runs details deleted successfully")
        Button(fr2,text="Add_Run",command=add_runs,bg="light green",fg="green",font="Arial 8 bold").grid(row=6,column=7)
        Label(fr2,text="    ").grid(row=6,column=8)
        Button(fr2,text="Delete Run",command=delete_runs,bg="light green",fg="black",font="Arial 8 bold").grid(row=6,column=9)
        #Label(root,text="* suthij Travels Delhi 223433342 email ").grid(row=5,column=6)
        fr3=Frame(root)
        fr3.grid(row=7,column=1,columnspan=10)
        Label(fr3,text="\n\n").grid(row=7,column=1)
        def scr7():
            root.destroy()
            sel.screen2()
        home=PhotoImage(file="home.png")
        Button(fr3,image=home,command=scr7).grid(row=8,column=9,padx=550)
        root.mainloop()

        
sel=test(36,"manohar")
sel.screen1()
