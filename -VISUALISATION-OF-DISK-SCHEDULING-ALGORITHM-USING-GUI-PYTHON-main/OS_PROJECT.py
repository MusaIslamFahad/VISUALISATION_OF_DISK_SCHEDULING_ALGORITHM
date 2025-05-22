from tkinter import ttk
from matplotlib import pyplot as plt 
from functools import partial
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from gtts import gTTS    
import os 
from operator import itemgetter
import pyttsx3
from fpdf import FPDF
from tkinter.filedialog import asksaveasfile
root = Tk()
root.title("Disk Scheduling")
root.geometry("5000x1000")
my_notebook = ttk.Notebook(root,width=3000,height=1000)
my_notebook.grid(row=30,column=30)
my_notebook.pack(pady=1)
my_frame1 = Frame(my_notebook)
my_frame2 = Frame(my_notebook)
my_frame1.pack()
my_frame2.pack()
my_notebook.add(my_frame1, text="Practice")
my_notebook.add(my_frame2, text="Comparison")

     
def fcfs(arr,head,directions,mi_cyl,ma_cyl,num):
    initial_head=head
    seek_count = 0; 
    
    distance, cur_track = 0, mi_cyl;
    q=[]
    arr=[initial_head]+arr
    for i in range(len(arr)): 
        cur_track = arr[i] 
        distance = abs(cur_track - head)
        seek_count += distance
        q.append(seek_count)    
        head = cur_track  
    a="Total number of seek operations = "+str(seek_count)+"\n"
    print(a)
    print(l,"1")
    
    print(l,"2")
    if num=="2":
        report.delete("1.0","end")
        report.insert(INSERT,a)
        report.insert(INSERT,arr[0:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,arr[0:])
    else:
        T1.insert(INSERT,seek_count)
        #T11.insert(INSERT,arr[1:])
    if num=="2" or num=="4":           
        x=arr
        y=q
        #mylabel=Label(root,text=a).grid(row=4,column=4)
        fig = Figure(figsize=(3,3), dpi=130)      
        ax = fig.add_subplot()       
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]
        line, = ax.plot(0, 0,marker='o',color='r')
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])   
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        """plt.plot(arr,q).grid(row=10,column=2) 
        ax = plt.gca()
        ax.axes.yaxis.set_visible(False)
        ax.xaxis.set_ticks_position('top') 
        plt.gca().invert_yaxis()"""
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))       
        canvas.draw()
    if num=="3":
        return seek_count
        

    #mylabel=Label(root,text="okay").grid(row=3)
#root.grid()
def scan(arr,head,directions,mi_cyl,ma_cyl,num):    
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        d=i+1
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        answer+=abs(mi_cyl-Starting_posi)
        y.append(answer)
        l.append(mi_cyl)
        Starting_posi=mi_cyl
        
        
        while(d<len(array)):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
            Starting_posi=array[d]
            d=d+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
        
        answer+=abs((ma_cyl-1)-Starting_posi)
        y.append(answer)
        l.append(ma_cyl-1)
        Starting_posi=ma_cyl-1
        
        
        while(d>=0):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
        
            Starting_posi=array[d]
            d=d-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T3.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        print(x)
        print(y)
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer 
    
    
    
def cscan(arr,head,directions,mi_cyl,ma_cyl,num):    
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        m=len(array)
        d=i+1
        
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        answer+=abs(mi_cyl-Starting_posi)
        y.append(answer)
        l.append(mi_cyl)
        Starting_posi=mi_cyl
        answer+=abs(Starting_posi-(ma_cyl-1))
        y.append(answer)
        l.append(ma_cyl-1)
        Starting_posi=ma_cyl
        
        
        while(m>d):
            answer+=abs(array[m-1]-Starting_posi)
            y.append(answer)
            l.append(array[m-1])
            Starting_posi=array[m-1]
            m=m-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        print(i)
        print(array)
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
        
        answer+=abs((ma_cyl-1)-Starting_posi)
        y.append(answer)
        l.append(ma_cyl-1)
        Starting_posi=ma_cyl
        answer+=abs(Starting_posi-(mi_cyl))
        y.append(answer)
        l.append(mi_cyl)
        Starting_posi=mi_cyl
       
        j=0
        while(j<=d):
            answer+=abs(array[j]-Starting_posi)
            y.append(answer)
            l.append(array[j])
            Starting_posi=array[j]
            j=j+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T5.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
         
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer
    
    
def calculateDifference(queue, head, diff): 
    for i in range(len(diff)): 
        diff[i][0] = abs(queue[i] - head)  
      
