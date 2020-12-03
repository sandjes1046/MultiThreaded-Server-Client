from tkinter import *
import datetime
import sys
from gui_to_xml_generator import *
import socket
import os



class Advising:

    
    def __init__(self):
       self.window = Tk() # Create a window
       self.window.title("CS Advising") # Set a title

       self.canvas=Canvas(self.window,height = 800)
       self.canvas.pack(side = BOTTOM)
       frame = Frame(self.canvas).pack(side = RIGHT,anchor = E)
       self.Notes=Text(self.canvas,height = 20, width = 25)
       self.Notes.pack(side = RIGHT)
       self.Notes.insert(END,"Notes")
       #print(Notes.get("1.0",'end-1c')) gets the text from notes

       self.serverName = 'localhost'
       self.serverPort = 10000
       self.filename=''
       
       self.var = StringVar(self.window)
       self.var.set(" ")
       self.name=StringVar(self.window)
       self.name.set(" ")
       self.id=StringVar(self.window)
       self.id.set(" ")
       self.advisor=StringVar(self.window)
       self.advisor.set(" ")
       self.term1=StringVar(self.window)
       self.term1.set(" ")
       self.term2=StringVar(self.window)
       self.term2.set(" ")
       self.term3=StringVar(self.window)
       self.term3.set(" ")
       self.term_list=[self.term1,self.term2,self.term3]
       self.course_list=[]

       self.heading()
       
       for i in range (3):
           self.Courses(self.term_list[i])

           
       self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       try:   
           self.clientSocket.connect((self.serverName,self.serverPort))
       except:
           print("Unexpected error: Please check the server")
           
       self.window.mainloop()

    def heading(self):
        
        Logo = PhotoImage(file = "Logo.gif")
        
        HeadingFrame = Frame(self.window)
        HeadingFrame.pack()

        LogoLabel = Label(HeadingFrame, image = Logo)
        LogoLabel.Logo = Logo
        LogoLabel.pack(side = LEFT)
        
        Title = Label(HeadingFrame, text = "UTRV B.S Computer Science\nClass Planning Worksheet")
        Title.pack()

        InfoHeading = Frame(self.window)
        InfoHeading.pack(side = TOP)
        
        NameLabel = Label(InfoHeading, text = "Name:")
        NameLabel.pack(side = LEFT)
        NameEntry = Entry(InfoHeading,textvariable=self.name)
        NameEntry.pack(side = LEFT)

        IDLabel = Label(InfoHeading, text="ID#:")
        IDLabel.pack(side = LEFT)
        IDEntry = Entry(InfoHeading,textvariable=self.id)
        IDEntry.pack(side = LEFT)

        AdvisorLabel = Label(InfoHeading,text = "Faculty Advisor:")
        AdvisorLabel.pack(side = LEFT)
        
        
        self.var.set("  ")
        AdvisorOption = OptionMenu(InfoHeading,self.var,"Dr.Mahmoud Quweider",
                                   "Dr.Fitratullah Khan")
        AdvisorOption.pack(side =LEFT)
                                   
        

        
        d = datetime.datetime.today()
        DateLabel = Label(InfoHeading,text = "  Date: ")
        DateLabel.pack(side = LEFT)
        CurrentDate_Label = Label(InfoHeading, text = "" + str(d.day) + " /"+ str(d.month) + " /" + str(d.year))
        CurrentDate_Label.pack(side = LEFT)

        SubmitBttn=Button(InfoHeading,text="Submit",command = self.submit)
        SubmitBttn.pack(side =RIGHT,padx=30)

        
        
        
        
    def Courses(self,terms):
        
        SemsterFrame = Frame(self.canvas)
        SemsterFrame.pack()
        
        TermEntry = Entry(SemsterFrame,width=79,justify='center',textvariable=terms,)
        TermEntry.pack(pady=5)

        CourseNumLabel = Label(SemsterFrame,text = "Course Number"
                               ,borderwidth=1,relief="solid",font=10,width=26)
        CourseNumLabel.pack(side =LEFT)

        CourseNameLabel = Label(SemsterFrame,text="Course Name",
                                borderwidth=1,relief="solid",font=10,width=26)
        CourseNameLabel.pack(side = LEFT)

        CreditLabel = Label(SemsterFrame,text="Credit Hours",
                                borderwidth=1,relief="solid",font=10,width=26)
        CreditLabel.pack(side = LEFT)

        CourseEntryLabels = LabelFrame(self.canvas)
        CourseEntryLabels.pack()
        count = 0
        x = 0
        while count <= 14:
            
            for i in range(7):
            
                CoursesEntry=Entry(CourseEntryLabels,width=47,borderwidth=2,relief="solid") 
                CoursesEntry.pack(side = LEFT)

                
                self.course_list.append(CoursesEntry)
                
                count += 1
                if count % 3 == 0:
                    CourseEntryLabels = LabelFrame(self.canvas)
                    CourseEntryLabels.pack()
        TextFrame=Frame(self.canvas)
        TextFrame.pack(side=TOP)
        Notes=Entry(TextFrame,width=50)

        
    def submit(self):

        notes=self.Notes.get("1.0",'end-1c')
        text_name = list(self.name.get().split())
        #self.id = list(self.id.get().split())
        #self.var = list(self.var.get().split())
        #print(self.var.get())
        #print(self.name.get())
       # print(self.id.get())
        d = datetime.datetime.today()
        dday=str(d.day)
        dmonth=str(d.month)
        dyear=str(d.year)
        dtext = "" + dday + " /"+ dmonth + " /" + dyear
        #print(dtext)
        #for i in range (63):
         #   print(self.course_list[i].get())
        #for i in range (3):
            #print(self.term_list[i].get())
        new_term_list=[]
         

        advisingtree = ElementTree.Element('advising')
        comment = ElementTree.Comment('Generated for '+ text_name[0]+'_'+text_name[1])
        advisingtree.append(comment)
         

        studentinfo=insert_studentInfo2(advisingtree,text_name[0],text_name[1],self.id.get(),
                                        self.var.get(),dtext)

        for i in range (3):
            new_term_list.append(self.term_list[i].get().split())
            
        semester1 = insert_semester2(advisingtree,new_term_list[0][0],new_term_list[0][1])
        
        for i in range(0,20,3):
            
            course = insert_course2(semester1,self.course_list[i].get(),self.course_list[i+1].get(),self.course_list[i+2].get()) 
        
        semester2 = insert_semester2(advisingtree,new_term_list[1][0],new_term_list[1][1])

        for i in range(21,41,3):
            course = insert_course2(semester2,self.course_list[i].get(),self.course_list[i+1].get(),self.course_list[i+2].get())
            
        semester3 = insert_semester2(advisingtree,new_term_list[2][0],new_term_list[2][1])

        for i in range(42,62,3):
            course = insert_course2(semester3,self.course_list[i].get(),self.course_list[i+1].get(),self.course_list[i+2].get())

        insert_notes(advisingtree,notes)


        fname = ' '+text_name[1]+'_'+text_name[0]+'_'+self.id.get()+'.xml'

        xml_to_file(advisingtree,fname)
        self.filename= fname
        try:
            print(f"file to send {self.filename}")
            file_size = os.path.getsize(self.filename)
            file_to_send= os.path.basename(self.filename) 
            
            # Send metadata first
            line = file_to_send + ' '
            line += str(file_size)
            line += '\r\n'
            print(f"Metaddata line is:>>>{line}")
            metadata = line.encode()
            self.clientSocket.sendall(metadata)
            
            # Send data
            with open(file_to_send,"rb") as f:
                print(f'starting connection to server with file: {file_to_send}')
                data = f.read()
                self.clientSocket.sendall(data)
        finally:
            print('wait for confirmation from server...')
            text = self.clientSocket.recv(1024)
            print ('From Server: ', text.decode())
            print('closing socket after sendin data...')
            self.clientSocket.close()



           
        
        
Advising()  
    
        
        
        
    
    
