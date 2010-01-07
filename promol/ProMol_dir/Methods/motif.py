from pymol import cmd
import Tkinter as tk
import Pmw
from tkFileDialog import askopenfilename
from tkSimpleDialog import askstring
from tkMessageBox import showinfo
from pmg_tk.startup.ProMol_dir import promolglobals as pglob

Pmw.initialise()

def motifCaller(motif_function, camera = True):
    delta = pglob.Tabs['motifs']['delta'].get()
    pglob.deletemotif()
    pglob.update()
    motif = globals()[motif_function](delta)
    if motif != False:
        cmd.hide('everything')
        if camera:
            cmd.show('cartoon', 'all')
            cmd.set('cartoon_transparency', '0.5', 'all')
            cmd.set('stick_radius', '0.5')
        if type(motif).__name__ == 'dict':
            #pglob.cpk(motif['motif'])
            x = motif['extra']
            xlen = range(len(x))
            xkeys = x.keys()
            xvals = x.values()
            for l in xlen:
                pass
                #pglob.cpk(xvals[l],xkeys[l],0)
            cmd.orient(motif['motif'])
        else:
            #pglob.cpk(motif,'sticks')
            cmd.orient(motif)
        cmd.deselect()
    elif camera == True:
        showinfo('Not Found','The selected motif did not return a result.')

def byResidue(selection, num):
    byres, delete = '', ''
    numbers = delta(1, num)
    for number in numbers:
        if number == num:
            byres = str.join((byres, 'byres ', selection, number))
            delete = str.join((delete, selection, number))
        else:
            byres = str.join((byres, 'byres ', selection, number, ' and '))
            delete = str.join((delete, selection, number, ', '))
    cmd.do('select %s, %s'%(selection, byres))
    cmd.do('delete %s'%(delete))

def delSelections(*selections):
    delete = ''
    i = 1
    selecLen = len(selections)
    for selection in selections:
        if i == selecLen:
            delete = str.join((delete, selection, number))
        else:
            delete = str.join((delete, selection, number, ', '))
        i += 1
    cmd.do('delete %s'%(delete))

def aldosereductaseCaCb(delta):
    cmd.do('select temp0, name ca')
    cmd.do('select temp1, resn asp')
    cmd.do('select temp2, resn glu')
    cmd.do('select jessatom0, (((temp0 and temp1) or (temp0 and temp2)))')
    cmd.do('select temp3, name cb')
    cmd.do('select temp4, all within %s of (jessatom0)'%(delta*1.545300))
    cmd.do('select temp5, byres jessatom0')
    cmd.do('select jessatom1, (((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom1)'%(delta*1.545300))
    cmd.do('select temp6, resn tyr')
    cmd.do('select temp7, all within %s of (jessatom0)'%(delta*10.554500))
    cmd.do('select temp8, all within %s of (jessatom1)'%(delta*10.766600))
    cmd.do('select jessatom2, (temp0 and temp6 and temp7 and temp8)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom2)'%(delta*10.554500))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom2)'%(delta*10.766600))
    cmd.do('select temp9, all within %s of (jessatom0)'%(delta*9.120300))
    cmd.do('select temp10, all within %s of (jessatom1)'%(delta*9.342500))
    cmd.do('select temp11, all within %s of (jessatom2)'%(delta*1.545300))
    cmd.do('select temp12, byres jessatom2')
    cmd.do('select jessatom3, (temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom3)'%(delta*9.120300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom3)'%(delta*9.342500))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom3)'%(delta*1.545300))
    cmd.do('select temp13, resn lys')
    cmd.do('select temp14, all within %s of (jessatom0)'%(delta*8.918300))
    cmd.do('select temp15, all within %s of (jessatom1)'%(delta*9.241500))
    cmd.do('select temp16, all within %s of (jessatom2)'%(delta*9.857600))
    cmd.do('select temp17, all within %s of (jessatom3)'%(delta*9.504100))
    cmd.do('select jessatom4, (temp0 and temp13 and temp14 and temp15 and temp16 and temp17)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom4)'%(delta*8.918300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom4)'%(delta*9.241500))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom4)'%(delta*9.857600))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom4)'%(delta*9.504100))
    cmd.do('select temp18, all within %s of (jessatom0)'%(delta*8.544600))
    cmd.do('select temp19, all within %s of (jessatom1)'%(delta*8.625400))
    cmd.do('select temp20, all within %s of (jessatom2)'%(delta*9.281900))
    cmd.do('select temp21, all within %s of (jessatom3)'%(delta*8.888000))
    cmd.do('select temp22, all within %s of (jessatom4)'%(delta*1.565500))
    cmd.do('select temp23, byres jessatom4')
    cmd.do('select jessatom5, (temp3 and temp13 and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom5)'%(delta*8.544600))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom5)'%(delta*8.625400))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom5)'%(delta*9.281900))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom5)'%(delta*8.888000))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom5)'%(delta*1.565500))
    cmd.do('select temp24, resn his')
    cmd.do('select temp25, all within %s of (jessatom0)'%(delta*11.857400))
    cmd.do('select temp26, all within %s of (jessatom1)'%(delta*11.503900))
    cmd.do('select temp27, all within %s of (jessatom2)'%(delta*11.483700))
    cmd.do('select temp28, all within %s of (jessatom3)'%(delta*11.413000))
    cmd.do('select temp29, all within %s of (jessatom4)'%(delta*5.171200))
    cmd.do('select temp30, all within %s of (jessatom5)'%(delta*4.191500))
    cmd.do('select jessatom6, (temp0 and temp24 and temp25 and temp26 and temp27 and temp28 and temp29 and temp30)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom6)'%(delta*11.857400))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom6)'%(delta*11.503900))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom6)'%(delta*11.483700))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom6)'%(delta*11.413000))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom6)'%(delta*5.171200))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom6)'%(delta*4.191500))
    cmd.do('select temp31, all within %s of (jessatom0)'%(delta*11.665500))
    cmd.do('select temp32, all within %s of (jessatom1)'%(delta*11.402900))
    cmd.do('select temp33, all within %s of (jessatom2)'%(delta*10.140400))
    cmd.do('select temp34, all within %s of (jessatom3)'%(delta*10.190900))
    cmd.do('select temp35, all within %s of (jessatom4)'%(delta*4.817700))
    cmd.do('select temp36, all within %s of (jessatom5)'%(delta*3.797600))
    cmd.do('select temp37, all within %s of (jessatom6)'%(delta*1.535200))
    cmd.do('select temp38, byres jessatom6')
    cmd.do('select jessatom7, (temp3 and temp24 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom7)'%(delta*11.665500))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom7)'%(delta*11.402900))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom7)'%(delta*10.140400))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom7)'%(delta*10.190900))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom7)'%(delta*4.817700))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom7)'%(delta*3.797600))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom7)'%(delta*1.535200))
    cmd.do('select Aldose_Reductase_CaCb, byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
    return {'motif':'Aldose_Reductase_CaCb'}

def aldosereductaseFA(delta):
    cmd.do('select temp0, name cg')
    cmd.do('select temp1, resn asp')
    cmd.do('select temp2, resn glu')
    cmd.do('select jessatom0, (((temp0 and temp1) or (temp0 and temp2)))')
    cmd.do('select temp3, name od1')
    cmd.do('select temp4, name od2')
    cmd.do('select temp5, name oe1')
    cmd.do('select temp6, name oe2')
    cmd.do('select temp7, all within %s of (jessatom0)'%(delta*1.272600))
    cmd.do('select temp8, byres jessatom0')
    cmd.do('select jessatom1, ((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom1)'%(delta*1.272600))
    cmd.do('select temp9, name od2')
    cmd.do('select temp10, name od1')
    cmd.do('select temp11, name oe2')
    cmd.do('select temp12, name oe1')
    cmd.do('select temp13, all within %s of (jessatom0)'%(delta*1.262500))
    cmd.do('select temp14, byres jessatom0')
    cmd.do('select temp15, all within %s of (jessatom1)'%(delta*2.222000))
    cmd.do('select jessatom2, ((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp13 and temp14 and temp15)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom2)'%(delta*1.262500))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom2)'%(delta*2.222000))
    cmd.do('select temp16, name ce1')
    cmd.do('select temp17, resn tyr')
    cmd.do('select temp18, all within %s of (jessatom0)'%(delta*7.312400))
    cmd.do('select temp19, all within %s of (jessatom1)'%(delta*7.928500))
    cmd.do('select temp20, all within %s of (jessatom2)'%(delta*6.150900))
    cmd.do('select jessatom3, (temp16 and temp17 and temp18 and temp19 and temp20)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom3)'%(delta*7.312400))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom3)'%(delta*7.928500))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom3)'%(delta*6.150900))
    cmd.do('select temp21, name cz')
    cmd.do('select temp22, all within %s of (jessatom0)'%(delta*5.938800))
    cmd.do('select temp23, all within %s of (jessatom1)'%(delta*6.595300))
    cmd.do('select temp24, all within %s of (jessatom2)'%(delta*4.767200))
    cmd.do('select temp25, all within %s of (jessatom3)'%(delta*1.393800))
    cmd.do('select temp26, byres jessatom3')
    cmd.do('select jessatom4, (temp21 and temp17 and temp22 and temp23 and temp24 and temp25 and temp26)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom4)'%(delta*5.938800))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom4)'%(delta*6.595300))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom4)'%(delta*4.767200))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom4)'%(delta*1.393800))
    cmd.do('select temp27, name oh')
    cmd.do('select temp28, all within %s of (jessatom0)'%(delta*5.292400))
    cmd.do('select temp29, all within %s of (jessatom1)'%(delta*5.847900))
    cmd.do('select temp30, all within %s of (jessatom2)'%(delta*4.090500))
    cmd.do('select temp31, all within %s of (jessatom3)'%(delta*2.464400))
    cmd.do('select temp32, byres jessatom3')
    cmd.do('select temp33, all within %s of (jessatom4)'%(delta*1.383700))
    cmd.do('select jessatom5, (temp27 and temp17 and temp28 and temp29 and temp30 and temp31 and temp32 and temp33)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom5)'%(delta*5.292400))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom5)'%(delta*5.847900))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom5)'%(delta*4.090500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom5)'%(delta*2.464400))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom5)'%(delta*1.383700))
    cmd.do('select temp34, name  cd ')
    cmd.do('select temp35, resn lys')
    cmd.do('select temp36, all within %s of (jessatom0)'%(delta*5.575200))
    cmd.do('select temp37, all within %s of (jessatom1)'%(delta*5.110600))
    cmd.do('select temp38, all within %s of (jessatom2)'%(delta*5.151000))
    cmd.do('select temp39, all within %s of (jessatom3)'%(delta*5.918600))
    cmd.do('select temp40, all within %s of (jessatom4)'%(delta*5.231800))
    cmd.do('select temp41, all within %s of (jessatom5)'%(delta*4.545000))
    cmd.do('select jessatom6, (temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom6)'%(delta*5.575200))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom6)'%(delta*5.110600))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom6)'%(delta*5.151000))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom6)'%(delta*5.918600))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom6)'%(delta*5.231800))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom6)'%(delta*4.545000))
    cmd.do('select temp42, name  ce ')
    cmd.do('select temp43, all within %s of (jessatom0)'%(delta*4.171300))
    cmd.do('select temp44, all within %s of (jessatom1)'%(delta*3.737000))
    cmd.do('select temp45, all within %s of (jessatom2)'%(delta*3.757200))
    cmd.do('select temp46, all within %s of (jessatom3)'%(delta*5.898400))
    cmd.do('select temp47, all within %s of (jessatom4)'%(delta*4.918700))
    cmd.do('select temp48, all within %s of (jessatom5)'%(delta*4.019800))
    cmd.do('select temp49, all within %s of (jessatom6)'%(delta*1.535200))
    cmd.do('select temp50, byres jessatom6')
    cmd.do('select jessatom7, (temp42 and temp35 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom7)'%(delta*4.171300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom7)'%(delta*3.737000))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom7)'%(delta*3.757200))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom7)'%(delta*5.898400))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom7)'%(delta*4.918700))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom7)'%(delta*4.019800))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom7)'%(delta*1.535200))
    cmd.do('select temp51, name nz')
    cmd.do('select temp52, all within %s of (jessatom0)'%(delta*3.444100))
    cmd.do('select temp53, all within %s of (jessatom1)'%(delta*3.464300))
    cmd.do('select temp54, all within %s of (jessatom2)'%(delta*2.767400))
    cmd.do('select temp55, all within %s of (jessatom3)'%(delta*4.888400))
    cmd.do('select temp56, all within %s of (jessatom4)'%(delta*3.747100))
    cmd.do('select temp57, all within %s of (jessatom5)'%(delta*3.030000))
    cmd.do('select temp58, all within %s of (jessatom6)'%(delta*2.525000))
    cmd.do('select temp59, byres jessatom6')
    cmd.do('select temp60, all within %s of (jessatom7)'%(delta*1.515000))
    cmd.do('select jessatom8, (temp51 and temp35 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom8)'%(delta*3.444100))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom8)'%(delta*3.464300))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom8)'%(delta*2.767400))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom8)'%(delta*4.888400))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom8)'%(delta*3.747100))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom8)'%(delta*3.030000))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom8)'%(delta*2.525000))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom8)'%(delta*1.515000))
    cmd.do('select temp61, resn his')
    cmd.do('select temp62, all within %s of (jessatom0)'%(delta*9.069800))
    cmd.do('select temp63, all within %s of (jessatom1)'%(delta*8.776900))
    cmd.do('select temp64, all within %s of (jessatom2)'%(delta*8.372900))
    cmd.do('select temp65, all within %s of (jessatom3)'%(delta*6.120600))
    cmd.do('select temp66, all within %s of (jessatom4)'%(delta*6.272100))
    cmd.do('select temp67, all within %s of (jessatom5)'%(delta*5.888300))
    cmd.do('select temp68, all within %s of (jessatom6)'%(delta*3.767300))
    cmd.do('select temp69, all within %s of (jessatom7)'%(delta*5.060100))
    cmd.do('select temp70, all within %s of (jessatom8)'%(delta*5.686300))
    cmd.do('select jessatom9, (temp0 and temp61 and temp62 and temp63 and temp64 and temp65 and temp66 and temp67 and temp68 and temp69 and temp70)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom9)'%(delta*9.069800))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom9)'%(delta*8.776900))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom9)'%(delta*8.372900))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom9)'%(delta*6.120600))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom9)'%(delta*6.272100))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom9)'%(delta*5.888300))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom9)'%(delta*3.767300))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom9)'%(delta*5.060100))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom9)'%(delta*5.686300))
    cmd.do('select temp71, name nd1')
    cmd.do('select temp72, all within %s of (jessatom0)'%(delta*8.817300))
    cmd.do('select temp73, all within %s of (jessatom1)'%(delta*8.665800))
    cmd.do('select temp74, all within %s of (jessatom2)'%(delta*8.049700))
    cmd.do('select temp75, all within %s of (jessatom3)'%(delta*5.130800))
    cmd.do('select temp76, all within %s of (jessatom4)'%(delta*5.433800))
    cmd.do('select temp77, all within %s of (jessatom5)'%(delta*5.332800))
    cmd.do('select temp78, all within %s of (jessatom6)'%(delta*3.848100))
    cmd.do('select temp79, all within %s of (jessatom7)'%(delta*5.100500))
    cmd.do('select temp80, all within %s of (jessatom8)'%(delta*5.363100))
    cmd.do('select temp81, all within %s of (jessatom9)'%(delta*1.403900))
    cmd.do('select temp82, byres jessatom9')
    cmd.do('select jessatom10, (temp71 and temp61 and temp72 and temp73 and temp74 and temp75 and temp76 and temp77 and temp78 and temp79 and temp80 and temp81 and temp82)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom10)'%(delta*8.817300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom10)'%(delta*8.665800))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom10)'%(delta*8.049700))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom10)'%(delta*5.130800))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom10)'%(delta*5.433800))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom10)'%(delta*5.332800))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom10)'%(delta*3.848100))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom10)'%(delta*5.100500))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom10)'%(delta*5.363100))
    cmd.do('select jessatom9, jessatom9 within %s of (jessatom10)'%(delta*1.403900))
    cmd.do('select temp83, name ne2')
    cmd.do('select temp84, all within %s of (jessatom0)'%(delta*8.100200))
    cmd.do('select temp85, all within %s of (jessatom1)'%(delta*8.080000))
    cmd.do('select temp86, all within %s of (jessatom2)'%(delta*7.181100))
    cmd.do('select temp87, all within %s of (jessatom3)'%(delta*4.343000))
    cmd.do('select temp88, all within %s of (jessatom4)'%(delta*4.524800))
    cmd.do('select temp89, all within %s of (jessatom5)'%(delta*4.040000))
    cmd.do('select temp90, all within %s of (jessatom6)'%(delta*3.827900))
    cmd.do('select temp91, all within %s of (jessatom7)'%(delta*4.565200))
    cmd.do('select temp92, all within %s of (jessatom8)'%(delta*4.797500))
    cmd.do('select temp93, all within %s of (jessatom9)'%(delta*2.222000))
    cmd.do('select temp94, byres jessatom9')
    cmd.do('select temp95, all within %s of (jessatom10)'%(delta*2.191700))
    cmd.do('select jessatom11, (temp83 and temp61 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89 and temp90 and temp91 and temp92 and temp93 and temp94 and temp95)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom11)'%(delta*8.100200))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom11)'%(delta*8.080000))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom11)'%(delta*7.181100))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom11)'%(delta*4.343000))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom11)'%(delta*4.524800))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom11)'%(delta*4.040000))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom11)'%(delta*3.827900))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom11)'%(delta*4.565200))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom11)'%(delta*4.797500))
    cmd.do('select jessatom9, jessatom9 within %s of (jessatom11)'%(delta*2.222000))
    cmd.do('select jessatom10, jessatom10 within %s of (jessatom11)'%(delta*2.191700))
    cmd.do('select Aldose_Reductase_FA, byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
    return {'motif':'Aldose_Reductase_FA'}

def chondroitinaseCaCb(delta):
    cmd.do('select temp0, name  ca ')
    cmd.do('select temp1, resn his')
    cmd.do('select jessatom0, (temp0 and temp1)')
    cmd.do('select temp2, name  cb ')
    cmd.do('select temp3, resn his')
    cmd.do('select temp4, all within %s of (jessatom0)'%(delta*1.545300))
    cmd.do('select temp5, byres jessatom0')
    cmd.do('select jessatom1, (temp2 and temp3 and temp4 and temp5)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom1)'%(delta*1.545300))
    cmd.do('select temp6, resn tyr')
    cmd.do('select temp7, all within %s of (jessatom0)'%(delta*9.332400))
    cmd.do('select temp8, all within %s of (jessatom1)'%(delta*9.110200))
    cmd.do('select jessatom2, (temp0 and temp6 and temp7 and temp8)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom2)'%(delta*9.332400))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom2)'%(delta*9.110200))
    cmd.do('select temp9, all within %s of (jessatom0)'%(delta*7.807300))
    cmd.do('select temp10, all within %s of (jessatom1)'%(delta*7.676000))
    cmd.do('select temp11, all within %s of (jessatom2)'%(delta*1.555400))
    cmd.do('select temp12, byres jessatom2')
    cmd.do('select jessatom3, (temp2 and temp6 and temp9 and temp10 and temp11 and temp12)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom3)'%(delta*7.807300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom3)'%(delta*7.676000))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom3)'%(delta*1.555400))
    cmd.do('select temp13, resn arg')
    cmd.do('select temp14, all within %s of (jessatom0)'%(delta*11.635200))
    cmd.do('select temp15, all within %s of (jessatom1)'%(delta*10.201000))
    cmd.do('select temp16, all within %s of (jessatom2)'%(delta*10.655500))
    cmd.do('select temp17, all within %s of (jessatom3)'%(delta*10.554500))
    cmd.do('select jessatom4, (temp0 and temp13 and temp14 and temp15 and temp16 and temp17)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom4)'%(delta*11.635200))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom4)'%(delta*10.201000))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom4)'%(delta*10.655500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom4)'%(delta*10.554500))
    cmd.do('select temp18, all within %s of (jessatom0)'%(delta*11.049400))
    cmd.do('select temp19, all within %s of (jessatom1)'%(delta*9.554600))
    cmd.do('select temp20, all within %s of (jessatom2)'%(delta*10.877700))
    cmd.do('select temp21, all within %s of (jessatom3)'%(delta*10.645400))
    cmd.do('select temp22, all within %s of (jessatom4)'%(delta*1.565500))
    cmd.do('select temp23, byres jessatom4')
    cmd.do('select jessatom5, (temp2 and temp13 and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom5)'%(delta*11.049400))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom5)'%(delta*9.554600))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom5)'%(delta*10.877700))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom5)'%(delta*10.645400))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom5)'%(delta*1.565500))
    cmd.do('select Chondroitinase_CaCb, byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
    return {'motif':'Chondroitinase_CaCb'}

def chondroitinaseFA(delta):
    cmd.do('select temp0, name  cg ')
    cmd.do('select temp1, resn his')
    cmd.do('select jessatom0, (temp0 and temp1)')
    cmd.do('select temp2, name  nd1')
    cmd.do('select temp3, resn his')
    cmd.do('select temp4, all within %s of (jessatom0)'%(delta*1.383700))
    cmd.do('select temp5, byres jessatom0')
    cmd.do('select jessatom1, (temp2 and temp3 and temp4 and temp5)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom1)'%(delta*1.383700))
    cmd.do('select temp6, name  ne2')
    cmd.do('select temp7, all within %s of (jessatom0)'%(delta*2.222000))
    cmd.do('select temp8, byres jessatom0')
    cmd.do('select temp9, all within %s of (jessatom1)'%(delta*2.171500))
    cmd.do('select jessatom2, (temp6 and temp3 and temp7 and temp8 and temp9)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom2)'%(delta*2.222000))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom2)'%(delta*2.171500))
    cmd.do('select temp10, name  ce1')
    cmd.do('select temp11, resn tyr')
    cmd.do('select temp12, all within %s of (jessatom0)'%(delta*5.686300))
    cmd.do('select temp13, all within %s of (jessatom1)'%(delta*5.363100))
    cmd.do('select temp14, all within %s of (jessatom2)'%(delta*4.050100))
    cmd.do('select jessatom3, (temp10 and temp11 and temp12 and temp13 and temp14)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom3)'%(delta*5.686300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom3)'%(delta*5.363100))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom3)'%(delta*4.050100))
    cmd.do('select temp15, name  cz ')
    cmd.do('select temp16, all within %s of (jessatom0)'%(delta*4.979300))
    cmd.do('select temp17, all within %s of (jessatom1)'%(delta*4.383400))
    cmd.do('select temp18, all within %s of (jessatom2)'%(delta*3.474400))
    cmd.do('select temp19, all within %s of (jessatom3)'%(delta*1.383700))
    cmd.do('select temp20, byres jessatom3')
    cmd.do('select jessatom4, (temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom4)'%(delta*4.979300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom4)'%(delta*4.383400))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom4)'%(delta*3.474400))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom4)'%(delta*1.383700))
    cmd.do('select temp21, name  oh ')
    cmd.do('select temp22, all within %s of (jessatom0)'%(delta*5.019700))
    cmd.do('select temp23, all within %s of (jessatom1)'%(delta*4.201600))
    cmd.do('select temp24, all within %s of (jessatom2)'%(delta*3.272400))
    cmd.do('select temp25, all within %s of (jessatom3)'%(delta*2.403800))
    cmd.do('select temp26, byres jessatom3')
    cmd.do('select temp27, all within %s of (jessatom4)'%(delta*1.383700))
    cmd.do('select jessatom5, (temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom5)'%(delta*5.019700))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom5)'%(delta*4.201600))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom5)'%(delta*3.272400))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom5)'%(delta*2.403800))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom5)'%(delta*1.383700))
    cmd.do('select temp28, name  ne ')
    cmd.do('select temp29, resn arg')
    cmd.do('select temp30, all within %s of (jessatom0)'%(delta*7.787100))
    cmd.do('select temp31, all within %s of (jessatom1)'%(delta*6.413500))
    cmd.do('select temp32, all within %s of (jessatom2)'%(delta*7.039700))
    cmd.do('select temp33, all within %s of (jessatom3)'%(delta*7.453800))
    cmd.do('select temp34, all within %s of (jessatom4)'%(delta*6.201400))
    cmd.do('select temp35, all within %s of (jessatom5)'%(delta*5.241900))
    cmd.do('select jessatom6, (temp28 and temp29 and temp30 and temp31 and temp32 and temp33 and temp34 and temp35)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom6)'%(delta*7.787100))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom6)'%(delta*6.413500))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom6)'%(delta*7.039700))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom6)'%(delta*7.453800))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom6)'%(delta*6.201400))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom6)'%(delta*5.241900))
    cmd.do('select temp36, name  nh1')
    cmd.do('select temp37, name  nh2')
    cmd.do('select temp38, all within %s of (jessatom0)'%(delta*5.726700))
    cmd.do('select temp39, all within %s of (jessatom1)'%(delta*4.403600))
    cmd.do('select temp40, all within %s of (jessatom2)'%(delta*4.827800))
    cmd.do('select temp41, all within %s of (jessatom3)'%(delta*5.302500))
    cmd.do('select temp42, all within %s of (jessatom4)'%(delta*3.989500))
    cmd.do('select temp43, all within %s of (jessatom5)'%(delta*3.070400))
    cmd.do('select temp44, all within %s of (jessatom6)'%(delta*2.343200))
    cmd.do('select temp45, byres jessatom6')
    cmd.do('select jessatom7, ((temp36 or temp37) and temp29 and temp38 and temp39 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom7)'%(delta*5.726700))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom7)'%(delta*4.403600))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom7)'%(delta*4.827800))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom7)'%(delta*5.302500))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom7)'%(delta*3.989500))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom7)'%(delta*3.070400))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom7)'%(delta*2.343200))
    cmd.do('select temp46, name  nh2')
    cmd.do('select temp47, name  nh1')
    cmd.do('select temp48, all within %s of (jessatom0)'%(delta*7.595200))
    cmd.do('select temp49, all within %s of (jessatom1)'%(delta*6.363000))
    cmd.do('select temp50, all within %s of (jessatom2)'%(delta*6.241800))
    cmd.do('select temp51, all within %s of (jessatom3)'%(delta*6.039800))
    cmd.do('select temp52, all within %s of (jessatom4)'%(delta*5.019700))
    cmd.do('select temp53, all within %s of (jessatom5)'%(delta*3.858200))
    cmd.do('select temp54, all within %s of (jessatom6)'%(delta*2.323000))
    cmd.do('select temp55, byres jessatom6')
    cmd.do('select temp56, all within %s of (jessatom7)'%(delta*2.292700))
    cmd.do('select jessatom8, ((temp46 or temp47) and temp29 and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom8)'%(delta*7.595200))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom8)'%(delta*6.363000))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom8)'%(delta*6.241800))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom8)'%(delta*6.039800))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom8)'%(delta*5.019700))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom8)'%(delta*3.858200))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom8)'%(delta*2.323000))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom8)'%(delta*2.292700))
    cmd.do('select Chondroitinase_FA, byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
    return {'motif':'Chondroitinase_FA'}

def serineproteaseCaCb(delta):
    cmd.do('select temp0, name  n')
    cmd.do('select jessatom0, (temp0)')
    cmd.do('select temp1, name  ca')
    cmd.do('select temp2, all within %s of (jessatom0)'%(delta*1.464500))
    cmd.do('select temp3, byres jessatom0')
    cmd.do('select jessatom1, (temp1 and temp2 and temp3)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom1)'%(delta*1.464500))
    cmd.do('select temp4, resn ser')
    cmd.do('select temp5, resn thr')
    cmd.do('select temp6, all within %s of (jessatom0)'%(delta*6.352900))
    cmd.do('select temp7, all within %s of (jessatom1)'%(delta*7.474000))
    cmd.do('select jessatom2, (((temp1 and temp4) or (temp1 and temp5)) and temp6 and temp7)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom2)'%(delta*6.352900))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom2)'%(delta*7.474000))
    cmd.do('select temp8, name  cb')
    cmd.do('select temp9, all within %s of (jessatom0)'%(delta*5.423700))
    cmd.do('select temp10, all within %s of (jessatom1)'%(delta*6.453900))
    cmd.do('select temp11, all within %s of (jessatom2)'%(delta*1.535200))
    cmd.do('select temp12, byres jessatom2')
    cmd.do('select jessatom3, (((temp8 and temp4) or (temp8 and temp5)) and temp9 and temp10 and temp11 and temp12)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom3)'%(delta*5.423700))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom3)'%(delta*6.453900))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom3)'%(delta*1.535200))
    cmd.do('select temp13, name  n')
    cmd.do('select temp14, all within %s of (jessatom0)'%(delta*4.646000))
    cmd.do('select temp15, all within %s of (jessatom1)'%(delta*5.757000))
    cmd.do('select temp16, all within %s of (jessatom2)'%(delta*2.474500))
    cmd.do('select temp17, all within %s of (jessatom3)'%(delta*2.727000))
    cmd.do('select jessatom4, (temp13 and temp14 and temp15 and temp16 and temp17)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom4)'%(delta*4.646000))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom4)'%(delta*5.757000))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom4)'%(delta*2.474500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom4)'%(delta*2.727000))
    cmd.do('select temp18, all within %s of (jessatom1)'%(delta*5.676200))
    cmd.do('select temp19, all within %s of (jessatom2)'%(delta*3.868300))
    cmd.do('select temp20, all within %s of (jessatom3)'%(delta*4.191500))
    cmd.do('select temp21, all within %s of (jessatom4)'%(delta*1.474600))
    cmd.do('select temp22, byres jessatom4')
    cmd.do('select jessatom5, (temp1 and temp14 and temp18 and temp19 and temp20 and temp21 and temp22)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom5)'%(delta*4.646000))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom5)'%(delta*5.676200))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom5)'%(delta*3.868300))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom5)'%(delta*4.191500))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom5)'%(delta*1.474600))
    cmd.do('select temp23, resn asp')
    cmd.do('select temp24, resn glu')
    cmd.do('select temp25, all within %s of (jessatom0)'%(delta*15.119700))
    cmd.do('select temp26, all within %s of (jessatom1)'%(delta*15.564100))
    cmd.do('select temp27, all within %s of (jessatom2)'%(delta*10.877700))
    cmd.do('select temp28, all within %s of (jessatom3)'%(delta*10.574700))
    cmd.do('select temp29, all within %s of (jessatom4)'%(delta*12.917900))
    cmd.do('select temp30, all within %s of (jessatom5)'%(delta*14.271300))
    cmd.do('select jessatom6, (((temp1 and temp23) or (temp1 and temp24)) and temp25 and temp26 and temp27 and temp28 and temp29 and temp30)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom6)'%(delta*15.119700))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom6)'%(delta*15.564100))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom6)'%(delta*10.877700))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom6)'%(delta*10.574700))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom6)'%(delta*12.917900))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom6)'%(delta*14.271300))
    cmd.do('select temp31, all within %s of (jessatom0)'%(delta*13.988500))
    cmd.do('select temp32, all within %s of (jessatom1)'%(delta*14.544000))
    cmd.do('select temp33, all within %s of (jessatom2)'%(delta*9.443500))
    cmd.do('select temp34, all within %s of (jessatom3)'%(delta*9.241500))
    cmd.do('select temp35, all within %s of (jessatom4)'%(delta*11.574600))
    cmd.do('select temp36, all within %s of (jessatom5)'%(delta*12.948200))
    cmd.do('select temp37, all within %s of (jessatom6)'%(delta*1.565500))
    cmd.do('select temp38, byres jessatom6')
    cmd.do('select jessatom7, (((temp8 and temp23) or (temp8 and temp24)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom7)'%(delta*13.988500))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom7)'%(delta*14.544000))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom7)'%(delta*9.443500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom7)'%(delta*9.241500))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom7)'%(delta*11.574600))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom7)'%(delta*12.948200))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom7)'%(delta*1.565500))
    cmd.do('select temp39, resn his')
    cmd.do('select temp40, all within %s of (jessatom0)'%(delta*11.877600))
    cmd.do('select temp41, all within %s of (jessatom1)'%(delta*12.554300))
    cmd.do('select temp42, all within %s of (jessatom2)'%(delta*8.019400))
    cmd.do('select temp43, all within %s of (jessatom3)'%(delta*7.494200))
    cmd.do('select temp44, all within %s of (jessatom4)'%(delta*10.170700))
    cmd.do('select temp45, all within %s of (jessatom5)'%(delta*11.645300))
    cmd.do('select temp46, all within %s of (jessatom6)'%(delta*4.928800))
    cmd.do('select temp47, all within %s of (jessatom7)'%(delta*3.908700))
    cmd.do('select jessatom8, (temp1 and temp39 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom8)'%(delta*11.877600))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom8)'%(delta*12.554300))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom8)'%(delta*8.019400))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom8)'%(delta*7.494200))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom8)'%(delta*10.170700))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom8)'%(delta*11.645300))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom8)'%(delta*4.928800))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom8)'%(delta*3.908700))
    cmd.do('select temp48, all within %s of (jessatom0)'%(delta*10.908000))
    cmd.do('select temp49, all within %s of (jessatom1)'%(delta*11.463500))
    cmd.do('select temp50, all within %s of (jessatom2)'%(delta*7.625500))
    cmd.do('select temp51, all within %s of (jessatom3)'%(delta*6.868000))
    cmd.do('select temp52, all within %s of (jessatom4)'%(delta*9.554600))
    cmd.do('select temp53, all within %s of (jessatom5)'%(delta*11.009000))
    cmd.do('select temp54, all within %s of (jessatom6)'%(delta*5.161100))
    cmd.do('select temp55, all within %s of (jessatom7)'%(delta*4.272300))
    cmd.do('select temp56, all within %s of (jessatom8)'%(delta*1.515000))
    cmd.do('select temp57, byres jessatom8')
    cmd.do('select jessatom9, (temp8 and temp39 and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom9)'%(delta*10.908000))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom9)'%(delta*11.463500))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom9)'%(delta*7.625500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom9)'%(delta*6.868000))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom9)'%(delta*9.554600))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom9)'%(delta*11.009000))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom9)'%(delta*5.161100))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom9)'%(delta*4.272300))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom9)'%(delta*1.515000))
    cmd.do('select Serine_Protease_CaCb, byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9')
    return {'motif':'Serine_Protease_CaCb'}

