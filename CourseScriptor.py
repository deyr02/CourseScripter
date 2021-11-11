# importing packages:
import os
import textwrap
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry
from datetime import datetime

import importData
import logic
import CustomTimePicker

root = tk.Tk()
root.title("AIS Course Scripter")
root.resizable(1, 1)
root.geometry('800x600')

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Home')
tabControl.add(tab2, text='Course Details')
tabControl.add(tab3, text='Lecturer')

# Edited  based on comment from Lecturer: Saghir Ahamed -----------------------------------------
# tabControl.add(tab4, text='Course Aim')
# tabControl.add(tab5, text='Learning Outcome')
tabControl.add(tab6, text='Average Learning')
tabControl.add(tab7, text='Assessment')
tabControl.add(tab8, text='Download')

tabControl.pack(expand=1, fill="both")

# ----------------------------Styles -------------------------------------------
# style = ttk.Style()
# ttk.Style().configure("BW.TLabel",  background="red")
ttk.Style().configure("BW.TFrame", background="red", padding=10)

# ----------------------------Styles -------------------------------------------


# ----------------------------Home tab -------------------------------------------
homeTab = ttk.Frame(tab1, width=800, height=600)
homeTab.place(x=0, y=0)

# Logo --------------------------------------
# Read the Image and Resize the image using resize() method
image = Image.open("logo.png").resize((250, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
# create label and add resize image
imageLabel = ttk.Label(homeTab, image=img)
imageLabel.image = img
imageLabel.place(x=28, y=180)
# Logo --------------------------------------

# Title Box -----------------------------------
ttk.Style().configure("BW.TLabel", font=('calibri', 30, 'bold'), background='red')
titleLabel = ttk.Label(homeTab, text="Course Scripter", style="BW.TLabel")
titleLabel.place(x=28, y=290)


# ----------------------------------------------

# File Control----------------------------------


def browseCourseDescripter():
    '''
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    '''

    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("MSWord files",
                                                      "*.docx*"),
                                                     ("all files",
                                                      "*.*")))
    if (filename == ''):  # if user clicks Cancel buton
        return 0
    uploadCD = importData.setFileCD(filename)
    if (uploadCD != 1):
        tkinter.messagebox.showerror(title="Error",
                                     message="Wrong file uploaded. Please input the correct course descripter")
        descriptor.set("Please input the correct file")
    else:
        descriptor.set(filename)
        readData()

    # Change label contents


descriptor = tk.StringVar(tab1, value="Course Description file is not available")
courseDescriptor = ttk.Entry(homeTab, width=48, textvariable=descriptor)
courseDescriptor.config(state='disabled')
courseDescriptor.place(x=300, y=210, height=30)

courseDescriptorButton = ttk.Button(homeTab, width=30, text="Upload Course Descriptor", command=browseCourseDescripter)
courseDescriptorButton.place(x=600, y=210, height=30)


def browseCourseOutput():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("MS Word",
                                                      "*.docx*"),
                                                     ("all files",
                                                      "*.*")))
    if (filename == ''):  # if user clicks Cancel buton
        return 0
    # Change label contents
    output.set(filename)


output = tk.StringVar(tab1, value="Course Description file is not available")
courseOutput = ttk.Entry(homeTab, width=48, textvariabl=output)
courseOutput.config(state='disabled')
courseOutput.place(x=300, y=265, height=30)

courseOutputButton = ttk.Button(homeTab, width=30, text="Upload Course Outline Template", command=browseCourseOutput)
courseOutputButton.place(x=600, y=265, height=30)
# -----------------------------------------------

# homeTabLevel=ttk.Label(homeTab, text=root.winfo_reqheight(),  style="BW.TLabel")
# homeTabLevel.place(x=240, y=250)
# ----------------------------End Home tab ----------------------------------------


# Course Tab ---------------------------------------------------------------------------
courseDetailTab = ttk.Frame(tab2, width=800, height=600)
courseDetailTab.place(x=0, y=0)

ttk.Label(courseDetailTab, text="Trimester", font=('Arial', 10)).place(x=50, y=50, width=100)