# find unaccessed track which is  
# at minimum distance from head  
def findMin(diff):  
  
    index = -1
    minimum = 999999999
  
    for i in range(len(diff)): 
        if (not diff[i][1] and 
                minimum > diff[i][0]): 
            minimum = diff[i][0] 
            index = i 
    return index  
      
def sstgraph(request, head,directions,mi_cyl,ma_cyl,num):
        initial_head=head              
        if (len(request) == 0):  
            return
          
        l = len(request)  
        diff = [0] * l 
          
        # initialize array  
        for i in range(l): 
            diff[i] = [0, 0] 
          
        # count total number of seek operation      
        seek_count = 0
        q=[0] 
        # stores sequence in which disk  
        # access is done  
        seek_sequence = [0] * (l + 1)  
        x_array=[]
        
        for i in range(l):
            
            seek_sequence[i] = head  
            calculateDifference(request, head, diff)  
            index = findMin(diff)  
            diff[index][1] = True
            cur_track=request[index]
            x_array.append(cur_track)
            # increase the total count  
            seek_count += diff[index][0]  
            q.append(seek_count)
            # accessed track is now new head  
            head = request[index]  
      
        # for last accessed track  
        seek_sequence[len(seek_sequence) - 1] = head  
          
        a="Total number of seek operations = "+str(seek_count)+"\n"
        #mylabel=Label(root,text=a).grid(row=3,column=1)
        x_array.insert(0,initial_head )
        if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,x_array[1:])
        elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,x_array[1:])
        else:
            T2.insert(INSERT,seek_count)
            #T22.insert(INSERT,x_array[1:])
            
        if num=="2" or num=="4":
            x=x_array
            y=q
            fig = Figure(figsize=(3,3), dpi=130)       
            ax = fig.add_subplot()
            ax.set_xlim(mi_cyl, ma_cyl)
            ax.set_ylim(mi_cyl, max(q)+100)
            ax.set_xlabel('READ/WRITE HEAD POSITION')
            ax.set_ylabel('SEEK TIME SPENT')
            fig.tight_layout()
            x_data=[]
            y_data=[]
            line, = ax.plot(0, 0,marker='o',color='r')
            def animation_frame(i):
                x_data.append(x[i])
                y_data.append(y[i])   
                line.set_xdata(x_data)
                line.set_ydata(y_data)
                return line
            if num=="2":
                canvas = FigureCanvasTkAgg(fig, master=my_frame1)
                canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
            else:
                canvas = FigureCanvasTkAgg(fig, master=my_frame2)
                canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
            animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
            
            """plt.plot(x_array,q)
            ax = plt.gca()
            ax.axes.yaxis.set_visible(False)
            ax.xaxis.set_ticks_position('top') 
            plt.gca().invert_yaxis()"""
            for i in range(len(x)):
                ax.annotate(x[i],(x[i],y[i]))
            canvas.draw() 
        if num=="3":
            return seek_count


