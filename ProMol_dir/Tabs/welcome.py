splash = PhotoImage(file="%ssplashmol.gif" % (PROMOL_PATH))

page = notebook.add('Welcome')
notebook.tab('Welcome').focus_set()
canvas=Canvas(page)
canvas.pack(fill='both', expand=1)
canvas.create_image(0,0,image=splash,anchor=NW)