trimesterList = ["Select Trimester", "Trimester one", "Trimester two", "Trimester three"]
selectedTrimester = tk.StringVar(homeTab)
selectedTrimester.set(trimesterList[0])
ttk.Style().configure("BW.TOptionMenu", background="red", padding=10)
trimesterMenu = ttk.OptionMenu(courseDetailTab, selectedTrimester, *trimesterList).place(x=251, y=50, width=202)

ttk.Label(courseDetailTab, text="Year", font=('Arial', 10)).place(x=50, y=90, width=100)
year = tk.StringVar(courseDetailTab, value="")
courseYear = ttk.Entry(courseDetailTab, width=33, textvariabl=year).place(x=251, y=89, height=23)

# Edited  based on comment from Lecturer: Saghir Ahamed -----------------------------------------
# ttk.Label(courseDetailTab, text="Course Code", font=('Arial', 10)).place(x=50, y=130, width=100)
courseCodeText = tk.StringVar(value="No data available")
# courseCode = ttk.Label(courseDetailTab, textvariable=courseCodeText, font=('Arial', 10)).place(x=251, y=130)

# ttk.Label(courseDetailTab, text="Course Title", font=('Arial', 10)).place(x=50, y=170, width=100)
courseTitleText = tk.StringVar(value="No data available")
# courseTitle = ttk.Label(courseDetailTab, textvariable=courseTitleText,  font=('Arial', 10)).place(x=251, y=170)

# ttk.Label(courseDetailTab, text="NZQF Level", font=('Arial', 10)).place(x=50, y=210, width=100)
nzqfLevelText = tk.StringVar(value="No data available")
# nzqfLevel = ttk.Label(courseDetailTab, textvariable=nzqfLevelText, font=('Arial', 10)).place(x=251, y=210)

# ttk.Label(courseDetailTab, text="Credits", font=('Arial', 10)).place(x=50, y=250, width=100)
creditText = tk.StringVar(value="No data available")
# credit = ttk.Label(courseDetailTab, textvariable=creditText, font=('Arial', 10)).place(x=251, y=250)

# ttk.Label(courseDetailTab, text="Pre-requisites", font=('Arial', 10)).place(x=50, y=290, width=100)
preRequisitesText = tk.StringVar(value="No data available")
# preRequisites = ttk.Label(courseDetailTab, textvariable=preRequisitesText, font=('Arial', 10)).place(x=251, y=290)

# ttk.Label(courseDetailTab, text="Co-requisite", font=('Arial', 10)).place(x=50, y=330, width=100)
coRequisiteText = tk.StringVar(value="No data available")
# coRequisites = ttk.Label(courseDetailTab, textvariable=coRequisiteText, font=('Arial', 10)).place(x=251, y=330)

# ttk.Label(courseDetailTab, text="Restrictions", font=('Arial', 10)).place(x=50, y=370, width=100)
restrictionsText = tk.StringVar(value="No data available")
# restrictions = ttk.Label(courseDetailTab, textvariable=restrictionsText, font=('Arial', 10)).place(x=251, y=370)


# --------------------------------------------------------------------------------------


# Lecturer Tab ---------------------------------------------------------------------------
lecturerTab = ttk.Frame(tab3, width=800, height=600)
lecturerTab.place(x=0, y=0)

ttk.Label(lecturerTab, text="First Name", font=('Arial', 10)).place(x=50, y=50, width=100)
fName = tk.StringVar(lecturerTab, value="")
lecturerLastName = ttk.Entry(lecturerTab, width=33, textvariab=fName).place(x=251, y=50, height=23)

ttk.Label(lecturerTab, text="Last Name", font=('Arial', 10)).place(x=50, y=90, width=100)
lName = tk.StringVar(lecturerTab, value="")
lecturerFirstName = ttk.Entry(lecturerTab, width=33, textvariab=lName).place(x=251, y=90, height=23)

ttk.Label(lecturerTab, text="Room Number", font=('Arial', 10)).place(x=50, y=130, width=100)
room = tk.StringVar(lecturerTab, value="")
roomNumber = ttk.Entry(lecturerTab, width=33, textvariab=room).place(x=251, y=130, height=23)

