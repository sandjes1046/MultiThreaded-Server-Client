from tkinter import *
import datetime

class Advising:
    
    def __init__(self):
        
       self.window = Tk() # Create a window
       self.window.title("CS Advising") # Set a title

       self.canvas=Canvas(self.window,height = 800)
       self.canvas.pack(side = BOTTOM)
       
       self.var = StringVar(self.window)
       self.name=StringVar(self.window)
       self.id=StringVar(self.window)
       self.advisor=StringVar(self.window)
       self.term1=StringVar(self.window)
       self.term2=StringVar(self.window)
       self.term3=StringVar(self.window)
       
       self.term_list=[self.term1,self.term2,self.term3]
       self.course_list=[]

       
   #frame = Frame(self.canvas).pack(side = RIGHT,anchor = E)

     #  self.Notes=Text(self.canvas,height = 20, width = 25)
       #self.Notes.pack(side = RIGHT)
       #self.Notes.insert(END,"Notes")
       #print(Notes.get("1.0",'end-1c')) gets the text from notes

       


       self.heading()
       for i in range (3):
           self.Courses(self.term_list[i])
           
       
       self.window.mainloop()

    def heading(self):
        
       
        
        HeadingFrame = Frame(self.window)
        HeadingFrame.pack()

        #LogoLabel = Label(HeadingFrame, image = Logo)
        #LogoLabel.Logo = Logo
        #LogoLabel.pack(side = LEFT)
        
        Title = Label(HeadingFrame, text = "Class Planning Worksheet")
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
        
        
        
        AdvisorOption = OptionMenu(InfoHeading,self.var,"Advisor 1",
                                   "Advisor 2")
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

        #notes=self.Notes.get("1.0",'end-1c')
        text_name = list(self.name.get().split())
        
        d = datetime.datetime.today()
        dtext = "" + str(d.day) + " /"+ str(d.month) + " /" + str(d.year)
        
        file=open(text_name[1]+"_"+text_name[0]+".txt", "w+")
        
        file.write("ID#: "+ self.id.get() + "\tFaculty Advisor: " + self.var.get() +
                   "\tDate: " +  dtext +"\n\n\t\t\t"+self.term_list[0].get()+
                   "\nCourse Number:\t\tCourse Name:\t\tCredit Hours:\n")

        for i in range(0,20,3):
            file.write(self.course_list[i].get() + "\t\t\t"+self.course_list[i+1].get()+
                       "\t"+'{:>12}'.format(self.course_list[i+2].get())+"\n")
            
        file.write("\n\t\t\t"+self.term_list[1].get()+"\nCourse Number:\t\tCourse Name:\t\tCredit Hours:\n")
        
        for i in range(21,41,3):
            file.write(self.course_list[i].get() + "\t\t\t"+self.course_list[i+1].get()+
                       "\t"+'{:>12}'.format(self.course_list[i+2].get())+"\n")

        file.write("\n\t\t\t"+self.term_list[2].get()+"\nCourse Number:\t\tCourse Name:\t\tCredit Hours:\n")
        
        for i in range(42,62,3):
            file.write(self.course_list[i].get() + "\t\t\t"+self.course_list[i+1].get()+
                       "\t"+'{:>12}'.format(self.course_list[i+2].get())+"\n")

        
        
Advising()  
    
        
        
        
    
    