def serineproteaseFA(delta):
    cmd.do('select temp0, name  n')
    cmd.do('select jessatom0, (temp0)')
    cmd.do('select temp1, name  ca')
    cmd.do('select temp2, all within %s of (jessatom0)'%(delta*1.454400))
    cmd.do('select temp3, byres jessatom0')
    cmd.do('select jessatom1, (temp1 and temp2 and temp3)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom1)'%(delta*1.454400))
    cmd.do('select temp4, name  c')
    cmd.do('select temp5, all within %s of (jessatom0)'%(delta*2.393700))
    cmd.do('select temp6, byres jessatom0')
    cmd.do('select temp7, all within %s of (jessatom1)'%(delta*1.515000))
    cmd.do('select jessatom2, (temp4 and temp5 and temp6 and temp7)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom2)'%(delta*2.393700))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom2)'%(delta*1.515000))
    cmd.do('select temp8, resn ser')
    cmd.do('select temp9, resn thr')
    cmd.do('select temp10, all within %s of (jessatom0)'%(delta*6.009500))
    cmd.do('select temp11, all within %s of (jessatom1)'%(delta*7.191200))
    cmd.do('select temp12, all within %s of (jessatom2)'%(delta*7.393200))
    cmd.do('select jessatom3, (((temp1 and temp8) or (temp1 and temp9)) and temp10 and temp11 and temp12)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom3)'%(delta*6.009500))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom3)'%(delta*7.191200))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom3)'%(delta*7.393200))
    cmd.do('select temp13, name  cb')
    cmd.do('select temp14, all within %s of (jessatom0)'%(delta*5.060100))
    cmd.do('select temp15, all within %s of (jessatom1)'%(delta*6.150900))
    cmd.do('select temp16, all within %s of (jessatom2)'%(delta*6.514500))
    cmd.do('select temp17, all within %s of (jessatom3)'%(delta*1.535200))
    cmd.do('select temp18, byres jessatom3')
    cmd.do('select jessatom4, (((temp13 and temp8) or (temp13 and temp9)) and temp14 and temp15 and temp16 and temp17 and temp18)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom4)'%(delta*5.060100))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom4)'%(delta*6.150900))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom4)'%(delta*6.514500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom4)'%(delta*1.535200))
    cmd.do('select temp19, name  og')
    cmd.do('select temp20, all within %s of (jessatom0)'%(delta*4.999500))
    cmd.do('select temp21, all within %s of (jessatom1)'%(delta*5.827700))
    cmd.do('select temp22, all within %s of (jessatom2)'%(delta*5.979200))
    cmd.do('select temp23, all within %s of (jessatom3)'%(delta*2.424000))
    cmd.do('select temp24, byres jessatom3')
    cmd.do('select temp25, all within %s of (jessatom4)'%(delta*1.424100))
    cmd.do('select jessatom5, (((temp19 and temp8) or (temp19 and temp9)) and temp20 and temp21 and temp22 and temp23 and temp24 and temp25)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom5)'%(delta*4.999500))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom5)'%(delta*5.827700))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom5)'%(delta*5.979200))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom5)'%(delta*2.424000))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom5)'%(delta*1.424100))
    cmd.do('select temp26, name  n')
    cmd.do('select temp27, all within %s of (jessatom0)'%(delta*4.252100))
    cmd.do('select temp28, all within %s of (jessatom1)'%(delta*5.443900))
    cmd.do('select temp29, all within %s of (jessatom2)'%(delta*5.423700))
    cmd.do('select temp30, all within %s of (jessatom3)'%(delta*2.525000))
    cmd.do('select temp31, all within %s of (jessatom4)'%(delta*2.737100))
    cmd.do('select temp32, all within %s of (jessatom5)'%(delta*3.070400))
    cmd.do('select jessatom6, (temp26 and temp27 and temp28 and temp29 and temp30 and temp31 and temp32)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom6)'%(delta*4.252100))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom6)'%(delta*5.443900))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom6)'%(delta*5.423700))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom6)'%(delta*2.525000))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom6)'%(delta*2.737100))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom6)'%(delta*3.070400))
    cmd.do('select temp33, all within %s of (jessatom0)'%(delta*4.383400))
    cmd.do('select temp34, all within %s of (jessatom1)'%(delta*5.474200))
    cmd.do('select temp35, all within %s of (jessatom2)'%(delta*5.191400))
    cmd.do('select temp36, all within %s of (jessatom3)'%(delta*3.888500))
    cmd.do('select temp37, all within %s of (jessatom4)'%(delta*4.211700))
    cmd.do('select temp38, all within %s of (jessatom5)'%(delta*4.383400))
    cmd.do('select temp39, all within %s of (jessatom6)'%(delta*1.484700))
    cmd.do('select temp40, byres jessatom6')
    cmd.do('select jessatom7, (temp1 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom7)'%(delta*4.383400))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom7)'%(delta*5.474200))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom7)'%(delta*5.191400))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom7)'%(delta*3.888500))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom7)'%(delta*4.211700))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom7)'%(delta*4.383400))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom7)'%(delta*1.484700))
    cmd.do('select temp41, all within %s of (jessatom0)'%(delta*5.241900))
    cmd.do('select temp42, all within %s of (jessatom1)'%(delta*6.443800))
    cmd.do('select temp43, all within %s of (jessatom2)'%(delta*6.302400))
    cmd.do('select temp44, all within %s of (jessatom3)'%(delta*4.494500))
    cmd.do('select temp45, all within %s of (jessatom4)'%(delta*5.070200))
    cmd.do('select temp46, all within %s of (jessatom5)'%(delta*5.575200))
    cmd.do('select temp47, all within %s of (jessatom6)'%(delta*2.504800))
    cmd.do('select temp48, byres jessatom6')
    cmd.do('select temp49, all within %s of (jessatom7)'%(delta*1.565500))
    cmd.do('select jessatom8, (temp4 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom8)'%(delta*5.241900))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom8)'%(delta*6.443800))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom8)'%(delta*6.302400))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom8)'%(delta*4.494500))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom8)'%(delta*5.070200))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom8)'%(delta*5.575200))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom8)'%(delta*2.504800))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom8)'%(delta*1.565500))
    cmd.do('select temp50, name cg')
    cmd.do('select temp51, resn asp')
    cmd.do('select temp52, resn glu')
    cmd.do('select temp53, all within %s of (jessatom0)'%(delta*12.251300))
    cmd.do('select temp54, all within %s of (jessatom1)'%(delta*12.786600))
    cmd.do('select temp55, all within %s of (jessatom2)'%(delta*12.998700))
    cmd.do('select temp56, all within %s of (jessatom3)'%(delta*8.322400))
    cmd.do('select temp57, all within %s of (jessatom4)'%(delta*8.029500))
    cmd.do('select temp58, all within %s of (jessatom5)'%(delta*7.625500))
    cmd.do('select temp59, all within %s of (jessatom6)'%(delta*10.382800))
    cmd.do('select temp60, all within %s of (jessatom7)'%(delta*11.705900))
    cmd.do('select temp61, all within %s of (jessatom8)'%(delta*12.695700))
    cmd.do('select jessatom9, (((temp50 and temp51) or (temp50 and temp52)) and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom9)'%(delta*12.251300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom9)'%(delta*12.786600))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom9)'%(delta*12.998700))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom9)'%(delta*8.322400))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom9)'%(delta*8.029500))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom9)'%(delta*7.625500))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom9)'%(delta*10.382800))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom9)'%(delta*11.705900))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom9)'%(delta*12.695700))
    cmd.do('select temp62, name od1')
    cmd.do('select temp63, name od2')
    cmd.do('select temp64, name oe1')
    cmd.do('select temp65, name oe2')
    cmd.do('select temp66, all within %s of (jessatom0)'%(delta*12.049300))
    cmd.do('select temp67, all within %s of (jessatom1)'%(delta*12.453300))
    cmd.do('select temp68, all within %s of (jessatom2)'%(delta*12.675500))
    cmd.do('select temp69, all within %s of (jessatom3)'%(delta*8.686000))
    cmd.do('select temp70, all within %s of (jessatom4)'%(delta*8.201200))
    cmd.do('select temp71, all within %s of (jessatom5)'%(delta*7.655800))
    cmd.do('select temp72, all within %s of (jessatom6)'%(delta*10.564600))
    cmd.do('select temp73, all within %s of (jessatom7)'%(delta*11.887700))
    cmd.do('select temp74, all within %s of (jessatom8)'%(delta*12.968400))
    cmd.do('select temp75, all within %s of (jessatom9)'%(delta*1.212000))
    cmd.do('select temp76, byres jessatom9')
    cmd.do('select jessatom10, ((((temp62 or temp63) and temp51) or ((temp64 or temp65) and temp52)) and temp66 and temp67 and temp68 and temp69 and temp70 and temp71 and temp72 and temp73 and temp74 and temp75 and temp76)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom10)'%(delta*12.049300))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom10)'%(delta*12.453300))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom10)'%(delta*12.675500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom10)'%(delta*8.686000))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom10)'%(delta*8.201200))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom10)'%(delta*7.655800))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom10)'%(delta*10.564600))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom10)'%(delta*11.887700))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom10)'%(delta*12.968400))
    cmd.do('select jessatom9, jessatom9 within %s of (jessatom10)'%(delta*1.212000))
    cmd.do('select temp77, name od2')
    cmd.do('select temp78, name od1')
    cmd.do('select temp79, name oe2')
    cmd.do('select temp80, name oe1')
    cmd.do('select temp81, all within %s of (jessatom0)'%(delta*11.524100))
    cmd.do('select temp82, all within %s of (jessatom1)'%(delta*12.130100))
    cmd.do('select temp83, all within %s of (jessatom2)'%(delta*12.271500))
    cmd.do('select temp84, all within %s of (jessatom3)'%(delta*7.231600))
    cmd.do('select temp85, all within %s of (jessatom4)'%(delta*7.100300))
    cmd.do('select temp86, all within %s of (jessatom5)'%(delta*6.716500))
    cmd.do('select temp87, all within %s of (jessatom6)'%(delta*9.322300))
    cmd.do('select temp88, all within %s of (jessatom7)'%(delta*10.615100))
    cmd.do('select temp89, all within %s of (jessatom8)'%(delta*11.574600))
    cmd.do('select temp90, all within %s of (jessatom9)'%(delta*1.323100))
    cmd.do('select temp91, byres jessatom9')
    cmd.do('select temp92, all within %s of (jessatom10)'%(delta*2.232100))
    cmd.do('select jessatom11, ((((temp77 or temp78) and temp51) or ((temp79 or temp80) and temp52)) and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89 and temp90 and temp91 and temp92)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom11)'%(delta*11.524100))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom11)'%(delta*12.130100))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom11)'%(delta*12.271500))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom11)'%(delta*7.231600))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom11)'%(delta*7.100300))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom11)'%(delta*6.716500))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom11)'%(delta*9.322300))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom11)'%(delta*10.615100))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom11)'%(delta*11.574600))
    cmd.do('select jessatom9, jessatom9 within %s of (jessatom11)'%(delta*1.323100))
    cmd.do('select jessatom10, jessatom10 within %s of (jessatom11)'%(delta*2.232100))
    cmd.do('select temp93, resn his')
    cmd.do('select temp94, all within %s of (jessatom0)'%(delta*9.201100))
    cmd.do('select temp95, all within %s of (jessatom1)'%(delta*9.827300))
    cmd.do('select temp96, all within %s of (jessatom2)'%(delta*10.382800))
    cmd.do('select temp97, all within %s of (jessatom3)'%(delta*6.090300))
    cmd.do('select temp98, all within %s of (jessatom4)'%(delta*5.322700))
    cmd.do('select temp99, all within %s of (jessatom5)'%(delta*5.241900))
    cmd.do('select temp100, all within %s of (jessatom6)'%(delta*8.009300))
    cmd.do('select temp101, all within %s of (jessatom7)'%(delta*9.453600))
    cmd.do('select temp102, all within %s of (jessatom8)'%(delta*10.362600))
    cmd.do('select temp103, all within %s of (jessatom9)'%(delta*3.858200))
    cmd.do('select temp104, all within %s of (jessatom10)'%(delta*3.817800))
    cmd.do('select temp105, all within %s of (jessatom11)'%(delta*3.747100))
    cmd.do('select jessatom12, (temp50 and temp93 and temp94 and temp95 and temp96 and temp97 and temp98 and temp99 and temp100 and temp101 and temp102 and temp103 and temp104 and temp105)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom12)'%(delta*9.201100))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom12)'%(delta*9.827300))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom12)'%(delta*10.382800))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom12)'%(delta*6.090300))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom12)'%(delta*5.322700))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom12)'%(delta*5.241900))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom12)'%(delta*8.009300))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom12)'%(delta*9.453600))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom12)'%(delta*10.362600))
    cmd.do('select jessatom9, jessatom9 within %s of (jessatom12)'%(delta*3.858200))
    cmd.do('select jessatom10, jessatom10 within %s of (jessatom12)'%(delta*3.817800))
    cmd.do('select jessatom11, jessatom11 within %s of (jessatom12)'%(delta*3.747100))
    cmd.do('select temp106, name nd1')
    cmd.do('select temp107, all within %s of (jessatom0)'%(delta*9.029400))
    cmd.do('select temp108, all within %s of (jessatom1)'%(delta*9.665700))
    cmd.do('select temp109, all within %s of (jessatom2)'%(delta*10.029300))
    cmd.do('select temp110, all within %s of (jessatom3)'%(delta*5.423700))
    cmd.do('select temp111, all within %s of (jessatom4)'%(delta*4.837900))
    cmd.do('select temp112, all within %s of (jessatom5)'%(delta*4.565200))
    cmd.do('select temp113, all within %s of (jessatom6)'%(delta*7.383100))
    cmd.do('select temp114, all within %s of (jessatom7)'%(delta*8.787000))
    cmd.do('select temp115, all within %s of (jessatom8)'%(delta*9.766700))
    cmd.do('select temp116, all within %s of (jessatom9)'%(delta*3.363300))
    cmd.do('select temp117, all within %s of (jessatom10)'%(delta*3.474400))
    cmd.do('select temp118, all within %s of (jessatom11)'%(delta*2.858300))
    cmd.do('select temp119, all within %s of (jessatom12)'%(delta*1.393800))
    cmd.do('select temp120, byres jessatom12')
    cmd.do('select jessatom13, (temp106 and temp93 and temp107 and temp108 and temp109 and temp110 and temp111 and temp112 and temp113 and temp114 and temp115 and temp116 and temp117 and temp118 and temp119 and temp120)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom13)'%(delta*9.029400))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom13)'%(delta*9.665700))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom13)'%(delta*10.029300))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom13)'%(delta*5.423700))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom13)'%(delta*4.837900))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom13)'%(delta*4.565200))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom13)'%(delta*7.383100))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom13)'%(delta*8.787000))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom13)'%(delta*9.766700))
    cmd.do('select jessatom9, jessatom9 within %s of (jessatom13)'%(delta*3.363300))
    cmd.do('select jessatom10, jessatom10 within %s of (jessatom13)'%(delta*3.474400))
    cmd.do('select jessatom11, jessatom11 within %s of (jessatom13)'%(delta*2.858300))
    cmd.do('select jessatom12, jessatom12 within %s of (jessatom13)'%(delta*1.393800))
    cmd.do('select temp121, name ne2')
    cmd.do('select temp122, all within %s of (jessatom0)'%(delta*7.029600))
    cmd.do('select temp123, all within %s of (jessatom1)'%(delta*7.706300))
    cmd.do('select temp124, all within %s of (jessatom2)'%(delta*8.261800))
    cmd.do('select temp125, all within %s of (jessatom3)'%(delta*4.403600))
    cmd.do('select temp126, all within %s of (jessatom4)'%(delta*3.322900))
    cmd.do('select temp127, all within %s of (jessatom5)'%(delta*3.211800))
    cmd.do('select temp128, all within %s of (jessatom6)'%(delta*5.979200))
    cmd.do('select temp129, all within %s of (jessatom7)'%(delta*7.413400))
    cmd.do('select temp130, all within %s of (jessatom8)'%(delta*8.383000))
    cmd.do('select temp131, all within %s of (jessatom9)'%(delta*5.534800))
    cmd.do('select temp132, all within %s of (jessatom10)'%(delta*5.454000))
    cmd.do('select temp133, all within %s of (jessatom11)'%(delta*5.029800))
    cmd.do('select temp134, all within %s of (jessatom12)'%(delta*2.201800))
    cmd.do('select temp135, byres jessatom12')
    cmd.do('select temp136, all within %s of (jessatom13)'%(delta*2.201800))
    cmd.do('select jessatom14, (temp121 and temp93 and temp122 and temp123 and temp124 and temp125 and temp126 and temp127 and temp128 and temp129 and temp130 and temp131 and temp132 and temp133 and temp134 and temp135 and temp136)')
    cmd.do('select jessatom0, jessatom0 within %s of (jessatom14)'%(delta*7.029600))
    cmd.do('select jessatom1, jessatom1 within %s of (jessatom14)'%(delta*7.706300))
    cmd.do('select jessatom2, jessatom2 within %s of (jessatom14)'%(delta*8.261800))
    cmd.do('select jessatom3, jessatom3 within %s of (jessatom14)'%(delta*4.403600))
    cmd.do('select jessatom4, jessatom4 within %s of (jessatom14)'%(delta*3.322900))
    cmd.do('select jessatom5, jessatom5 within %s of (jessatom14)'%(delta*3.211800))
    cmd.do('select jessatom6, jessatom6 within %s of (jessatom14)'%(delta*5.979200))
    cmd.do('select jessatom7, jessatom7 within %s of (jessatom14)'%(delta*7.413400))
    cmd.do('select jessatom8, jessatom8 within %s of (jessatom14)'%(delta*8.383000))
    cmd.do('select jessatom9, jessatom9 within %s of (jessatom14)'%(delta*5.534800))
    cmd.do('select jessatom10, jessatom10 within %s of (jessatom14)'%(delta*5.454000))
    cmd.do('select jessatom11, jessatom11 within %s of (jessatom14)'%(delta*5.029800))
    cmd.do('select jessatom12, jessatom12 within %s of (jessatom14)'%(delta*2.201800))
    cmd.do('select jessatom13, jessatom13 within %s of (jessatom14)'%(delta*2.201800))
    cmd.do('select serineproteaseFA, byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11|byres jessatom12|byres jessatom13|byres jessatom14')
    return {'motif':'Serine_Protease_FA'}