ttk.Label(lecturerTab, text="Phone Number", font=('Arial', 10)).place(x=50, y=170, width=100)
phone = tk.StringVar(lecturerTab, value="")
phoneNumber = ttk.Entry(lecturerTab, width=33, textvariab=phone).place(x=251, y=170, height=23)

ttk.Label(lecturerTab, text="Email", font=('Arial', 10)).place(x=50, y=210, width=100)
email = tk.StringVar(lecturerTab, value="")
emailAddress = ttk.Entry(lecturerTab, width=33, textvariab=email).place(x=251, y=210, height=23)

ttk.Label(lecturerTab, text="Contact Hour", font=('Arial', 10)).place(x=50, y=250, width=100)

ttk.Label(lecturerTab, text="From:", font=('Arial', 8)).place(x=251, y=250, width=50)
startFrom = CustomTimePicker.CTPiker(tab3)
startFrom.place(x=300, y=250)

ttk.Label(lecturerTab, text="To:", font=('Arial', 8)).place(x=251, y=290, width=50)
to = CustomTimePicker.CTPiker(tab3)
to.place(x=300, y=290)

ttk.Label(lecturerTab, text="Days:", font=('Arial', 8)).place(x=251, y=330, width=50)

mon = tk.IntVar()
monday = ttk.Checkbutton(lecturerTab, text="Monday", variable=mon).place(x=300, y=330)

tue = tk.IntVar()
tuesday = ttk.Checkbutton(lecturerTab, text="Tuesday", variable=tue).place(x=380, y=330)

wed = tk.IntVar()
wednesday = ttk.Checkbutton(lecturerTab, text="Wednesday", variable=wed).place(x=460, y=330)

thu = tk.IntVar()
thursday = ttk.Checkbutton(lecturerTab, text="Thursday", variable=thu).place(x=560, y=330)

fri = tk.IntVar()
friday = ttk.Checkbutton(lecturerTab, text="Friday", variable=fri).place(x=640, y=330)


def getContactHour():
    if (startFrom.getTime() == to.getTime()):
        tkinter.messagebox.showerror(title="Error", message="Please specify the contact hours properly")
        return -1

    contactDays = tk.StringVar()
    if mon.get() == 0 and tue.get() == 0 and wed.get() == 0 and thu.get() == 0 and fri.get() == 0:
        tkinter.messagebox.showerror(title="Error", message="Please select the available days for contract hours")
        return -1
    elif mon.get() == 1 and tue.get() == 1 and wed.get() == 1 and thu.get() == 1 and fri.get() == 1:
        contactDays.set("(Monday - Friday)")
    elif mon.get() == 1 and tue.get() == 1 and wed.get() == 1 and thu.get() == 1 and fri.get() == 0:
        contactDays.set("(Monday - Thursday)")
    elif mon.get() == 1 and tue.get() == 1 and wed.get() == 1 and thu.get() == 0 and fri.get() == 0:
        contactDays.set("(Monday - Wednesday)")
    elif mon.get() == 1 and tue.get() == 1 and wed.get() == 0 and thu.get() == 0 and fri.get() == 0:
        contactDays.set("(Monday - Tuesday)")
    else:
        _arr = []
        if mon.get() == 1:
            _arr.append("Monday")
        if tue.get() == 1:
            _arr.append("Tuesday")
        if wed.get() == 1:
            _arr.append("Wednesday")
        if thu.get() == 1:
            _arr.append("Thursday")
        if fri.get() == 1:
            _arr.append("Friday")

        contactDays.set("(")
        for i in range(len(_arr)):
            temp = contactDays.get()
            if i == len(_arr) - 1:
                contactDays.set(temp + _arr[i] + ")")
            else:
                contactDays.set(temp + _arr[i] + ", ")

    return startFrom.getTime() + " - " + to.getTime() + " " + contactDays.get()


# --------------------------------------------------------------------------------------


# Course Aim Tab ---------------------------------------------------------------------------
courseAimTab = ttk.Frame(tab4, width=800, height=600)
courseAimTab.place(x=0, y=0)

ttk.Label(courseAimTab, text="Course Aim", font=('Arial', 10)).place(x=50, y=50, width=100)

