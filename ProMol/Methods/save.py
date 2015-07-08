def imgSave():
    
    file = asksaveasfilename(defaultextension = ".png", initialdir = "./PyMOL/")
    if len(file)>0:
        cmd.save(file)

def imgraysave():
    
    root = Tk()
    root.geometry('226x147+140+140')
    root.title('Ray Trace')
    msg = Message(root, width = 200,
        text = "Ray Trace before saving for a higher resolution image")
    msg.place(x = 5, y = 5)
    a_label = Label(root, text = "Width")
    name1 = Entry(root, width = 12)
    name1.insert(0, 640)
    b_label = Label(root, text = "Height")
    name2 = Entry(root, width = 12)
    a_button = Button(root, text = "Ray Trace")
    a_label.place(x = 10, y = 50)
    b_button = Button(root, text = "Save")
    name1.place(x = 50, y = 50)
    b_label.place(x = 10, y = 80)
    name2.place(x = 50, y = 80)
    name2.insert(0, 480)
    a_button.place(x = 10, y = 110)
    b_button.place(x = 80, y = 110)
    c_button = Button(root, text = "Auto Calc")
    c_button.place(x = 150, y = 64)
    d_button = Button(root, text = 'Help')
    d_button.place(x = 150, y = 110)
    d_button.configure(width = "8")
    b_button.configure(width = "8")
    a_button.configure(width = "8")
    c_button.configure(width = "8")
    #Help Message Box
    def rthelp(event):
        showinfo('Help', 'To save a higher resolution image you \n'+
            'must input width and height paramaters.\n \n'+
            'Or input just width or just height and\n'+
            ' use the Auto Calc button to get the other.\n\n'+
            ' Paramaters should be under 5 digits\n'+
            ' or else Ray Trace may take a long time. \n \n'+
            'Then click Save to save your image.')
        root.mainloop()
    d_button.bind('<Button-1>', rthelp)
    #Auto Calc Function
    def autocalc(event):
        try:
            if len(name1.get()) >= 1:
                name2.delete(0, 20)
                name2.insert(0, int(int(name1.get())*.75))
            elif len(name2.get()) >= 1:
                name1.delete(0, 20)
                name1.insert(0, int(int(name2.get())*(12/9)))
        except:
            showinfo("Error", "Enter an integer value for width or height")
            root.mainloop()
    c_button.bind('<Button-1>', autocalc)
    #Defines ray trace function
    def raytrace(event):
        try:
            if len(name1.get()) > 3:
                
                
                showinfo('Ray Trace', 'You have entered a large value. '+
                    'Please be patient.\nClick OK to continue.')
                cmd.ray(name1.get(), name2.get())
                root.mainloop()
            else:
                cmd.ray(name1.get(), name2.get())
                root.mainloop()
        except:
            
            
            showinfo("Error", "Enter an integer value for width and height")
            root.mainloop()
    def savestop(event):
        file = asksaveasfilename(defaultextension = ".png",
            initialdir = "./PyMOL/")
        if len(file)>0:
            cmd.save(file)
        root.destroy()
    a_button.bind('<Button-1>', raytrace)
    b_button.bind('<Button-1>', savestop)
    root.mainloop()

def openfilename(event):
  filename = askopenfilename()
  entry123.insert(0, filename)

def savefilename(*args):
  filename = asksaveasfilename(filetypes=myFormats,
                               title="Save Output As...")
  if (file == 0):
    showerror('Destination File Error',
                           'Destination does not exist')
  else:
    return filename

def savefile(filename, fileString):
    try:
        newFile = open(filename,"wb")
        newFile.write(fileString)
        newFile.close()
    except:
        pass
    topFrame = Frame(interior)
    bottomFrame = Frame(interior)
    
def molSave():
  try:
    try:
      a = int(enti.get()) + 1
      enti.delete(0,100000)
      enti.insert(0,a)

      file = asksaveasfilename(defaultextension=entfilex.get(), initialdir=glb.HOME, initialfile= "frame" + enti.get())
      if len(file)>0:
          cmd.save(file)
      glb.GUI.movie_maker['tab'].mainloop()
    except:
      a = int(enti.get()) + 1
      enti.delete(0,100000)
      enti.insert(0,a)

      file = asksaveasfilename(defaultextension=entfilex.get(), initialdir=glb.HOME, initialfile= "frame" + enti.get())
      if len(file)>0:
          cmd.save(file)
    glb.GUI.movie_maker['tab'].mainloop()
  except:


    showinfo("Error", 'Please enter a movie title')