def serineprotease(delta):
    cmd.do('select asp1, resn asp within %s of resn his'%(delta*3))
    cmd.do('select asp2, resn asp within %s of resn ser'%(delta*7))
    byResidue('asp', 2)
    cmd.do('select his1, resn his within %s of asp'%(delta*4))
    cmd.do('select his2, resn his within %s of resn ser'%(delta*4))
    byResidue('his', 2)
    cmd.do('select ser1, name og within %s of name ne2'%(delta*3.5))
    cmd.do('select ser2, resn ser within %s of asp'%(delta*7))
    byResidue('ser', 2)
    cmd.do('select Serine_Protease, byres (ser|his|asp)')
    return {'motif':'Serine_Protease'}

def Blactamase(delta):
    cmd.do('select lys1, name nz and resn lys within %s of (name oh and resn tyr)'%(delta*5))
    cmd.do('select lys2, name nz and resn lys within %s of (name cz and resn tyr)'%(delta*5.5))
    cmd.do('select lys3, name nz and resn lys within %s of (name ce1 and resn tyr)'%(delta*6.5))
    cmd.do('select lys4, name nz and resn lys within %s of (name ce2 and resn tyr)'%(delta*6.5))
    cmd.do('select lys5, name ce and resn lys within %s of (name oh and resn tyr)'%(delta*5))
    cmd.do('select lys6, name ce and resn lys within %s of (name cz and resn tyr)'%(delta*6))
    cmd.do('select lys7, name nz and resn lys within %s of (name og and resn ser)'%(delta*6))
    cmd.do('select lys8, name nz and resn lys within %s of (name cb and resn ser)'%(delta*5.2))
    cmd.do('select lys9, name cb and resn lys within %s of (name cb and resn ser)'%(delta*9.2))
    cmd.do('select lys10, name ce and resn lys within %s of (name oe1 and resn glu)'%(delta*11))
    cmd.do('select lys11, name nz and resn lys within %s of (name oe1 and resn glu)'%(delta*11))
    cmd.do('select lys12, name nz and resn lys within %s of (name oe2 and resn glu)'%(delta*12.5))
    cmd.do('select lys13, name ce and resn lys within %s of (name cd and resn glu)'%(delta*11))
    byResidue('lys', 13)
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nz and resn lys)'%(delta*5))
    cmd.do('select tyr2, name cz and resn tyr within %s of (name nz and resn lys)'%(delta*5.5))
    cmd.do('select tyr3, name ce1 and resn tyr within %s of (name nz and resn lys)'%(delta*6.5))
    cmd.do('select tyr4, name ce2 and resn tyr within %s of (name nz and lys)'%(delta*6.5))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name ce and resn lys)'%(delta*5))
    cmd.do('select tyr6, name cz and resn tyr within %s of (name ce and resn lys)'%(delta*6))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name og and resn ser)'%(delta*6))
    cmd.do('select tyr8, name cz and resn tyr within %s of (name og and resn ser)'%(delta*6.5))
    cmd.do('select tyr9, name oh and resn tyr within %s of (name cb and resn ser)'%(delta*6))
    cmd.do('select tyr10, name oh and resn tyr within %s of (name oe1 and resn glu)'%(delta*10))
    cmd.do('select tyr11, name oh and resn tyr within %s of (name oe2 and resn glu)'%(delta*10))
    cmd.do('select tyr12, name oh and resn tyr within %s of (name cd and resn glu)'%(delta*10))
    byResidue('tyr', 12)
    cmd.do('select ser1, name cb and resn ser within %s of (name nz and resn lys)'%(delta*6))
    cmd.do('select ser2, name og and resn ser within %s of (name nz and resn lys)'%(delta*6))
    cmd.do('select ser3, name cb and resn ser within %s of (name cb and lys)'%(delta*8.2))
    cmd.do('select ser4, name og and resn ser within %s of (name cz and resn tyr)'%(delta*6.5))
    cmd.do('select ser5, name cb and resn ser within %s of (name oh and resn tyr)'%(delta*6.5))
    cmd.do('select ser6, name og and resn ser within %s of (name oh and tyr)'%(delta*6))
    cmd.do('select ser7, name og and resn ser within %s of (name oe1 and resn glu)'%(delta*12))
    cmd.do('select ser8, name og and resn ser within %s of (name oe2 and resn glu)'%(delta*12))
    cmd.do('select ser9, name cb and resn ser within %s of (name oe1 and resn glu)'%(delta*11))
    cmd.do('select ser10, name cb and resn ser within %s of (name oe2 and resn glu)'%(delta*12.5))
    cmd.do('select ser11, name og and resn ser within %s of (name cd and resn glu)'%(delta*12.5))
    cmd.do('select ser12, name cb and resn ser within %s of (name cd and resn glu)'%(delta*11.5))
    byResidue('ser', 12)
    cmd.do('select glu1, name oe1 and resn glu within %s of (name ce and resn lys)'%(delta*8.5))
    cmd.do('select glu2, name oe1 and resn glu within %s of (name nz and resn lys)'%(delta*9.5))
    cmd.do('select glu3, name oe2 and resn glu within %s of (name nz and lys)'%(delta*11.2))
    cmd.do('select glu4, name cd and resn glu within %s of (name ce and resn lys)'%(delta*10.6))
    cmd.do('select glu5, name oe1 and resn glu within %s of (name oh and resn tyr)'%(delta*8.7))
    cmd.do('select glu6, name oe2 and resn glu within %s of (name oh and resn tyr)'%(delta*9.7))
    cmd.do('select glu7, name cd and resn glu within %s of (name oh and resn tyr)'%(delta*9.6))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name og and resn ser)'%(delta*10.5))
    cmd.do('select glu9, name oe2 and resn glu within %s of (name og and resn ser)'%(delta*10.5))
    cmd.do('select glu10, name oe1 and resn glu within %s of (name cb and resn ser)'%(delta*10))
    cmd.do('select glu11, name oe2 and resn glu within %s of (name cb and resn ser)'%(delta*11.8))
    cmd.do('select glu12, name cd and resn glu within %s of (name og and resn ser)'%(delta*11.8))
    cmd.do('select glu13, name cd and resn glu within %s of (name cb and ser)'%(delta*11))
    cmd.do('select glu14, name oe1 and resn glu within %s of (name cg and tyr)'%(delta*7.4))
    byResidue('glu', 14)
    cmd.select('Lactamase', 'ser(tyr(glu(lys)))')
    return {'motif':'Lactamase'}

def superoxide(delta):
    cmd.do('select his1, resn his within %s of elem cu'%(delta*4))
    cmd.do('select his2, his and elem zn around %s)'%(delta*4))
    cmd.do('select his3, his and elem cu around %s'%(delta*4))
    byResidue('his', 3)
    cmd.do('select arg1, resn arg within %s of elem cu'%(delta*6))
    cmd.do('select arg2, arg and elem zn around %s)'%(delta*6))
    cmd.do('select arg3, arg and elem cu around %s'%(delta*6))
    byResidue('arg', 3)
    cmd.do('select Superoxide, his(arg)')
    cmd.show('spheres', 'elem cu')
    cmd.show('spheres', 'elem zn')
    return {'motif':'Superoxide','extra':{'spheres':'cu','spheres','zn'}}

def metalloprotease(delta):
    cmd.select('zn', 'elem zn')
    cmd.do('select metalloprotease, byres zn(zn around %s)'%(delta*5))
    return {'motif':'Metalloprotease','extra':{'spheres':'zn'}}

def tyrophos(delta):
    cmd.do('select arg1, name nh1 and resn arg within %s of (name od1 and resn asp)'%(delta*7))
    cmd.do('select arg2, name nh2 and resn arg within %s of (name od2 and resn asp)'%(delta*7))
    cmd.do('select arg3, name ne and resn arg within %s of (name cb and resn asp)'%(delta*6.5))
    cmd.do('select arg4, name nh2 and resn arg within %s of (name ca and resn cys)'%(delta*7))
    cmd.do('select arg5, name nh1 and resn arg within %s of (name cb and resn cys)'%(delta*7))
    cmd.do('select arg6, name ne and resn arg within %s of (name sg and resn cys)'%(delta*6.5))
    cmd.do('select arg7, name nh2 and resn arg within %s of (name og and resn ser)'%(delta*10))
    cmd.do('select arg8, name nh1 and resn arg within %s of (name cb and resn ser)'%(delta*11.2))
    cmd.do('select arg9, name ne and resn arg within %s of (name ca and resn ser)'%(delta*9))
    byResidue('arg', 9)
    cmd.do('select asp1, name od1 and resn asp within %s of (name nh1 and arg)'%(delta*7))
    cmd.do('select asp2, name od2 and resn asp within %s of (name nh2 and arg)'%(delta*7))
    cmd.do('select asp3, name cb and resn asp within %s of (name ne and arg)'%(delta*6.5))
    cmd.do('select asp4, name od2 and resn asp within %s of (name c and resn ser)'%(delta*11))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ca and resn ser)'%(delta*12))
    cmd.do('select asp6, name cb and resn asp within %s of (name cb and resn ser)'%(delta*9.2))
    cmd.do('select asp7, name od1 and resn asp within %s of (name c and resn cys)'%(delta*12))
    cmd.do('select asp8, name od2 and resn asp within %s of (name cb and resn cys)'%(delta*11))
    cmd.do('select asp9, name cb and resn asp within %s of (name sg and resn cys)'%(delta*10))
    byResidue('asp', 9)
    cmd.do('select cys1, name ca and resn cys within %s of (name og and resn ser)'%(delta*6.5))
    cmd.do('select cys2, name cb and resn cys within %s of (name cb and resn ser)'%(delta*7))
    cmd.do('select cys3, name sg and resn cys within %s of (name ca and resn ser)'%(delta*6))
    cmd.do('select cys4, name c and resn cys within %s of (name od1 and asp)'%(delta*12))
    cmd.do('select cys5, name cb and resn cys within %s of (name od2 and asp)'%(delta*11))
    cmd.do('select cys6, name sg and resn cys within %s of (name cb and asp)'%(delta*10))
    cmd.do('select cys7, name ca and resn cys within %s of (name nh2 and arg)'%(delta*7))
    cmd.do('select cys8, name cb and resn cys within %s of (name nh1 and arg)'%(delta*7))
    cmd.do('select cys9, name sg and resn cys within %s of (name ne and arg)'%(delta*6.5))
    byResidue('cys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name nh2 and arg)'%(delta*10))
    cmd.do('select ser2, name cb and resn ser within %s of (name nh1 and arg)'%(delta*11.2))
    cmd.do('select ser3, name ca and resn ser within %s of (name ne and arg)'%(delta*9))
    cmd.do('select ser4, name c and resn ser within %s of (name od2 and asp)'%(delta*11))
    cmd.do('select ser5, name ca and resn ser within %s of (name od1 and asp)'%(delta*12))
    cmd.do('select ser6, name cb and resn ser within %s of (name cb and asp)'%(delta*9.2))
    cmd.do('select ser7, name og and resn ser within %s of (name ca and cys)'%(delta*6.5))
    cmd.do('select ser8, name cb and resn ser within %s of (name cb and cys)'%(delta*7))
    cmd.do('select ser9, name ca and resn ser within %s of (name sg and cys)'%(delta*6))
    byResidue('ser', 9)
    if(len(cmd.index('ser')) < 1):            
        cmd.select('Tyrophos', 'asp(arg(cys))')
    else:
        cmd.select('Tyrophos', 'ser(asp(arg(cys)))')
    return {'motif':'Tyrophos'}

def carbanhyd(delta):
    cmd.select('zn', 'elem zn')
    cmd.do('select his, resn his within %s of zn'%(delta*5))
    cmd.select('Carbonic_Anhydrase', 'byres his or zn')
    cmd.delete('zn')
    cmd.delete('his')
    return {'motif':'Carbonic_Anhydrase','extra':{'spheres':'zn'}}

def paplike(delta):
    cmd.do('select gln1, name ne2 and resn gln within %s of (name ne2 and resn his)'%(delta*7))
    cmd.do('select gln2, name cd and resn gln within %s of (name ce1 and resn his)'%(delta*6.7))
    cmd.do('select gln3, name oe1 and resn gln within %s of (name nd1 and resn his)'%(delta*7))
    cmd.do('select gln4, name ne2 and resn gln within %s of (name cb and resn cys)'%(delta*5.5))
    cmd.do('select gln5, name oe1 and resn gln within %s of (name sg and resn cys)'%(delta*6.7))
    byResidue('gln', 5)
    cmd.do('select his1, name ne2 and resn his within %s of (name ne2 and gln)'%(delta*7))
    cmd.do('select his2, name ce1 and resn his within %s of (name cd and gln)'%(delta*6.7))
    cmd.do('select his3, name nd1 and resn his within %s of (name oe1 and gln)'%(delta*7))
    cmd.do('select his4, name ce1 and resn his within %s of (name cb and resn cys)'%(delta*5.7))
    cmd.do('select his5, name nd1 and resn his within %s of (name sg and resn cys)'%(delta*6))
    byResidue('his', 5)
    cmd.do('select cys1, name cb and resn cys within %s of (name ce1 and his)'%(delta*5.7))
    cmd.do('select cys2, name sg and resn cys within %s of (name nd1 and his)'%(delta*6))
    cmd.do('select cys3, name cb and resn cys within %s of (name ne2 and gln)'%(delta*5.5))
    cmd.do('select cys4, name sg and resn cys within %s of (name oe1 and gln)'%(delta*6.7))
    byResidue('cys', 4)
    cmd.select('paplike', 'gln(his(cys))')
    return {'motif':'Paplike'}

def zincfinger(delta):
    if(len(cmd.index('elem zn')) >= 1):
        cmd.select('his', 'resn his')
        cmd.select('cys', 'resn cys')
        cmd.do('select cys1, cys around %s'%(delta*4))
        cmd.select('Zinc_Finger','(cys or his(byres cys1))')
        return {'motif':'Zinc_Finger','extra':{'spheres':'zn'}}
    else:
        return False

def aminotransferase(delta):
    cmd.do('select asp1, name od1 and resn asp within %s of (name cb and resn his)'%(delta*5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name cg and resn his)'%(delta*6))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nd1 and resn his)'%(delta*7))
    cmd.do('select asp4, name cg and resn asp within %s of (name cb and resn his)'%(delta*6.5))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select asp6, name od1 and resn asp within %s of (name cd2 and resn his)'%(delta*7))
    cmd.do('select asp7, name od2 and resn asp within %s of (name nz and resn lys)'%(delta*9))
    cmd.do('select asp8, name cg and resn asp within %s of (name nz and resn lys)'%(delta*9))
    byResidue('asp', 8)
    cmd.do('select his1, name cb and resn his within %s of (name od1 and resn asp)'%(delta*5))
    cmd.do('select his2, name cg and resn his within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select his3, name nd1 and resn his within %s of (name od1 and resn asp)'%(delta*7))
    cmd.do('select his4, name cb and resn his within %s of (name cg and asp)'%(delta*6.5))
    cmd.do('select his5, name ne2 and resn his within %s of (name od1 and asp)'%(delta*8))
    cmd.do('select his6, name cd2 and resn his within %s of (name od1 and asp)'%(delta*7))
    cmd.do('select his7, name nd1 and resn his within %s of (name nz and resn lys)'%(delta*7.5))
    cmd.do('select his8, name ne2 and resn his within %s of (name nz and resn lys)'%(delta*8))
    cmd.do('select his9, name ce1 and resn his within %s of (name nz and resn lys)'%(delta*7))
    byResidue('his', 9)
    cmd.do('select lys1, name nz and resn lys within %s of (name od2 and asp)'%(delta*9))
    cmd.do('select lys2, name nz and resn lys within %s of (name cg and asp)'%(delta*9))
    cmd.do('select lys3, name nz and resn lys within %s of (name nd1 and his)'%(delta*7.5))
    cmd.do('select lys4, name nz and resn lys within %s of (name ne2 and his)'%(delta*8))
    cmd.do('select lys5, name nz and resn lys within %s of (name ce1 and his)'%(delta*7))
    byResidue('lys', 5)
    cmd.select('Aminotransferase', 'asp(his(lys))')
    return {'motif':'Aminotranferase'}

def fisomerase(delta):
    cmd.do('select his, elem mn around %s|elem mn'%(delta*5))
    cmd.select('Fucose_Isomerase', 'byres (resn asp and his|resn glu and his|elem mn)')
    return {'motif':'Fucose_Isomerase','extra':{'spheres':'mn'}}

def glutamine_amidotransferase(delta):
    cmd.do('select his1, name ND1 within %s of name OE2'%(delta*3))
    cmd.do('select his2, name NE2 within %s of name SG'%(delta*3.5))
    byResidue('his', 2)
    cmd.do('select glu1, resn glu within %s of his'%(delta*3.2))
    cmd.do('select glu2, resn glu within %s of resn cys'%(delta*7))
    byResidue('glu', 2)
    cmd.do('select cys1, resn cys within %s of his'%(delta*3.5))
    cmd.do('select cys2, resn cys within %s of glu'%(delta*7))
    byResidue('cys', 2)
    cmd.select('Glu_Amidotransferase', 'cys(his(glu))')
    return {'motif':'Glu_Amidotransferase'}

def dnaligase(delta):
    cmd.select('amp', 'resn amp')
    cmd.select('atp', 'resn atp')
    if(len(cmd.index('amp')) >= 1):
        cmd.do('selct lys, resn amp around %s and resn lys'%(delta*7.4))
        cmd.do('select asp, resn amp around %s and resn asp within %s of lys'%(delta*5.3, delta*3))
        cmd.do('select arg, resn amp around %s and resn arg within %s of asp'%(delta*7, delta*5))
        cmd.select('Ligase', 'byres lys(amp(arg(asp)))')
        return {'motif':'Ligase','extra':{'spheres':'amp','sticks':'amp'}}
    elif(len(cmd.index('atp')) >= 1):
        cmd.do('select lys, resn atp around %s and resn lys'%(delta*7.4))
        cmd.do('select asp, resn atp around %s and(resn asp within %s of lys)'%(delta*5.3, delta*3))
        cmd.do('select arg, resn atp around %s and(resn arg within %s of asp)'%(delta*7, delta*5))
        cmd.select('Ligase', 'byres lys(atp(arg(asp)))')
        return {'motif':'Ligase','extra':{'spheres':'atp','sticks':'atp'}}
    elif(len(cmd.index('amp')) < 1 and len(cmd.index('atp')) < 1):
        cmd.do('select lys1, name NZ within %s of name OD2'%(delta*9))
        cmd.do('select lys2, name NZ within %s of name NH2'%(delta*10))
        cmd.do('select arg, resn arg and name NE within %s of name OD2'%(delta*5.5))
        cmd.do('select asp, resn asp and name OD2 within %s of name NE'%(delta*5.5))
        cmd.od('select lys, resn lys and lys1 and lys2')
        cmd.select('Ligase', 'byres arg(asp(lys))')
        return {'motif':'Ligase'}

def thymidinekinase(delta):
    cmd.do('select glu1, name OE1 and resn glu within %s of name NH2 and resn arg'%(delta*5))
    cmd.do('select glu2, resn glu and name OE2 within %s of name NE and resn arg'%(delta*5))
    cmd.do('select glu3, resn glu and name OE1 within %s of name NH1 and resn arg'%(delta*6))
    cmd.do('select glu4, resn glu and name OE1 within %s of name NE and resn arg'%(delta*6))
    cmd.do('select glu5, resn glu and name OE2 within %s of name NH2 and resn arg'%(delta*5.5))
    cmd.do('select glu6, resn glu and name oe1 within %s of name CZ and resn arg'%(delta*5))
    cmd.do('select glu7, resn glu and name oe2 within %s of name CZ and resn arg'%(delta*5))
    cmd.do('select glu8, resn glu and name oe1 within %s of name CD and resn arg'%(delta*5.8))
    cmd.do('select glu9, resn glu and name oe2 within %s of name CD and resn arg'%(delta*5.5))
    byResidue('glu', 9)
    cmd.do('select arg1, resn arg and name NH1 within %s of name OE2 and glu'%(delta*6))
    cmd.do('select arg2, resn arg and name NE within %s of name OE2 and glu'%(delta*5.2))
    cmd.do('select arg3, resn arg and name NH1 within %s of name oe1 and glu'%(delta*6))
    cmd.do('select arg4, resn arg and name ne within %s of name oe1 and resn glu'%(delta*6.5))
    cmd.do('select arg5, resn arg and name nh2 within %s of name oe2 and resn glu'%(delta*5.8))
    byResidue('arg', 5)
    cmd.do('select gly1, resn gly within %s of arg'%(delta*6.2))
    cmd.do('select gly2, resn gly within %s of glu'%(delta*9))
    byResidue('gly', 2)
    cmd.select('glu10', 'byres glu within 10 of gly')
    cmd.select('arg10', 'byres arg within 9 of gly')
    cmd.select('Tkinase', 'glu10(arg10(gly))')
    return {'motif':'Tkinase'}

def oglycosyl(delta):
    cmd.do('select asp1, name od1 and resn asp within %s of (name oe1 and resn glu)'%(delta*9.5))
    cmd.select('notasp', 'resn asp within %s of resn glu'%(4.5/delta))
    cmd.select('asp', 'asp1 and (byres not notasp)')
    cmd.do('select glu1, name oe1 and resn glu within %s of (name od1 and resn asp)'%(delta*9.5))
    cmd.select('glu0', 'resn glu within %s of resn asp'%(4.5/delta))
    cmd.select('glu', 'byres glu1 and (not glu0)')
    cmd.select('o-glycosyl', 'byres asp | byres glu')
    return {'motif':'O-Glycosyl'}

def carboncarbon(delta):
    cmd.do('select asp1, name od1 within %s of name nz'%(delta*3.5))
    cmd.do('select asp2, resn asp within %s of name ne2'%(delta*6))
    byResidue('asp', 2)
    cmd.do('select lys1, name nz within %s of asp'%(delta*6))
    cmd.do('select lys2, resn lys within %s of resn his'%(delta*8))
    byResidue('lys', 2)
    cmd.do('select his1, name ne2 within %s of name nz'%(delta*6))
    cmd.do('select his2, resn his within %s of lys'%(delta*6))
    cmd.do('select his3, resn his within %s of asp'%(delta*9))
    byResidue('his', 3)
    cmd.select('carboncarbon', 'asp(lys(his))')
    return {'motif':'Carbon_Carbon'}