tempText = "No information available"
courseAim = tk.Text(courseAimTab, width=43, font=('calibri', 10))
# courseAim.config(state='disabled')
courseAim.insert('1.0', tempText)
courseAim.place(x=251, y=50, height=250)
# ttk.Entry(courseAimTab, width=33, textvariab=aim).place(x=251, y=50, height=23)
# --------------------------------------------------------------------------------------


# learning outcome Tab ---------------------------------------------------------------------------
lOTab = ttk.Frame(tab5, width=800, height=600)
lOTab.place(x=0, y=0)

ttk.Label(lOTab, text="Learning Outcomes", font=('Arial', 15)).place(x=300, y=15, width=200)

ttk.Style().configure('MyStyle1.Treeview', rowheight=50, relief="raise")
lOTree = ttk.Treeview(lOTab, style='MyStyle1.Treeview')

lOTree['columns'] = ('Outcome', 'Outcome Details')

lOTree.column('#0', width=0, stretch='NO')
lOTree.column('Outcome', width=80)
lOTree.column('Outcome Details', width=500)

lOTree.heading('#0', text='', )
lOTree.heading('Outcome', text='Outcome', )
lOTree.heading('Outcome Details', text='Outcome Details')


def wrap(string, length=95):
    return '\n'.join(textwrap.wrap(string, length))


'''
lOTree.insert(parent='', index=0, iid=0, text='', values=('LO 1',wrap('Understand and construct structured programming designs for a given business requirement including basic elements of computer programming such as variables, data and error types, statements, expressions, operators and graphical user-interface.', length=95)))
lOTree.insert(parent='', index=1, iid=1, text='', values=('LO 2',wrap('Understand and apply the simple and nested selection/decision control structure when writing program code to make a decision.', length=95)))
lOTree.insert(parent='', index=2, iid=2, text='', values=('LO 3',wrap('Apply the knowledge of pre & post tested loop/repetitive control structure when writing program code to process same sequence of tasks/activities. ', length=95)))
lOTree.insert(parent='', index=3, iid=3, text='', values=('LO 4',wrap('Familiarise with the concept of divide & conquer, and use the technology of “method” for writing effective, efficient and reusable computer program. ', length=95)))
lOTree.insert(parent='', index=4, iid=4, text='', values=('LO 5',wrap('Demonstrate an understanding of static & dynamic arrays, single & multi-dimensional arrays which are frequently used in writing program code for searching and sorting data.', length=95)))
lOTree.insert(parent='', index=5, iid=5, text='', values=('Lo 6',wrap('Demonstrate an understanding of text file operation (reading/writing) and develop the appropriate program code for such operation including exception handling and data validation', length=95)))
lOTree.insert(parent='', index=6, iid=6, text='', values=('Lo 7',wrap('Develop workplace soft-skills including working in groups, writing formal reports, carrying out individual research and/or delivering oral presentations', length=95)))
'''
lOTree.place(x=110, y=60)
# --------------------------------------------------------------------------------------


# average learning Tab ---------------------------------------------------------------------------
aLTab = ttk.Frame(tab6, width=800, height=600)
aLTab.place(x=0, y=0)

ttk.Label(aLTab, text="Teaching Hours", font=('Arial', 10)).place(x=50, y=50, width=100)
teachingHourText = tk.StringVar(value="No data available")
teachingHour = ttk.Label(aLTab, textvariable=teachingHourText, font=('Arial', 10)).place(x=251, y=50)

ttk.Label(aLTab, text="Self Directed Hours", font=('Arial', 10)).place(x=50, y=90, width=100)
selfDirectedHourText = tk.StringVar(value="No data available")
selfDirectedHour = ttk.Label(aLTab, textvariable=selfDirectedHourText, font=('Arial', 10)).place(x=251, y=90)

ttk.Label(aLTab, text="Total Hours", font=('Arial', 10)).place(x=50, y=130, width=100)
totalHoursText = tk.StringVar(value="No data available")
totalHours = ttk.Label(aLTab, textvariable=totalHoursText, font=('Arial', 10)).place(x=251, y=130)

