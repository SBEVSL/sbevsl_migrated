from pymol import cmd
import Tkinter as tk
import Pmw
from tkFileDialog import askopenfilename
from tkSimpleDialog import askstring
from pmg_tk.startup.ProMol_dir import promolglobals as pglob

Pmw.initialise()

#----------Motif definitions consisting of measuring atom to atom between different
    #    amino acid residues and allowing them to be altered by a slider
    
def motifCaller(motif, camera):
    pass

def byResidue(selection, num):
    byres, delete = '', ''
    numbers = range(1, num)
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

def serineprotease(self, motifRange):
    update()#updates list of molecular groups
    #sees if objects are in objects
    #sets defaults
    #deletes created objects
    deletemotif()#deletes previous motif
    cmd.do('select asp1, resn asp within %s of resn his'%(motifRange*3))
    cmd.do('select asp2, resn asp within %s of resn ser'%(motifRange*7))
    self.byResidue('asp', 2)
    cmd.do('select his1, resn his within %s of asp'%(motifRange*4))
    cmd.do('select his2, resn his within %s of resn ser'%(motifRange*4))
    self.byResidue('his', 2)
    cmd.do('select ser1, name og within %s of name ne2'%(motifRange*3.5))
    cmd.do('select ser2, resn ser within %s of asp'%(motifRange*7))
    self.byResidue('ser', 2)
    cmd.select('serineprotease', 'ser(his(asp))')
    cmd.hide('everything')
    cmd.show('cartoon', 'all')
    cmd.set('cartoon_transparency', '0.5', 'all')
    cmd.show('sticks', 'serineprotease')
    cmd.set('stick_radius', '0.5')
    cpkserineprotease()#colors in cpk
    cmd.orient('serineprotease')
    cmd.deselect()#deselects

def Blactamase(self, motifRange):
    cmd.do('select lys1, name nz and resn lys within %s of (name oh and resn tyr)'%(motifRange*5))
    cmd.do('select lys2, name nz and resn lys within %s of (name cz and resn tyr)'%(motifRange*5.5))
    cmd.do('select lys3, name nz and resn lys within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
    cmd.do('select lys4, name nz and resn lys within %s of (name ce2 and resn tyr)'%(motifRange*6.5))
    cmd.do('select lys5, name ce and resn lys within %s of (name oh and resn tyr)'%(motifRange*5))
    cmd.do('select lys6, name ce and resn lys within %s of (name cz and resn tyr)'%(motifRange*6))
    cmd.do('select lys7, name nz and resn lys within %s of (name og and resn ser)'%(motifRange*6))
    cmd.do('select lys8, name nz and resn lys within %s of (name cb and resn ser)'%(motifRange*5.2))
    cmd.do('select lys9, name cb and resn lys within %s of (name cb and resn ser)'%(motifRange*9.2))
    cmd.do('select lys10, name ce and resn lys within %s of (name oe1 and resn glu)'%(motifRange*11))
    cmd.do('select lys11, name nz and resn lys within %s of (name oe1 and resn glu)'%(motifRange*11))
    cmd.do('select lys12, name nz and resn lys within %s of (name oe2 and resn glu)'%(motifRange*12.5))
    cmd.do('select lys13, name ce and resn lys within %s of (name cd and resn glu)'%(motifRange*11))
    self.byResidue('lys', 13)
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nz and resn lys)'%(motifRange*5))
    cmd.do('select tyr2, name cz and resn tyr within %s of (name nz and resn lys)'%(motifRange*5.5))
    cmd.do('select tyr3, name ce1 and resn tyr within %s of (name nz and resn lys)'%(motifRange*6.5))
    cmd.do('select tyr4, name ce2 and resn tyr within %s of (name nz and lys)'%(motifRange*6.5))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name ce and resn lys)'%(motifRange*5))
    cmd.do('select tyr6, name cz and resn tyr within %s of (name ce and resn lys)'%(motifRange*6))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name og and resn ser)'%(motifRange*6))
    cmd.do('select tyr8, name cz and resn tyr within %s of (name og and resn ser)'%(motifRange*6.5))
    cmd.do('select tyr9, name oh and resn tyr within %s of (name cb and resn ser)'%(motifRange*6))
    cmd.do('select tyr10, name oh and resn tyr within %s of (name oe1 and resn glu)'%(motifRange*10))
    cmd.do('select tyr11, name oh and resn tyr within %s of (name oe2 and resn glu)'%(motifRange*10))
    cmd.do('select tyr12, name oh and resn tyr within %s of (name cd and resn glu)'%(motifRange*10))
    self.byResidue('tyr', 12)
    cmd.do('select ser1, name cb and resn ser within %s of (name nz and resn lys)'%(motifRange*6))
    cmd.do('select ser2, name og and resn ser within %s of (name nz and resn lys)'%(motifRange*6))
    cmd.do('select ser3, name cb and resn ser within %s of (name cb and lys)'%(motifRange*8.2))
    cmd.do('select ser4, name og and resn ser within %s of (name cz and resn tyr)'%(motifRange*6.5))
    cmd.do('select ser5, name cb and resn ser within %s of (name oh and resn tyr)'%(motifRange*6.5))
    cmd.do('select ser6, name og and resn ser within %s of (name oh and tyr)'%(motifRange*6))
    cmd.do('select ser7, name og and resn ser within %s of (name oe1 and resn glu)'%(motifRange*12))
    cmd.do('select ser8, name og and resn ser within %s of (name oe2 and resn glu)'%(motifRange*12))
    cmd.do('select ser9, name cb and resn ser within %s of (name oe1 and resn glu)'%(motifRange*11))
    cmd.do('select ser10, name cb and resn ser within %s of (name oe2 and resn glu)'%(motifRange*12.5))
    cmd.do('select ser11, name og and resn ser within %s of (name cd and resn glu)'%(motifRange*12.5))
    cmd.do('select ser12, name cb and resn ser within %s of (name cd and resn glu)'%(motifRange*11.5))
    self.byResidue('ser', 12)
    cmd.do('select glu1, name oe1 and resn glu within %s of (name ce and resn lys)'%(motifRange*8.5))
    cmd.do('select glu2, name oe1 and resn glu within %s of (name nz and resn lys)'%(motifRange*9.5))
    cmd.do('select glu3, name oe2 and resn glu within %s of (name nz and lys)'%(motifRange*11.2))
    cmd.do('select glu4, name cd and resn glu within %s of (name ce and resn lys)'%(motifRange*10.6))
    cmd.do('select glu5, name oe1 and resn glu within %s of (name oh and resn tyr)'%(motifRange*8.7))
    cmd.do('select glu6, name oe2 and resn glu within %s of (name oh and resn tyr)'%(motifRange*9.7))
    cmd.do('select glu7, name cd and resn glu within %s of (name oh and resn tyr)'%(motifRange*9.6))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name og and resn ser)'%(motifRange*10.5))
    cmd.do('select glu9, name oe2 and resn glu within %s of (name og and resn ser)'%(motifRange*10.5))
    cmd.do('select glu10, name oe1 and resn glu within %s of (name cb and resn ser)'%(motifRange*10))
    cmd.do('select glu11, name oe2 and resn glu within %s of (name cb and resn ser)'%(motifRange*11.8))
    cmd.do('select glu12, name cd and resn glu within %s of (name og and resn ser)'%(motifRange*11.8))
    cmd.do('select glu13, name cd and resn glu within %s of (name cb and ser)'%(motifRange*11))
    cmd.do('select glu14, name oe1 and resn glu within %s of (name cg and tyr)'%(motifRange*7.4))
    self.byResidue('glu', 14)
    cmd.select('lactamase', 'ser(tyr(glu(lys)))')
    cmd.show('sticks', 'lactamase')

def superoxide(self, motifRange):
    cmd.do('select his1, resn his within %s of elem cu'%(motifRange*4))
    cmd.do('select his2, his and elem zn around %s)'%(motifRange*4))
    cmd.do('select his3, his and elem cu around %s'%(motifRange*4))
    self.byResidue('his', 3)
    cmd.do('select arg1, resn arg within %s of elem cu'%(motifRange*6))
    cmd.do('select arg2, arg and elem zn around %s)'%(motifRange*6))
    cmd.do('select arg3, arg and elem cu around %s'%(motifRange*6))
    self.byResidue('arg', 3)
    cmd.do('select superoxide, his(arg)')
    cmd.show('sticks', 'superoxide')
    cmd.show('spheres', 'elem cu')
    cmd.show('spheres', 'elem zn')

def metalloprotease(self, motifRange):
    cmd.select('zn', 'elem zn')
    cmd.do('select metalloprotease, byres zn(zn around %s)'%(motifRange*5))
    cmd.show('sticks', 'metalloprotease')
    cmd.show('sphere', 'zn')

def tyrophos(self, motifRange):
    cmd.do('select arg1, name nh1 and resn arg within %s of (name od1 and resn asp)'%(motifRange*7))
    cmd.do('select arg2, name nh2 and resn arg within %s of (name od2 and resn asp)'%(motifRange*7))
    cmd.do('select arg3, name ne and resn arg within %s of (name cb and resn asp)'%(motifRange*6.5))
    cmd.do('select arg4, name nh2 and resn arg within %s of (name ca and resn cys)'%(motifRange*7))
    cmd.do('select arg5, name nh1 and resn arg within %s of (name cb and resn cys)'%(motifRange*7))
    cmd.do('select arg6, name ne and resn arg within %s of (name sg and resn cys)'%(motifRange*6.5))
    cmd.do('select arg7, name nh2 and resn arg within %s of (name og and resn ser)'%(motifRange*10))
    cmd.do('select arg8, name nh1 and resn arg within %s of (name cb and resn ser)'%(motifRange*11.2))
    cmd.do('select arg9, name ne and resn arg within %s of (name ca and resn ser)'%(motifRange*9))
    self.byResidue('arg', 9)
    cmd.do('select asp1, name od1 and resn asp within %s of (name nh1 and arg)'%(motifRange*7))
    cmd.do('select asp2, name od2 and resn asp within %s of (name nh2 and arg)'%(motifRange*7))
    cmd.do('select asp3, name cb and resn asp within %s of (name ne and arg)'%(motifRange*6.5))
    cmd.do('select asp4, name od2 and resn asp within %s of (name c and resn ser)'%(motifRange*11))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ca and resn ser)'%(motifRange*12))
    cmd.do('select asp6, name cb and resn asp within %s of (name cb and resn ser)'%(motifRange*9.2))
    cmd.do('select asp7, name od1 and resn asp within %s of (name c and resn cys)'%(motifRange*12))
    cmd.do('select asp8, name od2 and resn asp within %s of (name cb and resn cys)'%(motifRange*11))
    cmd.do('select asp9, name cb and resn asp within %s of (name sg and resn cys)'%(motifRange*10))
    self.byResidue('asp', 9)
    cmd.do('select cys1, name ca and resn cys within %s of (name og and resn ser)'%(motifRange*6.5))
    cmd.do('select cys2, name cb and resn cys within %s of (name cb and resn ser)'%(motifRange*7))
    cmd.do('select cys3, name sg and resn cys within %s of (name ca and resn ser)'%(motifRange*6))
    cmd.do('select cys4, name c and resn cys within %s of (name od1 and asp)'%(motifRange*12))
    cmd.do('select cys5, name cb and resn cys within %s of (name od2 and asp)'%(motifRange*11))
    cmd.do('select cys6, name sg and resn cys within %s of (name cb and asp)'%(motifRange*10))
    cmd.do('select cys7, name ca and resn cys within %s of (name nh2 and arg)'%(motifRange*7))
    cmd.do('select cys8, name cb and resn cys within %s of (name nh1 and arg)'%(motifRange*7))
    cmd.do('select cys9, name sg and resn cys within %s of (name ne and arg)'%(motifRange*6.5))
    self.byResidue('cys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name nh2 and arg)'%(motifRange*10))
    cmd.do('select ser2, name cb and resn ser within %s of (name nh1 and arg)'%(motifRange*11.2))
    cmd.do('select ser3, name ca and resn ser within %s of (name ne and arg)'%(motifRange*9))
    cmd.do('select ser4, name c and resn ser within %s of (name od2 and asp)'%(motifRange*11))
    cmd.do('select ser5, name ca and resn ser within %s of (name od1 and asp)'%(motifRange*12))
    cmd.do('select ser6, name cb and resn ser within %s of (name cb and asp)'%(motifRange*9.2))
    cmd.do('select ser7, name og and resn ser within %s of (name ca and cys)'%(motifRange*6.5))
    cmd.do('select ser8, name cb and resn ser within %s of (name cb and cys)'%(motifRange*7))
    cmd.do('select ser9, name ca and resn ser within %s of (name sg and cys)'%(motifRange*6))
    self.byResidue('ser', 9)
    if(len(cmd.index('ser')) < 1):            
        cmd.select('tyrophos', 'asp(arg(cys))')
    else:
        cmd.select('tyrophos', 'ser(asp(arg(cys)))')
    cmd.show('sticks', 'tyrophos')

def carbanhyd(self, motifRange):
    cmd.select('zn', 'elem zn')
    cmd.do('select his, resn his within %s of zn'%(motifRange*5))
    cmd.select('carbonicanhydrase', 'byres his or zn')
    cmd.delete('zn')
    cmd.delete('his')

def paplike(self, motifRange):
    cmd.do('select gln1, name ne2 and resn gln within %s of (name ne2 and resn his)'%(motifRange*7))
    cmd.do('select gln2, name cd and resn gln within %s of (name ce1 and resn his)'%(motifRange*6.7))
    cmd.do('select gln3, name oe1 and resn gln within %s of (name nd1 and resn his)'%(motifRange*7))
    cmd.do('select gln4, name ne2 and resn gln within %s of (name cb and resn cys)'%(motifRange*5.5))
    cmd.do('select gln5, name oe1 and resn gln within %s of (name sg and resn cys)'%(motifRange*6.7))
    self.byResidue('gln', 5)
    cmd.do('select his1, name ne2 and resn his within %s of (name ne2 and gln)'%(motifRange*7))
    cmd.do('select his2, name ce1 and resn his within %s of (name cd and gln)'%(motifRange*6.7))
    cmd.do('select his3, name nd1 and resn his within %s of (name oe1 and gln)'%(motifRange*7))
    cmd.do('select his4, name ce1 and resn his within %s of (name cb and resn cys)'%(motifRange*5.7))
    cmd.do('select his5, name nd1 and resn his within %s of (name sg and resn cys)'%(motifRange*6))
    self.byResidue('his', 5)
    cmd.do('select cys1, name cb and resn cys within %s of (name ce1 and his)'%(motifRange*5.7))
    cmd.do('select cys2, name sg and resn cys within %s of (name nd1 and his)'%(motifRange*6))
    cmd.do('select cys3, name cb and resn cys within %s of (name ne2 and gln)'%(motifRange*5.5))
    cmd.do('select cys4, name sg and resn cys within %s of (name oe1 and gln)'%(motifRange*6.7))
    self.byResidue('cys', 4)
    cmd.select('paplike', 'gln(his(cys))')

def zincfinger(self, motifRange):
    if(len(cmd.index('elem zn')) >= 1):
        cmd.select('zn1', 'elem zn')
        cmd.select('his', 'resn his')
        cmd.select('cys', 'resn cys')
        cmd.do('select cys1, resn cys around %s'%(motifRange*4))
        cmd.select('Zinc_finger', '(resn cys or resn his(and byres cys1))')