def peroxidase(delta):
    cmd.do('select asn1, name od1 within %s of name nd1'%(delta*8))
    cmd.do('select asn2, name od1 within %s of name ne2'%(delta*6))
    cmd.do('select asn3, name nd2 within %s of name nd1'%(delta*10))
    cmd.do('select asn4, name nd2 within %s of name ne2'%(delta*8))
    cmd.do('select asn5, name od1 within %s of name nh2'%(delta*7))
    cmd.do('select asn6, name od1 within %s of name nh1'%(delta*8.6))
    cmd.do('select asn7, name od1 within %s of name ne'%(delta*8))
    cmd.do('select asn8, name nd2 within %s of name nh2'%(delta*9))
    cmd.do('select asn9, name nd2 within %s of name nh1'%(delta*11))
    cmd.do('select asn10, name nd2 within %s of name ne'%(delta*9.8))
    byResidue('asn', 10)
    cmd.do('select his1, name nd1 within %s of name od1'%(delta*5))
    cmd.do('select his2, name ne2 within %s of name od1'%(delta*5))
    cmd.do('select his3, name nd1 within %s of name nd2'%(delta*8))
    cmd.do('select his4, name ne2 within %s of name nd2'%(delta*8.5))
    cmd.do('select his5, name ne2 within %s of name ne'%(delta*5.8))
    cmd.do('select his6, name ne2 within %s of name nh2'%(delta*6))
    cmd.do('select his7, name ne2 within %s of name nh1'%(delta*8.2))
    cmd.do('select his8, name nd1 within %s of name nh1'%(delta*7.2))
    cmd.do('select his9, name nd1 within %s of name nh2'%(delta*5.8))
    cmd.do('select his10, name nd1 within %s of name ne'%(delta*7))
    byResidue('his', 10)
    cmd.do('select arg1, name nh2 within %s of name od1'%(delta*7.5))
    cmd.do('select arg2, name nh2 within %s of name nd2'%(delta*9.5))
    cmd.do('select arg3, name nh2 within %s of name ne2'%(delta*6))
    cmd.do('select arg4, name nh2 within %s of name nd1'%(delta*6))
    cmd.do('select arg5, name nh1 within %s of name od1'%(delta*8))
    cmd.do('select arg6, name nh1 within %s of name nd2'%(delta*10))
    cmd.do('select arg7, name nh1 within %s of name ne2'%(delta*8))
    cmd.do('select arg8, name nh1 within %s of name nd1'%(delta*7.4))
    cmd.do('select arg9, name ne within %s of name od1'%(delta*7.2))
    cmd.do('select arg10, name ne within %s of name nd2'%(delta*8.9))
    cmd.do('select arg11, name ne within %s of name ne2'%(delta*5.9))
    cmd.do('select arg12, name ne within %s of name nd1'%(delta*6))
    byResidue('arg', 12)
    cmd.select('Peroxidase', 'asn(his(arg))')
    return {'motif':'Peroxidase'}

def trioseisomerase(delta):
    cmd.do('select lys1, name nz and resn lys within %s of (name od1 and resn asn)'%(delta*7.5))
    cmd.do('select lys2, name nz and resn lys within %s of (name nd2 and resn asn)'%(delta*7.5))
    cmd.do('select lys3, name nz and resn lys within %s of (name cg and resn asn)'%(delta*7.5))
    cmd.do('select lys4, name ce and resn lys within %s of (name od1 and resn asn)'%(delta*6.5))
    cmd.do('select lys5, name ce and resn lys within %s of (name nd2 and resn asn)'%(delta*6.5))
    cmd.do('select lys6, name ce and resn lys within %s of (name cg and resn asn)'%(delta*6.5))
    cmd.do('select lys7, name cd and resn lys within %s of (name od1 and resn asn)'%(delta*6.2))
    cmd.do('select lys8, name cd and resn lys within %s of (name cg and resn asn)'%(delta*6.5))
    cmd.do('select lys9, name cd and resn lys within %s of (name nd2 and resn asn)'%(delta*6.5))
    cmd.do('select lys10, name nz and resn lys within %s of (name ne2 and resn his)'%(delta*6.5))
    cmd.do('select lys11, name nz and resn lys within %s of (name nd1 and resn his)'%(delta*7.5))
    cmd.do('select lys12, name nz and resn lys within %s of (name ce1 and resn his)'%(delta*6.7))
    cmd.do('select lys13, name nz and resn lys within %s of (name cd2 and resn his)'%(delta*7.5))
    cmd.do('select lys14, name nz and resn lys within %s of (name cg and resn his)'%(delta*8))
    cmd.do('select lys15, name ce and resn lys within %s of (name ne2 and resn his)'%(delta*6.2))
    cmd.do('select lys16, name ce and resn lys within %s of (name nd1 and resn his)'%(delta*7.6))
    cmd.do('select lys17, name ce and resn lys within %s of (name ce1 and resn his)'%(delta*6.6))
    cmd.do('select lys18, name ce and resn lys within %s of (name cd2 and resn his)'%(delta*7))
    cmd.do('select lys19, name ce and resn lys within %s of (name cg and resn his)'%(delta*7.5))
    cmd.do('select lys20, name nz and resn lys within %s of (name oe2 and resn glu)'%(delta*8.5))
    cmd.do('select lys21, name nz and resn lys within %s of (name oe1 and resn glu)'%(delta*10))
    cmd.do('select lys22, name nz and resn lys within %s of (name cd and resn glu)'%(delta*9.5))
    cmd.do('select lys23, name ce and resn lys within %s of (name oe2 and resn glu)'%(delta*9))
    cmd.do('select lys24, name ce and resn lys within %s of (name oe1 and resn glu)'%(delta*10.2))
    cmd.do('select lys25, name ce and resn lys within %s of (name cd and resn glu)'%(delta*10))
    byResidue('lys', 25)
    cmd.do('select asn1, name od1 and resn asn within %s of (name nz and resn lys)'%(delta*7.5))
    cmd.do('select asn2, name nd2 and resn asn within %s of (name nz and resn lys)'%(delta*7.5))
    cmd.do('select asn3, name cg and resn asn within %s of (name nz and resn lys)'%(delta*7.5))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ce and resn lys)'%(delta*6.5))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ce and resn lys)'%(delta*6.5))
    cmd.do('select asn6, name cg and resn asn within %s of (name ce and resn lys)'%(delta*6.5))
    cmd.do('select asn7, name od1 and resn asn within %s of (name cd and resn lys)'%(delta*6.2))
    cmd.do('select asn8, name cg and resn asn within %s of (name cd and resn lys)'%(delta*6.5))
    cmd.do('select asn9, name nd2 and resn asn within %s of (name cd and resn lys)'%(delta*6.5))
    cmd.do('select asn10, name nd2 and resn asn within %s of (name ne2 and resn his)'%(delta*6.3))
    cmd.do('select asn11, name nd2 and resn asn within %s of (name cd2 and resn his)'%(delta*6.2))
    cmd.do('select asn12, name nd2 and resn asn within %s of (name ce1 and resn his)'%(delta*7.3))
    cmd.do('select asn13, name nd2 and resn asn within %s of (name nd1 and resn his)'%(delta*8))
    cmd.do('select asn14, name od1 and resn asn within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select asn15, name od1 and resn asn within %s of (name ce1 and resn his)'%(delta*9.2))
    cmd.do('select asn16, name od1 and resn asn within %s of (name cd2 and resn his)'%(delta*8.3))
    cmd.do('select asn17, name cg and resn asn within %s of (name ne2 and resn his)'%(delta*7.5))
    cmd.do('select asn18, name cg and resn asn within %s of (name ce1 and resn his)'%(delta*8.5))
    cmd.do('select asn19, name cg and resn asn within %s of (name cd2 and resn his)'%(delta*7.5))
    cmd.do('select asn20, name nd2 and resn asn within %s of (name oe2 and resn glu)'%(delta*9))
    cmd.do('select asn21, name nd2 and resn asn within %s of (name oe1 and resn glu)'%(delta*10.5))
    cmd.do('select asn22, name nd2 and resn asn within %s of (name cd and resn glu)'%(delta*10.2))
    cmd.do('select asn23, name cg and resn asn within %s of (name oe2 and resn glu)'%(delta*10))
    cmd.do('select asn24, name cg and resn asn within %s of (name cd and resn glu)'%(delta*11))
    cmd.do('select asn25, name cg and resn asn within %s of (name oe1 and resn glu)'%(delta*11.3))
    cmd.do('select asn26, name od1 and resn asn within %s of (name oe2 and resn glu)'%(delta*11))
    cmd.do('select asn27, name od1 and resn asn within %s of (name cd and resn glu)'%(delta*11))
    cmd.do('select asn28, name od1 and resn asn within %s of (name oe1 and resn glu)'%(delta*12))
    byResidue('asn', 28)
    cmd.do('select glu1, name oe2 and resn glu within %s of (name nz and resn lys)'%(delta*8.5))
    cmd.do('select glu2, name oe1 and resn glu within %s of (name nz and resn lys)'%(delta*10))
    cmd.do('select glu3, name cd and resn glu within %s of (name nz and resn lys)'%(delta*9.5))
    cmd.do('select glu4, name oe2 and resn glu within %s of (name ce and resn lys)'%(delta*9))
    cmd.do('select glu5, name oe1 and resn glu within %s of (name ce and resn lys)'%(delta*10.2))
    cmd.do('select glu6, name cd and resn glu within %s of (name ce and resn lys)'%(delta*10))
    cmd.do('select glu7, name oe2 and resn glu within %s of (name nd2 and resn asn)'%(delta*9))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name nd2 and resn asn)'%(delta*10.5))
    cmd.do('select glu9, name cd and resn glu within %s of (name nd2 and resn asn)'%(delta*10.2))
    cmd.do('select glu10, name oe2 and resn glu within %s of (name cg and resn asn)'%(delta*10))
    cmd.do('select glu11, name cd and resn glu within %s of (name cg and resn asn)'%(delta*11))
    cmd.do('select glu12, name oe1 and resn glu within %s of (name cg and resn asn)'%(delta*11.3))
    cmd.do('select glu13, name oe2 and resn glu within %s of (name od1 and resn asn)'%(delta*11))
    cmd.do('select glu14, name cd and resn glu within %s of (name od1 and resn asn)'%(delta*11))
    cmd.do('select glu15, name oe1 and resn glu within %s of (name od1 and resn asn)'%(delta*12))
    cmd.do('select glu16, name oe2 and resn glu within %s of (name ne2 and resn his)'%(delta*5.6))
    cmd.do('select glu17, name oe2 and resn glu within %s of (name cd2 and resn his)'%(delta*6.5))
    cmd.do('select glu18, name oe2 and resn glu within %s of (name ce1 and resn his)'%(delta*5.8))
    cmd.do('select glu19, name oe2 and resn glu within %s of (name nd1 and resn his)'%(delta*6.5))
    cmd.do('select glu20, name oe2 and resn glu within %s of (name cg and resn his)'%(delta*6.6))
    cmd.do('select glu21, name oe1 and resn glu within %s of (name ne2 and resn his)'%(delta*6.6))
    cmd.do('select glu22, name oe1 and resn glu within %s of (name cd2 and resn his)'%(delta*6.5))
    cmd.do('select glu23, name oe1 and resn glu within %s of (name ce1 and resn his)'%(delta*5.8))
    cmd.do('select glu24, name oe1 and resn glu within %s of (name nd1 and resn his)'%(delta*6.5))
    cmd.do('select glu25, name oe1 and resn glu within %s of (name cg and resn his)'%(delta*6.6))
    byResidue('glu', 25)
    cmd.do('select his1, name ne2 and resn his within %s of (name nz and resn lys)'%(delta*6.5))
    cmd.do('select his2, name nd1 and resn his within %s of (name nz and resn lys)'%(delta*7.5))
    cmd.do('select his3, name ce1 and resn his within %s of (name nz and resn lys)'%(delta*6.7))
    cmd.do('select his4, name cd2 and resn his within %s of (name nz and resn lys)'%(delta*7.5))
    cmd.do('select his5, name cg and resn his within %s of (name nz and resn lys)'%(delta*8))
    cmd.do('select his6, name ne2 and resn his within %s of (name ce and resn lys)'%(delta*6.2))
    cmd.do('select his7, name nd1 and resn his within %s of (name ce and resn lys)'%(delta*7.6))
    cmd.do('select his8, name ce1 and resn his within %s of (name ce and resn lys)'%(delta*6.6))
    cmd.do('select his9, name cd2 and resn his within %s of (name ce and resn lys)'%(delta*7))
    cmd.do('select his10, name cg and resn his within %s of (name ce and resn lys)'%(delta*7.5))
    cmd.do('select his11, name ne2 and resn his within %s of (name nd2 and resn asn)'%(delta*6.3))
    cmd.do('select his12, name cd2 and resn his within %s of (name nd2 and resn asn)'%(delta*6.2))
    cmd.do('select his13, name ce1 and resn his within %s of (name nd2 and resn asn)'%(delta*7.3))
    cmd.do('select his14, name nd1 and resn his within %s of (name nd2 and resn asn)'%(delta*8))
    cmd.do('select his15, name ne2 and resn his within %s of (name od1 and resn asn)'%(delta*8))
    cmd.do('select his16, name ce1 and resn his within %s of (name od1 and resn asn)'%(delta*9.2))
    cmd.do('select his17, name cd2 and resn his within %s of (name od1 and resn asn)'%(delta*8.3))
    cmd.do('select his18, name ne2 and resn his within %s of (name cg and resn asn)'%(delta*7.5))
    cmd.do('select his19, name ce1 and resn his within %s of (name cg and resn asn)'%(delta*8.5))
    cmd.do('select his20, name cd2 and resn his within %s of (name cg and resn asn)'%(delta*7.5))
    cmd.do('select his21, name ne2 and resn his within %s of (name oe2 and resn glu)'%(delta*5.6))
    cmd.do('select his22, name cd2 and resn his within %s of (name oe2 and resn glu)'%(delta*6.5))
    cmd.do('select his23, name ce1 and resn his within %s of (name oe2 and resn glu)'%(delta*5.8))
    cmd.do('select his24, name nd1 and resn his within %s of (name oe2 and resn glu)'%(delta*6.5))
    cmd.do('select his25, name cg and resn his within %s of (name oe2 and resn glu)'%(delta*6.6))
    cmd.do('select his26, name ne2 and resn his within %s of (name oe1 and resn glu)'%(delta*6.6))
    cmd.do('select his27, name cd2 and resn his within %s of (name oe1 and resn glu)'%(delta*6.5))
    cmd.do('select his28, name ce1 and resn his within %s of (name oe1 and resn glu)'%(delta*5.8))
    cmd.do('select his29, name nd1 and resn his within %s of (name oe1 and resn glu)'%(delta*6.5))
    cmd.do('select his30, name cg and resn his within %s of (name oe1 and resn glu)'%(delta*6.6))
    byResidue('his', 30)
    cmd.select('Triose_Isomerase', 'glu(his(asn(lys)))')
    return {'motif':'Triose_Isomerase'}

def alcoholdehyd(delta):
    cmd.do('select tyr1, name cd1 and resn tyr within %s of (name nd2 and resn asn)'%(delta*5))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name od1 and resn asn)'%(delta*8))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name nz and resn lys)'%(delta*6))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name og and resn ser)'%(delta*5.5))
    cmd.do('select tyr5, name ce2 and resn tyr within %s of (name cg and resn lys)'%(delta*6))
    cmd.do('select tyr6, name cg and resn tyr within %s of (name nd2 and resn asn)'%(delta*6.5))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name cb and resn ser)'%(delta*5.5))
    byResidue('tyr', 7)
    cmd.do('select asn1, name nd2 and resn asn within %s of (name cd1 and tyr)'%(delta*5))
    cmd.do('select asn2, name nd2 and resn asn within %s of (name oh and tyr)'%(delta*7))
    cmd.do('select asn3, name od1 and resn asn within %s of (name oh and tyr)'%(delta*7))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ce1 and tyr)'%(delta*6))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ce and resn lys)'%(delta*5.5))
    cmd.do('select asn6, name od1 and resn asn within %s5 of (name nz and resn lys)'%(delta*5.5))
    cmd.do('select asn7, name nd2 and resn asn within %s of (name og and resn ser)'%(delta*10))
    byResidue('asn', 7)
    cmd.do('select lys1, name nz and resn lys within %s of (name od1 and asn)'%(delta*6))
    cmd.do('select lys2, name ce and resn lys within %s of (name nd2 and asn)'%(delta*6.5))
    cmd.do('select lys3, name nz and resn lys within %s of (name oh and tyr)'%(delta*6))
    cmd.do('select lys4, name ce and resn lys within %s of (name cz and tyr)'%(delta*6))
    cmd.do('select lys4, name nz and resn lys within %s of (name cb and resn ser)'%(delta*7))
    cmd.do('select lys5, name ce and resn lys within %s of (name og and resn ser)'%(delta*7))
    cmd.do('select lys6, name cg and resn lys within %s of (name ce2 and resn tyr)'%(delta*6))
    cmd.do('select lys7, name cd and resn lys within %s of (name cb and resn ser)'%(delta*6))
    cmd.do('select lys8, name cd and resn lys within %s of (name cb and resn asn)'%(delta*7))
    cmd.do('select lys9, name ce and resn lys within %s of (name ce1 and resn tyr)'%(delta*6))
    byResidue('lys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name oh and tyr)'%(delta*6))
    cmd.do('select ser2, name og and resn ser within %s of (name ce2 and tyr)'%(delta*6))
    cmd.do('select ser3, name og and resn ser within %s of (name nz and lys)'%(delta*8))
    cmd.do('select ser4, name cb and resn ser within %s of (name oh and tyr)'%(delta*6))
    cmd.do('select ser5, name cb and resn ser within %s of (name cd and lys)'%(delta*6))
    cmd.do('select ser6, name cb and resn ser within %s of (name od1 and asn)'%(delta*10))
    cmd.do('select ser7, name ca and resn ser within %s of (name nd2 and asn)'%(delta*10))
    byResidue('ser', 7)
    cmd.select('Alcohol_Dehyd', 'ser(tyr(lys(asn)))')
    return {'motif':'Alcohol_Dehyd'}

def aldosereductase(delta):
    cmd.do('select lys1, name cd and resn lys within %s of (name cg and resn his)'%(delta*6))
    cmd.do('select lys2, name ce and resn lys within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select lys3, name cd and resn lys within %s of (name nd1 and resn his)'%(delta*7))
    cmd.do('select lys4, name nz and resn lys within %s of (name oh and resn tyr)'%(delta*5))
    cmd.do('select lys5, name nz and resn lys within %s of (name ce2 and resn tyr)'%(delta*6))
    cmd.do('select lys6, name cg and resn lys within %s of (name cz and resn tyr)'%(delta*8))
    cmd.do('select lys7, name nz and resn lys within %s of (name od1 and resn asp)'%(delta*5))
    cmd.do('select lys8, name ce and resn lys within %s of (name od1 and resn asp)'%(delta*5.5))
    cmd.do('select lys9, name cg and resn lys within %s of (name ca and resn asp)'%(delta*9))
    byResidue('lys', 9)
    cmd.do('select his1, name cg and resn his within %s of (name cd and resn lys)'%(delta*6))
    cmd.do('select his2, name ne2 and resn his within %s of (name ce and resn lys)'%(delta*8))
    cmd.do('select his3, name nd1 and resn his within %s of (name cd and resn lys)'%(delta*7))
    cmd.do('select his4, name ne2 and resn his within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select his5, name ce1 and resn his within %s of (name cz and resn tyr)'%(delta*6))
    cmd.do('select his6, name nd1 and resn his within %s of (name ce1 and resn tyr)'%(delta*7))
    cmd.do('select his7, name nd1 and resn his within %s of (name od1 and resn asp)'%(delta*10.5))
    cmd.do('select his8, name ne2 and resn his within %s of (name cg and resn asp)'%(delta*10))
    cmd.do('select his9, name ce1 and resn his within %s of (name od2 and resn asp)'%(delta*9))
    byResidue('his', 9)
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nz and resn lys )'%(delta*5))
    cmd.do('select tyr2, name ce2 and resn tyr within %s of (name nz and resn lys )'%(delta*6))
    cmd.do('select tyr3, name cz and resn tyr within %s of (name cg and resn lys)'%(delta*8))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name ne2 and resn his)'%(delta*6))
    cmd.do('select tyr5, name cz and resn tyr within %s of (name ce1 and resn his)'%(delta*6))
    cmd.do('select tyr6, name ce1 and resn tyr within %s of (name nd1 and resn his)'%(delta*7))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name od2 and resn asp)'%(delta*7))
    cmd.do('select tyr8, name cz and resn tyr within %s of (name cb and resn asp)'%(delta*9))
    cmd.do('select tyr9, name ce2 and resn tyr within %s of (name ca and resn asp)'%(delta*8))
    byResidue('tyr', 9)
    cmd.do('select asp1, name od1 and resn asp within %s of (name nz and resn lys)'%(delta*5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name ce and resn lys)'%(delta*5.5))
    cmd.do('select asp3, name ca and resn asp within %s of (name cg and resn lys)'%(delta*9))
    cmd.do('select asp4, name od1 and resn asp within %s of (name nd1 and resn his)'%(delta*10.5))
    cmd.do('select asp5, name cg and resn asp within %s of (name ne2 and resn his)'%(delta*10))
    cmd.do('select asp6, name od2 and resn asp within %s of (name ce1 and resn his)'%(delta*9))
    cmd.do('select asp7, name od2 and resn asp within %s of (name oh and resn tyr)'%(delta*7))
    cmd.do('select asp8, name cb and resn asp within %s of (name cz and resn tyr)'%(delta*9))
    cmd.do('select asp9, name ca and resn asp within %s of (name ce2 and resn tyr)'%(delta*8))
    byResidue('asp', 9)
    cmd.select('Aldose_Reductase', 'asp(his(lys(tyr)))')
    return {'motif':'Aldose_Reductase'}

def cistransisomerase(delta):
    cmd.do('select tyr1, name oh and resn tyr within %s of (name od2 and resn asp)'%(delta*9))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name od1 and resn asp)'%(delta*11))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name cg and resn asp)'%(delta*9.8))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name cb and resn asp)'%(delta*9.8))
    cmd.do('select tyr5, name cz and resn tyr within %s of (name od2 and resn asp)'%(delta*10.2))
    cmd.do('select tyr6, name cz and resn tyr within %s of (name od1 and resn asp)'%(delta*11.5))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name cd1 and resn ile)'%(delta*6.5))
    cmd.do('select tyr8, name oh and resn tyr within %s of (name cg1 and resn ile)'%(delta*6.5))
    cmd.do('select tyr9, name oh and resn tyr within %s of (name cg2 and resn ile)'%(delta*5.5))
    cmd.do('select tyr10, name cz and resn tyr within %s of (name cd1 and resn ile)'%(delta*6.5))
    cmd.do('select tyr11, name cz and resn tyr within %s of (name cg1 and resn ile)'%(delta*6.8))
    cmd.do('select tyr12, name cz and resn tyr within %s of (name cg2 and resn ile)'%(delta*5.5))
    cmd.do('select tyr13, name ce1 and resn tyr within %s of (name cd1 and resn ile)'%(delta*6.3))
    cmd.do('select tyr14, name ce1 and resn tyr within %s of (name cg1 and resn ile)'%(delta*6.5))
    cmd.do('select tyr15, name ce1 and resn tyr within %s of (name cg2 and resn ile)'%(delta*5.5))
    byResidue('tyr', 15)
    cmd.do('select asp1, name od2 and resn asp within %s of (name oh and tyr)'%(delta*8.7))
    cmd.do('select asp2, name od1 and resn asp within %s of (name oh and tyr)'%(delta*10.5))
    cmd.do('select asp3, name cg and resn asp within %s of (name oh and tyr)'%(delta*9.3))
    cmd.do('select asp4, name cb and resn asp within %s of (name oh and tyr)'%(delta*9.3))
    cmd.do('select asp5, name od2 and resn asp within %s of (name cz and tyr)'%(delta*10))
    cmd.do('select asp6, name od1 and resn asp within %s of (name cz and resn tyr)'%(delta*11.1))
    cmd.do('select asp7, name od2 and resn asp within %s of (name cg2 and resn ile)'%(delta*11.1))
    cmd.do('select asp8, name od2 and resn asp within %s of (name cd1 and resn ile)'%(delta*11.1))
    cmd.do('select asp9, name od2 and resn asp within %s of (name cg1 and resn ile)'%(delta*11.1))
    cmd.do('select asp10, name cb and resn asp within %s of (name cd1 and resn ile)'%(delta*10.8))
    cmd.do('select asp11, name cb and resn asp within %s of (name cg2 and resn ile)'%(delta*11.1))
    cmd.do('select asp12, name cb and resn asp within %s of (name cg1 and resn ile)'%(delta*11.1))
    byResidue('asp', 12)
    cmd.do('select ile1, name cd1 and resn ile within %s of (name oh and tyr)'%(delta*6.5))
    cmd.do('select ile2, name cg1 and resn ile within %s of (name oh and tyr)'%(delta*6.5))
    cmd.do('select ile3, name cg2 and resn ile within %s of (name oh and tyr)'%(delta*5.5))
    cmd.do('select ile4, name cd1 and resn ile within %s of (name cz and resn tyr)'%(delta*6.5))
    cmd.do('select ile5, name cg1 and resn ile within %s of (name cz and resn tyr)'%(delta*6.8))
    cmd.do('select ile6, name cg2 and resn ile within %s of (name cz and resn tyr)'%(delta*5.5))
    cmd.do('select ile7, name cd1 and resn ile within %s of (name ce1 and resn tyr)'%(delta*6.3))
    cmd.do('select ile8, name cg1 and resn ile within %s of (name ce1 and resn tyr)'%(delta*6.5))
    cmd.do('select ile9, name cg2 and resn ile within %s of (name ce1 and resn tyr)'%(delta*5.5))
    cmd.do('select ile10, name cg2 and resn ile within %s of (name od2 and asp)'%(delta*11.5))
    cmd.do('select ile11, name cd1 and resn ile within %s of (name od2 and asp)'%(delta*11.5))
    cmd.do('select ile12, name cg1 and resn ile within %s of (name od2 and asp)'%(delta*11.5))
    cmd.do('select ile13, name cd1 and resn ile within %s of (name cb and asp)'%(delta*11))
    cmd.do('select ile14, name cg2 and resn ile within %s of (name cb and resn asp)'%(delta*11.5))
    cmd.do('select ile15, name cg1 and resn ile within %s of (name cb and resn asp)'%(delta*11.5))
    byResidue('ile', 15)
    cmd.select('Cis_trans', 'ile(asp(tyr))')
    return {'motif':'Cis_trans'}