ttk.Label(aLTab, text="Total Weeks ", font=('Arial', 10)).place(x=50, y=170, width=100)
totalWeeksText = tk.StringVar(value="No data available")
totalWeeks = ttk.Label(aLTab, textvariable=totalWeeksText, font=('Arial', 10)).place(x=251, y=170)
# --------------------------------------------------------------------------------------


# Assessment Tab ---------------------------------------------------------------------------
assessmentTab = ttk.Frame(tab7, width=800, height=600)
assessmentTab.place(x=0, y=0)

ttk.Label(assessmentTab, text="Assessments", font=('Arial', 15)).place(x=300, y=15, width=200)

ttk.Style().configure('MyStyle2.Treeview', rowheight=25)

assessmentTree = ttk.Treeview(assessmentTab, style='MyStyle2.Treeview')

assessmentTree['columns'] = ('Description', 'Weight', "Learning Outcomes")

assessmentTree.column('#0', width=0, stretch='NO')
assessmentTree.column('Description', width=200, anchor='center')
assessmentTree.column('Weight', width=100, anchor='center')
assessmentTree.column('Learning Outcomes', width=200, anchor='center')

assessmentTree.heading('#0', text='', )
assessmentTree.heading('Description', text='Description', )
assessmentTree.heading('Weight', text='Weight')
assessmentTree.heading('Learning Outcomes', text='Learning Outcomes')

'''
assessmentTree.insert(parent='', index=0, iid=0, text='', values=('Assignment 1','15%', '1,2,3,4,7'))
assessmentTree.insert(parent='', index=1, iid=1, text='', values=('Mid Semester Test','20%', '1,2,3,4,5'))
assessmentTree.insert(parent='', index=2, iid=2, text='', values=('Assignment 2','25%', '1,2,3,4,5,67'))
assessmentTree.insert(parent='', index=3, iid=3, text='', values=('Examination','50%', '1,2,3,4,5,6'))
'''
assessmentTree.place(x=110, y=60)
# --------------------------------------------------------------------------------------


# Download Tab ---------------------------------------------------------------------------
downloadTab = ttk.Frame(tab8, width=800, height=600)
downloadTab.place(x=0, y=0)


# def checkInfo():
# if ... :
#    tkinter.messagebox.showerror(title="Error", message="Wrong file uploaded. Please input the correct course descripter")
#    return 0

def browseSavingLocation():
    filename = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    # Change label contents
    location.set(filename)
    print(filename)



    # validate All field
    if selectedTrimester.get() == "Select Trimester":
        tkinter.messagebox.showerror(title="Error", message="Please select Trimester")
        return -1

    if ((validateEmptyValue(year, "Course Year should not be empty") == -1)
            or (validateEmptyValue(lName, "Lecturer's Last Name should not be empty") == -1)
            or (validateEmptyValue(fName, "Lecturer's First Name should not be empty") == -1)
            or (validateEmptyValue(room, "Room number should not be empty") == -1)
            or (validateEmptyValue(phone, "Phone Number should not be empty") == -1)
            or (validateEmptyValue(email, "Email address should not be empty") == -1)
            or (getContactHour() == -1 )):
        print("data validated")
        return -1



    lecturer = ['', '', '', '', '']
    print(lName.get())
    print(room.get())
    print(phone.get())
    print(email.get())
    print(getContactHour())
    print(selectedTrimester.get())
    print(year.get())
    print(descriptor.get())  # CD
    print(output.get())  # CO

    # check data
    lecturer[0] = fName.get() + " " + lName.get()
    lecturer[1] = room.get()
    lecturer[2] = phone.get()
    lecturer[3] = email.get()
    lecturer[4] = getContactHour()

    # trimister info
    _trimester = tk.StringVar()
    if selectedTrimester.get() == "Trimester one":
        _trimester.set("T1")
    elif selectedTrimester.get() == "Trimester two":
        _trimester.set("T2")
    elif selectedTrimester.get() == "Trimester three":
        _trimester.set("T3")

    _fileName ='/'+ courseCodeText.get()+'-'+_trimester.get()+'-'+year.get()+'-CourseOutline-draft1-' + fName.get()[0].upper() + lName.get()[0].upper()+'.docx'

    try:
        result = logic.mergeFile(output.get(), descriptor.get(), location.get() + _fileName, lecturer,
                                 selectedTrimester.get(), year.get())
        if (result != 1):
            tkinter.messagebox.showerror(title="Error", message="Something went wrong, please check all input data")
            return 0
        response = tkinter.messagebox.askyesno(title="Done", message="Your output file is ready. \nWould like to open the file?")
        if response == True:
            os.startfile(location.get()+_fileName)
        else:
            return 0
    except:
        tkinter.messagebox.showerror(title="Error", message="Something went wrong, please check all input data")
        return 0


