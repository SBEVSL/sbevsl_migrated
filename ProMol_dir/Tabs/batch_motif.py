page = notebook.add('Batch Motif')
group = Pmw.Group(page, tag_text='Enter Location of List')
group.grid(row=0, column=0, padx=0, pady=0)
interior=group.interior()
    
myFormats = [('Text File', '*.txt')]

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
        newFile = open(filename,"w")
        newFile.write(fileString)
        newFile.close()
      except:
        pass
    
    topFrame = Frame(interior)
    bottomFrame = Frame(interior)

w = Text(interior, height = 3)
    w.insert(END, "\n")
    w.insert(END, "Make a comma separated list of sensitivities")
    w.insert(END, "\n")
w.insert(END, "Find your text file of molecules.")


w.config(state = DISABLED)
    
    sensEntry = Entry(interior)
entry123 = Entry(interior)
button123 = Button(interior,
                       text = 'Run')
browse = Button(interior, text = 'Browse')
browse.bind('<Button-1>', openfilename);

w.grid(row = 0, column = 0, columnspan = 2)
    Label(interior, text = 'Sensitivities:').grid(row = 1, column = 0, sticky =  E)
    Label(interior, text = 'File:').grid(row = 2, column = 0, sticky = E)
    sensEntry.grid(row = 1, column = 1, sticky = W)
entry123.grid(row = 2, column = 1, sticky = W)
button123.grid(row = 3, column = 0, sticky = E)
interior.pack()
browse.grid(row = 3, column = 1, sticky = W)
    
    def myGetPdb(pdbNum):
        
        
        pdbCode = pdbNum
        pdbCode = string.upper(pdbCode)
        filename = urllib.urlretrieve('http://www.rcsb.org/pdb/cgi/export.cgi/' +
                        pdbCode + '.pdb.gz?format=PDB&pdbId=' +
                        pdbCode + '&compression=gz')[0]
        
        # If 0, then pdb code was invalid
        if (os.path.getsize(filename) > 0):
            
            # Decompress the file while reading
            fpin = gzip.open(filename)
            
            # Form the pdb output name
            outputname = os.path.dirname(filename) + os.sep + pdbCode + '.pdb'
            fpout = open(outputname, 'w')
            fpout.write(fpin.read()) # Write pdb file
            
            fpin.close()
            fpout.close()
            
            cmd.load(outputname) # Load the fresh pdb
            
            
            #---------------THIS WAS JUST ADDED---------------------------
            #update()
            cmd.deselect()
        
        else:
            showerror('Invalid Code',
                       'You entered an invalid pdb code:' + pdbCode)
            
            os.remove(filename) # Remove tmp file (leave the pdb)
    
    def batchLoop(*args):
      #f = ''
      ranges = []
      string = ""
      #filename = savefilename(self)
      if (len(args) == 1):
        try:
          f=open(entry123.get())
        except:
          showerror('No input file',
                                 'You did not choose an input file yet')
          pass
      else:
        try:
          f=open('./temp', 'w')
        except:
          showerror('Filewrite error',
                                 'Sorry, there was an error writing the file')
        for each in args:
          try:
            float(each)
            ranges.append(float(each))
          except:
            f.write(each + '\n')
      f.close()
      try:
        f=open('./temp')
      except:
        pass
      try:
        f=open(entry123.get())
      except:
        pass
      try:
        f=open(args[0])
      except:
        pass
      
      for line in f.readlines():
        if (len(args) == 1):
          ranges = sensEntry.get().split(',')
        for each in ranges:
          try:
            float(each)
          except ValueError:
            showerror('Incorrect Formatting',
                                   'Check the formatting of sensitivities')
            #sensEntry.delete(0,END)
          else:
            self.range.set(each)
            line = line.strip()
            cmd.delete('all')
            myGetPdb(line)
            motifList = motifchecker(self)
            string += line
            string +='\t' + str(self.range.get()) + '\n'
            for i in motifList:
              string += '\t'*3 + str(i) + '\n'
            print string
            filename = savefilename(self)
            savefile(filename, string)
    cmd.extend('batchLoop',batchLoop)
    button123.bind('<Button-1>', batchLoop)