def nadhbinderasp(delta):
    cmd.do('select asp1, name od2 and resn asp within %s of (name sg and resn cys)'%(delta*5))
    cmd.do('select asp2, name od2 and resn asp within %s of (name cb and resn cys)'%(delta*5.5))
    cmd.do('select asp3, name od1 and resn asp within %s of (name sg and resn cys)'%(delta*6.4))
    cmd.do('select asp4, name od1 and resn asp within %s of (name cb and resn cys)'%(delta*7.2))
    cmd.do('select asp5, name cg and resn asp within %s of (name sg and resn cys)'%(delta*5.5))
    cmd.do('select asp6, name od2 and resn asp within %s of (name og and resn ser)'%(delta*4.5))
    cmd.do('select asp7, name od2 and resn asp within %s of (name cb and resn ser)'%(delta*5.5))
    cmd.do('select asp8, name od1 and resn asp within %s of (name og and resn ser)'%(delta*6))
    cmd.do('select asp9, name od1 and resn asp within %s of (name cb and resn ser)'%(delta*7))
    cmd.do('select asp10, name cg and resn asp within %s of (name og and resn ser)'%(delta*5.3))
    cmd.do('select asp11, name cg and resn asp within %s of (name cb and resn ser)'%(delta*6.4))
    byResidue('asp', 11)
    cmd.do('select cys1, name sg and resn cys within %s of (name od2 and resn asp)'%(delta*5))
    cmd.do('select cys2, name cb and resn cys within %s of (name od2 and resn asp)'%(delta*5.5))
    cmd.do('select cys3, name sg and resn cys within %s of (name od1 and resn asp)'%(delta*6.4))
    cmd.do('select cys4, name cb and resn cys within %s of (name od1 and resn asp)'%(delta*7.2))
    cmd.do('select cys5, name sg and resn cys within %s of (name cg and resn asp)'%(delta*5.5))
    cmd.do('select cys6, name sg and resn cys within %s of (name og and resn ser)'%(delta*6.4))
    cmd.do('select cys7, name sg and resn cys within %s of (name cb and resn ser)'%(delta*7))
    cmd.do('select cys8, name cb and resn cys within %s of (name og and resn ser)'%(delta*8))
    cmd.do('select cys9, name cb and resn cys within %s of (name cb and resn ser)'%(delta*8.5))
    byResidue('cys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name od2 and resn asp)'%(delta*4.5))
    cmd.do('select ser2, name cb and resn ser within %s of (name od2 and resn asp)'%(delta*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select ser4, name cb and resn ser within %s of (name od1 and resn asp)'%(delta*7))
    cmd.do('select ser5, name og and resn ser within %s of (name cg and resn asp)'%(delta*5.3))
    cmd.do('select ser6, name cb and resn ser within %s of (name cg and resn asp)'%(delta*6.4))
    cmd.do('select ser7, name og and resn ser within %s of (name sg and resn cys)'%(delta*6.4))
    cmd.do('select ser8, name cb and resn ser within %s of (name sg and resn cys)'%(delta*7))
    cmd.do('select ser9, name og and resn ser within %s of (name cb and resn cys)'%(delta*8))
    cmd.do('select ser10, name cb and resn ser within %s of (name cb and resn cys)'%(delta*8.5))
    byResidue('ser', 10)
    cmd.select('NAD_reductase', 'ser(asp(cys))')
    return {'motif','NAD_reductase_Asp'}

def nadhbinderglu(delta):
    cmd.do('select glu1, name oe2 and resn glu within %s of (name sg and resn cys)'%(delta*6.5))
    cmd.do('select glu2, name oe2 and resn glu within %s of (name cb and resn cys)'%(delta*5.5))
    cmd.do('select glu3, name oe1 and resn glu within %s of (name sg and resn cys)'%(delta*6.5))
    cmd.do('select glu4, name oe1 and resn glu within %s of (name cb and resn cys)'%(delta*7.2))
    cmd.do('select glu5, name cg and resn glu within %s of (name sg and resn cys)'%(delta*5.5))
    cmd.do('select glu6, name oe2 and resn glu within %s of (name og and resn ser)'%(delta*4.5))
    cmd.do('select glu7, name oe2 and resn glu within %s of (name cb and resn ser)'%(delta*5.5))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name og and resn ser)'%(delta*6))
    cmd.do('select glu9, name oe1 and resn glu within %s of (name cb and resn ser)'%(delta*7))
    cmd.do('select glu10, name cg and resn glu within %s of (name og and resn ser)'%(delta*5.5))
    cmd.do('select glu11, name cg and resn glu within %s of (name cb and resn ser)'%(delta*6.5))
    byResidue('glu', 11)
    cmd.do('select cys1, name sg and resn cys within %s of (name oe2 and resn glu)'%(delta*6.5))
    cmd.do('select cys2, name cb and resn cys within %s of (name oe2 and resn glu)'%(delta*6.5))
    cmd.do('select cys3, name sg and resn cys within %s of (name oe1 and resn glu)'%(delta*6.5))
    cmd.do('select cys4, name cb and resn cys within %s of (name oe1 and resn glu)'%(delta*7.5))
    cmd.do('select cys5, name sg and resn cys within %s of (name cg and resn glu)'%(delta*5.5))
    cmd.do('select cys6, name sg and resn cys within %s of (name og and resn ser)'%(delta*6.5))
    cmd.do('select cys7, name sg and resn cys within %s of (name cb and resn ser)'%(delta*7))
    cmd.do('select cys8, name cb and resn cys within %s of (name og and resn ser)'%(delta*8))
    cmd.do('select cys9, name cb and resn cys within %s of (name cb and resn ser)'%(delta*8.5))
    byResidue('cys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name oe2 and resn glu)'%(delta*4.5))
    cmd.do('select ser2, name cb and resn ser within %s of (name oe2 and resn glu)'%(delta*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name oe1 and resn glu)'%(delta*6))
    cmd.do('select ser4, name cb and resn ser within %s of (name oe1 and resn glu)'%(delta*7))
    cmd.do('select ser5, name og and resn ser within %s of (name cg and resn glu)'%(delta*5.5))
    cmd.do('select ser6, name cb and resn ser within %s of (name cg and resn glu)'%(delta*6.5))
    cmd.do('select ser7, name og and resn ser within %s of (name sg and resn cys)'%(delta*6.5))
    cmd.do('select ser8, name cb and resn ser within %s of (name sg and resn cys)'%(delta*7))
    cmd.do('select ser9, name og and resn ser within %s of (name cb and resn cys)'%(delta*8))
    cmd.do('select ser10, name cb and resn ser within %s of (name cb and resn cys)'%(delta*8.5))
    byResidue('ser', 10)
    cmd.select('NAD_reductase_Glu', 'ser(glu(cys))')
    return {'motif':'NAD_reductase_Glu'}

def cephdeacetylase(delta):
    cmd.do('select his1, name nd1 and resn his within %s of (name od2 and resn asp)'%(delta*4.5))
    cmd.do('select his2, name nd1 and resn his within %s of (name od1 and resn asp)'%(delta*5))
    cmd.do('select his3, name nd1 and resn his within %s of (name cg and resn asp)'%(delta*5.5))
    cmd.do('select his4, name ce1 and resn his within %s of (name od2 and resn asp)'%(delta*5.5))
    cmd.do('select his5, name ce1 and resn his within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select his6, name ne2 and resn his within %s of (name od1 and resn asp)'%(delta*7))
    cmd.do('select his7, name ne2 and resn his within %s of (name od2 and resn asp)'%(delta*6.5))
    cmd.do('select his8, name ne2 and resn his within %s of (name cb and resn ala)'%(delta*5.5))
    cmd.do('select his9, name ce1 and resn his within %s of (name cb and resn ala)'%(delta*5.5))
    cmd.do('select his10, name nd1 and resn his within %s of (name cb and resn ala)'%(delta*6.5))
    byResidue('his', 10)
    cmd.do('select asp1, name od2 and resn asp within %s of (name cb and resn ala)'%(delta*8.5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name cb and resn ala)'%(delta*9.5))
    cmd.do('select asp3, name cg and resn asp within %s of (name cb and resn ala)'%(delta*9.5))
    cmd.do('select asp4, name od2 and resn asp within %s of (name nd1 and resn his)'%(delta*4.5))
    cmd.do('select asp5, name od1 and resn asp within %s of (name nd1 and resn his)'%(delta*5))
    cmd.do('select asp6, name cg and resn asp within %s of (name nd1 and resn his)'%(delta*5.5))
    cmd.do('select asp7, name od2 and resn asp within %s of (name ce1 and resn his)'%(delta*5.5))
    cmd.do('select asp8, name od1 and resn asp within %s of (name ce1 and resn his)'%(delta*6))
    cmd.do('select asp9, name od1 and resn asp within %s of (name ne2 and resn his)'%(delta*7))
    cmd.do('select asp10, name od2 and resn asp within %s of (name ne2 and resn his)'%(delta*6.5))
    byResidue('asp', 10)
    cmd.do('select ala1, name cb and resn ala within %s of (name ne2 and resn his)'%(delta*5.5))
    cmd.do('select ala2, name cb and resn ala within %s of (name ce1 and resn his)'%(delta*5.5))
    cmd.do('select ala3, name cb and resn ala within %s of (name nd1 and resn his)'%(delta*6.5))
    cmd.do('select ala4, name cb and resn ala within %s of (name od2 and resn asp)'%(delta*8.5))
    cmd.do('select ala5, name cb and resn ala within %s of (name od1 and resn asp)'%(delta*9.5))
    cmd.do('select ala6, name cb and resn ala within %s of (name cg and resn asp)'%(delta*9.5))
    cmd.do('select ala7, name c and resn ala within %s of (name n and resn gln)'%(delta*2.5))
    byResidue('ala', 7)
    cmd.do('select gln1, byres resn gln within %s of his'%(delta*9.5))
    cmd.do('select gln2, byres resn gln within %s of asp'%(delta*13.5))
    cmd.do('select gln3, byres resn gln within %s of ala'%(delta*3))
    byResidue('gln', 3)
    cmd.select('deacetylase', 'his(asp(ala(gln)))')
    return {'motif':'Deacetylase'}

def chondrolyase(delta):
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nh2 and resn arg)'%(delta*6))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name nh1 and resn arg)'%(delta*5))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name cz and resn arg)'%(delta*6))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name ne and resn arg)'%(delta*7))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name ne2 and resn his)'%(delta*5))
    cmd.do('select tyr6, name oh and resn tyr within %s of (name nd1 and resn his)'%(delta*6))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name ce1 and resn his)'%(delta*5))
    cmd.do('select tyr8, name ce2 and resn tyr within %s of (name nd1 and resn his)'%(delta*6))
    cmd.do('select tyr9, name ce1 and resn tyr within %s of (name ne2 and resn his)'%(delta*6))
    cmd.do('select tyr10, name oh and resn tyr within %s of (name od1 and resn asn)'%(delta*7.5))
    cmd.do('select tyr11, name oh and resn tyr within %s of (name nd2 and resn asn)'%(delta*7.5))
    cmd.do('select tyr12, name ce1 and resn tyr within %s of (name od1 and resn asn)'%(delta*6.5))
    cmd.do('select tyr13, name ce1 and resn tyr within %s of (name nd2 and resn asn)'%(delta*6))
    byResidue('tyr', 13)
    cmd.do('select his1, name ne2 and resn his within %s of (name od1 and resn asn)'%(delta*7))
    cmd.do('select his2, name ne2 and resn his within %s of (name nd2 and resn asn)'%(delta*8))
    cmd.do('select his3, name cd2 and resn his within %s of (name od1 and resn asn)'%(delta*7))
    cmd.do('select his4, name ne2 and resn his within %s of (name cg and resn asn)'%(delta*8))
    cmd.do('select his5, name ne2 and resn his within %s of (name oh and resn tyr)'%(delta*5))
    cmd.do('select his6, name nd1 and resn his within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select his7, name ce1 and resn his within %s of (name oh and resn tyr)'%(delta*5))
    cmd.do('select his8, name nd1 and resn his within %s of (name ce2 and resn tyr)'%(delta*6))
    cmd.do('select his9, name ne2 and resn his within %s of (name ce1 and resn tyr)'%(delta*6))
    cmd.do('select his10, name ne2 and resn his within %s of (name nh2 and resn arg)'%(delta*8))
    cmd.do('select his11, name ce1 and resn his within %s of (name cz and resn arg)'%(delta*7))
    cmd.do('select his12, name nd1 and resn his within %s of (name nh1 and resn arg)'%(delta*6.5))
    cmd.do('select his13, name nd1 and resn his within %s of (name cd and resn arg)'%(delta*9))
    byResidue('his', 13)
    cmd.do('select arg1, name nh2 and resn arg within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select arg2, name nh1 and resn arg within %s of (name oh and tyr)'%(delta*6))
    cmd.do('select arg3, name cz and resn arg within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select arg4, name ne and resn arg within %s of (name oh and resn tyr)'%(delta*7))
    cmd.do('select arg5, name nh2 and resn arg within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select arg6, name cz and resn arg within %s of (name ce1 and resn his)'%(delta*7))
    cmd.do('select arg7, name nh1 and resn arg within %s of (name nd1 and resn his)'%(delta*6.5))
    cmd.do('select arg8, name cd and resn arg within %s of (name nd1 and resn his)'%(delta*9))
    cmd.do('select arg9, name nh1 and resn arg within %s of (name od1 and resn asn)'%(delta*11))
    cmd.do('select arg10, name cz and resn arg within %s of (name cg and resn asn)'%(delta*12))
    cmd.do('select arg11, name nh2 and resn arg within %s of (name nd2 and resn asn)'%(delta*11.5))
    byResidue('arg', 11)
    cmd.do('select asn1, name od1 and resn asn within %s of (name nh1 and resn arg)'%(delta*11))
    cmd.do('select asn2, name cg and resn asn within %s of (name cz and resn arg)'%(delta*11.5))
    cmd.do('select asn3, name nd2 and resn asn within %s of (name nh2 and resn arg)'%(delta*10.5))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ne2 and resn his)'%(delta*7))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select asn6, name od1 and resn asn within %s of (name cd2 and resn his)'%(delta*7))
    cmd.do('select asn7, name cg and resn asn within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select asn8, name od1 and resn asn within %s of (name oh and resn tyr)'%(delta*7.5))
    cmd.do('select asn9, name nd2 and resn asn within %s of (name oh and resn tyr)'%(delta*7.5))
    cmd.do('select asn10, name od1 and resn asn within %s of (name ce1 and resn tyr)'%(delta*6.5))
    cmd.do('select asn11, name nd2 and resn asn within %s of (name ce1 and resn tyr)'%(delta*6.5))
    byResidue('asn', 11)
    cmd.select('chondroitinase', 'asn(his(arg(tyr)))')
    return {'motif':'Chondroitinase'}

def hyaluronlyase(delta):
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nh2 and resn arg)'%(delta*6))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name nh1 and resn arg)'%(delta*5))
    cmd.do('select tyr3, name oh and resn tyr within %sof (name cz and resn arg)'%(delta*6))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name ne and resn arg)'%(delta*7))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name ne2 and resn his)'%(delta*5))
    cmd.do('select tyr6, name oh and resn tyr within %s of (name nd1 and resn his)'%(delta*6))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name ce1 and resn his)'%(delta*5))
    cmd.do('select tyr8, name ce2 and resn tyr within %s of (name nd1 and resn his)'%(delta*6))
    cmd.do('select tyr9, name ce1 and resn tyr within %s of (name ne2 and resn his)'%(delta*6))
    cmd.do('select tyr10, name oh and resn tyr within %s of (name od1 and resn asn)'%(delta*7.5))
    cmd.do('select tyr11, name oh and resn tyr within %s of (name nd2 and resn asn)'%(delta*7.5))
    cmd.do('select tyr12, name ce1 and resn tyr within %s of (name od1 and resn asn)'%(delta*6.5))
    cmd.do('select tyr13, name ce1 and resn tyr within %s of (name nd2 and resn asn)'%(delta*6))
    byResidue('tyr', 13)
    cmd.do('select his1, name ne2 and resn his within %s of (name od1 and resn asn)'%(delta*7))
    cmd.do('select his2, name ne2 and resn his within %s of (name nd2 and resn asn)'%(delta*8))
    cmd.do('select his3, name cd2 and resn his within %s of (name od1 and resn asn)'%(delta*7))
    cmd.do('select his4, name ne2 and resn his within %s of (name cg and resn asn)'%(delta*8))
    cmd.do('select his5, name ne2 and resn his within %s of (name oh and resn tyr)'%(delta*5))
    cmd.do('select his6, name nd1 and resn his within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select his7, name ce1 and resn his within %s of (name oh and resn tyr)'%(delta*5))
    cmd.do('select his8, name nd1 and resn his within %s of (name ce2 and resn tyr)'%(delta*6))
    cmd.do('select his9, name ne2 and resn his within %s of (name ce1 and resn tyr)'%(delta*6))
    cmd.do('select his10, name ne2 and resn his within %s of (name nh2 and resn arg)'%(delta*8))
    cmd.do('select his11, name ce1 and resn his within %s of (name cz and resn arg)'%(delta*7))
    cmd.do('select his12, name nd1 and resn his within %s of (name nh1 and resn arg)'%(delta*6.5))
    cmd.do('select his13, name nd1 and resn his within %s of (name cd and resn arg)'%(delta*9))
    byResidue('his', 13)
    cmd.do('select arg1, name nh2 and resn arg within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select arg2, name nh1 and resn arg within %s of (name oh and tyr)'%(delta*6))
    cmd.do('select arg3, name cz and resn arg within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select arg4, name ne and resn arg within %s of (name oh and resn tyr)'%(delta*7))
    cmd.do('select arg5, name nh2 and resn arg within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select arg6, name cz and resn arg within %s of (name ce1 and resn his)'%(delta*7))
    cmd.do('select arg7, name nh1 and resn arg within %s of (name nd1 and resn his)'%(delta*6.5))
    cmd.do('select arg8, name cd and resn arg within %s of (name nd1 and resn his)'%(delta*9))
    cmd.do('select arg9, name nh1 and resn arg within %s of (name od1 and resn asn)'%(delta*11))
    cmd.do('select arg10, name cz and resn arg within %s of (name cg and resn asn)'%(delta*12))
    cmd.do('select arg11, name nh2 and resn arg within %s of (name nd2 and resn asn)'%(delta*11.5))
    byResidue('arg', 11)
    cmd.do('select asn1, name od1 and resn asn within %s of (name nh1 and resn arg)'%(delta*11))
    cmd.do('select asn2, name cg and resn asn within %s of (name cz and resn arg)'%(delta*11.5))
    cmd.do('select asn3, name nd2 and resn asn within %s of (name nh2 and resn arg)'%(delta*10.5))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ne2 and resn his)'%(delta*7))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select asn6, name od1 and resn asn within %s of (name cd2 and resn his)'%(delta*7))
    cmd.do('select asn7, name cg and resn asn within %s of (name ne2 and resn his)'%(delta*8))
    cmd.do('select asn8, name od1 and resn asn within %s of (name oh and resn tyr)'%(delta*7.5))
    cmd.do('select asn9, name nd2 and resn asn within %s of (name oh and resn tyr)'%(delta*7.5))
    cmd.do('select asn10, name od1 and resn asn within %s of (name ce1 and resn tyr)'%(delta*6.5))
    cmd.do('select asn11, name nd2 and resn asn within %s of (name ce1 and resn tyr)'%(delta*6.5))
    byResidue('asn', 11)
    cmd.select('Hyaluronate_Lyase', 'asn(his(arg(tyr)))')
    return {'motif':'Hyaluronate_Lyase'}

def ACTase(delta):
    showinfo('Info', 'This motif is based on sequence not position')
    cmd.select('gln', 'resi 231 and resn gln')
    cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
    cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
    cmd.select('his', 'resi 134 and resn his')
    cmd.select('lys', 'resi 84 and resn lys')
    cmd.select('ser', 'resi 80 and resn ser')
    cmd.select('ACTase', 'gln(arg(thr(his(lys(ser)))))')
    return {'motif':'ACTase'}

def exonucleaseiii(delta):
    cmd.do('select his1, name ne2 and resn his within %s of (name nd2 and resn asn)'%(delta*5.5))
    cmd.do('select his2, name ne2 and resn his within %s of (name od1 and resn asn)'%(delta*6.5))
    cmd.do('select his3, name ne2 and resn his within %s of (name cg and resn asn)'%(delta*5.5))
    cmd.do('select his4, name cd2 and resn his within %s of (name cg and resn asn)'%(delta*5.5))
    cmd.do('select his5, name nd1 and resn his within %s of (name cg and resn asn)'%(delta*6.5))
    cmd.do('select his6, name ce1 and resn his within %s of (name od2 and resn asp)'%(delta*5.5))
    cmd.do('select his7, name nd1 and resn his within %s of (name od2 and resn asp)'%(delta*5))
    cmd.do('select his8, name nd1 and resn his within %s of (name od1 and resn asp)'%(delta*5.5))
    cmd.do('select his9, name nd1 and resn his within %s of (name cg and resn asp)'%(delta*5.5))
    byResidue('his', 9)
    cmd.do('select asp1, name od2 and resn asp within %s of (name ce1 and resn his)'%(delta*5.5))
    cmd.do('select asp2, name od2 and resn asp within %s of (name nd1 and resn his)'%(delta*5))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nd1 and resn his)'%(delta*5.5))
    cmd.do('select asp4, name cg and resn asp within %s of (name nd1 and resn his)'%(delta*5.5))
    cmd.do('select asp5, name od2 and resn asp within %s of (name nd2 and resn asn)'%(delta*5.7))
    cmd.do('select asp6, name od1 and resn asp within %s of (name nd2 and resn asn)'%(delta*6))
    cmd.do('select asp7, name od1 and resn asp within %s of (name od1 and resn asn)'%(delta*6))
    byResidue('asp8', 7)
    cmd.do('select asp9, byres resn asp within %s of asp8'%(delta*5.5))
    cmd.do('select asp10, byres resn asp within %s of his'%(delta*5.5))
    cmd.select('asp', 'byres asp8 or (byres asp9 and byres asp10)')
    cmd.do('select asn1, name nd2 and resn asn within %s of (name ne2 and resn his)'%(delta*5.5))
    cmd.do('select asn2, name od1 and resn asn within %s of (name ne2 and resn his)'%(delta*6.5))
    cmd.do('select asn3, name cg and resn asn within %s of (name ne2 and resn his)'%(delta*5.5))
    cmd.do('select asn4, name cg and resn asn within %s of (name cd2 and resn his)'%(delta*5.5))
    cmd.do('select asn5, name cg and resn asn within %s of (name nd1 and resn his)'%(delta*6.5))
    cmd.do('select asn6, name nd2 and resn asn within %s of (name od2 and resn asp)'%(delta*5.7))
    cmd.do('select asn7, name nd2 and resn asn within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select asn8, name od1 and resn asn within %s of (name od1 and resn asp)'%(delta*6))
    byResidue('asn9', 8)
    cmd.do('select asn10, byres resn asn within %s of asn9'%(delta*8))
    cmd.do('select asn11, byres resn asn within %s of his'%(delta*8))
    cmd.do('select asn12, byres resn asn within %s of asp8'%(delta*6))
    cmd.select('asn', 'byres asn9 or (byres asn10 and byres asn11 and byres asn12)')
    cmd.select('Exonuclease3', 'his(asp(asn))')
    return {'motif':'Exonuclease3'}