location = tk.StringVar(downloadTab, value="Chose the location to save file.")
savingLocation = ttk.Entry(downloadTab, width=48, textvariable=location)
savingLocation.config(state='disabled')
savingLocation.place(x=150, y=100, height=30)

savingLocationButton = ttk.Button(downloadTab, width=25, text="Download To", command=browseSavingLocation)
savingLocationButton.place(x=460, y=100, height=30)


# --------------------------------------------------------------------------------------


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# window funtionalities --------------------------------------------


# ------------read course Descriptor---------------------
# clearing fields ------------------------------------------------------------
def clearFields():
    # course Details
    selectedTrimester.set(trimesterList[0])
    year.set("")
    courseCodeText.set("No data available")
    courseTitleText.set("No data available")
    nzqfLevelText.set("No data available")
    creditText.set("No data available")
    preRequisitesText.set("No data available")
    coRequisiteText.set("No data available")
    restrictionsText.set("No data available")
    # lecturer information
    fName.set("")
    lName.set("")
    room.set("")
    phone.set("")
    email.set("")
    # hour.set("")
    # course Aim
    courseAim.delete("1.0", "end")
    courseAim.insert("end", "No data available")
    # Learning outcomes
    for i in lOTree.get_children():
        lOTree.delete(i)

    # average Learning
    teachingHourText.set("No data available")
    selfDirectedHourText.set("No data available")
    totalHoursText.set("No data available")
    totalWeeksText.set("No data available")
    # assessment
    for i in assessmentTree.get_children():
        assessmentTree.delete(i)


# End of clearing fields -----------------------------------------------------


def readData():
    clearFields()

    # update course detils ---------------------
    courseTitleText.set((importData.dataCourseTitle[4]))
    courseCodeText.set(importData.dataCourseCode[4])
    nzqfLevelText.set(importData.dataNZQFLevel[4])
    creditText.set(importData.dataCredits[4])
    preRequisitesText.set(importData.dataPrerequisites[4])
    coRequisiteText.set(importData.dataCorequisites[4])
    restrictionsText.set(importData.dataRestrictions[4])

    # update course aim-----------------------------
    courseAim.delete("1.0", "end")
    courseAim.insert("end", importData.dataCourseAims[4])

    # learning outcomes----------------------
    loutcome_Data = importData.getLearningOutcomes()
    index = 0
    for lo in loutcome_Data:
        if lo[0] != 0:
            lOTree.insert(parent='', index=index, iid=index, text='',
                          values=('LO {}'.format(lo[0]), wrap(lo[1], length=95)))
            index += 1

    # Average Learning ---------------------
    teachingHourText.set(importData.dataTotalHours)
    selfDirectedHourText.set(importData.dataSelfDirectedHours)
    totalHoursText.set(importData.dataTotalHours)
    totalWeeksText.set(importData.dataTotalWeeks)
    # Assessment ---------------------------------
    assessmentData = importData.getSummativeAssesment()
    asIndex = 0
    for asData in assessmentData:
        assessmentTree.insert(parent='', index=asIndex, iid=asIndex, text='', values=(asData[0], asData[1], asData[2]))
        asIndex += 1
    # read data complteted--------------------------------------------------------------


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# Field validation
def validateEmptyValue(field, message):
    if field.get() == '':
        tkinter.messagebox.showerror(title="Error", message=message)
        return -1
    return 1


# ttk.Label(tab2, text="Lets dive into the world of computers").grid(column=0, row=0, padx=30, pady=30)
root.mainloop()