def aminotransferase(self, motifRange):
    cmd.do('select asp1, name od1 and resn asp within %s of (name cb and resn his)'%(motifRange*5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name cg and resn his)'%(motifRange*6))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*7))
    cmd.do('select asp4, name cg and resn asp within %s of (name cb and resn his)'%(motifRange*6.5))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select asp6, name od1 and resn asp within %s of (name cd2 and resn his)'%(motifRange*7))
    cmd.do('select asp7, name od2 and resn asp within %s of (name nz and resn lys)'%(motifRange*9))
    cmd.do('select asp8, name cg and resn asp within %s of (name nz and resn lys)'%(motifRange*9))
    self.byResidue('asp', 8)
    cmd.do('select his1, name cb and resn his within %s of (name od1 and resn asp)'%(motifRange*5))
    cmd.do('select his2, name cg and resn his within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select his3, name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*7))
    cmd.do('select his4, name cb and resn his within %s of (name cg and asp)'%(motifRange*6.5))
    cmd.do('select his5, name ne2 and resn his within %s of (name od1 and asp)'%(motifRange*8))
    cmd.do('select his6, name cd2 and resn his within %s of (name od1 and asp)'%(motifRange*7))
    cmd.do('select his7, name nd1 and resn his within %s of (name nz and resn lys)'%(motifRange*7.5))
    cmd.do('select his8, name ne2 and resn his within %s of (name nz and resn lys)'%(motifRange*8))
    cmd.do('select his9, name ce1 and resn his within %s of (name nz and resn lys)'%(motifRange*7))
    self.byResidue('his', 9)
    cmd.do('select lys1, name nz and resn lys within %s of (name od2 and asp)'%(motifRange*9))
    cmd.do('select lys2, name nz and resn lys within %s of (name cg and asp)'%(motifRange*9))
    cmd.do('select lys3, name nz and resn lys within %s of (name nd1 and his)'%(motifRange*7.5))
    cmd.do('select lys4, name nz and resn lys within %s of (name ne2 and his)'%(motifRange*8))
    cmd.do('select lys5, name nz and resn lys within %s of (name ce1 and his)'%(motifRange*7))
    self.byResidue('lys', 5)
    cmd.select('Aminotransferase', 'asp(his(lys))')

'''CHECK THIS'''
def fisomerase(self, motifRange):
    cmd.do('select his, elem mn around %s(elem mn)'%(motifRange*5))
    cmd.select('fucoseisomerase', 'byres resn asp and his(byres resn glu and his(elem mn))')

def glutamine_amidotransferase(self, motifRange):
    cmd.do('select his1, name ND1 within %s of name OE2'%(motifRange*3))
    cmd.do('select his2, name NE2 within %s of name SG'%(motifRange*3.5))
    self.byResidue('his', 2)
    cmd.do('select glu1, resn glu within %s of his'%(motifRange*3.2))
    cmd.do('select glu2, resn glu within %s of resn cys'%(motifRange*7))
    self.byResidue('glu', 2)
    cmd.do('select cys1, resn cys within %s of his'%(motifRange*3.5))
    cmd.do('select cys2, resn cys within %s of glu'%(motifRange*7))
    self.byResidue('cys', 2)
    cmd.select('glu_amidotransferase', 'cys(his(glu))')

'''sucks, redo'''
def dnaligase(self, motifRange):
    cmd.select('amp', 'resn amp')
    cmd.select('atp', 'resn atp')
    if(len(cmd.index('amp')) >= 1):
        cmd.do('selct lys, resn amp around %s and resn lys'%(motifRange*7.4))
        cmd.do('select asp, resn amp around %s and resn asp within %s of lys'%(motifRange*5.3, motifRange*3))
        cmd.do('select arg, resn amp around %s and resn arg within %s of asp'%(motifRange*7, motifRange*5))
        cmd.select('Ligase', 'byres lys(amp(arg(asp)))')
    elif(len(cmd.index('atp')) >= 1):
        cmd.do('select lys, resn atp around %s and resn lys'%(motifRange*7.4))
        cmd.do('select asp, resn atp around %s and(resn asp within %s of lys)'%(motifRange*5.3, motifRange*3))
        cmd.do('select arg, resn atp around %s and(resn arg within %s of asp)'%(motifRange*7, motifRange*5))
        cmd.select('Ligase', 'byres lys(atp(arg(asp)))')
    elif(len(cmd.index('amp')) < 1 and len(cmd.index('atp')) < 1):
        cmd.do('select lys1, name NZ within %s of name OD2'%(motifRange*9))
        cmd.do('select lys2, name NZ within %s of name NH2'%(motifRange*10))
        cmd.do('select arg, resn arg and name NE within %s of name OD2'%(motifRange*5.5))
        cmd.do('select asp, resn asp and name OD2 within %s of name NE'%(motifRange*5.5))
        cmd.od('select lys, resn lys and lys1 and lys2')
        cmd.select('Ligase', 'byres arg(asp(lys))')

def thymidinekinase(self, motifRange):
    cmd.do('select glu1, name OE1 and resn glu within %s of name NH2 and resn arg'%(motifRange*5))
    cmd.do('select glu2, resn glu and name OE2 within %s of name NE and resn arg'%(motifRange*5))
    cmd.do('select glu3, resn glu and name OE1 within %s of name NH1 and resn arg'%(motifRange*6))
    cmd.do('select glu4, resn glu and name OE1 within %s of name NE and resn arg'%(motifRange*6))
    cmd.do('select glu5, resn glu and name OE2 within %s of name NH2 and resn arg'%(motifRange*5.5))
    cmd.do('select glu6, resn glu and name oe1 within %s of name CZ and resn arg'%(motifRange*5))
    cmd.do('select glu7, resn glu and name oe2 within %s of name CZ and resn arg'%(motifRange*5))
    cmd.do('select glu8, resn glu and name oe1 within %s of name CD and resn arg'%(motifRange*5.8))
    cmd.do('select glu9, resn glu and name oe2 within %s of name CD and resn arg'%(motifRange*5.5))
    self.byResidue('glu', 9)
    cmd.do('select arg1, resn arg and name NH1 within %s of name OE2 and glu'%(motifRange*6))
    cmd.do('select arg2, resn arg and name NE within %s of name OE2 and glu'%(motifRange*5.2))
    cmd.do('select arg3, resn arg and name NH1 within %s of name oe1 and glu'%(motifRange*6))
    cmd.do('select arg4, resn arg and name ne within %s of name oe1 and resn glu'%(motifRange*6.5))
    cmd.do('select arg5, resn arg and name nh2 within %s of name oe2 and resn glu'%(motifRange*5.8))
    self.byResidue('arg', 5)
    cmd.do('select gly1, resn gly within %s of arg'%(motifRange*6.2))
    cmd.do('select gly2, resn gly within %s of glu'%(motifRange*9))
    self.byResidue('gly', 2)
    cmd.select('glu10', 'byres glu within 10 of gly')
    cmd.select('arg10', 'byres arg within 9 of gly')
    cmd.select('Tkinase', 'glu10(arg10(gly))')

def oglycosyl(self, motifRange):
    cmd.do('select asp1, name od1 and resn asp within %s of (name oe1 and resn glu)'%(motifRange*9.5))
    cmd.select('notasp', 'resn asp within %s of resn glu'%(4.5/motifRange))
    cmd.select('asp', 'asp1 and (byres not notasp)')
    cmd.do('select glu1, name oe1 and resn glu within %s of (name od1 and resn asp)'%(motifRange*9.5))
    cmd.select('glu0', 'resn glu within %s of resn asp'%(4.5/motifRange))
    cmd.select('glu', 'byres glu1 and (not glu0)')
    cmd.select('o-glycosyl', 'byres asp | byres glu')

def carboncarbon(self, motifRange):
    cmd.do('select asp1, name od1 within %s of name nz'%(motifRange*3.5))
    cmd.do('select asp2, resn asp within %s of name ne2'%(motifRange*6))
    self.byResidue('asp', 2)
    cmd.do('select lys1, name nz within %s of asp'%(motifRange*6))
    cmd.do('select lys2, resn lys within %s of resn his'%(motifRange*8))
    self.byResidue('lys', 2)
    cmd.do('select his1, name ne2 within %s of name nz'%(motifRange*6))
    cmd.do('select his2, resn his within %s of lys'%(motifRange*6))
    cmd.do('select his3, resn his within %s of asp'%(motifRange*9))
    self.byResidue('his', 3)
    cmd.select('carboncarbon', 'asp(lys(his))')

def peroxidase(self, motifRange):
    cmd.do('select asn1, name od1 within %s of name nd1'%(motifRange*8))
    cmd.do('select asn2, name od1 within %s of name ne2'%(motifRange*6))
    cmd.do('select asn3, name nd2 within %s of name nd1'%(motifRange*10))
    cmd.do('select asn4, name nd2 within %s of name ne2'%(motifRange*8))
    cmd.do('select asn5, name od1 within %s of name nh2'%(motifRange*7))
    cmd.do('select asn6, name od1 within %s of name nh1'%(motifRange*8.6))
    cmd.do('select asn7, name od1 within %s of name ne'%(motifRange*8))
    cmd.do('select asn8, name nd2 within %s of name nh2'%(motifRange*9))
    cmd.do('select asn9, name nd2 within %s of name nh1'%(motifRange*11))
    cmd.do('select asn10, name nd2 within %s of name ne'%(motifRange*9.8))
    self.byResidue('asn', 10)
    cmd.do('select his1, name nd1 within %s of name od1'%(motifRange*5))
    cmd.do('select his2, name ne2 within %s of name od1'%(motifRange*5))
    cmd.do('select his3, name nd1 within %s of name nd2'%(motifRange*8))
    cmd.do('select his4, name ne2 within %s of name nd2'%(motifRange*8.5))
    cmd.do('select his5, name ne2 within %s of name ne'%(motifRange*5.8))
    cmd.do('select his6, name ne2 within %s of name nh2'%(motifRange*6))
    cmd.do('select his7, name ne2 within %s of name nh1'%(motifRange*8.2))
    cmd.do('select his8, name nd1 within %s of name nh1'%(motifRange*7.2))
    cmd.do('select his9, name nd1 within %s of name nh2'%(motifRange*5.8))
    cmd.do('select his10, name nd1 within %s of name ne'%(motifRange*7))
    self.byResidue('his', 10)
    cmd.do('select arg1, name nh2 within %s of name od1'%(motifRange*7.5))
    cmd.do('select arg2, name nh2 within %s of name nd2'%(motifRange*9.5))
    cmd.do('select arg3, name nh2 within %s of name ne2'%(motifRange*6))
    cmd.do('select arg4, name nh2 within %s of name nd1'%(motifRange*6))
    cmd.do('select arg5, name nh1 within %s of name od1'%(motifRange*8))
    cmd.do('select arg6, name nh1 within %s of name nd2'%(motifRange*10))
    cmd.do('select arg7, name nh1 within %s of name ne2'%(motifRange*8))
    cmd.do('select arg8, name nh1 within %s of name nd1'%(motifRange*7.4))
    cmd.do('select arg9, name ne within %s of name od1'%(motifRange*7.2))
    cmd.do('select arg10, name ne within %s of name nd2'%(motifRange*8.9))
    cmd.do('select arg11, name ne within %s of name ne2'%(motifRange*5.9))
    cmd.do('select arg12, name ne within %s of name nd1'%(motifRange*6))
    self.byResidue('arg', 12)
    cmd.select('Peroxidase', 'asn(his(arg))')

def trioseisomerase(self, motifRange):
    cmd.do('select lys1, name nz and resn lys within %s of (name od1 and resn asn)'%(motifRange*7.5))
    cmd.do('select lys2, name nz and resn lys within %s of (name nd2 and resn asn)'%(motifRange*7.5))
    cmd.do('select lys3, name nz and resn lys within %s of (name cg and resn asn)'%(motifRange*7.5))
    cmd.do('select lys4, name ce and resn lys within %s of (name od1 and resn asn)'%(motifRange*6.5))
    cmd.do('select lys5, name ce and resn lys within %s of (name nd2 and resn asn)'%(motifRange*6.5))
    cmd.do('select lys6, name ce and resn lys within %s of (name cg and resn asn)'%(motifRange*6.5))
    cmd.do('select lys7, name cd and resn lys within %s of (name od1 and resn asn)'%(motifRange*6.2))
    cmd.do('select lys8, name cd and resn lys within %s of (name cg and resn asn)'%(motifRange*6.5))
    cmd.do('select lys9, name cd and resn lys within %s of (name nd2 and resn asn)'%(motifRange*6.5))
    cmd.do('select lys10, name nz and resn lys within %s of (name ne2 and resn his)'%(motifRange*6.5))
    cmd.do('select lys11, name nz and resn lys within %s of (name nd1 and resn his)'%(motifRange*7.5))
    cmd.do('select lys12, name nz and resn lys within %s of (name ce1 and resn his)'%(motifRange*6.7))
    cmd.do('select lys13, name nz and resn lys within %s of (name cd2 and resn his)'%(motifRange*7.5))
    cmd.do('select lys14, name nz and resn lys within %s of (name cg and resn his)'%(motifRange*8))
    cmd.do('select lys15, name ce and resn lys within %s of (name ne2 and resn his)'%(motifRange*6.2))
    cmd.do('select lys16, name ce and resn lys within %s of (name nd1 and resn his)'%(motifRange*7.6))
    cmd.do('select lys17, name ce and resn lys within %s of (name ce1 and resn his)'%(motifRange*6.6))
    cmd.do('select lys18, name ce and resn lys within %s of (name cd2 and resn his)'%(motifRange*7))
    cmd.do('select lys19, name ce and resn lys within %s of (name cg and resn his)'%(motifRange*7.5))
    cmd.do('select lys20, name nz and resn lys within %s of (name oe2 and resn glu)'%(motifRange*8.5))
    cmd.do('select lys21, name nz and resn lys within %s of (name oe1 and resn glu)'%(motifRange*10))
    cmd.do('select lys22, name nz and resn lys within %s of (name cd and resn glu)'%(motifRange*9.5))
    cmd.do('select lys23, name ce and resn lys within %s of (name oe2 and resn glu)'%(motifRange*9))
    cmd.do('select lys24, name ce and resn lys within %s of (name oe1 and resn glu)'%(motifRange*10.2))
    cmd.do('select lys25, name ce and resn lys within %s of (name cd and resn glu)'%(motifRange*10))
    self.byResidue('lys', 25)
    cmd.do('select asn1, name od1 and resn asn within %s of (name nz and resn lys)'%(motifRange*7.5))
    cmd.do('select asn2, name nd2 and resn asn within %s of (name nz and resn lys)'%(motifRange*7.5))
    cmd.do('select asn3, name cg and resn asn within %s of (name nz and resn lys)'%(motifRange*7.5))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ce and resn lys)'%(motifRange*6.5))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ce and resn lys)'%(motifRange*6.5))
    cmd.do('select asn6, name cg and resn asn within %s of (name ce and resn lys)'%(motifRange*6.5))
    cmd.do('select asn7, name od1 and resn asn within %s of (name cd and resn lys)'%(motifRange*6.2))
    cmd.do('select asn8, name cg and resn asn within %s of (name cd and resn lys)'%(motifRange*6.5))
    cmd.do('select asn9, name nd2 and resn asn within %s of (name cd and resn lys)'%(motifRange*6.5))
    cmd.do('select asn10, name nd2 and resn asn within %s of (name ne2 and resn his)'%(motifRange*6.3))
    cmd.do('select asn11, name nd2 and resn asn within %s of (name cd2 and resn his)'%(motifRange*6.2))
    cmd.do('select asn12, name nd2 and resn asn within %s of (name ce1 and resn his)'%(motifRange*7.3))
    cmd.do('select asn13, name nd2 and resn asn within %s of (name nd1 and resn his)'%(motifRange*8))
    cmd.do('select asn14, name od1 and resn asn within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select asn15, name od1 and resn asn within %s of (name ce1 and resn his)'%(motifRange*9.2))
    cmd.do('select asn16, name od1 and resn asn within %s of (name cd2 and resn his)'%(motifRange*8.3))
    cmd.do('select asn17, name cg and resn asn within %s of (name ne2 and resn his)'%(motifRange*7.5))
    cmd.do('select asn18, name cg and resn asn within %s of (name ce1 and resn his)'%(motifRange*8.5))
    cmd.do('select asn19, name cg and resn asn within %s of (name cd2 and resn his)'%(motifRange*7.5))
    cmd.do('select asn20, name nd2 and resn asn within %s of (name oe2 and resn glu)'%(motifRange*9))
    cmd.do('select asn21, name nd2 and resn asn within %s of (name oe1 and resn glu)'%(motifRange*10.5))
    cmd.do('select asn22, name nd2 and resn asn within %s of (name cd and resn glu)'%(motifRange*10.2))
    cmd.do('select asn23, name cg and resn asn within %s of (name oe2 and resn glu)'%(motifRange*10))
    cmd.do('select asn24, name cg and resn asn within %s of (name cd and resn glu)'%(motifRange*11))
    cmd.do('select asn25, name cg and resn asn within %s of (name oe1 and resn glu)'%(motifRange*11.3))
    cmd.do('select asn26, name od1 and resn asn within %s of (name oe2 and resn glu)'%(motifRange*11))
    cmd.do('select asn27, name od1 and resn asn within %s of (name cd and resn glu)'%(motifRange*11))
    cmd.do('select asn28, name od1 and resn asn within %s of (name oe1 and resn glu)'%(motifRange*12))
    self.byResidue('asn', 28)
    cmd.do('select glu1, name oe2 and resn glu within %s of (name nz and resn lys)'%(motifRange*8.5))
    cmd.do('select glu2, name oe1 and resn glu within %s of (name nz and resn lys)'%(motifRange*10))
    cmd.do('select glu3, name cd and resn glu within %s of (name nz and resn lys)'%(motifRange*9.5))
    cmd.do('select glu4, name oe2 and resn glu within %s of (name ce and resn lys)'%(motifRange*9))
    cmd.do('select glu5, name oe1 and resn glu within %s of (name ce and resn lys)'%(motifRange*10.2))
    cmd.do('select glu6, name cd and resn glu within %s of (name ce and resn lys)'%(motifRange*10))
    cmd.do('select glu7, name oe2 and resn glu within %s of (name nd2 and resn asn)'%(motifRange*9))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name nd2 and resn asn)'%(motifRange*10.5))
    cmd.do('select glu9, name cd and resn glu within %s of (name nd2 and resn asn)'%(motifRange*10.2))
    cmd.do('select glu10, name oe2 and resn glu within %s of (name cg and resn asn)'%(motifRange*10))
    cmd.do('select glu11, name cd and resn glu within %s of (name cg and resn asn)'%(motifRange*11))
    cmd.do('select glu12, name oe1 and resn glu within %s of (name cg and resn asn)'%(motifRange*11.3))
    cmd.do('select glu13, name oe2 and resn glu within %s of (name od1 and resn asn)'%(motifRange*11))
    cmd.do('select glu14, name cd and resn glu within %s of (name od1 and resn asn)'%(motifRange*11))
    cmd.do('select glu15, name oe1 and resn glu within %s of (name od1 and resn asn)'%(motifRange*12))
    cmd.do('select glu16, name oe2 and resn glu within %s of (name ne2 and resn his)'%(motifRange*5.6))
    cmd.do('select glu17, name oe2 and resn glu within %s of (name cd2 and resn his)'%(motifRange*6.5))
    cmd.do('select glu18, name oe2 and resn glu within %s of (name ce1 and resn his)'%(motifRange*5.8))
    cmd.do('select glu19, name oe2 and resn glu within %s of (name nd1 and resn his)'%(motifRange*6.5))
    cmd.do('select glu20, name oe2 and resn glu within %s of (name cg and resn his)'%(motifRange*6.6))
    cmd.do('select glu21, name oe1 and resn glu within %s of (name ne2 and resn his)'%(motifRange*6.6))
    cmd.do('select glu22, name oe1 and resn glu within %s of (name cd2 and resn his)'%(motifRange*6.5))
    cmd.do('select glu23, name oe1 and resn glu within %s of (name ce1 and resn his)'%(motifRange*5.8))
    cmd.do('select glu24, name oe1 and resn glu within %s of (name nd1 and resn his)'%(motifRange*6.5))
    cmd.do('select glu25, name oe1 and resn glu within %s of (name cg and resn his)'%(motifRange*6.6))
    self.byResidue('glu', 25)
    cmd.do('select his1, name ne2 and resn his within %s of (name nz and resn lys)'%(motifRange*6.5))
    cmd.do('select his2, name nd1 and resn his within %s of (name nz and resn lys)'%(motifRange*7.5))
    cmd.do('select his3, name ce1 and resn his within %s of (name nz and resn lys)'%(motifRange*6.7))
    cmd.do('select his4, name cd2 and resn his within %s of (name nz and resn lys)'%(motifRange*7.5))
    cmd.do('select his5, name cg and resn his within %s of (name nz and resn lys)'%(motifRange*8))
    cmd.do('select his6, name ne2 and resn his within %s of (name ce and resn lys)'%(motifRange*6.2))
    cmd.do('select his7, name nd1 and resn his within %s of (name ce and resn lys)'%(motifRange*7.6))
    cmd.do('select his8, name ce1 and resn his within %s of (name ce and resn lys)'%(motifRange*6.6))
    cmd.do('select his9, name cd2 and resn his within %s of (name ce and resn lys)'%(motifRange*7))
    cmd.do('select his10, name cg and resn his within %s of (name ce and resn lys)'%(motifRange*7.5))
    cmd.do('select his11, name ne2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*6.3))
    cmd.do('select his12, name cd2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*6.2))
    cmd.do('select his13, name ce1 and resn his within %s of (name nd2 and resn asn)'%(motifRange*7.3))
    cmd.do('select his14, name nd1 and resn his within %s of (name nd2 and resn asn)'%(motifRange*8))
    cmd.do('select his15, name ne2 and resn his within %s of (name od1 and resn asn)'%(motifRange*8))
    cmd.do('select his16, name ce1 and resn his within %s of (name od1 and resn asn)'%(motifRange*9.2))
    cmd.do('select his17, name cd2 and resn his within %s of (name od1 and resn asn)'%(motifRange*8.3))
    cmd.do('select his18, name ne2 and resn his within %s of (name cg and resn asn)'%(motifRange*7.5))
    cmd.do('select his19, name ce1 and resn his within %s of (name cg and resn asn)'%(motifRange*8.5))
    cmd.do('select his20, name cd2 and resn his within %s of (name cg and resn asn)'%(motifRange*7.5))
    cmd.do('select his21, name ne2 and resn his within %s of (name oe2 and resn glu)'%(motifRange*5.6))
    cmd.do('select his22, name cd2 and resn his within %s of (name oe2 and resn glu)'%(motifRange*6.5))
    cmd.do('select his23, name ce1 and resn his within %s of (name oe2 and resn glu)'%(motifRange*5.8))
    cmd.do('select his24, name nd1 and resn his within %s of (name oe2 and resn glu)'%(motifRange*6.5))
    cmd.do('select his25, name cg and resn his within %s of (name oe2 and resn glu)'%(motifRange*6.6))
    cmd.do('select his26, name ne2 and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.6))
    cmd.do('select his27, name cd2 and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.5))
    cmd.do('select his28, name ce1 and resn his within %s of (name oe1 and resn glu)'%(motifRange*5.8))
    cmd.do('select his29, name nd1 and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.5))
    cmd.do('select his30, name cg and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.6))
    self.byResidue('his', 30)
    cmd.select('TrioseIsomerase', 'glu(his(asn(lys)))')

def alcoholdehyd(self, motifRange):
    cmd.do('select tyr1, name cd1 and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*5))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name od1 and resn asn)'%(motifRange*8))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name nz and resn lys)'%(motifRange*6))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name og and resn ser)'%(motifRange*5.5))
    cmd.do('select tyr5, name ce2 and resn tyr within %s of (name cg and resn lys)'%(motifRange*6))
    cmd.do('select tyr6, name cg and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*6.5))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name cb and resn ser)'%(motifRange*5.5))
    self.byResidue('tyr', 7)
    cmd.do('select asn1, name nd2 and resn asn within %s of (name cd1 and tyr)'%(motifRange*5))
    cmd.do('select asn2, name nd2 and resn asn within %s of (name oh and tyr)'%(motifRange*7))
    cmd.do('select asn3, name od1 and resn asn within %s of (name oh and tyr)'%(motifRange*7))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ce1 and tyr)'%(motifRange*6))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ce and resn lys)'%(motifRange*5.5))
    cmd.do('select asn6, name od1 and resn asn within %s5 of (name nz and resn lys)'%(motifRange*5.5))
    cmd.do('select asn7, name nd2 and resn asn within %s of (name og and resn ser)'%(motifRange*10))
    self.byResidue('asn', 7)
    cmd.do('select lys1, name nz and resn lys within %s of (name od1 and asn)'%(motifRange*6))
    cmd.do('select lys2, name ce and resn lys within %s of (name nd2 and asn)'%(motifRange*6.5))
    cmd.do('select lys3, name nz and resn lys within %s of (name oh and tyr)'%(motifRange*6))
    cmd.do('select lys4, name ce and resn lys within %s of (name cz and tyr)'%(motifRange*6))
    cmd.do('select lys4, name nz and resn lys within %s of (name cb and resn ser)'%(motifRange*7))
    cmd.do('select lys5, name ce and resn lys within %s of (name og and resn ser)'%(motifRange*7))
    cmd.do('select lys6, name cg and resn lys within %s of (name ce2 and resn tyr)'%(motifRange*6))
    cmd.do('select lys7, name cd and resn lys within %s of (name cb and resn ser)'%(motifRange*6))
    cmd.do('select lys8, name cd and resn lys within %s of (name cb and resn asn)'%(motifRange*7))
    cmd.do('select lys9, name ce and resn lys within %s of (name ce1 and resn tyr)'%(motifRange*6))
    self.byResidue('lys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name oh and tyr)'%(motifRange*6))
    cmd.do('select ser2, name og and resn ser within %s of (name ce2 and tyr)'%(motifRange*6))
    cmd.do('select ser3, name og and resn ser within %s of (name nz and lys)'%(motifRange*8))
    cmd.do('select ser4, name cb and resn ser within %s of (name oh and tyr)'%(motifRange*6))
    cmd.do('select ser5, name cb and resn ser within %s of (name cd and lys)'%(motifRange*6))
    cmd.do('select ser6, name cb and resn ser within %s of (name od1 and asn)'%(motifRange*10))
    cmd.do('select ser7, name ca and resn ser within %s of (name nd2 and asn)'%(motifRange*10))
    self.byResidue('ser', 7)
    cmd.select('alcoholdehyd', 'ser(tyr(lys(asn)))')

def aldoreductase(self, motifRange):
    cmd.do('select lys1, name cd and resn lys within %s of (name cg and resn his)'%(motifRange*6))
    cmd.do('select lys2, name ce and resn lys within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select lys3, name cd and resn lys within %s of (name nd1 and resn his)'%(motifRange*7))
    cmd.do('select lys4, name nz and resn lys within %s of (name oh and resn tyr)'%(motifRange*5))
    cmd.do('select lys5, name nz and resn lys within %s of (name ce2 and resn tyr)'%(motifRange*6))
    cmd.do('select lys6, name cg and resn lys within %s of (name cz and resn tyr)'%(motifRange*8))
    cmd.do('select lys7, name nz and resn lys within %s of (name od1 and resn asp)'%(motifRange*5))
    cmd.do('select lys8, name ce and resn lys within %s of (name od1 and resn asp)'%(motifRange*5.5))
    cmd.do('select lys9, name cg and resn lys within %s of (name ca and resn asp)'%(motifRange*9))
    self.byResidue('lys', 9)
    cmd.do('select his1, name cg and resn his within %s of (name cd and resn lys)'%(motifRange*6))
    cmd.do('select his2, name ne2 and resn his within %s of (name ce and resn lys)'%(motifRange*8))
    cmd.do('select his3, name nd1 and resn his within %s of (name cd and resn lys)'%(motifRange*7))
    cmd.do('select his4, name ne2 and resn his within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select his5, name ce1 and resn his within %s of (name cz and resn tyr)'%(motifRange*6))
    cmd.do('select his6, name nd1 and resn his within %s of (name ce1 and resn tyr)'%(motifRange*7))
    cmd.do('select his7, name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*10.5))
    cmd.do('select his8, name ne2 and resn his within %s of (name cg and resn asp)'%(motifRange*10))
    cmd.do('select his9, name ce1 and resn his within %s of (name od2 and resn asp)'%(motifRange*9))
    self.byResidue('his', 9)
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nz and resn lys )'%(motifRange*5))
    cmd.do('select tyr2, name ce2 and resn tyr within %s of (name nz and resn lys )'%(motifRange*6))
    cmd.do('select tyr3, name cz and resn tyr within %s of (name cg and resn lys)'%(motifRange*8))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name ne2 and resn his)'%(motifRange*6))
    cmd.do('select tyr5, name cz and resn tyr within %s of (name ce1 and resn his)'%(motifRange*6))
    cmd.do('select tyr6, name ce1 and resn tyr within %s of (name nd1 and resn his)'%(motifRange*7))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name od2 and resn asp)'%(motifRange*7))
    cmd.do('select tyr8, name cz and resn tyr within %s of (name cb and resn asp)'%(motifRange*9))
    cmd.do('select tyr9, name ce2 and resn tyr within %s of (name ca and resn asp)'%(motifRange*8))
    self.byResidue('tyr', 9)
    cmd.do('select asp1, name od1 and resn asp within %s of (name nz and resn lys)'%(motifRange*5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name ce and resn lys)'%(motifRange*5.5))
    cmd.do('select asp3, name ca and resn asp within %s of (name cg and resn lys)'%(motifRange*9))
    cmd.do('select asp4, name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*10.5))
    cmd.do('select asp5, name cg and resn asp within %s of (name ne2 and resn his)'%(motifRange*10))
    cmd.do('select asp6, name od2 and resn asp within %s of (name ce1 and resn his)'%(motifRange*9))
    cmd.do('select asp7, name od2 and resn asp within %s of (name oh and resn tyr)'%(motifRange*7))
    cmd.do('select asp8, name cb and resn asp within %s of (name cz and resn tyr)'%(motifRange*9))
    cmd.do('select asp9, name ca and resn asp within %s of (name ce2 and resn tyr)'%(motifRange*8))
    self.byResidue('asp', 9)
    cmd.select('aldoreductase', 'asp(his(lys(tyr)))')

def cistransisomerase(self, motifRange):
    cmd.do('select tyr1, name oh and resn tyr within %s of (name od2 and resn asp)'%(motifRange*9))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name od1 and resn asp)'%(motifRange*11))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name cg and resn asp)'%(motifRange*9.8))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name cb and resn asp)'%(motifRange*9.8))
    cmd.do('select tyr5, name cz and resn tyr within %s of (name od2 and resn asp)'%(motifRange*10.2))
    cmd.do('select tyr6, name cz and resn tyr within %s of (name od1 and resn asp)'%(motifRange*11.5))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name cd1 and resn ile)'%(motifRange*6.5))
    cmd.do('select tyr8, name oh and resn tyr within %s of (name cg1 and resn ile)'%(motifRange*6.5))
    cmd.do('select tyr9, name oh and resn tyr within %s of (name cg2 and resn ile)'%(motifRange*5.5))
    cmd.do('select tyr10, name cz and resn tyr within %s of (name cd1 and resn ile)'%(motifRange*6.5))
    cmd.do('select tyr11, name cz and resn tyr within %s of (name cg1 and resn ile)'%(motifRange*6.8))
    cmd.do('select tyr12, name cz and resn tyr within %s of (name cg2 and resn ile)'%(motifRange*5.5))
    cmd.do('select tyr13, name ce1 and resn tyr within %s of (name cd1 and resn ile)'%(motifRange*6.3))
    cmd.do('select tyr14, name ce1 and resn tyr within %s of (name cg1 and resn ile)'%(motifRange*6.5))
    cmd.do('select tyr15, name ce1 and resn tyr within %s of (name cg2 and resn ile)'%(motifRange*5.5))
    self.byResidue('tyr', 15)
    cmd.do('select asp1, name od2 and resn asp within %s of (name oh and tyr)'%(motifRange*8.7))
    cmd.do('select asp2, name od1 and resn asp within %s of (name oh and tyr)'%(motifRange*10.5))
    cmd.do('select asp3, name cg and resn asp within %s of (name oh and tyr)'%(motifRange*9.3))
    cmd.do('select asp4, name cb and resn asp within %s of (name oh and tyr)'%(motifRange*9.3))
    cmd.do('select asp5, name od2 and resn asp within %s of (name cz and tyr)'%(motifRange*10))
    cmd.do('select asp6, name od1 and resn asp within %s of (name cz and resn tyr)'%(motifRange*11.1))
    cmd.do('select asp7, name od2 and resn asp within %s of (name cg2 and resn ile)'%(motifRange*11.1))
    cmd.do('select asp8, name od2 and resn asp within %s of (name cd1 and resn ile)'%(motifRange*11.1))
    cmd.do('select asp9, name od2 and resn asp within %s of (name cg1 and resn ile)'%(motifRange*11.1))
    cmd.do('select asp10, name cb and resn asp within %s of (name cd1 and resn ile)'%(motifRange*10.8))
    cmd.do('select asp11, name cb and resn asp within %s of (name cg2 and resn ile)'%(motifRange*11.1))
    cmd.do('select asp12, name cb and resn asp within %s of (name cg1 and resn ile)'%(motifRange*11.1))
    self.byResidue('asp', 12)
    cmd.do('select ile1, name cd1 and resn ile within %s of (name oh and tyr)'%(motifRange*6.5))
    cmd.do('select ile2, name cg1 and resn ile within %s of (name oh and tyr)'%(motifRange*6.5))
    cmd.do('select ile3, name cg2 and resn ile within %s of (name oh and tyr)'%(motifRange*5.5))
    cmd.do('select ile4, name cd1 and resn ile within %s of (name cz and resn tyr)'%(motifRange*6.5))
    cmd.do('select ile5, name cg1 and resn ile within %s of (name cz and resn tyr)'%(motifRange*6.8))
    cmd.do('select ile6, name cg2 and resn ile within %s of (name cz and resn tyr)'%(motifRange*5.5))
    cmd.do('select ile7, name cd1 and resn ile within %s of (name ce1 and resn tyr)'%(motifRange*6.3))
    cmd.do('select ile8, name cg1 and resn ile within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
    cmd.do('select ile9, name cg2 and resn ile within %s of (name ce1 and resn tyr)'%(motifRange*5.5))
    cmd.do('select ile10, name cg2 and resn ile within %s of (name od2 and asp)'%(motifRange*11.5))
    cmd.do('select ile11, name cd1 and resn ile within %s of (name od2 and asp)'%(motifRange*11.5))
    cmd.do('select ile12, name cg1 and resn ile within %s of (name od2 and asp)'%(motifRange*11.5))
    cmd.do('select ile13, name cd1 and resn ile within %s of (name cb and asp)'%(motifRange*11))
    cmd.do('select ile14, name cg2 and resn ile within %s of (name cb and resn asp)'%(motifRange*11.5))
    cmd.do('select ile15, name cg1 and resn ile within %s of (name cb and resn asp)'%(motifRange*11.5))
    self.byResidue('ile', 15)
    cmd.select('Cis-trans', 'ile(asp(tyr))')

def nadhbinder(self, motifRange):
    cmd.do('select asp1, name od2 and resn asp within %s of (name sg and resn cys)'%(motifRange*5))
    cmd.do('select asp2, name od2 and resn asp within %s of (name cb and resn cys)'%(motifRange*5.5))
    cmd.do('select asp3, name od1 and resn asp within %s of (name sg and resn cys)'%(motifRange*6.4))
    cmd.do('select asp4, name od1 and resn asp within %s of (name cb and resn cys)'%(motifRange*7.2))
    cmd.do('select asp5, name cg and resn asp within %s of (name sg and resn cys)'%(motifRange*5.5))
    cmd.do('select asp6, name od2 and resn asp within %s of (name og and resn ser)'%(motifRange*4.5))
    cmd.do('select asp7, name od2 and resn asp within %s of (name cb and resn ser)'%(motifRange*5.5))
    cmd.do('select asp8, name od1 and resn asp within %s of (name og and resn ser)'%(motifRange*6))
    cmd.do('select asp9, name od1 and resn asp within %s of (name cb and resn ser)'%(motifRange*7))
    cmd.do('select asp10, name cg and resn asp within %s of (name og and resn ser)'%(motifRange*5.3))
    cmd.do('select asp11, name cg and resn asp within %s of (name cb and resn ser)'%(motifRange*6.4))
    self.byResidue('asp', 11)
    cmd.do('select cys1, name sg and resn cys within %s of (name od2 and resn asp)'%(motifRange*5))
    cmd.do('select cys2, name cb and resn cys within %s of (name od2 and resn asp)'%(motifRange*5.5))
    cmd.do('select cys3, name sg and resn cys within %s of (name od1 and resn asp)'%(motifRange*6.4))
    cmd.do('select cys4, name cb and resn cys within %s of (name od1 and resn asp)'%(motifRange*7.2))
    cmd.do('select cys5, name sg and resn cys within %s of (name cg and resn asp)'%(motifRange*5.5))
    cmd.do('select cys6, name sg and resn cys within %s of (name og and resn ser)'%(motifRange*6.4))
    cmd.do('select cys7, name sg and resn cys within %s of (name cb and resn ser)'%(motifRange*7))
    cmd.do('select cys8, name cb and resn cys within %s of (name og and resn ser)'%(motifRange*8))
    cmd.do('select cys9, name cb and resn cys within %s of (name cb and resn ser)'%(motifRange*8.5))
    self.byResidue('cys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name od2 and resn asp)'%(motifRange*4.5))
    cmd.do('select ser2, name cb and resn ser within %s of (name od2 and resn asp)'%(motifRange*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select ser4, name cb and resn ser within %s of (name od1 and resn asp)'%(motifRange*7))
    cmd.do('select ser5, name og and resn ser within %s of (name cg and resn asp)'%(motifRange*5.3))
    cmd.do('select ser6, name cb and resn ser within %s of (name cg and resn asp)'%(motifRange*6.4))
    cmd.do('select ser7, name og and resn ser within %s of (name sg and resn cys)'%(motifRange*6.4))
    cmd.do('select ser8, name cb and resn ser within %s of (name sg and resn cys)'%(motifRange*7))
    cmd.do('select ser9, name og and resn ser within %s of (name cb and resn cys)'%(motifRange*8))
    cmd.do('select ser10, name cb and resn ser within %s of (name cb and resn cys)'%(motifRange*8.5))
    self.byResidue('ser', 10)
    cmd.select('NAD-reductase', 'ser(asp(cys))')

def nadhbinder2(self, motifRange):
    cmd.do('select glu1, name oe2 and resn glu within %s of (name sg and resn cys)'%(motifRange*6.5))
    cmd.do('select glu2, name oe2 and resn glu within %s of (name cb and resn cys)'%(motifRange*5.5))
    cmd.do('select glu3, name oe1 and resn glu within %s of (name sg and resn cys)'%(motifRange*6.5))
    cmd.do('select glu4, name oe1 and resn glu within %s of (name cb and resn cys)'%(motifRange*7.2))
    cmd.do('select glu5, name cg and resn glu within %s of (name sg and resn cys)'%(motifRange*5.5))
    cmd.do('select glu6, name oe2 and resn glu within %s of (name og and resn ser)'%(motifRange*4.5))
    cmd.do('select glu7, name oe2 and resn glu within %s of (name cb and resn ser)'%(motifRange*5.5))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name og and resn ser)'%(motifRange*6))
    cmd.do('select glu9, name oe1 and resn glu within %s of (name cb and resn ser)'%(motifRange*7))
    cmd.do('select glu10, name cg and resn glu within %s of (name og and resn ser)'%(motifRange*5.5))
    cmd.do('select glu11, name cg and resn glu within %s of (name cb and resn ser)'%(motifRange*6.5))
    self.byResidue('glu', 11)
    cmd.do('select cys1, name sg and resn cys within %s of (name oe2 and resn glu)'%(motifRange*6.5))
    cmd.do('select cys2, name cb and resn cys within %s of (name oe2 and resn glu)'%(motifRange*6.5))
    cmd.do('select cys3, name sg and resn cys within %s of (name oe1 and resn glu)'%(motifRange*6.5))
    cmd.do('select cys4, name cb and resn cys within %s of (name oe1 and resn glu)'%(motifRange*7.5))
    cmd.do('select cys5, name sg and resn cys within %s of (name cg and resn glu)'%(motifRange*5.5))
    cmd.do('select cys6, name sg and resn cys within %s of (name og and resn ser)'%(motifRange*6.5))
    cmd.do('select cys7, name sg and resn cys within %s of (name cb and resn ser)'%(motifRange*7))
    cmd.do('select cys8, name cb and resn cys within %s of (name og and resn ser)'%(motifRange*8))
    cmd.do('select cys9, name cb and resn cys within %s of (name cb and resn ser)'%(motifRange*8.5))
    self.byResidue('cys', 9)
    cmd.do('select ser1, name og and resn ser within %s of (name oe2 and resn glu)'%(motifRange*4.5))
    cmd.do('select ser2, name cb and resn ser within %s of (name oe2 and resn glu)'%(motifRange*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name oe1 and resn glu)'%(motifRange*6))
    cmd.do('select ser4, name cb and resn ser within %s of (name oe1 and resn glu)'%(motifRange*7))
    cmd.do('select ser5, name og and resn ser within %s of (name cg and resn glu)'%(motifRange*5.5))
    cmd.do('select ser6, name cb and resn ser within %s of (name cg and resn glu)'%(motifRange*6.5))
    cmd.do('select ser7, name og and resn ser within %s of (name sg and resn cys)'%(motifRange*6.5))
    cmd.do('select ser8, name cb and resn ser within %s of (name sg and resn cys)'%(motifRange*7))
    cmd.do('select ser9, name og and resn ser within %s of (name cb and resn cys)'%(motifRange*8))
    cmd.do('select ser10, name cb and resn ser within %s of (name cb and resn cys)'%(motifRange*8.5))
    self.byResidue('ser', 10)
    cmd.select('NAD-reductase2', 'ser(glu(cys))')

def cephdeacetylase(self, motifRange):
    cmd.do('select his1, name nd1 and resn his within %s of (name od2 and resn asp)'%(motifRange*4.5))
    cmd.do('select his2, name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*5))
    cmd.do('select his3, name nd1 and resn his within %s of (name cg and resn asp)'%(motifRange*5.5))
    cmd.do('select his4, name ce1 and resn his within %s of (name od2 and resn asp)'%(motifRange*5.5))
    cmd.do('select his5, name ce1 and resn his within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select his6, name ne2 and resn his within %s of (name od1 and resn asp)'%(motifRange*7))
    cmd.do('select his7, name ne2 and resn his within %s of (name od2 and resn asp)'%(motifRange*6.5))
    cmd.do('select his8, name ne2 and resn his within %s of (name cb and resn ala)'%(motifRange*5.5))
    cmd.do('select his9, name ce1 and resn his within %s of (name cb and resn ala)'%(motifRange*5.5))
    cmd.do('select his10, name nd1 and resn his within %s of (name cb and resn ala)'%(motifRange*6.5))
    self.byResidue('his', 10)
    cmd.do('select asp1, name od2 and resn asp within %s of (name cb and resn ala)'%(motifRange*8.5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name cb and resn ala)'%(motifRange*9.5))
    cmd.do('select asp3, name cg and resn asp within %s of (name cb and resn ala)'%(motifRange*9.5))
    cmd.do('select asp4, name od2 and resn asp within %s of (name nd1 and resn his)'%(motifRange*4.5))
    cmd.do('select asp5, name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*5))
    cmd.do('select asp6, name cg and resn asp within %s of (name nd1 and resn his)'%(motifRange*5.5))
    cmd.do('select asp7, name od2 and resn asp within %s of (name ce1 and resn his)'%(motifRange*5.5))
    cmd.do('select asp8, name od1 and resn asp within %s of (name ce1 and resn his)'%(motifRange*6))
    cmd.do('select asp9, name od1 and resn asp within %s of (name ne2 and resn his)'%(motifRange*7))
    cmd.do('select asp10, name od2 and resn asp within %s of (name ne2 and resn his)'%(motifRange*6.5))
    self.byResidue('asp', 10)
    cmd.do('select ala1, name cb and resn ala within %s of (name ne2 and resn his)'%(motifRange*5.5))
    cmd.do('select ala2, name cb and resn ala within %s of (name ce1 and resn his)'%(motifRange*5.5))
    cmd.do('select ala3, name cb and resn ala within %s of (name nd1 and resn his)'%(motifRange*6.5))
    cmd.do('select ala4, name cb and resn ala within %s of (name od2 and resn asp)'%(motifRange*8.5))
    cmd.do('select ala5, name cb and resn ala within %s of (name od1 and resn asp)'%(motifRange*9.5))
    cmd.do('select ala6, name cb and resn ala within %s of (name cg and resn asp)'%(motifRange*9.5))
    cmd.do('select ala7, name c and resn ala within %s of (name n and resn gln)'%(motifRange*2.5))
    self.byResidue('ala', 7)
    cmd.do('select gln1, byres resn gln within %s of his'%(motifRange*9.5))
    cmd.do('select gln2, byres resn gln within %s of asp'%(motifRange*13.5))
    cmd.do('select gln3, byres resn gln within %s of ala'%(motifRange*3))
    self.byResidue('gln', 3)
    cmd.select('deacetylase', 'his(asp(ala(gln)))')
#hyaluronate/chondroitin lyase

def chondrolyase(self, motifRange):
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nh2 and resn arg)'%(motifRange*6))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name nh1 and resn arg)'%(motifRange*5))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name cz and resn arg)'%(motifRange*6))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name ne and resn arg)'%(motifRange*7))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name ne2 and resn his)'%(motifRange*5))
    cmd.do('select tyr6, name oh and resn tyr within %s of (name nd1 and resn his)'%(motifRange*6))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name ce1 and resn his)'%(motifRange*5))
    cmd.do('select tyr8, name ce2 and resn tyr within %s of (name nd1 and resn his)'%(motifRange*6))
    cmd.do('select tyr9, name ce1 and resn tyr within %s of (name ne2 and resn his)'%(motifRange*6))
    cmd.do('select tyr10, name oh and resn tyr within %s of (name od1 and resn asn)'%(motifRange*7.5))
    cmd.do('select tyr11, name oh and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*7.5))
    cmd.do('select tyr12, name ce1 and resn tyr within %s of (name od1 and resn asn)'%(motifRange*6.5))
    cmd.do('select tyr13, name ce1 and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*6))
    self.byResidue('tyr', 13)
    cmd.do('select his1, name ne2 and resn his within %s of (name od1 and resn asn)'%(motifRange*7))
    cmd.do('select his2, name ne2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*8))
    cmd.do('select his3, name cd2 and resn his within %s of (name od1 and resn asn)'%(motifRange*7))
    cmd.do('select his4, name ne2 and resn his within %s of (name cg and resn asn)'%(motifRange*8))
    cmd.do('select his5, name ne2 and resn his within %s of (name oh and resn tyr)'%(motifRange*5))
    cmd.do('select his6, name nd1 and resn his within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select his7, name ce1 and resn his within %s of (name oh and resn tyr)'%(motifRange*5))
    cmd.do('select his8, name nd1 and resn his within %s of (name ce2 and resn tyr)'%(motifRange*6))
    cmd.do('select his9, name ne2 and resn his within %s of (name ce1 and resn tyr)'%(motifRange*6))
    cmd.do('select his10, name ne2 and resn his within %s of (name nh2 and resn arg)'%(motifRange*8))
    cmd.do('select his11, name ce1 and resn his within %s of (name cz and resn arg)'%(motifRange*7))
    cmd.do('select his12, name nd1 and resn his within %s of (name nh1 and resn arg)'%(motifRange*6.5))
    cmd.do('select his13, name nd1 and resn his within %s of (name cd and resn arg)'%(motifRange*9))
    self.byResidue('his', 13)
    cmd.do('select arg1, name nh2 and resn arg within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select arg2, name nh1 and resn arg within %s of (name oh and tyr)'%(motifRange*6))
    cmd.do('select arg3, name cz and resn arg within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select arg4, name ne and resn arg within %s of (name oh and resn tyr)'%(motifRange*7))
    cmd.do('select arg5, name nh2 and resn arg within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select arg6, name cz and resn arg within %s of (name ce1 and resn his)'%(motifRange*7))
    cmd.do('select arg7, name nh1 and resn arg within %s of (name nd1 and resn his)'%(motifRange*6.5))
    cmd.do('select arg8, name cd and resn arg within %s of (name nd1 and resn his)'%(motifRange*9))
    cmd.do('select arg9, name nh1 and resn arg within %s of (name od1 and resn asn)'%(motifRange*11))
    cmd.do('select arg10, name cz and resn arg within %s of (name cg and resn asn)'%(motifRange*12))
    cmd.do('select arg11, name nh2 and resn arg within %s of (name nd2 and resn asn)'%(motifRange*11.5))
    self.byResidue('arg', 11)
    cmd.do('select asn1, name od1 and resn asn within %s of (name nh1 and resn arg)'%(motifRange*11))
    cmd.do('select asn2, name cg and resn asn within %s of (name cz and resn arg)'%(motifRange*11.5))
    cmd.do('select asn3, name nd2 and resn asn within %s of (name nh2 and resn arg)'%(motifRange*10.5))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ne2 and resn his)'%(motifRange*7))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select asn6, name od1 and resn asn within %s of (name cd2 and resn his)'%(motifRange*7))
    cmd.do('select asn7, name cg and resn asn within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select asn8, name od1 and resn asn within %s of (name oh and resn tyr)'%(motifRange*7.5))
    cmd.do('select asn9, name nd2 and resn asn within %s of (name oh and resn tyr)'%(motifRange*7.5))
    cmd.do('select asn10, name od1 and resn asn within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
    cmd.do('select asn11, name nd2 and resn asn within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
    self.byResidue('asn', 11)
    cmd.select('chondroitinase', 'asn(his(arg(tyr)))')

def hyaluronlyase(self, motifRange):
    cmd.do('select tyr1, name oh and resn tyr within %s of (name nh2 and resn arg)'%(motifRange*6))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name nh1 and resn arg)'%(motifRange*5))
    cmd.do('select tyr3, name oh and resn tyr within %sof (name cz and resn arg)'%(motifRange*6))
    cmd.do('select tyr4, name oh and resn tyr within %s of (name ne and resn arg)'%(motifRange*7))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name ne2 and resn his)'%(motifRange*5))
    cmd.do('select tyr6, name oh and resn tyr within %s of (name nd1 and resn his)'%(motifRange*6))
    cmd.do('select tyr7, name oh and resn tyr within %s of (name ce1 and resn his)'%(motifRange*5))
    cmd.do('select tyr8, name ce2 and resn tyr within %s of (name nd1 and resn his)'%(motifRange*6))
    cmd.do('select tyr9, name ce1 and resn tyr within %s of (name ne2 and resn his)'%(motifRange*6))
    cmd.do('select tyr10, name oh and resn tyr within %s of (name od1 and resn asn)'%(motifRange*7.5))
    cmd.do('select tyr11, name oh and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*7.5))
    cmd.do('select tyr12, name ce1 and resn tyr within %s of (name od1 and resn asn)'%(motifRange*6.5))
    cmd.do('select tyr13, name ce1 and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*6))
    self.byResidue('tyr', 13)
    cmd.do('select his1, name ne2 and resn his within %s of (name od1 and resn asn)'%(motifRange*7))
    cmd.do('select his2, name ne2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*8))
    cmd.do('select his3, name cd2 and resn his within %s of (name od1 and resn asn)'%(motifRange*7))
    cmd.do('select his4, name ne2 and resn his within %s of (name cg and resn asn)'%(motifRange*8))
    cmd.do('select his5, name ne2 and resn his within %s of (name oh and resn tyr)'%(motifRange*5))
    cmd.do('select his6, name nd1 and resn his within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select his7, name ce1 and resn his within %s of (name oh and resn tyr)'%(motifRange*5))
    cmd.do('select his8, name nd1 and resn his within %s of (name ce2 and resn tyr)'%(motifRange*6))
    cmd.do('select his9, name ne2 and resn his within %s of (name ce1 and resn tyr)'%(motifRange*6))
    cmd.do('select his10, name ne2 and resn his within %s of (name nh2 and resn arg)'%(motifRange*8))
    cmd.do('select his11, name ce1 and resn his within %s of (name cz and resn arg)'%(motifRange*7))
    cmd.do('select his12, name nd1 and resn his within %s of (name nh1 and resn arg)'%(motifRange*6.5))
    cmd.do('select his13, name nd1 and resn his within %s of (name cd and resn arg)'%(motifRange*9))
    self.byResidue('his', 13)
    cmd.do('select arg1, name nh2 and resn arg within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select arg2, name nh1 and resn arg within %s of (name oh and tyr)'%(motifRange*6))
    cmd.do('select arg3, name cz and resn arg within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select arg4, name ne and resn arg within %s of (name oh and resn tyr)'%(motifRange*7))
    cmd.do('select arg5, name nh2 and resn arg within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select arg6, name cz and resn arg within %s of (name ce1 and resn his)'%(motifRange*7))
    cmd.do('select arg7, name nh1 and resn arg within %s of (name nd1 and resn his)'%(motifRange*6.5))
    cmd.do('select arg8, name cd and resn arg within %s of (name nd1 and resn his)'%(motifRange*9))
    cmd.do('select arg9, name nh1 and resn arg within %s of (name od1 and resn asn)'%(motifRange*11))
    cmd.do('select arg10, name cz and resn arg within %s of (name cg and resn asn)'%(motifRange*12))
    cmd.do('select arg11, name nh2 and resn arg within %s of (name nd2 and resn asn)'%(motifRange*11.5))
    self.byResidue('arg', 11)
    cmd.do('select asn1, name od1 and resn asn within %s of (name nh1 and resn arg)'%(motifRange*11))
    cmd.do('select asn2, name cg and resn asn within %s of (name cz and resn arg)'%(motifRange*11.5))
    cmd.do('select asn3, name nd2 and resn asn within %s of (name nh2 and resn arg)'%(motifRange*10.5))
    cmd.do('select asn4, name od1 and resn asn within %s of (name ne2 and resn his)'%(motifRange*7))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select asn6, name od1 and resn asn within %s of (name cd2 and resn his)'%(motifRange*7))
    cmd.do('select asn7, name cg and resn asn within %s of (name ne2 and resn his)'%(motifRange*8))
    cmd.do('select asn8, name od1 and resn asn within %s of (name oh and resn tyr)'%(motifRange*7.5))
    cmd.do('select asn9, name nd2 and resn asn within %s of (name oh and resn tyr)'%(motifRange*7.5))
    cmd.do('select asn10, name od1 and resn asn within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
    cmd.do('select asn11, name nd2 and resn asn within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
    self.byResidue('asn', 11)
    cmd.select('Hyaluronate_Lyase', 'asn(his(arg(tyr)))')

def ACTase(self, motifRange):
    showinfo('Info', 'This motif is based on sequence not position')
    cmd.select('gln', 'resi 231 and resn gln')
    cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
    cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
    cmd.select('his', 'resi 134 and resn his')
    cmd.select('lys', 'resi 84 and resn lys')
    cmd.select('ser', 'resi 80 and resn ser')
    cmd.select('actase', 'gln(arg(thr(his(lys(ser)))))')

def ACTase2(self, motifRange):
    cmd.select('gln', 'resi 231 and resn gln')
    cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
    cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
    cmd.select('his', 'resi 134 and resn his')
    cmd.select('lys', 'resi 84 and resn lys')
    cmd.select('ser', 'resi 80 and resn ser')
    cmd.select('actase', 'gln(arg(thr(his(lys(ser)))))')

def exonucleaseiii(self, motifRange):
    cmd.do('select his1, name ne2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*5.5))
    cmd.do('select his2, name ne2 and resn his within %s of (name od1 and resn asn)'%(motifRange*6.5))
    cmd.do('select his3, name ne2 and resn his within %s of (name cg and resn asn)'%(motifRange*5.5))
    cmd.do('select his4, name cd2 and resn his within %s of (name cg and resn asn)'%(motifRange*5.5))
    cmd.do('select his5, name nd1 and resn his within %s of (name cg and resn asn)'%(motifRange*6.5))
    cmd.do('select his6, name ce1 and resn his within %s of (name od2 and resn asp)'%(motifRange*5.5))
    cmd.do('select his7, name nd1 and resn his within %s of (name od2 and resn asp)'%(motifRange*5))
    cmd.do('select his8, name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*5.5))
    cmd.do('select his9, name nd1 and resn his within %s of (name cg and resn asp)'%(motifRange*5.5))
    self.byResidue('his', 9)
    cmd.do('select asp1, name od2 and resn asp within %s of (name ce1 and resn his)'%(motifRange*5.5))
    cmd.do('select asp2, name od2 and resn asp within %s of (name nd1 and resn his)'%(motifRange*5))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*5.5))
    cmd.do('select asp4, name cg and resn asp within %s of (name nd1 and resn his)'%(motifRange*5.5))
    cmd.do('select asp5, name od2 and resn asp within %s of (name nd2 and resn asn)'%(motifRange*5.7))
    cmd.do('select asp6, name od1 and resn asp within %s of (name nd2 and resn asn)'%(motifRange*6))
    cmd.do('select asp7, name od1 and resn asp within %s of (name od1 and resn asn)'%(motifRange*6))
    self.byResidue('asp8', 7)
    cmd.do('select asp9, byres resn asp within %s of asp8'%(motifRange*5.5))
    cmd.do('select asp10, byres resn asp within %s of his'%(motifRange*5.5))
    cmd.select('asp', 'byres asp8 or (byres asp9 and byres asp10)')
    cmd.do('select asn1, name nd2 and resn asn within %s of (name ne2 and resn his)'%(motifRange*5.5))
    cmd.do('select asn2, name od1 and resn asn within %s of (name ne2 and resn his)'%(motifRange*6.5))
    cmd.do('select asn3, name cg and resn asn within %s of (name ne2 and resn his)'%(motifRange*5.5))
    cmd.do('select asn4, name cg and resn asn within %s of (name cd2 and resn his)'%(motifRange*5.5))
    cmd.do('select asn5, name cg and resn asn within %s of (name nd1 and resn his)'%(motifRange*6.5))
    cmd.do('select asn6, name nd2 and resn asn within %s of (name od2 and resn asp)'%(motifRange*5.7))
    cmd.do('select asn7, name nd2 and resn asn within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select asn8, name od1 and resn asn within %s of (name od1 and resn asp)'%(motifRange*6))
    self.byResidue('asn9', 8)
    cmd.do('select asn10, byres resn asn within %s of asn9'%(motifRange*8))
    cmd.do('select asn11, byres resn asn within %s of his'%(motifRange*8))
    cmd.do('select asn12, byres resn asn within %s of asp8'%(motifRange*6))
    cmd.select('asn', 'byres asn9 or (byres asn10 and byres asn11 and byres asn12)')
    cmd.select('Exonuclease3', 'his(asp(asn))')

def cyclinkinase(self, motifRange):
    cmd.do('select glu1, name oe2 and resn glu within %s of (name nz and resn lys)'%(motifRange*6.5))
    cmd.do('select glu2, name oe1 and resn glu within %s of (name nz and resn lys)'%(motifRange*7))
    cmd.do('select glu3, name cd and resn glu within %s of (name nz and resn lys)'%(motifRange*7))
    cmd.do('select glu4, name oe1 and resn glu within %s of (name ce and resn lys)'%(motifRange*6))
    cmd.do('select glu5, name cd and resn glu within %s of (name ce and resn lys)'%(motifRange*6))
    cmd.do('select glu6, name oe1 and resn glu within %s of (name cd and resn lys)'%(motifRange*5.5))
    cmd.do('select glu7, name oe2 and resn glu within %s of (name ce and resn lys)'%(motifRange*6))
    cmd.do('select glu8, name oe1 and resn glu within %s of (name cg and resn lys)'%(motifRange*5.5))
    cmd.do('select glu9, name oe1 and resn glu within %s of (name od1 and resn asp)'%(motifRange*10))
    cmd.do('select glu10, name oe2 and resn glu within %s of (name od1 and resn asp)'%(motifRange*10))
    self.byResidue('glu', 10)
    cmd.do('select lys1, name nz and resn lys within %s of (name oe2 and resn glu)'%(motifRange*6.5))
    cmd.do('select lys2, name nz and resn lys within %s of (name oe1 and resn glu)'%(motifRange*7))
    cmd.do('select lys3, name nz and resn lys within %s of (name cd and glu)'%(motifRange*7))
    cmd.do('select lys4, name ce and resn lys within %s of (name oe1 and resn glu)'%(motifRange*6))
    cmd.do('select lys5, name ce and resn lys within %s of (name cd and resn glu)'%(motifRange*6))
    cmd.do('select lys6, name cd and resn lys within %s of (name oe1 and resn glu)'%(motifRange*5.5))
    cmd.do('select lys7, name ce and resn lys within %s of (name oe2 and resn glu)'%(motifRange*6))
    cmd.do('select lys8, name cg and resn lys within %s of (name oe1 and resn glu)'%(motifRange*5.5))
    cmd.do('select lys9, name nz and resn lys within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select lys10, name nz and resn lys within %s of (name od2 and resn asp)'%(motifRange*6))
    cmd.do('select lys11, name ce and resn lys within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select lys12, name ce and resn lys within %s of (name od2 and resn asp)'%(motifRange*6.5))
    cmd.do('select lys13, name cd and resn lys within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select lys14, name cd and resn lys within %s of (name od2 and resn asp)'%(motifRange*7))
    self.byResidue('lys', 14)
    cmd.do('select asp1, name od1 and resn asp within %s of (name oe1 and glu)'%(motifRange*10))
    cmd.do('select asp2, name od1 and resn asp within %s of (name oe2 and glu)'%(motifRange*10))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nz and lys)'%(motifRange*6))
    cmd.do('select asp4, name od2 and resn asp within %s of (name nz and lys)'%(motifRange*6))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ce and lys)'%(motifRange*6))
    cmd.do('select asp6, name od2 and resn asp within %s of (name ce and resn lys)'%(motifRange*6.5))
    cmd.do('select asp7, name od1 and resn asp within %s of (name cd and resn lys)'%(motifRange*6))
    cmd.do('select asp8, name od2 and resn asp within %s of (name cd and resn lys)'%(motifRange*7))
    cmd.do('select asp9, name cg and resn asp within %s of (name cd and resn lys)'%(motifRange*7))
    self.byResidue('asp', 9)
    cmd.select('Cyclin_Kinase', 'lys(asp(glu))')
'''CHECK THIS'''
def adenylatekinase(self, motifRange):
    #p-loop first
    cmd.do('select lys1, name nz and resn lys within %s of (name n and resn gly)'%(motifRange*7.5))
    cmd.do('select lys2, name cg and resn lys within %s of (name c and resn gly)'%(motifRange*6))
    cmd.do('select lys3, name n and resn lys within %s of (name n and resn gly)'%(motifRange*5))
    cmd.do('select lys4, name n and resn lys within %s of (resn gly)'%(motifRange*2))
    cmd.do('select lys5, name c and resn lys within %s of (resn gly)'%(motifRange*2))
    cmd.do('select lys6, name nz and resn lys within %s of (name od2 and resn asp)'%(motifRange*13))
    cmd.do('select lys7, name nz and resn lys within %s of (name ne and resn arg)'%(motifRange*11))
    cmd.do('select lys8, name nz and resn lys within %s of (name nh2 and resn arg)'%(motifRange*9.5))
    self.byResidue('lys', 8)
    cmd.do('select glya1, name n and resn gly within %s of (name nz and lys)'%(motifRange*7.5))
    cmd.do('select glya2, name ca and resn gly within %s of (name cg and lys)'%(motifRange*7))
    cmd.do('select glya3, name c and resn gly within %s of (name n and lys)'%(motifRange*2))
    cmd.do('select glya4, name n and resn gly within %s of (name nh1 and resn arg)'%(motifRange*10))
    self.byResidue('glya', 4)
    cmd.do('select glyb, name n and resn gly within %s of (name c and lys)'%(motifRange*2))
    cmd.select('p-loop', 'lys(glya(byres glyb))')
    cmd.do('select asp1, name od2 and resn asp within %s of (name ne and resn arg)'%(motifRange*5))
    cmd.do('select asp2, name od1 and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5))
    cmd.do('select asp3, name od1 and resn asp within %s of (name nh1 and resn arg)'%(motifRange*5))
    cmd.do('select asp4, name od2 and resn asp within %s of p-loop'%(motifRange*15))
    self.byResidue('aspa', 4)
    cmd.do('select aspb1, name od2 and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5))
    cmd.do('select aspb2, name cg and resn asp within %s of (name cz and resn arg)'%(motifRange*6))
    cmd.do('select aspb3, name od1 and resn asp within %s of (name ne and resn arg)'%(motifRange*5))
    cmd.do('select aspb4, name od2 and resn asp within %s of (name od1 and aspa)'%(motifRange*7))
    cmd.do('select aspb5, name cg and resn asp within %s of (name cg and aspa)'%(motifRange*7))
    cmd.do('select aspb6, name od1 and resn asp within %s of (name od2 and aspa)'%(motifRange*7))
    self.byResidue('asp', 6)
    cmd.do('select arg1, name nh1 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(motifRange*4.9))
    cmd.do('select arg2, name nh2 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(motifRange*4.9))
    self.byResidue('arg', 2)
    cmd.select('adenylatekinase', 'p-loop(asp(aspa(arg)))')
'''CHECK THIS'''
def citratesynth(self, motifRange):
    cmd.do('select his1, name ne2 and resn his within %s of (name og and resn ser)'%(motifRange*5))
    cmd.do('select his2, name ne2 and resn his within %s of (name cb and resn ser)'%(motifRange*5.5))
    cmd.do('select his3, name ce1 and resn his within %s of (name og and resn ser)'%(motifRange*5.5))
    cmd.do('select his4, name ce1 and resn his within %s of (name cb and resn ser)'%(motifRange*6.5))
    cmd.do('select his5, name cd2 and resn his within %s of (name og and resn ser)'%(motifRange*6))
    cmd.do('select his6, name nd1 and resn his within %s of (name og and resn ser)'%(motifRange*7))
    cmd.do('select his7, name nd1 and resn his within %s of (name od2 and resn asp)'%(motifRange*8))
    cmd.do('select his8, name nd1 and resn his within %s of (name cg and resn asp)'%(motifRange*8.5))
    cmd.do('select his9, name o and resn his within %s of (name od2 and resn asp)'%(motifRange*5.5))
    self.byResidue('his10', 9)
    cmd.do('select his11, byres resn his within %s of his10'%(motifRange*8.2))
    cmd.do('select ser1, name og and resn ser within %s of (name ne2 and his10)'%(motifRange*5))
    cmd.do('select ser2, name cb and resn ser within %s of (name ne2 and his10)'%(motifRange*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name ce1 and his10)'%(motifRange*5.5))
    cmd.do('select ser4, name cb and resn ser within %s of (name ce1 and his10)'%(motifRange*6.5))
    cmd.do('select ser5, name og and resn ser within %s of (name cd2 and his10)'%(motifRange*6))
    cmd.do('select ser6, name og and resn ser within %s of (name nd1 and his10)'%(motifRange*7))
    cmd.do('select ser7, name og and resn ser within %s of (name od2 and resn asp)'%(motifRange*12))
    cmd.do('select ser8, name og and resn ser within %s of (name cg and resn asp)'%(motifRange*12))
    cmd.do('select ser9, name og and resn ser within %s of (name od1 and resn asp)'%(motifRange*12))
    self.byResidue('ser', 9)
    cmd.do('select his12, byres resn his within %s of ser'%(motifRange*12))
    cmd.do('select asp1, name od2 and resn asp within %s of (name og and ser)'%(motifRange*12))
    cmd.do('select asp2, name cg and resn asp within %s of (name og and ser)'%(motifRange*12))
    cmd.do('select asp3, name od1 and resn asp within %s of (name og and ser)'%(motifRange*12))
    cmd.do('select asp4, name od2 and resn asp within %s of (name nd1 and his10)'%(motifRange*8))
    cmd.do('select asp5, name cg and resn asp within %s of (name nd1 and his10)'%(motifRange*8.5))
    cmd.do('select asp6, name od2 and resn asp within %s of (name o and his10)'%(motifRange*5.5))
    self.byResidue('asp', 6)
    cmd.do('select his13, byres resn his within %s of asp'%(motifRange*8.5))
    cmd.select('his', 'byres his10 or (byres his11 and byres his12 and byres his13)')
    cmd.select('Citrate_Synth', 'his(asp(ser))')

def tyrosinekinase(self, motifRange):
    cmd.do('select arg1, name nh1 and resn arg within %s of (name cb and resn ala)'%(motifRange*5))
    cmd.do('select arg2, name nh2 and resn arg within %s of (name cb and resn ala)'%(motifRange*5.5))
    cmd.do('select arg3, name cz and resn arg within %s of (name cb and resn ala)'%(motifRange*5.5))
    cmd.do('select arg4, name ne and resn arg within %s of (name cb and resn ala)'%(motifRange*6))
    cmd.do('select arg5, name nh2 and resn arg within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select arg6, name nh2 and resn arg within %s of (name cg and resn asp)'%(motifRange*5.5))
    cmd.do('select arg7, name nh2 and resn arg within %s of (name od2 and resn asp)'%(motifRange*6))
    cmd.do('select arg8, name cz and resn arg within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select arg9, name ne and resn arg within %s of (name od1 and resn asp)'%(motifRange*6))
    cmd.do('select arg10, name ne and resn arg within %s of (name cg and resn asp)'%(motifRange*6.5))
    self.byResidue('arg', 10)
    cmd.do('select asp1, name od1 and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5.5))
    cmd.do('select asp2, name cg and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5.5))
    cmd.do('select asp3, name od2 and resn asp within %s of (name nh2 and arg)'%(motifRange*7))
    cmd.do('select asp4, name od1 and resn asp within %s of (name cz and resn arg)'%(motifRange*6))
    cmd.do('select asp5, name od1 and resn asp within %s of (name ne and resn arg)'%(motifRange*6))
    cmd.do('select asp6, name cg and resn asp within %s of (name ne and resn arg)'%(motifRange*6.5))
    cmd.do('select asp7, name od1 and resn asp within %s of (name cb and resn ala)'%(motifRange*9))
    cmd.do('select asp8, name o and resn asp within %s of (name cb and resn ala)'%(motifRange*8))
    cmd.do('select asp9, name cg and resn asp within %s of (name cb and resn ala)'%(motifRange*8))
    self.byResidue('asp', 9)
    cmd.do('select ala1, name cb and resn ala within %s of (name nh1 and arg)'%(motifRange*5))
    cmd.do('select ala2, name cb and resn ala within %s of (name nh2 and arg)'%(motifRange*5.5))
    cmd.do('select ala3, name cb and resn ala within %s of (name cz and arg)'%(motifRange*5.5))
    cmd.do('select ala4, name cb and resn ala within %s of (name ne and arg)'%(motifRange*6))
    cmd.do('select ala5, name cb and resn ala within %s of (name od1 and asp)'%(motifRange*9))
    cmd.do('select ala6, name cb and resn ala within %s of (name o and asp)'%(motifRange*8))
    cmd.do('select ala7, name cb and resn ala within %s of (name cg and asp)'%(motifRange*8))
    self.byResidue('ala', 7)
    cmd.select('SRC-Kinase', 'ala(asp(arg))')

def hhal(self, motifRange):
    cmd.do('select glu1, name oe2 and resn glu within %s of (name sg and resn cys)'%(motifRange*10))
    cmd.do('select glu2, name cd and resn glu within %s of (name cb and resn cys)'%(motifRange*10))
    cmd.do('select glu3, name oe1 and resn glu within %s of (name ca and resn cys)'%(motifRange*10))
    cmd.do('select glu4, name oe2 and resn glu within %s of (name ne and resn arg)'%(motifRange*5))
    cmd.do('select glu5, name cd and resn glu within %s of (name cz and resn arg)'%(motifRange*6))
    cmd.do('select glu6, name oe1 and resn glu within %s of (name nh2 and resn arg)'%(motifRange*5))
    cmd.do('select glu7, name cg and resn glu within %s of (name ca and resn phe)'%(motifRange*10))
    cmd.do('select glu8, name cd and resn glu within %s of (name cb and resn phe)'%(motifRange*10))
    cmd.do('select glu9, name ca and resn glu within %s of (name cd1 and resn phe)'%(motifRange*7.5))
    self.byResidue('glu', 9)
    cmd.do('select cys1, name sg and resn cys within %s of (name nh1 and resn arg)'%(motifRange*6))
    cmd.do('select cys2, name cb and resn cys within %s of (name cz and resn arg)'%(motifRange*7))
    cmd.do('select cys3, name ca and resn cys within %s of (name nh2 and resn arg)'%(motifRange*8))
    cmd.do('select cys4, name sg and resn cys within %s of (name oe2 and glu)'%(motifRange*10))
    cmd.do('select cys5, name cb and resn cys within %s of (name cd and glu)'%(motifRange*10))
    cmd.do('select cys6, name ca and resn cys within %s of (name oe1 and glu)'%(motifRange*10))
    cmd.do('select cys7, name ca and resn cys within %s of (name ca and resn phe)'%(motifRange*8.5))
    cmd.do('select cys8, name cb and resn cys within %s of (name cd2 and resn phe)'%(motifRange*9))
    cmd.do('select cys9, name sg and resn cys within %s of (name cd1 and resn phe)'%(motifRange*12))
    self.byResidue('cys', 9)
    cmd.do('select arg1, name nh1 and resn arg within %s of (name sg and resn cys)'%(motifRange*6))
    cmd.do('select arg2, name cz and resn arg within %s of (name cb and resn cys)'%(motifRange*7))
    cmd.do('select arg3, name nh2 and resn arg within %s of (name ca and resn cys)'%(motifRange*8))
    cmd.do('select arg4, name ne and resn arg within %s of (name oe2 and glu)'%(motifRange*5))
    cmd.do('select arg5, name cz and resn arg within %s of (name cd and glu)'%(motifRange*6))
    cmd.do('select arg6, name nh2 and resn arg within %s of (name oe1 and glu)'%(motifRange*5))
    cmd.do('select arg7, name nh2 and resn arg within %s of (name ce1 and resn phe)'%(motifRange*10.5))
    cmd.do('select arg8, name cz and resn arg within %s of (name cz and resn phe)'%(motifRange*11.5))
    cmd.do('select arg9, name nh1 and resn arg within %s of (name ce2 and resn phe)'%(motifRange*12))
    self.byResidue('arg', 9)
    cmd.do('select phe1, name ca and resn phe within %s of (name cg and glu)'%(motifRange*10))
    cmd.do('select phe2, name cb and resn phe within %s of (name cb and glu)'%(motifRange*10))
    cmd.do('select phe3, name cd1 and resn phe within %s of (name ca and glu)'%(motifRange*7.5))
    cmd.do('select phe4, name ce1 and resn phe within %s of (name nh2 and resn arg)'%(motifRange*10.5))
    cmd.do('select phe5, name cz and resn phe within %s of (name cz and resn arg)'%(motifRange*11.5))
    cmd.do('select phe6, name ce2 and resn phe within %s of (name nh1 and resn arg)'%(motifRange*12))
    cmd.do('select phe7, name ca and resn phe within %s of (name ca and cys)'%(motifRange*8.5))
    cmd.do('select phe8, name cd2 and resn phe within %s of (name cb and cys)'%(motifRange*9))
    cmd.do('select phe9, name cd1 and resn phe within %s of (name sg and cys)'%(motifRange*12))
    self.byResidue('phe', 9)
    cmd.select('hhal', 'glu(arg(phe(cys)))')

def betainedehydrogenase(self, motifRange):
    cmd.do('select cys1, name sg and resn cys within %s of (name od1 and resn asn)'%(motifRange*8.5))
    cmd.do('select cys2, name cb and resn cys within %s of (name cg and resn asn)'%(motifRange*8.5))
    cmd.do('select cys3, name ca and resn cys within %s of (name nd2 and resn asn)'%(motifRange*7.5))
    cmd.do('select cys4, name sg and resn cys within %s of (name oe1 and resn glu)'%(motifRange*8))
    cmd.do('select cys5, name cb and resn cys within %s of (name cb and resn glu)'%(motifRange*9))
    self.byResidue('cys', 5)
    cmd.do('select glu1, name oe1 and resn glu within %s of (name sg and cys)'%(motifRange*8))
    cmd.do('select glu2, name cb and resn glu within %s of (name cb and cys)'%(motifRange*9))
    cmd.do('select glu3, name oe1 and resn glu within %s of (name nd2 and resn asn)'%(motifRange*13))
    cmd.do('select glu4, name oe2 and resn glu within %s of (name od1 and resn asn)'%(motifRange*14))
    self.byResidue('glu', 4)
    cmd.do('select asn1, name nd2 and resn asn within %s of (name oe1 and glu)'%(motifRange*13))
    cmd.do('select asn2, name od1 and resn asn within %s of (name oe2 and glu)'%(motifRange*14))
    cmd.do('select asn3, name od1 and resn asn within %s of (name sg and cys)'%(motifRange*8.5))
    cmd.do('select asn4, name cg and resn asn within %s of (name cb and cys)'%(motifRange*8.5))
    cmd.do('select asn5, name nd2 and resn asn within %s of (name ca and cys)'%(motifRange*8.5))
    self.byResidue('asn', 5)
    cmd.select('betaine_dehydrogenase', 'cys(asn(glu))')
'''CHECK THIS'''
def serotoninacetyl(self, motifRange):
    cmd.do('select his1, name ne2 and resn his within %s of (name og and resn ser)'%(motifRange*4.5))
    cmd.do('select his2, name ne2 and resn his within %s of (name cb and resn ser)'%(motifRange*5.5))
    cmd.do('select his3, name cd2 and resn his within %s of (name og and resn ser)'%(motifRange*5.5))
    cmd.do('select his4, name cd2 and resn his within %s of (name cb and resn ser)'%(motifRange*6))
    cmd.do('select his5, name ne2 and resn his within %s of (name o and resn leu)'%(motifRange*6))
    cmd.do('select his6, name ce1 and resn his within %s of (name cd1 and resn leu)'%(motifRange*10))
    cmd.do('select his7, name ce1 and resn his within %s of (name cb and resn leu)'%(motifRange*9))
    cmd.do('select his8, name nd1 and resn his within %s of (name og and resn ser)'%(motifRange*7.5))
    cmd.do('select his9, name o and resn his within %s of (name oh and resn tyr)'%(motifRange*10))
    cmd.do('select his10, name cb and resn his within %s of (name oh and resn tyr)'%(motifRange*12))
    self.byResidue('his', 10)
    cmd.do('select ser1, name og and resn ser within %s of (name ne2 and his)'%(motifRange*4.5))
    cmd.do('select ser2, name cb and resn ser within %s of (name ne2 and his)'%(motifRange*5.5))
    cmd.do('select ser3, name og and resn ser within %s of (name cd2 and his)'%(motifRange*5.5))
    cmd.do('select ser4, name cb and resn ser within %s of (name cd2 and his)'%(motifRange*6))
    cmd.do('select ser5, name og and resn ser within %s of (name nd1 and his)'%(motifRange*7.5))
    cmd.do('select ser6, name og and resn ser within %s of (name o and resn leu)'%(motifRange*5))
    cmd.do('select ser7, name og and resn ser within %s of (name cb and resn leu)'%(motifRange*8))
    cmd.do('select ser8, name cb and resn ser within %s of (name o and resn leu)'%(motifRange*5.5))
    cmd.do('select ser9, name n and resn ser within %s of (name cd2 and his)'%(motifRange*5.5))
    self.byResidue('ser', 9)
    cmd.do('select leu1, name o and resn leu within %s of (name ne2 and his)'%(motifRange*6))
    cmd.do('select leu2, name cd1 and resn leu within %s of (name ce1 and his)'%(motifRange*10))
    cmd.do('select leu3, name cb and resn leu within %s of (name ce1 and his)'%(motifRange*9))
    cmd.do('select leu4, name o and resn leu within %s of (name og and ser)'%(motifRange*5))
    cmd.do('select leu5, name cb and resn leu within %s of (name og and ser)'%(motifRange*8))
    cmd.do('select leu6, name o and resn leu within %s of (name cb and ser)'%(motifRange*5.5))
    cmd.do('select leu7, name n and resn leu within %s of (name ce1 and resn his)'%(motifRange*7.5))
    self.byResidue('leu8', 7)
    cmd.do('select leu9, name n and resn leu within %s of (name o and his)'%(motifRange*7))
    cmd.do('select leu10, name n and resn leu within %s of (name c and his)'%(motifRange*6.5))
    cmd.do('select leu11, name n and resn leu within %s of (name n and his)'%(motifRange*8))
    cmd.do('select leu12, name cd1 and resn leu within %s of (name oh and resn tyr)'%(motifRange*6))
    cmd.do('select leu13, name cb and resn leu within %s of (name oh and resn tyr)'%(motifRange*5.5))
    cmd.do('select leu14, name cg and resn leu within %s of (name oh and resn tyr)'%(motifRange*7))
    cmd.do('select leu15, name cd1 and resn leu within %s of (name cz and resn tyr)'%(motifRange*6.5))
    cmd.do('select leu15b, name cd1 and resn leu within %s of (name ce1 and resn tyr)'%(motifRange*5.5))
    self.byResidue('leu16', 15)
    cmd.do('select tyr1, name oh and resn tyr within %s of (name cd1 and leu16)'%(motifRange*6))
    cmd.do('select tyr2, name oh and resn tyr within %s of (name cb and leu16)'%(motifRange*6.5))
    cmd.do('select tyr3, name oh and resn tyr within %s of (name cg and leu16)'%(motifRange*7))
    cmd.do('select tyr4, name cz and resn tyr within %s of (name cd1 and leu16)'%(motifRange*6.5))
    cmd.do('select tyr5, name oh and resn tyr within %s of (name n and his)'%(motifRange*10))
    cmd.do('select tyr6, name cz and resn tyr within %s of (name c and his)'%(motifRange*10.2))
    cmd.do('select tyr7, name ce1 and resn tyr within %s of (name o and ser)'%(motifRange*16))
    self.byResidue('tyr', 7)
    cmd.select('Serotonin_transferase', 'his(ser(leu8(leu16(tyr))))')

#motif options
def motifoption(self, tag):
    if tag == 'Surface Pocket':
        self.surfmotifer()
    elif tag == 'Polar Contacts':
        self.motifcontact()
    elif tag == 'Hide Contacts':
        self.hidecontact()
    elif tag == 'Show Substrate':
        self.showsubstrate()
    elif tag == 'Show label':
        self.labelmotif()
    elif tag == 'Hide Label':
        self.dellabel()
    elif tag == 'Hide Substrate':
        self.hidesubstrate()

#Show binding pocket
def surfmotifer(self):
    objects = cmd.get_names('all')
    cmd.set('transparency', '0.5', 'all')
    try:
        if 'Adjacent' in objects:
            if 'Peroxidase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Peroxidase and !Adjacent')
            if 'carboncarbon' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!carboncarbon and !Adjacent')
            if 'o-glycosyl' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!o-glycosyl and !Adjacent')
            if 'Tkinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Tkinase and !Adjacent')
            if 'Ligase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Ligase and !Adjacent')
            if 'glu_amidotransferase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!glu_amidotransferase and !Adjacent')
            if 'fucoseisomerase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!fucoseisomerase and !Adjacent')
            if 'Aminotransferase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Aminotransferase and !Adjacent')
            if 'Zinc_finger' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Zinc_finger and !Adjacent')
            if 'paplike' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!paplike and !Adjacent')
            if 'carbonicanhydrase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!carbonicanhydrase and !Adjacent')
            if 'tyrophos' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!tyrophos and !Adjacent')
            if 'metalloprotease' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!metalloprotease and !Adjacent')
            if 'superoxide' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!superoxide and !Adjacent')
            if 'lactamase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!lactamase and !Adjacent')
            if 'serineprotease' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!serineprotease and !Adjacent')
            if 'TrioseIsomerase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!TrioseIsomerase and !Adjacent')
            if 'alcoholdehyd' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!alcoholdehyd and !Adjacent')
            if 'aldoreductase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!aldoreductase and !Adjacent')
            if 'Cis-trans' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Cis-trans and !Adjacent')
            if 'NAD-reductase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!NAD-reductase and !Adjacent')
            if 'NAD-reductase2' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!NAD-reductase2 and !Adjacent')
            if 'deacetylase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!deacetylase and !Adjacent')
            if 'chondroitinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!chondroitinase and !Adjacent')
            if 'Hyaluronate_Lyase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Hyaluronate_Lyase and !Adjacent')
            if 'Cyclin_Kinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Cyclin_Kinase and !Adjacent')
            if 'SRC-Kinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!SRC-Kinase and !Adjacent')
            if 'Serotonin_transferase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Serotonin_transferase and !Adjacent')
            if 'deacetylase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!deacetylase and !Adjacent')
            if 'adenylatekinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!adenylatekinase and !Adjacent')
            if 'actase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!actase and !Adjacent')
            if 'Exonuclease3' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Exonuclease3 and !Adjacent')
            if 'Citrate_Synth' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Citrate_Synth and !Adjacent')
            if 'hhal' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!hhal and !Adjacent')
            if 'Exonuclease3' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Exonuclease3 and !Adjacent')
            
            cpksubstrate()
            cmd.orient('all')
        else:
            if 'Peroxidase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Peroxidase')
            if 'carboncarbon' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!carboncarbon')
            if 'o-glycosyl' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!o-glycosyl')
            if 'Tkinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Tkinase')
            if 'Ligase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Ligase')
            if 'glu_amidotransferase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!glu_amidotransferase')
            if 'fucoseisomerase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!fucoseisomerase')
            if 'Aminotransferase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Aminotransferase')
            if 'Zinc_finger' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Zinc_finger')
            if 'paplike' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!paplike')
            if 'carbonicanhydrase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!carbonicanhydrase')
            if 'tyrophos' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!tyrophos')
            if 'metalloprotease' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!metalloprotease')
            if 'superoxide' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!superoxide')
            if 'lactamase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!lactamase')
            if 'serineprotease' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!serineprotease')
            if 'TrioseIsomerase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!TrioseIsomerase')
            if 'alcoholdehyd' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!alcoholdehyd')
            if 'aldoreductase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!aldoreductase')
            if 'Cis-trans' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Cis-trans')
            if 'NAD-reductase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!NAD-reductase')
            if 'NAD-reductase2' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!NAD-reductase2')
            if 'deacetylase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!deacetylase')
            if 'chondroitinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!chondroitinase')
            if 'Hyaluronate_Lyase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Hyaluronate_Lyase')
            if 'Cyclin_Kinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Cyclin_Kinase')
            if 'SRC-Kinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!SRC-Kinase')
            if 'Serotonin_transferase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Serotonin_transferase')
            if 'deacetylase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!deacetylase')
            if 'adenylatekinase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!adenylatekinase')
            if 'actase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!actase')
            if 'Exonuclease3' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Exonuclease3')
            if 'Citrate_Synth' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!Citrate_Synth')
            if 'hhal' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!hhal')
            if 'betaine_dehydrogenase' in objects:
                cmd.show('surface', 'all')
                cmd.hide('cartoon', 'all')
                cmd.color('white', '!betaine_dehydrogenase')
            cpksubstrate()
            cmd.orient('all')
    except:
        showinfo('Alert', 'You must select a motif')