def cyclinkinase(delta):
    cmd.do('select glu1, name oe2 and resn glu within %s of (name nz and resn lys)'%(delta*6.5))
    cmd.do('select glu2, name oe1 and resn glu within %s of (name nz and resn lys)'%(delta*7))
    cmd.do('select glu3, name cd and resn glu within %s of (name nz and resn lys)'%(delta*7))
    cmd.do('select glu4, name oe1 and resn glu within %s of (name ce and resn lys)'%(delta*6))
    cmd.do('select glu5, name cd and resn glu within %s of (name ce and resn lys)'%(delta*6))
    cmd.do('select glu6, name oe1 and resn glu within %s of (name cd and resn lys)'%(delta*5.5))
    cmd.do('select glu7, name oe2 and resn glu within %s of (name ce and resn lys)'%(delta*6))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name cg and resn lys)'%(delta*5.5))
    cmd.do('select glu9, name oe1 and resn glu within %s of (name od1 and resn asp)'%(delta*10))
    cmd.do('select glu10, name oe2 and resn glu within %s of (name od1 and resn asp)'%(delta*10))
    byResidue('glu', 10)
    cmd.do('select lys1, name nz and resn lys within %s of (name oe2 and resn glu)'%(delta*6.5))
    cmd.do('select lys2, name nz and resn lys within %s of (name oe1 and resn glu)'%(delta*7))
    cmd.do('select lys3, name nz and resn lys within %s of (name cd and glu)'%(delta*7))
    cmd.do('select lys4, name ce and resn lys within %s of (name oe1 and resn glu)'%(delta*6))
    cmd.do('select lys5, name ce and resn lys within %s of (name cd and resn glu)'%(delta*6))
    cmd.do('select lys6, name cd and resn lys within %s of (name oe1 and resn glu)'%(delta*5.5))
    cmd.do('select lys7, name ce and resn lys within %s of (name oe2 and resn glu)'%(delta*6))
    cmd.do('select lys8, name cg and resn lys within %s of (name oe1 and resn glu)'%(delta*5.5))
    cmd.do('select lys9, name nz and resn lys within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select lys10, name nz and resn lys within %s of (name od2 and resn asp)'%(delta*6))
    cmd.do('select lys11, name ce and resn lys within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select lys12, name ce and resn lys within %s of (name od2 and resn asp)'%(delta*6.5))
    cmd.do('select lys13, name cd and resn lys within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select lys14, name cd and resn lys within %s of (name od2 and resn asp)'%(delta*7))
    byResidue('lys', 14)
    cmd.do('select asp1, name od1 and resn asp within %s of (name oe1 and glu)'%(delta*10))
    cmd.do('select asp2, name od1 and resn asp within %s of (name oe2 and glu)'%(delta*10))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nz and lys)'%(delta*6))
    cmd.do('select asp4, name od2 and resn asp within %s of (name nz and lys)'%(delta*6))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ce and lys)'%(delta*6))
    cmd.do('select asp6, name od2 and resn asp within %s of (name ce and resn lys)'%(delta*6.5))
    cmd.do('select asp7, name od1 and resn asp within %s of (name cd and resn lys)'%(delta*6))
    cmd.do('select asp8, name od2 and resn asp within %s of (name cd and resn lys)'%(delta*7))
    cmd.do('select asp9, name cg and resn asp within %s of (name cd and resn lys)'%(delta*7))
    byResidue('asp', 9)
    cmd.select('Cyclin_Kinase', 'lys(asp(glu))')
    return {'motif':'Cyclin_Kinase'}

def adenylatekinase(delta):
    #p-loop first
    cmd.do('select lys1, name nz and resn lys within %s of (name n and resn gly)'%(delta*7.5))
    cmd.do('select lys2, name cg and resn lys within %s of (name c and resn gly)'%(delta*6))
    cmd.do('select lys3, name n and resn lys within %s of (name n and resn gly)'%(delta*5))
    cmd.do('select lys4, name n and resn lys within %s of (resn gly)'%(delta*2))
    cmd.do('select lys5, name c and resn lys within %s of (resn gly)'%(delta*2))
    cmd.do('select lys6, name nz and resn lys within %s of (name od2 and resn asp)'%(delta*13))
    cmd.do('select lys7, name nz and resn lys within %s of (name ne and resn arg)'%(delta*11))
    cmd.do('select lys8, name nz and resn lys within %s of (name nh2 and resn arg)'%(delta*9.5))
    byResidue('lys', 8)
    cmd.do('select glya1, name n and resn gly within %s of (name nz and lys)'%(delta*7.5))
    cmd.do('select glya2, name ca and resn gly within %s of (name cg and lys)'%(delta*7))
    cmd.do('select glya3, name c and resn gly within %s of (name n and lys)'%(delta*2))
    cmd.do('select glya4, name n and resn gly within %s of (name nh1 and resn arg)'%(delta*10))
    byResidue('glya', 4)
    cmd.do('select glyb, name n and resn gly within %s of (name c and lys)'%(delta*2))
    cmd.select('p-loop', 'lys(glya(byres glyb))')
    cmd.do('select asp1, name od2 and resn asp within %s of (name ne and resn arg)'%(delta*5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name nh2 and resn arg)'%(delta*5))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nh1 and resn arg)'%(delta*5))
    cmd.do('select asp4, name od2 and resn asp within %s of p-loop'%(delta*15))
    byResidue('asp', 4)
    cmd.do('select aspi1, name od2 and resn asp within %s of (name nh2 and resn arg)'%(delta*5))
    cmd.do('select aspi2, name cg and resn asp within %s of (name cz and resn arg)'%(delta*6))
    cmd.do('select aspi3, name od1 and resn asp within %s of (name ne and resn arg)'%(delta*5))
    cmd.do('select aspi4, name od2 and resn asp within %s of (name od1 and asp)'%(delta*7))
    cmd.do('select aspi5, name cg and resn asp within %s of (name cg and asp)'%(delta*7))
    cmd.do('select aspi6, name od1 and resn asp within %s of (name od2 and asp)'%(delta*7))
    byResidue('aspi', 6)
    cmd.do('select arg1, name nh1 and resn arg within %s of (name od1 and aspi or name od2 and aspi)'%(delta*4.9))
    cmd.do('select arg2, name nh2 and resn arg within %s of (name od1 and aspi or name od2 and aspi)'%(delta*4.9))
    byResidue('arg', 2)
    cmd.select('adenylatekinase', 'p-loop(asp(aspi(arg)))')
    return {'motif':'Adenylatekinase'}

def citratesynth(delta):
    cmd.do('select his1, name ne2 and resn his within %s of (name og and resn ser)'%(delta*5))
    cmd.do('select his2, name ne2 and resn his within %s of (name cb and resn ser)'%(delta*5.5))
    cmd.do('select his3, name ce1 and resn his within %s of (name og and resn ser)'%(delta*5.5))
    cmd.do('select his4, name ce1 and resn his within %s of (name cb and resn ser)'%(delta*6.5))
    cmd.do('select his5, name cd2 and resn his within %s of (name og and resn ser)'%(delta*6))
    cmd.do('select his6, name nd1 and resn his within %s of (name og and resn ser)'%(delta*7))
    cmd.do('select his7, name nd1 and resn his within %s of (name od2 and resn asp)'%(delta*8))
    cmd.do('select his8, name nd1 and resn his within %s of (name cg and resn asp)'%(delta*8.5))
    cmd.do('select his9, name o and resn his within %s of (name od2 and resn asp)'%(delta*5.5))
    byResidue('his', 9)
    cmd.do('select his1, byres resn his within %s of his'%(delta*8.2))
    cmd.do('select ser1, name og and resn ser within %s of (name ne2 and his)'%(delta*5))
    cmd.do('select ser2, name cb and resn ser within %s of (name ne2 and his)'%(delta*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name ce1 and his)'%(delta*5.5))
    cmd.do('select ser4, name cb and resn ser within %s of (name ce1 and his)'%(delta*6.5))
    cmd.do('select ser5, name og and resn ser within %s of (name cd2 and his)'%(delta*6))
    cmd.do('select ser6, name og and resn ser within %s of (name nd1 and his)'%(delta*7))
    cmd.do('select ser7, name og and resn ser within %s of (name od2 and resn asp)'%(delta*12))
    cmd.do('select ser8, name og and resn ser within %s of (name cg and resn asp)'%(delta*12))
    cmd.do('select ser9, name og and resn ser within %s of (name od1 and resn asp)'%(delta*12))
    byResidue('ser', 9)
    cmd.do('select his2, byres resn his within %s of ser'%(delta*12))
    cmd.do('select asp1, name od2 and resn asp within %s of (name og and ser)'%(delta*12))
    cmd.do('select asp2, name cg and resn asp within %s of (name og and ser)'%(delta*12))
    cmd.do('select asp3, name od1 and resn asp within %s of (name og and ser)'%(delta*12))
    cmd.do('select asp4, name od2 and resn asp within %s of (name nd1 and his)'%(delta*8))
    cmd.do('select asp5, name cg and resn asp within %s of (name nd1 and his)'%(delta*8.5))
    cmd.do('select asp6, name od2 and resn asp within %s of (name o and his)'%(delta*5.5))
    byResidue('asp', 6)
    cmd.do('select his3, byres resn his within %s of asp'%(delta*8.5))
    cmd.select('his', 'byres his or (byres his1 and byres his2 and byres his3)')
    cmd.select('Citrate_Synth', 'his(asp(ser))')
    return {'motif':'Citrate_Synth'}

def tyrosinekinase(delta):
    cmd.do('select arg1, name nh1 and resn arg within %s of (name cb and resn ala)'%(delta*5))
    cmd.do('select arg2, name nh2 and resn arg within %s of (name cb and resn ala)'%(delta*5.5))
    cmd.do('select arg3, name cz and resn arg within %s of (name cb and resn ala)'%(delta*5.5))
    cmd.do('select arg4, name ne and resn arg within %s of (name cb and resn ala)'%(delta*6))
    cmd.do('select arg5, name nh2 and resn arg within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select arg6, name nh2 and resn arg within %s of (name cg and resn asp)'%(delta*5.5))
    cmd.do('select arg7, name nh2 and resn arg within %s of (name od2 and resn asp)'%(delta*6))
    cmd.do('select arg8, name cz and resn arg within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select arg9, name ne and resn arg within %s of (name od1 and resn asp)'%(delta*6))
    cmd.do('select arg10, name ne and resn arg within %s of (name cg and resn asp)'%(delta*6.5))
    byResidue('arg', 10)
    cmd.do('select asp1, name od1 and resn asp within %s of (name nh2 and resn arg)'%(delta*5.5))
    cmd.do('select asp2, name cg and resn asp within %s of (name nh2 and resn arg)'%(delta*5.5))
    cmd.do('select asp3, name od2 and resn asp within %s of (name nh2 and arg)'%(delta*7))
    cmd.do('select asp4, name od1 and resn asp within %s of (name cz and resn arg)'%(delta*6))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ne and resn arg)'%(delta*6))
    cmd.do('select asp6, name cg and resn asp within %s of (name ne and resn arg)'%(delta*6.5))
    cmd.do('select asp7, name od1 and resn asp within %s of (name cb and resn ala)'%(delta*9))
    cmd.do('select asp8, name o and resn asp within %s of (name cb and resn ala)'%(delta*8))
    cmd.do('select asp9, name cg and resn asp within %s of (name cb and resn ala)'%(delta*8))
    byResidue('asp', 9)
    cmd.do('select ala1, name cb and resn ala within %s of (name nh1 and arg)'%(delta*5))
    cmd.do('select ala2, name cb and resn ala within %s of (name nh2 and arg)'%(delta*5.5))
    cmd.do('select ala3, name cb and resn ala within %s of (name cz and arg)'%(delta*5.5))
    cmd.do('select ala4, name cb and resn ala within %s of (name ne and arg)'%(delta*6))
    cmd.do('select ala5, name cb and resn ala within %s of (name od1 and asp)'%(delta*9))
    cmd.do('select ala6, name cb and resn ala within %s of (name o and asp)'%(delta*8))
    cmd.do('select ala7, name cb and resn ala within %s of (name cg and asp)'%(delta*8))
    byResidue('ala', 7)
    cmd.select('SRC-Kinase', 'ala(asp(arg))')
    return {'motif':'SRC-Kinase'}

def hhal(delta):
    cmd.do('select glu1, name oe2 and resn glu within %s of (name sg and resn cys)'%(delta*10))
    cmd.do('select glu2, name cd and resn glu within %s of (name cb and resn cys)'%(delta*10))
    cmd.do('select glu3, name oe1 and resn glu within %s of (name ca and resn cys)'%(delta*10))
    cmd.do('select glu4, name oe2 and resn glu within %s of (name ne and resn arg)'%(delta*5))
    cmd.do('select glu5, name cd and resn glu within %s of (name cz and resn arg)'%(delta*6))
    cmd.do('select glu6, name oe1 and resn glu within %s of (name nh2 and resn arg)'%(delta*5))
    cmd.do('select glu7, name cg and resn glu within %s of (name ca and resn phe)'%(delta*10))
    cmd.do('select glu8, name cd and resn glu within %s of (name cb and resn phe)'%(delta*10))
    cmd.do('select glu9, name ca and resn glu within %s of (name cd1 and resn phe)'%(delta*7.5))
    byResidue('glu', 9)
    cmd.do('select cys1, name sg and resn cys within %s of (name nh1 and resn arg)'%(delta*6))
    cmd.do('select cys2, name cb and resn cys within %s of (name cz and resn arg)'%(delta*7))
    cmd.do('select cys3, name ca and resn cys within %s of (name nh2 and resn arg)'%(delta*8))
    cmd.do('select cys4, name sg and resn cys within %s of (name oe2 and glu)'%(delta*10))
    cmd.do('select cys5, name cb and resn cys within %s of (name cd and glu)'%(delta*10))
    cmd.do('select cys6, name ca and resn cys within %s of (name oe1 and glu)'%(delta*10))
    cmd.do('select cys7, name ca and resn cys within %s of (name ca and resn phe)'%(delta*8.5))
    cmd.do('select cys8, name cb and resn cys within %s of (name cd2 and resn phe)'%(delta*9))
    cmd.do('select cys9, name sg and resn cys within %s of (name cd1 and resn phe)'%(delta*12))
    byResidue('cys', 9)
    cmd.do('select arg1, name nh1 and resn arg within %s of (name sg and resn cys)'%(delta*6))
    cmd.do('select arg2, name cz and resn arg within %s of (name cb and resn cys)'%(delta*7))
    cmd.do('select arg3, name nh2 and resn arg within %s of (name ca and resn cys)'%(delta*8))
    cmd.do('select arg4, name ne and resn arg within %s of (name oe2 and glu)'%(delta*5))
    cmd.do('select arg5, name cz and resn arg within %s of (name cd and glu)'%(delta*6))
    cmd.do('select arg6, name nh2 and resn arg within %s of (name oe1 and glu)'%(delta*5))
    cmd.do('select arg7, name nh2 and resn arg within %s of (name ce1 and resn phe)'%(delta*10.5))
    cmd.do('select arg8, name cz and resn arg within %s of (name cz and resn phe)'%(delta*11.5))
    cmd.do('select arg9, name nh1 and resn arg within %s of (name ce2 and resn phe)'%(delta*12))
    byResidue('arg', 9)
    cmd.do('select phe1, name ca and resn phe within %s of (name cg and glu)'%(delta*10))
    cmd.do('select phe2, name cb and resn phe within %s of (name cb and glu)'%(delta*10))
    cmd.do('select phe3, name cd1 and resn phe within %s of (name ca and glu)'%(delta*7.5))
    cmd.do('select phe4, name ce1 and resn phe within %s of (name nh2 and resn arg)'%(delta*10.5))
    cmd.do('select phe5, name cz and resn phe within %s of (name cz and resn arg)'%(delta*11.5))
    cmd.do('select phe6, name ce2 and resn phe within %s of (name nh1 and resn arg)'%(delta*12))
    cmd.do('select phe7, name ca and resn phe within %s of (name ca and cys)'%(delta*8.5))
    cmd.do('select phe8, name cd2 and resn phe within %s of (name cb and cys)'%(delta*9))
    cmd.do('select phe9, name cd1 and resn phe within %s of (name sg and cys)'%(delta*12))
    byResidue('phe', 9)
    cmd.select('HHAL', 'glu(arg(phe(cys)))')
    return {'motif':'HHAL'}

def betainedehydrogenase(delta):
    cmd.do('select cys1, name sg and resn cys within %s of (name od1 and resn asn)'%(delta*8.5))
    cmd.do('select cys2, name cb and resn cys within %s of (name cg and resn asn)'%(delta*8.5))
    cmd.do('select cys3, name ca and resn cys within %s of (name nd2 and resn asn)'%(delta*7.5))
    cmd.do('select cys4, name sg and resn cys within %s of (name oe1 and resn glu)'%(delta*8))
    cmd.do('select cys5, name cb and resn cys within %s of (name cb and resn glu)'%(delta*9))
    byResidue('cys', 5)
    cmd.do('select glu1, name oe1 and resn glu within %s of (name sg and cys)'%(delta*8))
    cmd.do('select glu2, name cb and resn glu within %s of (name cb and cys)'%(delta*9))
    cmd.do('select glu3, name oe1 and resn glu within %s of (name nd2 and resn asn)'%(delta*13))
    cmd.do('select glu4, name oe2 and resn glu within %s of (name od1 and resn asn)'%(delta*14))
    byResidue('glu', 4)
    cmd.do('select asn1, name nd2 and resn asn within %s of (name oe1 and glu)'%(delta*13))
    cmd.do('select asn2, name od1 and resn asn within %s of (name oe2 and glu)'%(delta*14))
    cmd.do('select asn3, name od1 and resn asn within %s of (name sg and cys)'%(delta*8.5))
    cmd.do('select asn4, name cg and resn asn within %s of (name cb and cys)'%(delta*8.5))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ca and cys)'%(delta*8.5))
    byResidue('asn', 5)
    cmd.select('betaine_dehydrogenase', 'cys(asn(glu))')
    return {'motif':'Betaine_Dehydrogenase'}

def serotoninacetyl(delta):
    cmd.do('select his1, name ne2 and resn his within %s of (name og and resn ser)'%(delta*4.5))
    cmd.do('select his2, name ne2 and resn his within %s of (name cb and resn ser)'%(delta*5.5))
    cmd.do('select his3, name cd2 and resn his within %s of (name og and resn ser)'%(delta*5.5))
    cmd.do('select his4, name cd2 and resn his within %s of (name cb and resn ser)'%(delta*6))
    cmd.do('select his5, name ne2 and resn his within %s of (name o and resn leu)'%(delta*6))
    cmd.do('select his6, name ce1 and resn his within %s of (name cd1 and resn leu)'%(delta*10))
    cmd.do('select his7, name ce1 and resn his within %s of (name cb and resn leu)'%(delta*9))
    cmd.do('select his8, name nd1 and resn his within %s of (name og and resn ser)'%(delta*7.5))
    cmd.do('select his9, name o and resn his within %s of (name oh and resn tyr)'%(delta*10))
    cmd.do('select his10, name cb and resn his within %s of (name oh and resn tyr)'%(delta*12))
    byResidue('his', 10)
    cmd.do('select ser1, name og and resn ser within %s of (name ne2 and his)'%(delta*4.5))
    cmd.do('select ser2, name cb and resn ser within %s of (name ne2 and his)'%(delta*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name cd2 and his)'%(delta*5.5))
    cmd.do('select ser4, name cb and resn ser within %s of (name cd2 and his)'%(delta*6))
    cmd.do('select ser5, name og and resn ser within %s of (name nd1 and his)'%(delta*7.5))
    cmd.do('select ser6, name og and resn ser within %s of (name o and resn leu)'%(delta*5))
    cmd.do('select ser7, name og and resn ser within %s of (name cb and resn leu)'%(delta*8))
    cmd.do('select ser8, name cb and resn ser within %s of (name o and resn leu)'%(delta*5.5))
    cmd.do('select ser9, name n and resn ser within %s of (name cd2 and his)'%(delta*5.5))
    byResidue('ser', 9)
    cmd.do('select leu1, name o and resn leu within %s of (name ne2 and his)'%(delta*6))
    cmd.do('select leu2, name cd1 and resn leu within %s of (name ce1 and his)'%(delta*10))
    cmd.do('select leu3, name cb and resn leu within %s of (name ce1 and his)'%(delta*9))
    cmd.do('select leu4, name o and resn leu within %s of (name og and ser)'%(delta*5))
    cmd.do('select leu5, name cb and resn leu within %s of (name og and ser)'%(delta*8))
    cmd.do('select leu6, name o and resn leu within %s of (name cb and ser)'%(delta*5.5))
    cmd.do('select leu7, name n and resn leu within %s of (name ce1 and resn his)'%(delta*7.5))
    byResidue('leu', 7)
    cmd.do('select leui1, name n and resn leu within %s of (name o and his)'%(delta*7))
    cmd.do('select leui2, name n and resn leu within %s of (name c and his)'%(delta*6.5))
    cmd.do('select leui3, name n and resn leu within %s of (name n and his)'%(delta*8))
    cmd.do('select leui4, name cd1 and resn leu within %s of (name oh and resn tyr)'%(delta*6))
    cmd.do('select leui5, name cb and resn leu within %s of (name oh and resn tyr)'%(delta*5.5))
    cmd.do('select leui6, name cg and resn leu within %s of (name oh and resn tyr)'%(delta*7))
    cmd.do('select leui7, name cd1 and resn leu within %s of (name cz and resn tyr)'%(delta*6.5))
    cmd.do('select leui8, name cd1 and resn leu within %s of (name ce1 and resn tyr)'%(delta*5.5))
    byResidue('leui', 8)
    cmd.do('select tyr1, name oh and resn tyr within %s of (name cd1 and leui)'%(delta*6))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name cb and leui)'%(delta*6.5))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name cg and leui)'%(delta*7))
    cmd.do('select tyr4, name cz and resn tyr within %s of (name cd1 and leui)'%(delta*6.5))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name n and his)'%(delta*10))
    cmd.do('select tyr6, name cz and resn tyr within %s of (name c and his)'%(delta*10.2))
    cmd.do('select tyr7, name ce1 and resn tyr within %s of (name o and ser)'%(delta*16))
    byResidue('tyr', 7)
    cmd.select('Serotonin_Transferase', 'his(ser(leu(leui(tyr))))')
    return {'motif':'Serotonin_Transferase'}

#motif options
def motifoption(tag):
    if tag == 'Surface Pocket':
        surfmotifer()
    elif tag == 'Polar Contacts':
        motifcontact()
    elif tag == 'Hide Contacts':
        hidecontact()
    elif tag == 'Show Substrate':
        showsubstrate()
    elif tag == 'Show label':
        labelmotif()
    elif tag == 'Hide Label':
        dellabel()
    elif tag == 'Hide Substrate':
        hidesubstrate()