def LOOK(arr,head,directions,mi_cyl,ma_cyl,num):
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        d=i+1
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        
        while(d<len(array)):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
            Starting_posi=array[d]
            d=d+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
        
        while(d>=0):
            answer+=abs(array[d]-Starting_posi)
            y.append(answer)
            l.append(array[d])
        
            Starting_posi=array[d]
            d=d-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T7.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        print(x)
        print(y)
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer
        
        
def C_LOOK(arr,head,directions,mi_cyl,ma_cyl,num):
    array=sorted(arr)
    Starting_posi=head
    answer = 0; 
    y=[mi_cyl]
    total_tracks=ma_cyl; 
    
    maximum=max(array)
    minimum=min(array)
    l=[head]
    a=""
    if(directions=="LEFT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        i=i-1
        m=len(array)-1
        d=i+1
        
        while(i>=0):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)
            l.append(array[i])
            Starting_posi=array[i]
            i=i-1
        
        answer+=abs(array[i]-array[m])
        Starting_posi=array[m]
        l.append(array[m])
        y.append(answer)
        while(m>d):
            answer+=abs(array[m-1]-Starting_posi)
            y.append(answer)
            l.append(array[m-1])
            Starting_posi=array[m-1]
            m=m-1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"

    if(directions=="RIGHT"):
        for i in range(len(array)):
            if(array[i]<=Starting_posi):
                i=i+1
            else:
                break
        d=i-1
        print(i)
        print(array)
        while(i<len(array)):
            answer+=abs(array[i]-Starting_posi)
            y.append(answer)	 	
            l.append(array[i])
            Starting_posi=array[i]
            i=i+1
            
           
        
        m=0
        answer+=abs(array[i-1]-array[m])
        Starting_posi=array[m]
        l.append(array[m])
        y.append(answer)
        while(m<d):
            answer+=abs(array[m+1]-Starting_posi)
            y.append(answer)
            l.append(array[m+1])
            Starting_posi=array[m+1]
            m=m+1
        
        a="Total no of movements it will require is :"+str(answer)+"\n"
    if num=="2":
            report.delete("1.0","end")
            report.insert(INSERT,a)
            report.insert(INSERT,l[1:])
    elif num=="4":
            report2.delete("1.0","end")
            report2.insert(INSERT,a)
            report2.insert(INSERT,l[1:])
    else:
            T8.insert(INSERT,answer)
            #T77.insert(INSERT,l[1:])
    x=l
    
    if num=="2" or num=="4":
        fig = Figure(figsize=(3,3), dpi=130)       
        ax = fig.add_subplot()
        
        ax.set_xlim(mi_cyl, ma_cyl)
        ax.set_ylim(0, max(y)+100)
        ax.set_xlabel('READ/WRITE HEAD POSITION')
        ax.set_ylabel('SEEK TIME SPENT')
        fig.tight_layout()
        x_data=[]
        y_data=[]

        line, = ax.plot(0, 0,marker='o',color='r')
        
        def animation_frame(i):
            x_data.append(x[i])
            y_data.append(y[i])
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            return line
        if num=="2":
            canvas = FigureCanvasTkAgg(fig, master=my_frame1)
            canvas.get_tk_widget().grid(row=3,column=5,columnspan=10,rowspan=20,padx=0,pady=0)
        else:
         
            canvas = FigureCanvasTkAgg(fig, master=my_frame2)
            canvas.get_tk_widget().grid(row=12,column=3,columnspan=10,rowspan=20,padx=0,pady=0)
        animation = FuncAnimation(fig, func=animation_frame, frames= np.arange(0, len(x), 1), interval=1000, repeat=False)
        for i in range(len(x)):
            ax.annotate(x[i],(x[i],y[i]))
        canvas.draw()
    if num=="3":
        return answer
	    
   
k = Label(my_frame1,text = " Enter Request Points :").grid(row=3,column=0)


