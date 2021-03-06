# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
import tkinter.messagebox
from tkcalendar import Calendar
 
# Create Object
root = Tk()
 
# Set geometry for main window
root.geometry("600x700")

lab = Label(root)

# Use Threading
def Threading():
    t1=Thread(target=alarm)
    #dat.config(text = "Selected Date is: " + cal.get_date())
    t1.start()

date = datetime.datetime.now()
# Create Label to display the Date
label = Label(root, text=f"{date:%A, %B %d, %Y}", font="Helvetica 10")



dat = Label(root, text = "")
dat.pack(pady = 20)

cal = Calendar(root, selectmode = 'day',year = 2021, month = 12, day = 10)

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

clock()

def prin():
    cal.get_date()

def alarm():
    # Infinite Loop
    
    tkinter.messagebox.showinfo("Remainder"," Defined date and time is set")
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        
        # Wait for one seconds
        time.sleep(1)
        
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            tkinter.messagebox.showinfo("Remainder.", text1.get())
            print("Time to take medicines")
            print(e1)
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
 
# Add Labels, Frame, Button, Optionmenus


 
Label(root,text="Activity Remainder",font=("Helvetica 20 bold"),fg="red").pack(pady=5)

Label(root,text="Date:",font=("Helvetica 10 bold")).pack()
label.pack(pady=5)
Label(root,text="Current Time:",font=("Helvetica 10 bold")).pack()
current_time = datetime.datetime.now().strftime("%H:%M")
Label(root,text=lab.pack(),font=("Helvetica 10 bold")).pack()



Label(root,text="Set Medicine name",font=("Helvetica 15 bold")).pack()



text1=StringVar(root)
e1= Entry(root, textvariable=text1).pack(pady=10)

Label(root,text="Set Time",font=("Helvetica 15 bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)
 
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

cal.pack(pady = 20)


Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=15)

 
# Execute Tkinter
root.mainloop()