#Show binding pocket
def surfmotifer(self):
    objects = cmd.get_names('all')
    cmd.set('transparency', '0.5', 'all')
    try:
        adjacent = ''
        cmd.show('surface', 'all')
        cmd.hide('cartoon', 'all')
        if 'Adjacent' in objects:
            adjacent = ' and !Adjacent'
        if 'Peroxidase' in objects:
            cmd.color('white', '!Peroxidase%s'%(adjacent))
        if 'Carbon_Carbon' in objects:
            cmd.color('white', '!Carbon_Carbon%s'%(adjacent))
        if 'O-Glycosyl' in objects:
            cmd.color('white', '!O-Glycosyl%s'%(adjacent))
        if 'Tkinase' in objects:
            cmd.color('white', '!Tkinase%s'%(adjacent))
        if 'Ligase' in objects:
            cmd.color('white', '!Ligase%s'%(adjacent))
        if 'Glu_Amidotransferase' in objects:
            cmd.color('white', '!Glu_Amidotransferase%s'%(adjacent))
        if 'Fucose_Isomerase' in objects:
            cmd.color('white', '!Fucose_Isomerase%s'%(adjacent))
        if 'Aminotransferase' in objects:
            cmd.color('white', '!Aminotransferase%s'%(adjacent))
        if 'Zinc_finger' in objects:
            cmd.color('white', '!Zinc_finger%s'%(adjacent))
        if 'Paplike' in objects:
            cmd.color('white', '!Paplike%s'%(adjacent))
        if 'Carbonic_Anhydrase' in objects:
            cmd.color('white', '!Carbonic_Anhydrase%s'%(adjacent))
        if 'Tyrophos' in objects:
            cmd.color('white', '!Tyrophos%s'%(adjacent))
        if 'Metalloprotease' in objects:
            cmd.color('white', '!Metalloprotease%s'%(adjacent))
        if 'Superoxide' in objects:
            cmd.color('white', '!Superoxide%s'%(adjacent))
        if 'Lactamase' in objects:
            cmd.color('white', '!Lactamase%s'%(adjacent))
        if 'Serine_Protease' in objects:
            cmd.color('white', '!Serine_Protease%s'%(adjacent))
        if 'Triose_Isomerase' in objects:
            cmd.color('white', '!Triose_Isomerase%s'%(adjacent))
        if 'Alcohol_Dehyd' in objects:
            cmd.color('white', '!Alcohol_Dehyd%s'%(adjacent))
        if 'Aldose_Reductase' in objects:
            cmd.color('white', '!Aldose_Reductase%s'%(adjacent))
        if 'Cis_trans' in objects:
            cmd.color('white', '!Cis_trans%s'%(adjacent))
        if 'NAD_reductase_Asp' in objects:
            cmd.color('white', '!NAD_reductase_Asp%s'%(adjacent))
        if 'NAD_reductase_Glu' in objects:
            cmd.color('white', '!NAD_reductase_Glu%s'%(adjacent))
        if 'Deacetylase' in objects:
            cmd.color('white', '!Deacetylase%s'%(adjacent))
        if 'Chondroitinase' in objects:
            cmd.color('white', '!Chondroitinase%s'%(adjacent))
        if 'Hyaluronate_Lyase' in objects:
            cmd.color('white', '!Hyaluronate_Lyase%s'%(adjacent))
        if 'Cyclin_Kinase' in objects:
            cmd.color('white', '!Cyclin_Kinase%s'%(adjacent))
        if 'SRC-Kinase' in objects:
            cmd.color('white', '!SRC-Kinase%s'%(adjacent))
        if 'Serotonin_Transferase' in objects:
            cmd.color('white', '!Serotonin_Transferase%s'%(adjacent))
        if 'Deacetylase' in objects:
            cmd.color('white', '!Deacetylase%s'%(adjacent))
        if 'Adenylatekinase' in objects:
            cmd.color('white', '!Adenylatekinase%s'%(adjacent))
        if 'ACTase' in objects:
            cmd.color('white', '!ACTase%s'%(adjacent))
        if 'Exonuclease3' in objects:
            cmd.color('white', '!Exonuclease3%s'%(adjacent))
        if 'Citrate_Synth' in objects:
            cmd.color('white', '!Citrate_Synth%s'%(adjacent))
        if 'HHAL' in objects:
            cmd.color('white', '!HHAL%s'%(adjacent))
        cpksubstrate()
        cmd.orient('all')
    except:
        showinfo('Alert', 'You must select a motif')