#polar contacts

def motifcontact(self):
    objects = cmd.get_names('all')
    try:        
        try:
            cmd.dist(self.mot+"_polar_conts", self.mot, self.mot, quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable(self.mot+"_polar_conts")
        except:
            cmd.dist("motif_polar_conts", "motif", "motif", quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable("motif_polar_conts")
        if 'Adjacent' in objects:
            cmd.dist('Adjacent_polar_conts', 'Adjacent', 'Adjacent',
                quiet = 1, mode = 2, label = 0, reset = 1)
        if 'substrate' in objects:
            cmd.dist(self.mot+"_around_polar_conts", self.mot,
                "(byobj ("+self.mot+")) and (not ("+self.mot+"))", quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable(self.mot+"_around_polar_conts")
    except:
        showinfo('Alert', "Select a motif first")

def hidecontact(self):
    objects = cmd.get_names('all')
    try:
        try:
            cmd.delete(self.mot+"_polar_conts")
        except:
            cmd.delete("motif_polar_conts")
        if 'Adjacent' in objects:
            cmd.delete('Adjacent_polar_conts')
        if 'substrate' in objects:
            cmd.delete(self.mot+"_around"+"_polar_conts")
    except:
        showinfo('Alert', "No motif polar contacts to hide")

def showsubstrate(self):
    try:
        try:
            cmd.select('substrate', 'byres het within 7 of '+self.mot)
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
            cmd.label(self.mot, "''")
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
            cmd.label('''(name ca+C1*+C1' and (byres('''+self.mot+''')))''',
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

def oxidoreductase(self, tag):
    if tag == 'Superoxide Dismutase':
            self.superoxide()
            self.mot = 'superoxide'
    elif tag == 'Peroxidase':
            self.peroxidase()
            self.mot = 'Peroxidase'
    elif tag == 'Alcohol Dehydrogenase':
            self.alcoholdehyd()
            self.mot = 'alcoholdehyd'
    elif tag == 'Aldose Reductase':
            self.aldoreductase()
            self.mot = 'aldoreductase'
    elif tag == 'NAD Reductase':
            self.nadhbinder()
            self.mot = 'NAD-reductase'
    elif tag == 'NAD Reductase2':
            self.nadhbinder2()
            self.mot = 'NAD-reductase2'
    elif tag == 'Betaine aldehyde dehydrogenase':
            self.betainedehydrogenase()
            self.mot = 'betaine_dehydrogenase'


def transferase(self, tag):
    
    if tag == 'Amino Transferase':
            self.aminotransferase()
            self.mot = 'Aminotransferase'
    elif tag == 'Glutamine Amidotransferase':
            self.glutamine_amidotransferase()
            self.mot = 'glu_amidotransferase'
    elif tag == 'Thymidine Kinase':
            self.thymidinekinase()
            self.mot = 'Tkinase'
    elif tag == 'ACTase':
            self.ACTase()
            self.mot = 'actase'
    elif tag == 'Adenylate Kinase':
            self.adenylatekinase()
            self.mot = 'adenylatekinase'
    elif tag == 'SRC Family Kinase':
            self.tyrosinekinase()
            self.mot = 'SRC-Kinase'
    elif tag == 'Hhal Methyltransferase':
            self.hhal()
            self.mot = 'hhal'
    
    elif tag == 'Serotonin Acetyltransferase':
            self.serotoninacetyl()
            self.mot = 'Serotonin_transferase'
    elif tag == 'Cyclin Dependent Kinase':
            self.cyclinkinase()
            self.mot = 'Cyclin_Kinase'


def hydrolase(self, tag):
    if tag == 'Serine Protease':
            self.serineprotease()
            self.mot = 'serineprotease'
    elif tag == 'Papain Like':
            self.paplike()
            self.mot = 'paplike'
    elif tag == 'Metalloprotease':
            self.metalloprotease()
            self.mot = 'metalloprotease'
    elif tag == 'Tyrosine Phosphatase':
            self.tyrophos()
            self.mot = 'tyrophos'
    elif tag == 'Beta Lactamase':
            self.Blactamase()
            self.mot = 'lactamase'
    elif tag == 'O-Glycosyl':
            self.oglycosyl()
            self.mot = 'o-glycosyl'
    elif tag == 'Cephalosporin deacetylase':
            self.cephdeacetylase()
            self.mot = 'deacetylase'

def lyase(self, tag):
    if tag == 'Carbonic Anhydrase':
            self.carbanhyd()
            self.mot = 'carbonicanhydrase'
    elif tag == 'Carbon Carbon':
            self.carboncarbon()
            self.mot = 'carboncarbon'
    elif tag == 'Chondroitinase':
            self.chondrolyase()
            self.mot = 'chondroitinase'
    elif tag == 'Hyaluronate-Lyase':
            self.hyaluronlyase()
            self.mot = 'Hyaluronate_Lyase'
    elif tag == 'Exonuclease 3':
            self.exonucleaseiii()
            self.mot = 'Exonuclease3'
    elif tag == 'Citrate Synthase':
            self.citratesynth()
            self.mot = 'Citrate_Synth'

def isomerase(self, tag):
    if tag == 'Fucose Isomerase':
            self.fisomerase()
            self.mot = 'fucoseisomerase'
    elif tag == 'Triose Phosphate Isomerase':
            self.trioseisomerase()
            self.mot = 'TrioseIsomerase'
    elif tag == 'FK506 Cis-Trans':
            self.cistransisomerase()
            self.mot = 'Cis-trans'

def ligase(self, tag):
    if tag == 'DNA Ligase':
            self.dnaligase()
            self.mot = 'ligase'

def other(self, tag):
    if tag == 'Zinc Finger':
            self.zincfinger()
            self.mot = 'Zinc_finger'
#after appending motif to motif search field allows user to click on it
#and run the motif function

def allmotif(self):
    motif = self.motifbox.getcurselection()
    for item in motif:
        tag = item
    try:
        if len(tag) == 0:
            print 'No selection for double click'
        elif tag == '2-Cyclin Dependent Kinase':
                self.cyclinkinase()
                self.mot = 'Cyclin_Kinase'
        elif tag == '1-Cyclin Dependent Kinase':
                self.cyclinkinase()
                self.mot = 'Cyclin_Kinase'
        elif tag == '1-Betaine aldehyde dehydrogenase':
                self.betainedehydrogenase()
                self.mot = 'betaine_dehydrogenase'
        elif tag == '1-Betaine aldehyde dehydrogenase':
                self.betainedehydrogenase()
                self.mot = 'betaine_dehydrogenase'
        elif tag == '1-Serotonin Acetyltransferase':
                self.serotoninacetyl()
                self.mot = 'Serotonin_transferase'
        elif tag == '2-Serotonin Acetyltransferase':
                self.serotoninacetyl()
                self.mot = 'Serotonin_transferase'
        elif tag == '1-Zinc Finger':
                self.zincfinger()
                self.mot = 'Zinc_finger'
        elif tag == '1-DNA Ligase':
                self.dnaligase()
                self.mot = 'ligase'
        elif tag == '1-Fucose Isomerase':
                self.fisomerase()
                self.mot = 'fucoseisomerase'
        elif tag == '1-Triose Phosphate Isomerase':
                self.trioseisomerase()
                self.mot = 'TrioseIsomerase'
        elif tag == '1-FK506 Cis-Trans':
                self.cistransisomerase()
                self.mot = 'Cis-trans'
        elif tag == '1-Carbonic Anhydrase':
                self.carbanhyd()
                self.mot = 'carbonicanhydrase'
        elif tag == '1-Carbon Carbon':
                self.carboncarbon()
                self.mot = 'carboncarbon'
        elif tag == '1-Chondroitinase':
                self.chondrolyase()
                self.mot = 'chondroitinase'
        elif tag == '1-Hyaluronate-Lyase':
                self.hyaluronlyase()
                self.mot = 'Hyaluronate_Lyase'
        elif tag == '1-Exonuclease 3':
                self.exonucleaseiii()
                self.mot = 'Exonuclease3'
        elif tag == '1-Citrate Synthase':
                self.citratesynth()
                self.mot = 'Citrate_Synth'
        elif tag == '1-Serine Protease':
                self.serineprotease()
                self.mot = 'serineprotease'
        elif tag == '1-Papain Like':
                self.paplike()
                self.mot = 'paplike'
        elif tag == '1-Metalloprotease':
                self.metalloprotease()
                self.mot = 'metalloprotease'
        elif tag == '1-Tyrosine Phosphatase':
                self.tyrophos()
                self.mot = 'tyrophos'
        elif tag == '1-Beta Lactamase':
                self.Blactamase()
                self.mot = 'lactamase'
        elif tag == '1-O-Glycosyl':
                self.oglycosyl()
                self.mot = 'o-glycosyl'
        elif tag == '1-Cephalosporin deacetylase':
                self.cephdeacetylase()
                self.mot = 'deacetylase'
        elif tag == '1-Amino Transferase':
                self.aminotransferase()
                self.mot = 'Aminotransferase'
        elif tag == '1-Glutamine Amidotransferase':
                self.glutamine_amidotransferase()
                self.mot = 'glu_amidotransferase'
        elif tag == '1-Thymidine Kinase':
                self.thymidinekinase()
                self.mot = 'Tkinase'
        elif tag == '1-ACTase':
                self.ACTase()
                self.mot = 'actase'
        elif tag == '1-Adenylate Kinase':
                self.adenylatekinase()
                self.mot = 'adenylatekinase'
        elif tag == '1-SRC Family Kinase':
                self.tyrosinekinase()
                self.mot = 'SRC-Kinase'
        elif tag == '1-Hhal Methyltransferase':
                self.hhal()
                self.mot = 'hhal'
        elif tag == '1-Superoxide Dismutase':
                self.superoxide()
                self.mot = 'superoxide'
        elif tag == '1-Peroxidase':
                self.peroxidase()
                self.mot = 'Peroxidase'
        elif tag == '1-Alcohol Dehydrogenase':
                self.alcoholdehyd()
                self.mot = 'alcoholdehyd'
        elif tag == '1-Aldose Reductase':
                self.aldoreductase()
                self.mot = 'aldoreductase'
        elif tag == '1-NAD Reductase':
                self.nadhbinder()
                self.mot = 'NAD-reductase'
        elif tag == '1-NAD Reductase2':
                self.nadhbinder2()
                self.mot = 'NAD-reductase2'
        elif tag == '2-Zinc Finger':
                self.zincfinger()
                self.mot = 'Zinc_finger'
        elif tag == '2-DNA Ligase':
                self.dnaligase()
                self.mot = 'ligase'
        elif tag == '2-Fucose Isomerase':
                self.fisomerase()
                self.mot = 'fucoseisomerase'
        elif tag == '2-Triose Phosphate Isomerase':
                self.trioseisomerase()
                self.mot = 'TrioseIsomerase'
        elif tag == '2-FK506 Cis-Trans':
                self.cistransisomerase()
                self.mot = 'Cis-trans'
        elif tag == '2-Carbonic Anhydrase':
                self.carbanhyd()
                self.mot = 'carbonicanhydrase'
        elif tag == '2-Carbon Carbon':
                self.carboncarbon()
                self.mot = 'carboncarbon'
        elif tag == '2-Chondroitinase':
                self.chondrolyase()
                self.mot = 'chondroitinase'
        elif tag == '2-Hyaluronate-Lyase':
                self.hyaluronlyase()
                self.mot = 'Hyaluronate_Lyase'
        elif tag == '2-Exonuclease 3':
                self.exonucleaseiii()
                self.mot = 'Exonuclease3'
        elif tag == '2-Citrate Synthase':
                self.citratesynth()
                self.mot = 'Citrate_Synth'
        elif tag == '2-Serine Protease':
                self.serineprotease()
                self.mot = 'serineprotease'
        elif tag == '2-Papain Like':
                self.paplike()
                self.mot = 'paplike'
        elif tag == '2-Metalloprotease':
                self.metalloprotease()
                self.mot = 'metalloprotease'
        elif tag == '2-Tyrosine Phosphatase':
                self.tyrophos()
                self.mot = 'tyrophos'
        elif tag == '2-Beta Lactamase':
                self.Blactamase()
                self.mot = 'lactamase'
        elif tag == '2-O-Glycosyl':
                self.oglycosyl()
                self.mot = 'o-glycosyl'
        elif tag == '2-Cephalosporin deacetylase':
                self.cephdeacetylase()
                self.mot = 'deacetylase'
        elif tag == '2-Amino Transferase':
                self.aminotransferase()
                self.mot = 'Aminotransferase'
        elif tag == '2-Glutamine Amidotransferase':
                self.glutamine_amidotransferase()
                self.mot = 'glu_amidotransferase'
        elif tag == '2-Thymidine Kinase':
                self.thymidinekinase()
                self.mot = 'Tkinase'
        elif tag == '2-ACTase':
                self.ACTase()
                self.mot = 'actase'
        elif tag == '2-Adenylate Kinase':
                self.adenylatekinase()
                self.mot = 'adenylatekinase'
        elif tag == '2-SRC Family Kinase':
                self.tyrosinekinase()
                self.mot = 'SRC-Kinase'
        elif tag == '2-Hhal Methyltransferase':
                self.hhal()
                self.mot = 'hhal'
        elif tag == '2-Superoxide Dismutase':
                self.superoxide()
                self.mot = 'superoxide'
        elif tag == '2-Peroxidase':
                self.peroxidase()
                self.mot = 'Peroxidase'
        elif tag == '2-Alcohol Dehydrogenase':
                self.alcoholdehyd()
                self.mot = 'alcoholdehyd'
        elif tag == '2-Aldose Reductase':
                self.aldoreductase()
                self.mot = 'aldoreductase'
        elif tag == '2-NAD Reductase':
                self.nadhbinder()
                self.mot = 'NAD-reductase'
        elif tag == '2-NAD Reductase2':
                self.nadhbinder2()
                self.mot = 'NAD-reductase2'
    
    except:
        
        showinfo('Alert', 'There is no motif there')

#def custom motif dropdown selection

def set_motifA(self, tag):
    cmd.deselect()
    self.mA = tag

def set_motifB(self, tag):
    cmd.deselect()
    self.mB = tag

def set_motifC(self, tag):
    cmd.deselect()
    self.mC = tag

def set_motifD(self, tag):
    cmd.deselect()
    self.mD = tag
 
 #def custom motif dropdown selection
def set_motifAA(self, tag):
    cmd.deselect()
    self.mAA = tag

def set_motifAB(self, tag):
    cmd.deselect()
    self.mAB = tag

def set_motifAC(self, tag):
    cmd.deselect()
    self.mAC = tag

def set_motifAD(self, tag):
    cmd.deselect()
    self.mAD = tag

#Custom motif functions


def bimotif(self):
    try:
        update()
        objects = cmd.get_names('all')
        
        
        
        cmd.delete('motif')
        cmd.hide('everything')
        mA = self.mA
        mB = self.mB
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
        mA = self.mA
        mB = self.mB
        mC = self.mC
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
        mA = self.mA
        mB = self.mB
        mC = self.mC
        mD = self.mD
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
        mAA = self.mAA
        mAB = self.mAB
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
        mAA = self.mAA
        mAB = self.mAB
        mAC = self.mAC
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
        mAA = self.mAA
        mAB = self.mAB
        mAC = self.mAC
        mAD = self.mAD
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
    self.range.set(1.0)

def setcusmotif(self):
    a = []
    for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
        a.append(object)
    self.motifdrop.setlist(a)

def runcusmotif(self):
        a = ['']
        for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
            a.append(object)
        motif = self.motifdrop.getcurselection()
        for item in motif:
            tag = item
        try:
             for i in range(1, 100, 1):
                if a[i] in tag:
                    cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[i])
        except:
            pass
            
def motifchecker(event):

    cmd.hide('everything', 'all')
    cmd.remove("(all) and hydro")
    list=[]

    exonucleaseiii2()
    x = cmd.count_atoms('Exonuclease3')
    if x == 42:
       list.append('1-Exonuclease 3')
    if x < 42 and x > 32:
       list.append('2-Exonuclease 3')

    cmd.delete('Exonuclease3')


    cyclinkinase2()
    x = cmd.count_atoms('Cyclin_Kinase')
    if x == 26:
      list.append('1-Cyclin Dependent Kinase')
    if x < 35 and x > 26:
      list.append('2-Cyclin Dependent Kinase')
    if x < 26 and x > 23:
      list.append('2-Cyclin Dependent Kinase')


    citratesynth2()
    x = cmd.count_atoms('Citrate_Synth')
    if x == 34:
       list.append('1-Citrate Synthase')
    if x < 34 and x > 28:
        list.append('2-Citrate Synthase')

    cmd.delete('Citrate_Synth')

    trioseisomerase2()
    x = cmd.count_atoms('TrioseIsomerase')
    if x == 40:
       list.append('1-Triose Phosphate Isomerase')
    if x < 45 and x > 40:
        list.append('2-Triose Phosphate Isomerase')
    if x < 40 and x > 32:
        list.append('2-Triose Phosphate Isomerase')
    if x == 80:
       list.append('1-Triose Phosphate Isomerase')
    if x < 90 and x > 80:
        list.append('2-Triose Phosphate Isomerase')
    if x < 80 and x > 64:
        list.append('2-Triose Phosphate Isomerase')

    serineprotease2()
    x = cmd.count_atoms('serineprotease')
    if x == 24:
       list.append('1-Serine Protease')
    if x < 33 and x > 24:
        list.append('2-Serine Protease')
    if x < 24 and x > 18:
        list.append('2-Serine Protease')
    if x == 48:
       list.append('1-Serine Protease')
    if x < 66 and x > 48:
        list.append('2-Serine Protease')
    if x < 48 and x > 36:
        list.append('2-Serine Protease')
    cmd.delete('serineprotease')

    Blactamase2()
    x = cmd.count_atoms('lactamase')
    if x == 45:
       list.append('1-Beta Lactamase')
    if x < 55 and x > 45:
        list.append('2-Beta Lactamase')
    if x < 45 and x > 35:
        list.append('2-Beta Lactamase')
    if x == 90:
       list.append('1-Beta Lactamase')
    if x < 110 and x > 90:
        list.append('2-Beta Lactamase')
    if x < 90 and x > 70:
        list.append('2-Beta Lactamase')
    cmd.delete('lactamase')

    cmd.select('zn', 'elem zn(elem cu)')
    x = cmd.count_atoms('zn')
    if x > 2:
        superoxide2()
        x = cmd.count_atoms('superoxide')
        if x == 70:
           list.append('1-Superoxide Dismutase')
        if x < 90 and x > 70:
            list.append('2-Superoxide Dismutase')
        if x < 70 and x > 60:
            list.append('2-Superoxide Dismutase')
        if x == 140:
           list.append('1-Superoxide Dismutase')
        if x < 150 and x > 140:
            list.append('2-Superoxide Dismutase')
        if x < 140 and x > 115:
            list.append('2-Superoxide Dismutase')
        cmd.delete('superoxide')
        cmd.delete('zn')
    else:
        cmd.delete('zn')



    cmd.select('zn', 'elem zn')
    x = cmd.count_atoms('zn')
    if x > 1:
        zincfinger2()
        x = cmd.count_atoms('Zinc_finger')
        if x == 32:
           list.append('1-Zinc Finger')
        if x < 50 and x > 32:
            list.append('2-Zinc Finger')
        if x < 32 and x > 20:
            list.append('2-Zinc Finger')
        if x == 64:
           list.append('1-Zinc Finger')
        if x < 100 and x > 64:
            list.append('2-Zinc Finger')
        if x < 64 and x > 40:
            list.append('2-Zinc Finger')
        cmd.delete('zn')
        cmd.delete('Zince_finger')


    aminotransferase2()
    x = cmd.count_atoms('Aminotransferase')
    if x == 27 :
       list.append('1-Amino Transferase')
    if x < 40 and x > 27:
        list.append('2-Amino Transferase')
    if x < 27 and x > 20:
        list.append('2-Amino Transferase')
    if x == 54:
       list.append('1-Amino Transferase')
    if x < 80 and x > 54:
        list.append('2-Amino Transferase')
    if x < 54 and x > 40:
        list.append('2-Amino Transferase')
    cmd.delete('Aminotransferase')

    chondrolyase2()
    x = cmd.count_atoms('chondroitinase')
    if x == 41 :
       list.append('1-Chondroitinase')
    if x < 51 and x > 41:
        list.append('2-Chondroitinase')
    if x < 41 and x > 31:
        list.append('2-Chondroitinase')
    if x == 82:
       list.append('1-Chondroitinase')
    if x < 102 and x > 82:
        list.append('2-Chondroitinase')
    if x < 82 and x > 62:
        list.append('2-Chondroitinase')
    cmd.delete('chonroitinase')

    hyaluronlyase2()
    x = cmd.count_atoms('Hyaluronate_Lyase')
    if x == 41 :
       list.append('1-Hyaluronate-Lyase')
    if x < 51 and x > 41:
        list.append('2-Hyaluronate-Lyase')
    if x < 41 and x > 31:
        list.append('2-Hyaluronate-Lyase')
    if x == 82:
       list.append('1-Hyaluronate-Lyase')
    if x < 102 and x > 82:
        list.append('2-Hyaluronate-Lyase')
    if x < 82 and x > 62:
        list.append('2-Hyaluronate-Lyase')
    cmd.delete('Hyaluronate_Lyase')

    peroxidase2()
    x = cmd.count_atoms('Peroxidase')
    if x == 29 :
       list.append('1-Peroxidase')
    if x < 39 and x > 29:
        list.append('2-Peroxidase')
    if x < 29 and x > 19:
        list.append('2-Peroxidase')
    if x == 29*2 :
       list.append('1-Peroxidase')
    if x < 39*2 and x > 29*2:
        list.append('2-Peroxidase')
    if x < 29*2 and x > 19*2:
        list.append('2-Peroxidase')
    if x == 29*3 :
       list.append('1-Peroxidase')
    if x < 39*3 and x > 29*3:
        list.append('2-Peroxidase')
    if x < 29*3 and x > 19*3:
        list.append('2-Peroxidase')
    if x == 29*4 :
       list.append('1-Peroxidase')
    if x < 39*4 and x > 29*4:
        list.append('2-Peroxidase')
    if x < 29*4 and x > 19*4:
        list.append('2-Peroxidase')
    cmd.delete('Peroxidase')

    nadhbinder22()
    x = cmd.count_atoms('NAD-reductase')
    if x == 20 :
       list.append('1-NAD Reductase')
    if x < 27 and x > 20:
        list.append('2-NAD Reductase')
    if x < 20 and x > 16:
        list.append('2-NAD Reductase')
    if x == 20*2 :
       list.append('1-NAD Reductase')
    if x < 27*2 and x > 20*2:
        list.append('2-NAD Reductase')
    if x < 20*2 and x > 16*2:
        list.append('2-NAD Reductase')
    if x == 20*3 :
       list.append('1-NAD Reductase')
    if x < 27*3 and x > 20*3:
        list.append('2-NAD Reductase')
    if x < 20*3 and x > 16*3:
        list.append('2-NAD Reductase')
    if x == 20*4 :
       list.append('1-NAD Reductase')
    if x < 27*4 and x > 20*4:
        list.append('2-NAD Reductase')
    if x < 20*4 and x > 16*4:
        list.append('2-NAD Reductase')
    cmd.delete('NAD-reductase')

    nadhbinder222()
    x = cmd.count_atoms('NAD-reductase2')
    if x == 21 :
       list.append('1-NAD Reductase2')
    if x < 28 and x > 21:
        list.append('2-NAD Reductase2')
    if x < 21 and x > 17:
        list.append('2-NAD Reductase2')
    if x == 21*2 :
       list.append('1-NAD Reductase2')
    if x < 28*2 and x > 21*2:
        list.append('2-NAD Reductase2')
    if x < 21*2 and x > 17*2:
        list.append('2-NAD Reductase2')
    if x == 21*3 :
       list.append('1-NAD Reductase2')
    if x < 28*3 and x > 21*3:
        list.append('2-NAD Reductase2')
    if x < 21*3 and x > 17*3:
        list.append('2-NAD Reductase2')
    if x == 21*4 :
       list.append('1-NAD Reductase2')
    if x < 28*4 and x > 21*4:
        list.append('2-NAD Reductase2')
    if x < 21*4 and x > 17*4:
        list.append('2-NAD Reductase2')
    cmd.delete('NAD-reductase2')

    tyrosinekinase2()
    x = cmd.count_atoms('SRC-Kinase')
    if x == 24:
       list.append('1-SRC Family Kinase')
    if x < 30 and x > 24:
        list.append('2-SRC Family Kinase')
    if x < 24 and x > 16:
        list.append('2-SRC Family Kinase')
    if x == 24*2:
       list.append('1-SRC Family Kinase')
    if x < 30*2 and x > 24*2:
        list.append('2-SRC Family Kinase')
    if x < 24*2 and x > 16*2:
        list.append('2-SRC Family Kinase')
    cmd.delete('SRC-Kinase')


    cistransisomerase2()
    x = cmd.count_atoms('Cis-trans')
    if x == 36:
       list.append('1-FK506 Cis-Trans')
    if x < 46 and x > 36:
        list.append('2-FK506 Cis-Trans')
    if x < 36 and x > 26:
        list.append('2-FK506 Cis-Trans')
    if x == 36*2:
       list.append('1-FK506 Cis-Trans')
    if x < 46*2 and x > 36*2:
        list.append('2-FK506 Cis-Trans')
    if x < 36*2 and x > 26*2:
        list.append('2-FK506 Cis-Trans')
    cmd.delete('Cis-trans')


    cephdeacetylase2()
    x = cmd.count_atoms('deacetylase')
    if x == 32:
       list.append('1-Cephalosporin deacetylase')
    if x < 42 and x > 32:
        list.append('2-Cephalosporin deacetylase')
    if x < 32 and x > 26:
        list.append('2-Cephalosporin deacetylase')
    if x == 32*2:
       list.append('1-Cephalosporin deacetylase')
    if x < 42*2 and x > 32*2:
        list.append('2-Cephalosporin deacetylase')
    if x < 32*2 and x > 26*2:
        list.append('2-Cephalosporin deacetylase')
    cmd.delete('deacetylase')




    paplike2()
    x = cmd.count_atoms('paplike')
    if x == 25:
      list.append('1-Papain Like')
    if x < 33 and x > 25:
      list.append('2-Papain Like')
    if x < 25 and x > 17:
      list.append('2-Papain Like')
    if x == 25*2:
      list.append('1-Papain Like')
    if x < 33*2 and x > 25*2:
      list.append('2-Papain Like')
    if x < 25*2 and x > 17*2:
      list.append('2-Papain Like')
    if x == 25*3:
      list.append('1-Papain Like')
    if x < 33*3 and x > 25*3:
      list.append('2-Papain Like')
    if x < 25*3 and x > 17*3:
      list.append('2-Papain Like')
    if x == 25*4:
      list.append('1-Papain Like')
    if x < 33*4 and x > 25*4:
      list.append('2-Papain Like')
    if x < 25*4 and x > 17*4:
      list.append('2-Papain Like')
    cmd.delete('paplike')

    hhal2()
    x = cmd.count_atoms('hhal')
    if x == 37:
      list.append('1-Hhal Methyltransferase')
    if x < 47 and x > 37:
      list.append('2-Hhal Methyltransferase')
    if x < 37 and x > 27:
      list.append('2-Hhal Methyltransferase')
    if x == 37*2:
      list.append('1-Hhal Methyltransferase')
    if x < 47*2 and x > 37*2:
      list.append('2-Hhal Methyltransferase')
    if x < 37*2 and x > 27*2:
      list.append('2-Hhal Methyltransferase')
    if x == 37*3:
      list.append('1-Hhal Methyltransferase')
    if x < 47*3 and x > 37*3:
      list.append('2-Hhal Methyltransferase')
    if x < 37*3 and x > 27*3:
      list.append('2-Hhal Methyltransferase')
    if x == 37*4:
      list.append('1-Hhal Methyltransferase')
    if x < 47*4 and x > 37*4:
      list.append('2-Hhal Methyltransferase')
    if x < 37*4 and x > 27*4:
      list.append('2-Hhal Methyltransferase')
    cmd.delete('hhal')

    ACTase2()
    x = cmd.count_atoms('actase')
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

    alcoholdehyd2()
    x = cmd.count_atoms('alcoholdehyd')
    if x == 35:
      list.append('1-Alcohol Dehydrogenase')
    if x < 45 and x > 35:
      list.append('2-Alcohol Dehydrogenase')
    if x < 35 and x > 25:
      list.append('2-Alcohol Dehydrogenase')
    if x == 35*2:
      list.append('1-Alcohol Dehydrogenase')
    if x < 45*2 and x > 35*2:
      list.append('2-Alcohol Dehydrogenase')
    if x < 35*2 and x > 25*2:
      list.append('2-Alcohol Dehydrogenase')
    if x == 35*3:
      list.append('1-Alcohol Dehydrogenase')
    if x < 45*3 and x > 35*3:
      list.append('2-Alcohol Dehydrogenase')
    if x < 35*3 and x > 25*3:
      list.append('2-Alcohol Dehydrogenase')
    if x == 35*4:
      list.append('1-Alcohol Dehydrogenase')
    if x < 45*4 and x > 35*4:
      list.append('2-Alcohol Dehydrogenase')
    if x < 35*4 and x > 25*4:
      list.append('2-Alcohol Dehydrogenase')
    cmd.delete('alcoholdehyd')

    adenylatekinase2()
    x = cmd.count_atoms('adenylatekinase')
    if x == 66:
      list.append('1-Adenylate Kinase')
    if x < 76 and x > 66:
      list.append('2-Adenylate Kinase')
    if x < 66 and x > 56:
      list.append('2-Adenylate Kinase')
    if x == 66*2:
      list.append('1-Adenylate Kinase')
    if x < 76*2 and x > 66*2:
      list.append('2-Adenylate Kinase')
    if x < 66*2 and x > 56*2:
      list.append('2-Adenylate Kinase')
    if x == 66*3:
      list.append('1-Adenylate Kinase')
    if x < 76*3 and x > 66*3:
      list.append('2-Adenylate Kinase')
    if x < 66*3 and x > 56*3:
      list.append('2-Adenylate Kinase')
    if x == 66*4:
      list.append('1-Adenylate Kinase')
    if x < 76*4 and x > 66*4:
      list.append('2-Adenylate Kinase')
    if x < 66*4 and x > 56*4:
      list.append('2-Adenylate Kinase')
    cmd.delete('adenylatekinase')

    aldoreductase2()
    x = cmd.count_atoms('aldoreductase')
    if x == 39:
      list.append('1-Aldose Reductase')
    if x < 49 and x > 39:
      list.append('2-Aldose Reductase')
    if x < 39 and x > 29:
      list.append('2-Aldose Reductase')
    if x == 39*2:
      list.append('1-Aldose Reductase')
    if x < 49*2 and x > 39*2:
      list.append('2-Aldose Reductase')
    if x < 39*2 and x > 29*2:
      list.append('2-Aldose Reductase')
    if x == 39*3:
      list.append('1-Aldose Reductase')
    if x < 49*3 and x > 39*3:
      list.append('2-Aldose Reductase')
    if x < 39*3 and x > 29*3:
      list.append('2-Aldose Reductase')
    if x == 39*4:
      list.append('1Aldose Reductase')
    if x < 49*4 and x > 39*4:
      list.append('2-Aldose Reductase')
    if x < 39*4 and x > 29*4:
      list.append('2-Aldose Reductase')
    cmd.delete('aldoreductase')

    glutamine_amidotransferase2()
    x = cmd.count_atoms('glu_amidotransferase')
    if x == 25:
      list.append('1-Glutamine Amidotransferase')
    if x < 33 and x > 25:
      list.append('2-Glutamine Amidotransferase')
    if x < 25 and x > 17:
      list.append('2-Glutamine Amidotransferase')
    if x == 25*2:
      list.append('1-Glutamine Amidotransferase')
    if x < 33*2 and x > 25*2:
      list.append('2-Glutamine Amidotransferase')
    if x < 25*2 and x > 17*2:
      list.append('2-Glutamine Amidotransferase')
    if x == 25*3:
      list.append('1-Glutamine Amidotransferase')
    if x < 33*3 and x > 25*3:
      list.append('2-Glutamine Amidotransferase')
    if x < 25*3 and x > 17*3:
      list.append('2-Glutamine Amidotransferase')
    if x == 39*4:
      list.append('1-Glutamine Amidotransferase')
    if x < 33*4 and x > 25*4:
      list.append('2-Glutamine Amidotransferase')
    if x < 25*4 and x > 17*4:
      list.append('2-Glutamine Amidotransferase')
    cmd.delete('glu_amidotransferase')

    carboncarbon2()
    x = cmd.count_atoms('carboncarbon')
    if x == 25:
      list.append('1-Carbon Carbon')
    if x < 33 and x > 25:
      list.append('2-Carbon Carbon')
    if x < 25 and x > 17:
      list.append('2-Carbon Carbon')
    if x == 25*2:
      list.append('1-Carbon Carbon')
    if x < 33*2 and x > 25*2:
      list.append('2-Carbon Carbon')
    if x < 25*2 and x > 17*2:
      list.append('2-Carbon Carbon')
    if x == 25*3:
      list.append('1-Carbon Carbon')
    if x < 33*3 and x > 25*3:
      list.append('2-Carbon Carbon')
    if x < 25*3 and x > 17*3:
      list.append('2-Carbon Carbon')
    if x == 39*4:
      list.append('1-Carbon Carbon')
    if x < 33*4 and x > 25*4:
      list.append('2-Carbon Carbon')
    if x < 25*4 and x > 17*4:
      list.append('2-Carbon Carbon')
    cmd.delete('carboncarbon')

    carbanhyd2()
    x = cmd.count_atoms('carbonicanhydrase')
    if x == 32:
      list.append('1-Carbonic Anhydrase')
    if x < 42 and x > 32:
      list.append('2-Carbonic Anhydrase')
    if x < 32 and x > 22:
      list.append('2-Carbonic Anhydrase')
    if x == 32*2:
      list.append('1-Carbonic Anhydrase')
    if x < 42*2 and x > 32*2:
      list.append('2-Carbonic Anhydrase')
    if x < 32*2 and x > 22*2:
      list.append('2-Carbonic Anhydrase')
    if x == 32*3:
      list.append('1-Carbonic Anhydrase')
    if x < 42*3 and x > 32*3:
      list.append('2-Carbonic Anhydrase')
    if x < 32*3 and x > 22*3:
      list.append('2-Carbonic Anhydrase')
    if x == 32*4:
      list.append('1-Carbonic Anhydrase')
    if x < 42*4 and x > 32*4:
      list.append('2-Carbonic Anhydrase')
    if x < 32*4 and x > 22*4:
      list.append('2-Carbonic Anhydrase')
    cmd.delete('carbonicanhydrase')


    fisomerase2()
    x = cmd.count_atoms('fucoseisomerase')
    if x == 19:
      list.append('1-Fucose Isomerase')
    if x < 24 and x > 19:
      list.append('2-Fucose Isomerase')
    if x < 19 and x > 14:
      list.append('2-Fucose Isomerase')
    if x == 19*2:
      list.append('1-Fucose Isomerase')
    if x < 24*2 and x > 19*2:
      list.append('2-Fucose Isomerase')
    if x < 19*2 and x > 14*2:
      list.append('2-Fucose Isomerase')
    if x == 19*3:
      list.append('1-Fucose Isomerase')
    if x < 24*3 and x > 19*3:
      list.append('2-Fucose Isomerase')
    if x < 19*3 and x > 14*3:
      list.append('2-Fucose Isomerase')
    if x == 19*4:
      list.append('1-Fucose Isomerase')
    if x < 24*4 and x > 19*4:
      list.append('2-Fucose Isomerase')
    if x < 19*4 and x > 14*4:
      list.append('2-Fucose Isomerase')
    if x == 19*5:
      list.append('1-Fucose Isomerase')
    if x < 24*5 and x > 19*5:
      list.append('2-Fucose Isomerase')
    if x < 19*5 and x > 14*5:
      list.append('2-Fucose Isomerase')

    cmd.delete('fucoseisomerase')

    tyrophos2()
    x = cmd.count_atoms('tyrophos')
    if x == 31:
      list.append('1-Tyrosine Phosphatase')
    if x < 41 and x > 31:
      list.append('2-Tyrosine Phosphatase')
    if x < 31 and x > 21:
      list.append('2-Tyrosine Phosphatase')
    if x == 31*2:
      list.append('1-Tyrosine Phosphatase')
    if x < 41*2 and x > 31*2:
      list.append('2-Tyrosine Phosphatase')
    if x < 31*2 and x > 21*2:
      list.append('2-Tyrosine Phosphatase')
    if x == 31*3:
      list.append('1-Tyrosine Phosphatase')
    if x < 41*3 and x > 31*3:
      list.append('2-Tyrosine Phosphatase')
    if x < 31*3 and x > 21*3:
      list.append('2-Tyrosine Phosphatase')
    if x == 31*4:
      list.append('1-Tyrosine Phosphatase')
    if x < 41*4 and x > 31*4:
      list.append('2-Tyrosine Phosphatase')
    if x < 31*4 and x > 21*4:
      list.append('2-Tyrosine Phosphatase')
    if x == 31*5:
      list.append('1-Tyrosine Phosphatase')
    if x < 41*5 and x > 31*5:
      list.append('2-Tyrosine Phosphatase')
    if x < 31*5 and x > 21*5:
      list.append('2-Tyrosine Phosphatase')

    betainedehydrogenase2()
    x = cmd.count_atoms('betaine_dehydrogenase')
    if x == 23:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26 and x > 23:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23 and x > 20:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*2:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*2 and x > 23*2:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*2 and x > 20*2:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*3:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*3 and x > 23*3:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*3 and x > 20*3:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*4:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*4 and x > 23*4:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*4 and x > 20*4:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*5:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*5 and x > 20*5:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*5 and x > 20*5:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*6:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*6 and x > 23*6:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*6 and x > 20*6:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*7:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*7 and x > 23*7:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*7 and x > 20*7:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*8:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*8 and x > 23*8:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*8 and x > 20*8:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x == 23*9:
      list.append('1-Betaine aldehyde dehydrogenase')
    if x < 26*9 and x > 23*9:
      list.append('2-Betaine aldehyde dehydrogenase')
    if x < 23*9 and x > 20*9:
      list.append('2-Betaine aldehyde dehydrogenase')

    serotoninacetyl2()
    x = cmd.count_atoms('Serotonin_transferase')
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