l=[]
def comman():
    
    try: 
        l.clear()       
        INPUT = inputtxt.get("1.0", "end-1c")
        for i in INPUT.split(","):
            l.append(int(i))
        a=variablem.get()
        directions=variable1.get()
        initial_hp=int(head_texto.get("1.0", "end-1c"))
        mi_cyl=int(mincyl_text.get("1.0", "end-1c"))
        ma_cyl=int(maxcyl_text.get("1.0", "end-1c"))
        print(ma_cyl)
        if a=="LIFO":
            LIFO(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="SSTF":
            sstgraph(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="SCAN":
            scan(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="LOOK":
            LOOK(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="FCFS":
            fcfs(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="CLOOK":
            C_LOOK(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
        elif a=="CSCAN":
            cscan(l,initial_hp,directions,mi_cyl,ma_cyl,"2")
    except Exception as e:
        print(e)
        report.insert(INSERT,"Enter the points properly")
def pdfconversion():
        try:
            INPUT2 = inputtxt.get("1.0", "end-1c")
            directions2=variable1.get()
            initial_hp2=head_texto.get("1.0", "end-1c")
            mi_cyl2=mincyl_text.get("1.0", "end-1c")
            ma_cyl2=maxcyl_text.get("1.0", "end-1c")
            ans2=report.get("1.0", "end-1c")
            
            a2=variablem.get()
            out=a2+"\n"+"The request points are    "+INPUT2+"\n"+"The initial head position "+initial_hp2+"\n"+"The direction is          "+directions2+"\n"+"The Maximum cylinder is   "+ma_cyl2+"\n"+"The Minimum Cylinder is   "+mi_cyl2+"\n"+"The output is             "+ans2
            files = [('All Files', '*.*'),('Text Document', '*.txt')]
            file = asksaveasfile(filetypes = files, defaultextension = "w")
            file.write(out)
            file.close()
            """pdf.cell(200, 10, txt = ,ln = 3, align = 'L')
            pdf.cell(200, 10, txt =,ln = 4, align = 'L')
            pdf.cell(200, 10, txt = ,ln = 5, align = 'L')
            pdf.cell(200, 10, txt = ,ln = 6, align = 'L')
            pdf.cell(200, 10, txt =,ln = 7, align = 'L')
            pdf.output("OutputFile.pdf")"""
        except Exception as e:
            print(e)
                        

    
    
    
    
#first frame
variablem = StringVar(my_frame1)
variable1 = StringVar(my_frame1)


inputtxt = Text(my_frame1, height = 3,width = 25,bg = "light yellow")
inputtxt.grid(row=3,column=1)

blank1 = Label(my_frame1,text = " ").grid(row=0,columnspan=2)

variablem.set("FCFS") # default value

k1 = Label(my_frame1,text = "Select the Algorithm :").grid(row=1,column=0)

w = OptionMenu(my_frame1, variablem, "FCFS", "SSTF", "SCAN","CSCAN","LOOK","CLOOK")
w.grid(row=1,column=1)

button = Button(my_frame1, text="RUN", command=comman,padx=85).grid(row=15,column=1)
blank4 = Label(my_frame1,text = " ").grid(row=2,column=0)

blank2 = Label(my_frame1,text = " ").grid(row=4,column=0)

head = Label(my_frame1,text = "Intial Head Position :").grid(row=5,column=0)
head_texto = Text(my_frame1,height=1,width = 25,bg = "light yellow")
head_texto.grid(row=5,column=1,padx=50)

blank5 = Label(my_frame1,text = " ").grid(row=6,column=0)

variable1.set("RIGHT")
direction = Label(my_frame1,text = "Direction:").grid(row=7,column=0)
direction_op = OptionMenu(my_frame1, variable1, "RIGHT", "LEFT").grid(row=7,column=1)


blank6 = Label(my_frame1,text = " ").grid(row=8,column=0)

max_cyl = Label(my_frame1,text = "Maximum Cylinder :").grid(row=9,column=0)
maxcyl_text = Text(my_frame1,height=1,width = 25,bg = "light yellow")
maxcyl_text.grid(row=9,column=1)

blank7 = Label(my_frame1,text = " ").grid(row=10,column=0)

min_cyl = Label(my_frame1,text = "Minimum Cylinder :").grid(row=11,column=0)
mincyl_text = Text(my_frame1,height=1,width = 25,bg = "light yellow")
mincyl_text.grid(row=11,column=1)


answer = Label(my_frame1,text = "Answer :")
answer.grid(row=13,column=0)
blank3 = Label(my_frame1,text = " ").grid(row=12,column=0)

blank8 = Label(my_frame1,text = " ").grid(row=14,column=0)
blank9 = Label(my_frame1,text = " ").grid(row=16,column=0)
save = Button(my_frame1, text="SAVE", command=pdfconversion,padx=85).grid(row=17,column=1)
blank8 = Label(my_frame1,text = " ").grid(row=18,column=0)


report = Text(my_frame1, height = 3,width = 25,bg = "light yellow")
report.grid(row=13,column=1)





#for third
#For third frame
def checkBox():
    compare=[]
    l.clear()
    T1.delete("1.0","end")
    T2.delete("1.0","end")
    T3.delete("1.0","end")
    #T4.delete("1.0","end")
    T5.delete("1.0","end")
    
    T7.delete("1.0","end")
    T8.delete("1.0","end")
    compare.clear()
    t10.delete("1.0","end")
    try:
                      
        INPUT3 = inputtxt3.get("1.0", "end-1c")
        for i in INPUT3.split(","):
            l.append(int(i))
        directions3=variable3.get()
        initial_hp3=int(head_text3.get("1.0", "end-1c"))
        mi_cyl3=int(mincyl_text3.get("1.0", "end-1c"))
        ma_cyl3=int(maxcyl_text3.get("1.0", "end-1c"))        
        if(CheckVar1.get()==1):
            T1.delete("1.0","end")
            
            print(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            fc=fcfs(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            f=[int(fc),"fcfs"]
            compare.append(f)
           
        if(CheckVar2.get()==1):
            T2.delete("1.0","end")
            #T22.delete("1.0","end")
            sst=sstgraph(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            ss=[sst,"sstgraph"]
            compare.append(ss)
        if(CheckVar3.get()==1):
            T3.delete("1.0","end")
            #T33.delete("1.0","end")
            sca=scan(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            sc=[sca,"scan"]
            compare.append(sc)
        """if(CheckVar4.get()==1):
            T4.delete("1.0","end")
            #T44.delete("1.0","end")
            print(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            life=LIFO(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            lif=[life,"lifo"]
            compare.append(lif)"""
        if(CheckVar5.get()==1):
            T5.delete("1.0","end")
            csca=cscan(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            csc=[csca,"cscan"]
            compare.append(csc)
        if(CheckVar6.get()==1):
            print("call 6")
        if(CheckVar7.get()==1):
            T7.delete("1.0","end")
            #T77.delete("1.0","end")
            loo=LOOK(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            lo=[loo,"look"]
            compare.append(lo)
        if(CheckVar8.get()==1):
            T8.delete("1.0","end")
            #T77.delete("1.0","end")
            clo=C_LOOK(l,initial_hp3,directions3,mi_cyl3,ma_cyl3,"3")
            cl=[clo,"C_LOOK"]
            compare.append(cl)
        comp=sorted(compare,key = itemgetter(0))
        t10.insert(INSERT,comp[0][1])
            
            
            
    except Exception as e:
        print(e)
        if(CheckVar1.get()==1):
            T1.insert(INSERT,"Enter the points properly")
        if(CheckVar2.get()==1):
            T2.insert(INSERT,"Enter the points properly")
        if(CheckVar3.get()==1):
            T3.insert(INSERT,"Enter the points properly")              
       # if(CheckVar4.get()==1):
        #    T4.insert(INSERT,"Enter the points properly")
        if(CheckVar5.get()==1):
            T5.insert(INSERT,"Enter the points properly")
        if(CheckVar6.get()==1):
            T6.insert(INSERT,"Enter the points properly")
        if(CheckVar7.get()==1):
            T7.insert(INSERT,"Enter the points properly")
        if(CheckVar8.get()==1):
            T8.insert(INSERT,"Enter the points properly")






CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
#CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()

variable3 = StringVar(my_frame2)


blank1 = Label(my_frame2,text = " ").grid(row=0,column=0)
k3 = Label(my_frame2,text = " Enter Request Points :").grid(row=1,column=0)

inputtxt3 = Text(my_frame2, height = 3,width = 25,bg = "light yellow")
inputtxt3.grid(row=1,column=1)
blank2 = Label(my_frame2,text = " ").grid(row=2,column=0)

head3 = Label(my_frame2,text = "Intial Head Position :").grid(row=3,column=0)
head_text3 = Text(my_frame2,height=1,width = 25,bg = "light yellow")
head_text3.grid(row=3,column=1,padx=50)

blank3 = Label(my_frame2,text = " ").grid(row=4,column=0)

variable3.set("RIGHT")
direction3 = Label(my_frame2,text = "Direction:").grid(row=5,column=0)
direction_op3 = OptionMenu(my_frame2, variable3, "RIGHT", "LEFT").grid(row=5,column=1)
blank4 = Label(my_frame2,text = " ").grid(row=6,column=0)

max_cyl3 = Label(my_frame2,text = "Maximum Cylinder :").grid(row=7,column=0)
maxcyl_text3 = Text(my_frame2,height=1,width = 25,bg = "light yellow")
maxcyl_text3.grid(row=7,column=1)

blank5 = Label(my_frame2,text = " ").grid(row=8,column=0)

min_cyl3 = Label(my_frame2,text = "Minimum Cylinder :").grid(row=9,column=0)
mincyl_text3 = Text(my_frame2,height=1,width = 25,bg = "light yellow")
mincyl_text3.grid(row=9,column=1)
blank6 = Label(my_frame2,text = " ").grid(row=10,column=0)




k11 = Label(my_frame2,text = "Select the Algorithm").grid(row=11,column=0)
k22 = Label(my_frame2,text = "Total Seek Time").grid(row=11,column=1)


blank7 = Label(my_frame2,text = " ").grid(row=12,column=0)


C1 = Checkbutton(my_frame2, text = "FCFS", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20).grid(row=13,column=0)

T1 = Text(my_frame2,height=1,width=20)
T1.grid(row=13,column=1)


C2 = Checkbutton(my_frame2, text = "SSTF", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20).grid(row=14,column=0)
T2 = Text(my_frame2,height=1,width=20)
T2.grid(row=14,column=1)


C3 = Checkbutton(my_frame2, text = "SCAN", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20).grid(row=15,column=0)
T3 = Text(my_frame2,height=1,width=20)
T3.grid(row=15,column=1)
"""C4 = Checkbutton(my_frame3, text = "LIFO", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20).grid(row=19,column=0)
T4 = Text(my_frame3,height=1,width=20)
T4.grid(row=19,column=1)"""



C5 = Checkbutton(my_frame2, text = "CSCAN", variable = CheckVar5, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 23).grid(row=16,column=0)
T5 = Text(my_frame2,height=1,width=20)
T5.grid(row=16,column=1)


C7 = Checkbutton(my_frame2, text = "LOOK", variable = CheckVar7, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20).grid(row=17,column=0)
T7 = Text(my_frame2,height=1,width=20)
T7.grid(row=17,column=1)


C8 = Checkbutton(my_frame2, text = "CLOOK", variable = CheckVar8, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20).grid(row=18,column=0)
T8 = Text(my_frame2,height=1,width=20)
T8.grid(row=18,column=1)
T9=Label(my_frame2,text = "The best algorithm for the given value is ").grid(row=20,column=0)
t10=Text(my_frame2,height=1,width=20)
t10.grid(row=20,column=1)
save3 = Button(my_frame2, text="RUN", command=checkBox,padx=85)
blank7 = Label(my_frame2,text = " ").grid(row=21,column=0)
save3.grid(row=22,column=1)
mainloop()