#polar contacts
def motifcontact(self):
    objects = cmd.get_names('all')
    try:        
        try:
            cmd.dist(mot+"_polar_conts", mot, mot, quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable(mot+"_polar_conts")
        except:
            cmd.dist("motif_polar_conts", "motif", "motif", quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable("motif_polar_conts")
        if 'Adjacent' in objects:
            cmd.dist('Adjacent_polar_conts', 'Adjacent', 'Adjacent',
                quiet = 1, mode = 2, label = 0, reset = 1)
        if 'substrate' in objects:
            cmd.dist(mot+"_around_polar_conts", mot,
                "(byobj ("+mot+")) and (not ("+mot+"))", quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable(mot+"_around_polar_conts")
    except:
        showinfo('Alert', "Select a motif first")

def hidecontact(self):
    objects = cmd.get_names('all')
    try:
        try:
            cmd.delete(mot+"_polar_conts")
        except:
            cmd.delete("motif_polar_conts")
        if 'Adjacent' in objects:
            cmd.delete('Adjacent_polar_conts')
        if 'substrate' in objects:
            cmd.delete(mot+"_around"+"_polar_conts")
    except:
        showinfo('Alert', "No motif polar contacts to hide")

def showsubstrate(self):
    try:
        try:
            cmd.select('substrate', 'byres het within 7 of '+mot)
            objects = cmd.get_names('all')
            xp = cmd.index('substrate')
            np    = len(xp)
            if(np < 1):
                cmd.delete('substrate')
            if 'substrate' in objects:
                cmd.show('sticks', 'substrate')
                cmd.deselect()
                cpksubstrate()
        except:
            cmd.select('substrate', 'byres het within 7 of motif')
            objects = cmd.get_names('all')
            xp = cmd.index('substrate')
            np    = len(xp)
            if(np < 1):
                cmd.delete('substrate')
            if 'substrate' in objects:
                cmd.show('sticks', 'substrate')
                cmd.deselect()
                cpksubstrate()
    except:
        showinfo('Alert', "No substrate found")

def hidesubstrate(self):
    try:
        cmd.hide('sticks', 'substrate')
    except:
        showinfo('Alert', "No substrate selected")

#Labels

def dellabel(self):
    objects = cmd.get_names('all')
    try:
        try:
            cmd.label(mot, "''")
        except:
            cmd.label("motif", "''")
        if 'Adjacent' in objects:
            cmd.label('byres Adjacent', "''")
    except:
        showinfo('Alert', "No motif labels to hide")

def labelmotif(self):
    objects = cmd.get_names('all')
    try:
        try:
            cmd.label('''(name ca+C1*+C1' and (byres('''+mot+''')))''',
                '''"%s-%s"%(resn, resi)''')
        except:
            cmd.label('''(name ca+C1*+C1' and (byres(motif)))''',
                '''"%s-%s"%(resn, resi)''')
        if 'Adjacent' in objects:
            cmd.label('''(name ca+C1*+C1' and (byres(Adjacent)))''',
                '''"%s-%s"%(resn, resi)''')
    except:
        showinfo('Alert', "Select a motif first")

#bind to menu for motifs

def oxidoreductase(tag):
    if tag=='Superoxide Dismutase':
        MotifCaller('superoxide')
    elif tag=='Peroxidase':
        MotifCaller('peroxidase')
    elif tag=='Alcohol Dehydrogenase':
        MotifCaller('alcoholdehyd')
        mot= 'alcoholdehyd'
    elif tag=='Aldose Reductase':
        MotifCaller('aldosereductase')
    elif tag=='Aldose Reductase CaCb':
        MotifCaller('aldosereductaseCaCb')
    elif tag=='Aldose Reductase FA':
        MotifCaller('aldosereductaseFA')
    elif tag=='Chondroitinase CaCb':
        MotifCaller('chondroitinaseCaCb')
    elif tag=='Chondroitinase FA':
        MotifCaller('chondroitinaseFA')
    elif tag=='NAD Reductase Asp':
        MotifCaller('nadhbinderasp')
    elif tag=='NAD Reductase Glu':
        MotifCaller('nadhbinderglu')
    elif tag=='Betaine aldehyde dehydrogenase':
        MotifCaller('betainedehydrogenase')

def transferase(tag):
    if tag =='Amino Transferase':
        MotifCaller('aminotransferase')
    elif tag=='Glutamine Amidotransferase':
        MotifCaller('glutamine_amidotransferase')
    elif tag =='Thymidine Kinase':
        MotifCaller('thymidinekinase')
    elif tag =='ACTase':
        MotifCaller('ACTase')
    elif tag=='Adenylate Kinase':
        MotifCaller('adenylatekinase')
    elif tag=='SRC Family Kinase':
        MotifCaller('tyrosinekinase')
    elif tag=='Hhal Methyltransferase':
        MotifCaller('hhal')
    elif tag=='Serotonin Acetyltransferase':
        MotifCaller('serotoninacetyl')
    elif tag=='Cyclin Dependent Kinase':
        MotifCaller('cyclinkinase')

def hydrolase(tag):
    if tag =='Serine Protease':
        MotifCaller('serineprotease')
    elif tag == 'Serine Protease CaCb':
        MotifCaller('serineproteaseCaCb')
    elif tag == 'Serine Protease FA':
        MotifCaller('serineproteaseFA')
    elif tag == 'Papain Like':
        MotifCaller('paplike')
    elif tag == 'Metalloprotease':
        MotifCaller('metalloprotease')
    elif tag == 'Tyrosine Phosphatase':
        MotifCaller('tyrophos')
        mot= 'tyrophos'
    elif tag == 'Beta Lactamase':
        MotifCaller('Blactamase')
    elif tag == 'O-Glycosyl':
        MotifCaller('oglycosyl')
    elif tag == 'Cephalosporin deacetylase':
        MotifCaller('cephdeacetylase')

def lyase(tag):
    if tag =='Carbonic Anhydrase':
        MotifCaller('carbanhyd')
    elif tag=='Carbon Carbon':
        MotifCaller('carboncarbon')
    elif tag=='Chondroitinase':
        MotifCaller('chondrolyase')
    elif tag =='Hyaluronate-Lyase':
        MotifCaller('hyaluronlyase')
    elif tag=='Exonuclease 3':
        MotifCaller('exonucleaseiii')
    elif tag=='Citrate Synthase':
        MotifCaller('citratesynth')

def isomerase(tag):
    if tag =='Fucose Isomerase':
        MotifCaller('fisomerase')
    elif tag =='Triose Phosphate Isomerase':
        MotifCaller('trioseisomerase')
    elif tag=='FK506 Cis-Trans':
        MotifCaller('cistransisomerase')

def ligase(tag):
    if tag =='DNA Ligase':
        MotifCaller('dnaligase')

def other(tag):
    if tag =='Zinc Finger':
        MotifCaller('zincfinger')
      
#after appending motif to motif search field allows user to click on it
#and run the motif function

def allmotif(self):
    motif = motifbox.getcurselection()
    for item in motif:
        tag = item[2:]
    try:
        if len(tag) == 0:
            print 'No selection for double click'
        elif tag == 'Cyclin Dependent Kinase':
            motifCaller('cyclinkinase')
        elif tag == 'Betaine aldehyde dehydrogenase':
            motifCaller('betainedehydrogenase')
        elif tag == 'Serotonin Acetyltransferase':
            motifCaller('serotoninacetyl')
        elif tag == 'Zinc Finger':
            motifCaller('zincfinger')
        elif tag == 'DNA Ligase':
            motifCaller('dnaligase')
        elif tag == 'Fucose Isomerase':
            motifCaller('fisomerase')
        elif tag == 'Triose Phosphate Isomerase':
            motifCaller('trioseisomerase')
        elif tag == 'FK506 Cis-Trans':
            motifCaller('cistransisomerase')
        elif tag == 'Carbonic Anhydrase':
            motifCaller('carbanhyd')
        elif tag == 'Carbon Carbon':
            motifCaller('carboncarbon')
        elif tag == 'Chondroitinase':
            motifCaller('chondrolyase')
        elif tag == 'Hyaluronate-Lyase':
            motifCaller('hyaluronlyase')
        elif tag == 'Exonuclease 3':
            motifCaller('exonucleaseiii')
        elif tag == 'Citrate Synthase':
            motifCaller('citratesynth')
        elif tag == 'Serine Protease':
            motifCaller('serineprotease')
        elif tag == 'Papain Like':
            motifCaller('paplike')
        elif tag == 'Metalloprotease':
            motifCaller('metalloprotease')
        elif tag == 'Tyrosine Phosphatase':
            motifCaller('tyrophos')
        elif tag == 'Beta Lactamase':
            motifCaller('Blactamase')
        elif tag == 'O-Glycosyl':
            motifCaller('oglycosyl')
        elif tag == 'Cephalosporin deacetylase':
            motifCaller('cephdeacetylase')
        elif tag == 'Amino Transferase':
            motifCaller('aminotransferase')
        elif tag == 'Glutamine Amidotransferase':
            motifCaller('glutamine_amidotransferase')
        elif tag == 'Thymidine Kinase':
            motifCaller('thymidinekinase')
        elif tag == 'ACTase':
            motifCaller('ACTase')
        elif tag == 'Adenylate Kinase':
            motifCaller('adenylatekinase')
        elif tag == 'SRC Family Kinase':
            motifCaller('tyrosinekinase')
        elif tag == 'Hhal Methyltransferase':
            motifCaller('hhal')
        elif tag == 'Superoxide Dismutase':
            motifCaller('superoxide')
        elif tag == 'Peroxidase':
            motifCaller('peroxidase')
        elif tag == 'Alcohol Dehydrogenase':
            motifCaller('alcoholdehyd')
        elif tag == 'Aldose Reductase':
            motifCaller('aldosereductase')
        elif tag == 'NAD Reductase':
            motifCaller('nadhbinder')
        elif tag == 'NAD Reductase2':
            motifCaller('nadhbinder2')
    except:
        showinfo('Alert', 'There is no motif there')

#def custom motif dropdown selection

def set_motifA(tag):
    cmd.deselect()
    mA = tag

def set_motifB(tag):
    cmd.deselect()
    mB = tag

def set_motifC(tag):
    cmd.deselect()
    mC = tag

def set_motifD(tag):
    cmd.deselect()
    mD = tag
 
 #def custom motif dropdown selection
def set_motifAA(tag):
    cmd.deselect()
    mAA = tag

def set_motifAB(tag):
    cmd.deselect()
    mAB = tag

def set_motifAC(tag):
    cmd.deselect()
    mAC = tag

def set_motifAD(tag):
    cmd.deselect()
    mAD = tag

#Custom motif functions


def bimotif(self):
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mA = mA
        mB = mB
        cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.select('motif', 'byres AA | byres BB')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
    except:
        showinfo('Alert', 'You must select an amino acid for menus A and B')

def trimotif(self):
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mA = mA
        mB = mB
        mC = mC
        cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.do('sel CC, resn %s within %s of resn %s'%(mC, selB.get(), mB))
        cmd.select('motif', 'byres AA | byres BB | byres CC')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
    except:
        showinfo('Alert',
            'You must select an amino acid for menus A, B, and C')

def quadmotif(self):
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mA = mA
        mB = mB
        mC = mC
        mD = mD
        cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.do('sel CC, resn %s within %s of resn %s'%(mC, selB.get(), mB))
        cmd.do('sel DD, resn %s within %s of resn %s'%(mD, selC.get(), mC))
        cmd.select('motif', 'byres AA | byres BB | byres CC')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
        cmd.delete('DD')
    except:
        showinfo('Alert',
            'You must select an amino acid for menus A, B, C, and D')

def Abimotif(self):
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mAA = mAA
        mAB = mAB
        cmd.do('sel AA, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('motif', 'byres AA | byres BB')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
    except:
        showinfo('Alert', 'You must select an amino acid for menus A and B')

def Atrimotif(self):
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mAA = mAA
        mAB = mAB
        mAC = mAC
        cmd.do('sel AA1, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
        cmd.select('AA', 'byres AA1 and byres AA2')
        cmd.do('sel BB1, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
        cmd.select('BB', 'byres BB1 and byres BB2')
        cmd.do('sel CC1, resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
        cmd.select('CC2', 'resn %s within %s of resn %s'%(mAC, selAC.get(), mAA))
        cmd.select('CC', 'byres CC1 and byres CC2')
        cmd.select('motif', 'byres AA | byres BB | byres CC')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
    except:
        showinfo('Alert',
            'You must select an amino acid for menus A, B, and C')

def Aquadmotif(self):
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mAA = mAA
        mAB = mAB
        mAC = mAC
        mAD = mAD
        cmd.do('sel AA1, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
        cmd.select('AA3', 'resn %s within %s of resn %s'%(mAA, selAD.get(), mAD))
        cmd.select('AA', 'byres AA1 and byres AA2 and byres AA3')
        cmd.do('sel BB1, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
        cmd.select('BB3', 'resn %s within %s of resn %s'%(mAB, selBD.get(), mAD))
        cmd.select('BB', 'byres BB1 and byres BB2 and byres BB3')
        cmd.do('sel CC1, resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
        cmd.select('CC2', 'resn %s within %s of resn %s'%(mAC, selAC.get(), mAA))
        cmd.select('CC3', 'resn %s within %s of resn %s'%(mAC, selCD.get(), mAD))
        cmd.select('CC', 'byres CC1 and byres CC2 and byres CC3')
        cmd.do('sel DD1, resn %s within %s of resn %s'%(mAD, selAD.get(), mAA))
        cmd.select('DD2', 'resn %s within %s of resn %s'%(mAD, selBD.get(), mAB))
        cmd.select('DD3', 'resn %s within %s of resn %s'%(mAD, selCD.get(), mAC))
        cmd.select('DD', 'byres DD1 and byres DD2 and byres DD3')
        cmd.select('motif', 'byres AA | byres BB | byres CC | byres DD')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
        cmd.delete('DD')
    except:
        showinfo('Alert', 'You must select an amino acid for menus A, B, C, and D')

#reset the range sliders
def resetmotif(self):
    selA.set(4.0)
    selB.set(4.0)
    selC.set(4.0)
    selAB.set(4.0)
    selAC.set(4.0)
    selAD.set(4.0)
    selBC.set(4.0)
    selBD.set(4.0)
    selCD.set(4.0)

def resetrange(self):
    range.set(1.0)

def setcusmotif(self):
    a = []
    for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
        a.append(object)
    motifdrop.setlist(a)

def runcusmotif(self):
        a = ['']
        for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
            a.append(object)
        motif = motifdrop.getcurselection()
        for item in motif:
            tag = item
        try:
             for i in range(1, 100, 1):
                if a[i] in tag:
                    cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[i])
        except:
            pass
            
def motifchecker(event):
    def ModBounds(x, exact, upper=None, lower=None):
        if x % exact === 0:
            return '1'
        elif upper != None and lower != None:
            while x > lower:
                if x < upper:
                    return '2'
        return False

    cmd.hide('everything', 'all')
    cmd.remove("(all) and hydro")
    list=[]

    MotifCaller('exonucleaseiii')
    x = ModBounds(cmd.count_atoms('Exonuclease3'),42,42,32)
    if x != False: 
       list.append('%s-Exonuclease 3'%(x))
    cmd.delete('Exonuclease3')

    MotifCaller('cyclinkinase')
    x = ModBounds(cmd.count_atoms('Cyclin_Kinase'),26,35,23)
    if x != False:
      list.append('%s-Cyclin Dependent Kinase'%(x))
    cmd.delete('Cyclin_Kinase')

    MotifCaller('citratesynth')
    x = ModBounds(cmd.count_atoms('Citrate_Synth'),34,34,28)
    if x != False:
       list.append('%s-Citrate Synthase'%(x))
    cmd.delete('Citrate_Synth')

    MotifCaller('trioseisomerase')
    x = ModBounds(cmd.count_atoms('Triose_Isomerase'),40,45,32)
    if x != False:
       list.append('%s-Triose Phosphate Isomerase'%(x))
    cmd.delete('Triose_Isomerase')

    MotifCaller('serineprotease')
    x = ModBounds(cmd.count_atoms('Serine_Protease'),24,33,18)
    if x != False:
       list.append('%s-Serine Protease'%(x))
    cmd.delete('Serine_Protease')

    MotifCaller('Blactamase')
    x = ModBounds(cmd.count_atoms('Lactamase'),45,55,35)
    if x != False:
       list.append('%s-Beta Lactamase'%(x))
    cmd.delete('Lactamase')

    cmd.select('zn', 'elem zn(elem cu)')
    x = cmd.count_atoms('zn')
    if x > 2:
        MotifCaller('superoxide')
        x = cmd.count_atoms('Superoxide')
        if x != False:
           list.append('%s-Superoxide Dismutase'%(x))
        cmd.delete('Superoxide')
    cmd.delete('zn')

    cmd.select('zn', 'elem zn')
    x = cmd.count_atoms('zn')
    if x > 1:
        MotifCaller('zincfinger')
        x = ModBounds(cmd.count_atoms('Zinc_finger'),32,50,20)
        if x != False:
           list.append('%s-Zinc Finger'%(x))
        cmd.delete('Zince_finger')
    cmd.delete('zn')

    MotifCaller('aminotransferase')
    x = ModBounds(cmd.count_atoms('Aminotransferase'),27,40,20)
    if x != False:
       list.append('%s-Amino Transferase'%(x))
    cmd.delete('Aminotransferase')

    MotifCaller('chondrolyase')
    x = ModBounds(cmd.count_atoms('Chondroitinase'),41,51,31)
    if x != False:
       list.append('%s-Chondroitinase'%(x))
    cmd.delete('Chonroitinase')

    MotifCaller('hyaluronlyase')
    x = ModBounds(cmd.count_atoms('Hyaluronate_Lyase'),41,51,31)
    if x != False:
       list.append('%s-Hyaluronate-Lyase'%(x))
    cmd.delete('Hyaluronate_Lyase')

    MotifCaller('peroxidase')
    x = ModBounds(cmd.count_atoms('Peroxidase'),29,39,19)
    if x != False:
       list.append('%s-Peroxidase'%(x))
    cmd.delete('Peroxidase')

    MotifCaller('nadhbinderasp')
    x = ModBounds(cmd.count_atoms('NAD_reductase_Asp'),20,27,16)
    if x != False:
       list.append('%s-NAD Reductase Asp'%(x))
    cmd.delete('NAD_reductase_Asp')

    MotifCaller('nadhbinderglu')
    x = ModBounds(cmd.count_atoms('NAD_reductase_Glu'),21,28,17)
    if x != False:
       list.append('%s-NAD Reductase Glu')
    cmd.delete('NAD_reductase_Glu')

    MotifCaller('tyrosinekinase')
    x = ModBounds(cmd.count_atoms('SRC-Kinase'),24,30,16)
    if x != False:
       list.append('%s-SRC Family Kinase'%(x))
    cmd.delete('SRC-Kinase')

    MotifCaller('cistransisomerase')
    x = ModBounds(cmd.count_atoms('Cis-trans'),36,46,26)
    if x != False:
       list.append('%s-FK506 Cis-Trans'%(x))
    cmd.delete('Cis-trans')

    MotifCaller('cephdeacetylase')
    x = ModBounds(cmd.count_atoms('Deacetylase'),32,42,26)
    if x != False:
       list.append('%s-Cephalosporin deacetylase'%(x))
    cmd.delete('Deacetylase')

    MotifCaller('paplike')
    x = ModBounds(cmd.count_atoms('paplike'),25,33,17)
    if x != False:
      list.append('%s-Papain Like'%(x))
    cmd.delete('paplike')

    MotifCaller('hhal')
    x = ModBounds(cmd.count_atoms('hhal'),37,47,27)
    if x != False:
      list.append('%s-Hhal Methyltransferase'%(x))
    cmd.delete('hhal')

    MotifCaller('ACTase')
    x = ModBounds(cmd.count_atoms('actase'),
    if x == 140:
      list.append('1-ACTase')
    if x < 150 and x > 140:
      list.append('2-ACTase')
    if x < 140 and x > 130:
      list.append('2-ACTase')
    if x == 140*2:
      list.append('1-ACTase')
    if x < 150*2 and x > 140*2:
      list.append('2-ACTase')
    if x < 140*2 and x > 130*2:
      list.append('2-ACTase')
    if x == 140*3:
      list.append('1-ACTase')
    if x < 150*3 and x > 140*3:
      list.append('2-ACTase')
    if x < 140*3 and x > 130*3:
      list.append('2-ACTase')
    if x == 140*4:
      list.append('1-ACTase')
    if x < 150*4 and x > 140*4:
      list.append('2-ACTase')
    if x < 140*4 and x > 130*4:
      list.append('2-ACTase')
    cmd.delete('actase')

    MotifCaller('alcoholdehyd')
    x = ModBounds(cmd.count_atoms('Alcohol_Dehyd'),35,45,25)
    if x != False:
      list.append('%s-Alcohol Dehydrogenase'%(x))
    cmd.delete('Alcohol_Dehyd')

    MotifCaller('adenylatekinase')
    x = ModBounds(cmd.count_atoms('adenylatekinase'),66,76,56)
    if x != False:
      list.append('%s-Adenylate Kinase'%(x))
    cmd.delete('adenylatekinase')

    MotifCaller('aldosereductase')
    x = ModBounds(cmd.count_atoms('Aldose_Reductase'),39,49,29)
    if x != False:
      list.append('%s-Aldose Reductase'%(x))
    cmd.delete('Aldose_Reductase')

    MotifCaller('glutamine_amidotransferase')
    x = ModBounds(cmd.count_atoms('Glu_Amidotransferase'),25,33,17)
    if x != False:
      list.append('%s-Glutamine Amidotransferase'%(x))
    cmd.delete('Glu_Amidotransferase')

    MotifCaller('carboncarbon')
    x = ModBuonds(cmd.count_atoms('Carbon_Carbon'),25,33,17)
    if x != False:
      list.append('%s-Carbon Carbon'%(x))
    cmd.delete('carboncarbon')

    MotifCaller('carbanhyd')
    x = ModBounds(cmd.count_atoms('Carbonic_Anhydrase'),32,42,22)
    if x != False:
      list.append('%s-Carbonic Anhydrase'%(x))
    cmd.delete('Carbonic_Anhydrase')

    MotifCaller('fisomerase')
    x = ModBounds(cmd.count_atoms('Fucose_Isomerase'),19,24,14)
    if x != False:
      list.append('%s-Fucose Isomerase'%(x))
    cmd.delete('Fucose_Isomerase')

    MotifCaller('tyrophos')
    x = ModBounds(cmd.count_atoms('Tyrophos'),31,41,21)
    if x != False:
      list.append('%s-Tyrosine Phosphatase'%(x))
    cmd.delete('Tyrophos')

    MotifCaller('betainedehydrogenase')
    x = ModBounds(cmd.count_atoms('Betaine_Dehydrogenase'),23,26,20)
    if x != False:
      list.append('%s-Betaine aldehyde dehydrogenase'%(x))
    cmd.delete('Betaine_Dehydrogenase')

    MotifCaller('serotoninacetyl')
    x = ModBounds(cmd.count_atoms('Serotonin_transferase'),44,44,32)
    if x == 44:
       list.append('1-Serotonin Acetyltransferase')
    if x < 44 and x > 32:
       list.append('2-Serotonin Acetyltransferase')
    if x == 24:
       list.append('1-Serotonin Acetyltransferase')
    if x == 44*2:
       list.append('1-Serotonin Acetyltransferase')
    if x < 44*2 and x > 32*2:
       list.append('2-Serotonin Acetyltransferase')
    if x == 24*2:
       list.append('1-Serotonin Acetyltransferase')
    if x == 44*3:
       list.append('1-Serotonin Acetyltransferase')
    if x < 44*3 and x > 32*3:
       list.append('2-Serotonin Acetyltransferase')
    if x == 24*3:
       list.append('1-Serotonin Acetyltransferase')
    if x == 44*4:
       list.append('1-Serotonin Acetyltransferase')
    if x < 44*4 and x > 32*4:
       list.append('2-Serotonin Acetyltransferase')
    if x == 24*4:
       list.append('1-Serotonin Acetyltransferase')

    cmd.delete('tyrophos')
    deletemotif()
    cmd.orient('all')
    list.sort()
    motifbox.setlist(list)
    cmd.show('cartoon', 'all')
    cmd.color('grey', 'all')
    return list
    
def resdel(event):
    try:
        objects = cmd.get_names('all')
        cmd.hide('sticks', '!'+mot)
        cmd.color('white', '!'+mot)
        if 'Adjacent' in objects:
            cmd.delete('Adjacent_polar_conts')
        if 'Adjacent' in objects:
            cmd.label('byres Adjacent',"''")
        cmd.delete('Adjacent')
    except:

        showinfo('Alert', 'You must load a motif first')
        interior.mainloop()

def roundres(event):
    try:
        cmd.hide('sticks', '!'+mot)
        cmd.color('white', '!'+mot)
        cmd.select('Adjacent', 'byres '+mot+' around %s'%(selA.get()))
        cmd.show('sticks', 'Adjacent')
        cmd.color('orange', 'Adjacent')
        util.cnc('Adjacent')
        cmd.remove('hydro')
        cmd.deselect()
    except:
        
        showinfo('Alert', 'You must load a motif first')
        interior.mainloop()

def randomized(*args):
    cmd.delete('all')
    pdbCode = linecache.getline('./modules/pmg_tk/startup/pdb_entry_type.txt',random.randint(1, 41258))
    
    pdbCode = string.upper(pdbCode)
    try:
        filename = urllib.urlretrieve('http://www.rcsb.org/pdb/cgi/export.cgi/' +
                                                pdbCode + '.pdb.gz?format=PDB&pdbId=' +
                                                pdbCode + '&compression=gz')[0]
    except:
        showerror('Connection Error',
                               'Can not access to the PDB database.\n'+
                               'Please check your Internet access.',
                               parent=app.root)
    else:
        if (os.path.getsize(filename) > 0): # If 0, then pdb code was invalid
            # Uncompress the file while reading
            fpin = gzip.open(filename)
            
            # Form the pdb output name
            outputname = os.path.dirname(filename) + os.sep + pdbCode + '.pdb'
            fpout = open(outputname, 'w')
            fpout.write(fpin.read()) # Write pdb file
            
            fpin.close()
            fpout.close()
            
            cmd.load(outputname,quiet=0) # Load the fresh pdb
        else:
            showerror('Invalid Code',
                                          'You entered an invalid pdb code:' + pdbCode,
                                          parent=app.root)
        
        os.remove(filename) # Remove tmp file (leave the pdb)

cmd.extend('randomized',randomized)

def runum():#run all the motifs and count the atoms n the Motifs folder
        
        a = ['']
        entz.delete(0,1000)
        entz.insert(0,0)
        for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
            a.append(object)
        skipping =True
        list  = []
        while skipping:
            
            z = int(entz.get()) + 1
            entz.delete(0,1000)
            entz.insert(0,z)
            try:
                cmd.set("suspend_updates",1,quiet=1)
                time.sleep(1)#rate limiter
                cmd.delete('Motif')
                cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[z])
                cmd.set("suspend_updates",0,quiet=1)
                time.sleep(1)#rate limiter
                
                r = cmd.count_atoms('Motif')
                entcount.delete(0,100)
                entcount.insert(0,r)
                
                
                time.sleep(1)
                if len(entcount.get())==1:
                       list.append(entcount.get()+'        '+a[z])
                if len(entcount.get())==2:
                       list.append(entcount.get()+'       '+a[z])
                if len(entcount.get())==3:
                       list.append(entcount.get()+'      '+a[z])
            
            
            except:
                cmd.set("suspend_updates",0,quiet=1)
                skipping = False
                motifdrop.setlist(list)
                list.sort()

def loadmotifer():
    try:
        ###mRN = motif resn number aka number of residues in motif
        premRN = askstring('Motif Maker','How many residues are in your motif?\n'
                                          +'Please enter a number >= 2 and <=10.\n')
        if premRN == None:
            raise Exception
        else:
            mRN = int(premRN)
        if mRN < 2 or mRN > 10:
            raise ValueError
        
        def populate_chain_list():
            items=[]
            items.append('')
            for letter in pglob.AlphaSequence:
                if cmd.count_atoms("chain "+letter) > 0:
                    items.append(letter)
            items.sort()
            for i in range(1,mRN+1):
                chain[i].setitems(items)
        
        def makemotif():
            try:
                exception = False
                excepLoop = 0
                exceptions = ''
                skip = {}
                skip[0] = 0
                for i in range(1,mRN+1):
                    skip[i] = False
                    if resn[i].getvalue() == '' and resi[i].get() != '':
                        exception = True
                        exceptions += 'Please enter a residue for residue %s\n'%(i)
                    elif resn[i].getvalue() != '' and resi[i].get() == '':
                        exception = True
                        exceptions += 'Please enter a number for residue %s\n'%(i)
                    elif resn[i].getvalue() == '' and resi[i].get() == '':
                        ### this gives us the ability to skip whole blocks
                        skip[i] = True
                        skip[0] += 1
                    else:
                        excepLoop +=1
                        if chain[i].getvalue() == '':
                            exception = True
                            exceptions += 'Please select a chain for residue %s\n.'%(i)
                        elif resn[i].getvalue() == "gly" and backbone[i].getvalue() == "Off":
                            exception = True
                            exceptions += 'Please turn on the backbone for glycine residue %s\n'%(i)
                        elif cmd.count_atoms(chain[i].getvalue()+'/'+resn[i].getvalue()+'`'+resi[i].get()+'/') == 0:
                            exception = True
                            exceptions += 'There is no '+resn[i].getvalue()+' at number '+resi[i].get()+' on chain '+chain[i].getvalue()+'.\n'
                if excepLoop < 2:
                    exception = True
                    exceptions += 'Motifs require that 2 or more residues be entered.'
                if exception == True:
                    
                    showinfo('Error', 'The following errors have occurred:\n'+exceptions)
                    interior.mainloop()
                else:
                    cmd.remove('resn HOH')
                    
                    Q = asksaveasfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
                    if Q == None:
                        interior.mainloop()
                    f=open(Q, 'w')
                    f.write("######################################################################\n")
                    f.write("### This motif uses shortened selection algebra and property selectors\n")
                    f.write("### + = and\n")
                    f.write("### w. = within\n")
                    f.write("### br. = byres\n")
                    f.write("### r. = resn\n")
                    f.write("### n. = name\n")
                    f.write("### e. = elem\n")
                    f.write("######################################################################\n")
                    atomlist = {}
                    ### backbone off aka just side chains from beta carbon onwards
                    atomlist[0] = {'ala':('CB'),
                                   'arg':('CB','CG','CD','NE','CZ','NH1','NH2'),
                                   'asn':('CB','CG','OD1','ND2'),
                                   'asp':('CB','CG','OD1','OD2'),
                                   'cys':('CB','SG'),
                                   'gln':('CB','CG','CD','OE1','NE2'),
                                   'glu':('CB','CG','CD','OE1','OE2'),
                                   'gly':(),
                                   'his':('CB','CG','ND1','CD2','CE1','NE2'),
                                   'ile':('CB','CG1','CG2','CD'),
                                   'leu':('CB','CG','CD1','CD2'),
                                   'lys':('CB','CG','CD','CE','NZ'),
                                   'met':('CB','CG','SD','CE'),
                                   'phe':('CB','CG','CD1','CD2','CE1','CE2','CZ'),
                                   'pro':('CB','CG','CD'),
                                   'ser':('CB','OG'),
                                   'thr':('CB','OG1','CG2'),
                                   'trp':('CB','CG','CD1','CD2','NE1','CE2','CE3','CZ2','CZ3','CH2'),
                                   'tyr':('CB','CG','CD1','CD2','CE1','CE2','CZ','OH'),
                                   'val':('CB','CG1','CG2')}
                    atomlist[1] = ('O','C','CA','N')### backbone on
                    resnlist = ['']### residue list
                    resnlistf = ['']### residue list with appended 'i', making them unique
                    resilist = ['']### residue id list. Based on sequence number.
                    chainlist = ['']### chain list
                    bonelist = ['']### backbone list
                    
                    numOfi = 0
                    for i in range(1,mRN+1):
                        if skip[i] == False:
                            resnlist.append(resn[i].getvalue())
                            resilist.append(resi[i].get())
                            resnlistf.append(resn[i].getvalue()+('i'*(numOfi)))
                            chainlist.append(chain[i].getvalue())
                            bonelist.append(backbone[i].getvalue())
                            numOfi += 1
                    
                    ### This loop will increment through the amino acids. The amino acid we are looking
                    ### at right now is specified by the e variable. The a variable will count the
                    ### number of times it is compared to the carbons in the other amino acids. And is
                    ### used later on to print the "byres" and select line, and delete line below.
                    ### NOTE:
                    ### Because we are able to skip a whole block, mRN is not used beyond this point,
                    ### instead resnlen is used as it gives a more accurate picture of the motif.
                    resnlen = (len(resnlist)-1)
                    e = 0
                    while e < resnlen:
                        try:
                            try:
                                a = 0
                                e += 1
                                ### select stuff explained later on
                                selectlimit = 200
                                selectstart = 1 ### where to start selection
                                selectlimiter = 1 ### limit defined as a/200
                                selectextra = '' ### add to selection at the end
                                deleteextra = '' ### add to deletion at the end
                                
                                if bonelist[e] == 'Off':###just sidechains
                                    bList=atomlist[0][resnlist[e]]
                                else:### sidechain with backbone
                                    bList=atomlist[0][resnlist[e]]+atomlist[1]
                                
                                ### This loop will increment through the amino acids that we want
                                ### to compare to the amino acid we want to find. The amino acid
                                ### being compared is specified by the d variable.
                                d = 0
                                while d < resnlen:
                                    try:
                                        d += 1
                                        ### The following line: compare amino acids
                                        ### If they are the same, then lets increment one.
                                        if resnlistf[e] == resnlistf[d]:
                                            d += 1
                                            if d > resnlen:
                                                continue
                                        
                                        if bonelist[d] == 'Off':###just sidechains
                                            cList=atomlist[0][resnlist[d]]
                                        else:### sidechain with backbone
                                            cList=atomlist[0][resnlist[d]]+atomlist[1]
                                        
                                        ### This loop increments through all the carbons
                                        ### in the amino acid we want to find.
                                        blen = (len(bList)-1)
                                        clen = (len(cList)-1)
                                        b = -1
                                        while b < blen:
                                            b += 1
                                            ### This loop increments through all the carbons
                                            ### in the other amino acids that we are want to
                                            ### compare with.
                                            c = -1
                                            while c < clen:
                                                try:
                                                    c += 1
                                                    
                                                    ### Okay lets get the distance between our atoms in our selected amino acids.
                                                    r = cmd.get_distance(chainlist[e]+'/'+resilist[e]+'/'+bList[b],chainlist[d]+'/'+resilist[d]+'/'+cList[c])
                                                    ### The precision factor
                                                    ### The ranger is the slider that is moved.
                                                    ### r is set by the get_distance above.
                                                    g = '%.2f' %(float(r) + float(ranger1.get()))
                                                    
                                                    a += 1
                                                    
                                                    ### apparently pymol cannot handle over a number
                                                    ### between 248 and 264 selections at one time.
                                                    ### This fixes that by making sure we do not pass
                                                    ### "selectlimit" selections at one time.
                                                    if float(selectlimiter) < (float(a)/float(selectlimit)):
                                                        f.write("cmd.select('"+resnlistf[e]+str(selectlimiter*selectlimit)+"','")
                                                        for i in range(selectstart,a):
                                                            if i==(a-1):
                                                                f.write("br. "+resnlistf[e]+str(i)+"')\n")
                                                            else:
                                                                f.write("br. "+resnlistf[e]+str(i)+" and ")
                                                        f.write("cmd.delete('")
                                                        for i in range(selectstart,a):
                                                            if i==(a-1):
                                                                pass
                                                            elif i==(a-2):
                                                                f.write(resnlistf[e]+str(i)+"')\n")
                                                            else:
                                                                f.write(resnlistf[e]+str(i)+"+")
                                                        selectextra += ''+resnlistf[e]+str(selectlimiter*selectlimit)+' and '
                                                        deleteextra += ''+resnlistf[e]+str(selectlimiter*selectlimit)+'+'
                                                        selectlimiter += 1
                                                        selectstart += selectlimit
                                                    
                                                    ### e > d is all the combinations of residues
                                                    ### that would already have one of the residues
                                                    ### found in the motif, therefore the second
                                                    ### amino acid does not need an r. (resn)
                                                    ### property selection, as it is already a selection.
                                                    if e > d:
                                                        f.write( 'cmd.select("'+resnlistf[e]+''+str(a)+'", "n. '+bList[b]+' and r. '+resnlist[e]+' w. %s of n. '+cList[c]+' and '+resnlistf[d]+'"%('+g+'))\n')
                                                        continue
                                                    else:
                                                       f.write( 'cmd.select("'+resnlistf[e]+''+str(a)+'", "n. '+bList[b]+' and r. '+resnlist[e]+' w. %s of n. '+cList[c]+' and r. '+resnlist[d]+'"%('+g+'))\n')
                                                       continue
                                                except:
                                                    pass
                                    except:
                                        pass
                            except:
                                pass
                        finally:
                            f.write('cmd.select("'+resnlistf[e]+'","')
                            if selectextra != '':
                                f.write(selectextra)
                            for i in range(selectstart,a+1):
                                if i==a:
                                    f.write('br. '+resnlistf[e]+str(i)+'")\n')
                                else:
                                    f.write('br. '+resnlistf[e]+str(i)+' and ')
                            f.write('cmd.delete("')
                            if deleteextra != '':
                                f.write(deleteextra)
                            for i in range(selectstart,a+1):
                                if i==a:
                                    f.write(resnlistf[e]+str(i)+'")\n')
                                else:
                                    f.write(resnlistf[e]+str(i)+'+')
                
                resnlistfstr = ""
                for i in range(1,resnlen+1):
                    if i == resnlen:
                        resnlistfstr += resnlistf[i]
                    else:
                        resnlistfstr += resnlistf[i]+'+'
                
                f.write("cmd.select('Motif','"+resnlistfstr+"')\n")
                f.write("cmd.delete('"+resnlistfstr+"')\n")
                f.write('cmd.hide("everything","all")\n')
                f.write('cmd.show("cartoon", "all")\n')
                f.write('cmd.set("cartoon_transparency","0.5", "all")\n')
                f.write('cmd.show("sticks","Motif")\n')
                f.write('cmd.color("grey","all")\n')
                f.write('cmd.color("oxygen","(e. O+Motif)")\n')
                f.write('cmd.color("nitrogen","(e. N+Motif)")\n')
                f.write('cmd.color("sulfur","(e. S+Motif)")\n')
                f.write('cmd.color("hydrogen","(e. H+Motif)")\n')
                f.write('cmd.color("white","(e. C+Motif)")\n')
                f.write('cmd.deselect()\n')
                f.write('cmd.orient("Motif")\n')
                
                print '\n\n\n\n\n\nMotif Maker\nBy: Brett Hanson and Charlie Westin\n2007\nImproved by: Mario Rosa\n2009\n%s Amino Acid Motif Written \n\n\n\n'%(len(resnlist)-1)
                f.close()
                interior.mainloop()
            except:
                pass
        
        root = tk.Tk()
        root.title('Motif Maker')
        group = Pmw.Group(root, tag_text='Motif Maker')#And a new group
        group.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky = tk.NW)
        interior = group.interior()
        
        resn = {}
        for i in range(1,mRN+1):
            resn[i] = Pmw.OptionMenu(interior,labelpos = tk.W,
                                        label_text = 'Residue %s:'%(i),
                                        items = pglob.AminoMenuList,
                                        menubutton_width = 8)
            resn[i].grid(row = (i-1), column =0)
        
        lent = {}
        for i in range(1,mRN+1):
            lent[i] = tk.Label(interior, text = 'Number:')
            lent[i].grid(row = (i-1), column = 1)
        
        resi = {}
        for i in range(1,mRN+1):
            resi[i] = tk.Entry(interior, width = 8)
            resi[i].grid(row = (i-1), column = 2)
        
        backbone = {}
        for i in range(1,mRN+1):
            backbone[i] = Pmw.OptionMenu(interior,labelpos = tk.W,
                                         label_text = 'BackBone:',
                                         items = ('Off', 'On'),
                                         menubutton_width = 8)
            backbone[i].grid(row = (i-1), column = 3)
        
        chain = {}
        for i in range(1,mRN+1):
            chain[i] = Pmw.OptionMenu(interior,labelpos =  tk.W,
                                          label_text = 'Chain %s:'%(i),
                                          items = (''),
                                          menubutton_width = 8)
            chain[i].grid(row=(i-1), column=4)
        
        but1 = tk.Button(interior, text = 'Make Motif', width = 10, command = makemotif)
        but1.grid(row =mRN, column = 3, sticky = tk.SE)
        
        popbtn = tk.Button(interior, text = 'Chain Info', width = 10, command = populate_chain_list)
        popbtn.grid(row = mRN, column = 4, sticky = tk.SE)
        
        framerange = tk.Frame(interior)
        framerange.grid(row=mRN, column=0,columnspan = 3, sticky = tk.E)
        ballrange = Pmw.Balloon(interior)
        ballrange.bind(framerange, 'Changes Precision of Motif Definition\nDefault = 2')
        ranger1 = tk.Scale(framerange, width =8,
                        troughcolor="#ffffff",
                        length="160",
                        orient="horizontal",
                        resolution="0.1",
                        to="4.0")
        ranger1.grid(row=5, column=1,columnspan = 4, sticky = tk.E)
        ranger1.set(2)
        
        labrange = tk.Label(interior, text='Precision Factor:')
        labrange.grid(row=mRN, column=0, sticky = tk.SW)
        
        group = Pmw.Group(root, tag_text = 'Run Motif')
        group.grid(row=1, column=1, padx=2, pady=2, sticky = tk.W)
        interior = group.interior()
        
        def getmotif():
            
            f = askopenfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
            if f == None:
                interior.mainloop()
            else:
                cmd.do('run '+f+'')
                interior.mainloop()
        openbtn = tk.Button(interior, text= 'Open Motif', command = getmotif)
        openbtn.grid()
    
    #---------------------Show residues around active site---------------#
        def motifoption(tag):
                if tag=='Surface Pocket':
                    objects = cmd.get_names('all')
                    cmd.set('transparency', '0.5', 'all')
                    if 'Motif' in objects:
                        cmd.show('surface', 'all')
                        cmd.hide('cartoon', 'all')
                        cmd.color('white', '!Motif ')
                elif tag=='Polar Contacts':
                        try:
                            objects = cmd.get_names('all')
                            cmd.dist("Motif_polar_conts","Motif","Motif",quiet=1,mode=2,label=0,reset=1)
                            cmd.enable(mot+"_polar_conts")
                        except:
                            pass
                        
                        if 'Adjacent' in objects:
                            cmd.dist('Adjacent_polar_conts','Adjacent','Adjacent',quiet=1,mode=2,label=0,reset=1)
                        if 'substrate' in objects:
                            cmd.dist("Motif_around_polar_conts","Motif","(byobj (Motif)) and (not (Motif))",quiet=1,mode=2,label=0,reset=1)
                            cmd.enable("Motif_around_polar_conts")
                elif tag=='Hide Contacts':
                    objects = cmd.get_names('all')
                    try:
                          try:
                            cmd.delete("Motif_polar_conts")
                          except:
                            pass
                          if 'Adjacent' in objects:
                            cmd.delete('Adjacent_polar_conts')
                          if 'substrate' in objects:
                            cmd.delete("substrate_polar_conts")
                    except:
                          
                          showinfo('Alert', "No motif polar contacts to hide")
                elif tag=='Show Substrate':
                    try:
                      cmd.select('substrate', 'byres het within 7 of  Motif')
                      objects = cmd.get_names('all')
                      xp = cmd.index('substrate')
                      np  = len(xp)
                      if(np < 1):
                          cmd.delete('substrate')
                      if 'substrate' in objects:
                          cmd.show('sticks', 'substrate')
                          cmd.deselect()
                          cmd.color("oxygen","(elem O and substrate)")
                          cmd.color("nitrogen","(elem N and substrate)")
                          cmd.color("sulfur","(elem S and substrate)")
                          cmd.color("hydrogen","(elem H and substrate)")
                          cmd.color("white","(elem C and substrate)")
                    except:
                        
                        showinfo('Alert', "No substrate found")
                elif tag=='Show label':
                 objects = cmd.get_names('all')
                 try:
                              cmd.label('''(name ca+C1*+C1' and (byres(Motif)))''','''"%s-%s"%(resn,resi)''')
                              if 'Adjacent' in objects:
                                     cmd.label('''(name ca+C1*+C1' and (byres(Adjacent)))''','''"%s-%s"%(resn,resi)''')
                 except:
                            
                            showinfo('Alert', "Select a motif first")
                elif tag=='Hide Label':
                    objects = cmd.get_names('all')
                    try:
                          cmd.label("Motif","''")
                          if 'Adjacent' in objects:
                              cmd.label('byres Adjacent',"''")
                    except:
                            
                            showinfo('Alert', "No motif labels to hide")
                elif tag=='Hide Substrate':
                                  try:
                                    cmd.hide('sticks', 'substrate')
                                  except:
                                    
                                    showinfo('Alert', "No substrate selected")
        stereo = Pmw.OptionMenu(interior,label_text = 'Options:',labelpos = 'w',
                    items = ('','Surface Pocket','Polar Contacts', 'Hide Contacts', 'Show Substrate', 'Hide Substrate', 'Show label', 'Hide Label'),
                    menubutton_width = 8, command=motifoption)
        stereo.grid(row=0,column=3,sticky = tk.NW)
        
        group = Pmw.Group(root, tag_text='Adjacent')
        group.grid(row=1, column=0, padx=2, pady=2, sticky = tk.W)
        
        interior = group.interior()
        framesela = tk.Frame(interior)
        framesela.grid(row=0, column=0, columnspan = 2, padx=0, pady=0, sticky = tk.N)
        ballsela = Pmw.Balloon(interior)
        ballsela.bind(framesela, 'Within # Angstroms')
        selA = tk.Scale(framesela, width = 8)
        selA.configure(troughcolor="#ffffff")
        selA.configure(length="130")
        selA.configure(orient="horizontal")
        selA.configure(resolution="0.2")
        selA.configure(to="10.0")
        selA.grid(row=0, column=0, columnspan= 2, padx=0, pady=0, sticky = tk.N)
        selA.set(5.0)
        frameadj = tk.Frame(interior)
        frameadj.grid(row=1, column=0, padx=1, pady=1, sticky = tk.NW)
        balladj = Pmw.Balloon(interior)
        balladj.bind(frameadj, 'Display residues adjacent to motif')
        

        showround = tk.Button(frameadj, width = 12, text = 'Adjacent', command = roundres)
        showround.grid(row=1, column=0, padx=1, pady=1, sticky = tk.NW)
        showround.bind('<Button-1>', roundres)
        

        delres = tk.Button(interior, width = 14, text = 'Delete Adjacent', command = resdel)
        delres.grid(row=1, column=1, padx=1, pady=1, sticky = tk.NW)
        delres.bind('<Button-1>', resdel)
    
    except ValueError:
        
        showinfo('Error', 'Please enter a number greater than or equal to 2.\n'
                                                        +'Please enter a number less than or equal to 10.')
        loadmotifer()
