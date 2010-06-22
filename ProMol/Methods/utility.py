from pymol import cmd
from Tkinter import *
import Pmw
from pmg_tk.startup.ProMol import promolglobals as pglob
Pmw.initialise()

# ADD RADIO BUTTONS
# Create and add radio buttons to the GUI
def radioAdd(frame, pos, orient, cmd, label, btn_labels, gridrow,
         gridcol, cspan, rspan, gridstick):
    labels = btn_labels     #the list of labels passed in by the user

    # create the radio button
    newRadio = Pmw.RadioSelect(frame, labelpos = pos, labelmargin = 0,
                    buttontype = 'radiobutton',
                    orient = orient,
                    label_text = label,
                    command = cmd)
     # add it to the gui
    newRadio.grid(row = gridrow, column = gridcol, columnspan = cspan,
             rowspan = rspan, sticky = gridstick, padx = 5)

    # add text to the buttons
    for text in labels:
        newRadio.add(text)
        newRadio.setvalue(labels[0])

# ADD FORMATTING SPACERS
# Add white space to the GUI (used in formatting)
def addSpace(frame, gridrow, gridcol):
    # create the button
    space = Label(frame, text = '            ')
    space.grid(row = gridrow, column = gridcol)

def dim_dim(tag):
    if tag == '2D':
      diment.delete(0,2)
      diment.insert(0,'1')
    else:
      diment.delete(0,2)
      diment.insert(0,'2')

def aagive(event):
    try:
        if name6.get() == 'glycine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'gly, g')
            canvas79.create_image(0,0,image=GLYTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'gly, g')
            canvas79.create_image(0,0,image=GLYGUM,anchor=NW)
        if name6.get() == 'alanine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'ala, a')
            canvas79.create_image(0,0,image=TACOBUENO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'ala, a')
            canvas79.create_image(0,0,image=ALAGUM,anchor=NW)
        if name6.get() == 'valine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'val, v')
            canvas79.create_image(0,0,image=VALTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'val, v')
            canvas79.create_image(0,0,image=VALGUM,anchor=NW)
        if name6.get() == 'leucine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'leu, l')
            canvas79.create_image(0,0,image=LEUTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'leu, l')
            canvas79.create_image(0,0,image=LEUGUM,anchor=NW)
        if name6.get() == 'isoleucine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'ile, i')
            canvas79.create_image(0,0,image=ILETACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'ile, i')
            canvas79.create_image(0,0,image=ILEGUM,anchor=NW)
        if name6.get() == 'methionine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'met, m')
            canvas79.create_image(0,0,image=METTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'met, m')
            canvas79.create_image(0,0,image=METGUM,anchor=NW)
        if name6.get() == 'arginine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'arg, r')
            canvas79.create_image(0,0,image=ARGTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'arg, r')
            canvas79.create_image(0,0,image=ARGGUM,anchor=NW)
        if name6.get() == 'aspartate':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'asp, d')
            canvas79.create_image(0,0,image=ASPTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'asp, d')
            canvas79.create_image(0,0,image=ASPGUM,anchor=NW)
        if name6.get() == 'cysteine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'cys, c')
            canvas79.create_image(0,0,image=CYSTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'cys, c')
            canvas79.create_image(0,0,image=CYSGUM,anchor=NW)
        if name6.get() == 'glutamate':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'glu, e')
            canvas79.create_image(0,0,image=GLUTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'glu, e')
            canvas79.create_image(0,0,image=GLUGUM,anchor=NW)
        if name6.get() == 'glutamine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'gln, q')
            canvas79.create_image(0,0,image=GLNTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'gln, q')
            canvas79.create_image(0,0,image=GLNGUM,anchor=NW)
        if name6.get() == 'histidine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'his, h')
            canvas79.create_image(0,0,image=HISTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'his, h')
            canvas79.create_image(0,0,image=HISGUM,anchor=NW)
        if name6.get() == 'lysine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0,'lys, k')
            canvas79.create_image(0,0,image=LYSTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'lys, k')
            canvas79.create_image(0,0,image=LYSGUM,anchor=NW)
        if name6.get() == 'phenylalanine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'phe, f')
            canvas79.create_image(0,0,image=PHETACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'phe, f')
            canvas79.create_image(0,0,image=PHEGUM,anchor=NW)
        if name6.get() == 'proline':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'pro, p')
            canvas79.create_image(0,0,image=PROTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'pro, p')
            canvas79.create_image(0,0,image=PROGUM,anchor=NW)
        if name6.get() == 'serine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'ser, s')
            canvas79.create_image(0,0,image=SERTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'ser, s')
            canvas79.create_image(0,0,image=SERGUM,anchor=NW)
        if name6.get() == 'threonine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'thr, t')
            canvas79.create_image(0,0,image=THRTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'thr, t')
            canvas79.create_image(0,0,image=THRGUM,anchor=NW)
        if name6.get() == 'tryptophan':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'trp, w')
            canvas79.create_image(0,0,image=TRPTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'trp, w')
            canvas79.create_image(0,0,image=TRPGUM,anchor=NW)
        if name6.get() == 'tyrosine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'tyr, y')
            canvas79.create_image(0,0,image=TYRTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'tyr, y')
            canvas79.create_image(0,0,image=TYRGUM,anchor=NW)
        if name6.get() == 'asparagine':
          if diment.get() == '2':
            name5.delete(0,30)
            name5.insert(0, 'asn, n')
            canvas79.create_image(0,0,image=ASNTACO,anchor=NW)
          else:
            name5.delete(0,30)
            name5.insert(0, 'asn, n')
            canvas79.create_image(0,0,image=ASNGUM,anchor=NW)
    except:
        name5.delete(0,30)
        name5.insert(0, '')
def aaget(event):
    try:
        if name5.get() == 'g':
            if diment.get() == '2':
                name6.delete(0,30)
                name6.insert(0, 'glycine')
                canvas79.create_image(0,0,image=GLYTACO,anchor=NW)
            else:
                name6.delete(0,30)
                name6.insert(0, 'glycine')
                canvas79.create_image(0,0,image=GLYGUM,anchor=NW)
        if name5.get() == 'gly':
            if diment.get() == '2':
                name6.delete(0,30)
                name6.insert(0, 'glycine')
                canvas79.create_image(0,0,image=GLYTACO,anchor=NW)
            else:
                name6.delete(0,30)
                name6.insert(0, 'glycine')
                canvas79.create_image(0,0,image=GLYGUM,anchor=NW)
        if name5.get() == 'a':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'alanine')
              canvas79.create_image(0,0,image=TACOBUENO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'alanine')
              canvas79.create_image(0,0,image=ALAGUM,anchor=NW)
        if name5.get() == 'ala':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'alanine')
              canvas79.create_image(0,0,image=TACOBUENO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'alanine')
              canvas79.create_image(0,0,image=ALAGUM,anchor=NW)
        if name5.get() == 'v':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'valine')
              canvas79.create_image(0,0,image=VALTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'valine')
              canvas79.create_image(0,0,image=VALGUM,anchor=NW)
        if name5.get() == 'val':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'valine')
              canvas79.create_image(0,0,image=VALTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'valine')
              canvas79.create_image(0,0,image=VALGUM,anchor=NW)
        if name5.get() == 'l':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'leucine')
              canvas79.create_image(0,0,image=LEUTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'leucine')
              canvas79.create_image(0,0,image=LEUGUM,anchor=NW)
        if name5.get() == 'leu':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'leucine')
              canvas79.create_image(0,0,image=LEUTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'leucine')
              canvas79.create_image(0,0,image=LEUGUM,anchor=NW)
        if name5.get() == 'i':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'isoleucine')
              canvas79.create_image(0,0,image=ILETACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'isoleucine')
              canvas79.create_image(0,0,image=ILEGUM,anchor=NW)
        if name5.get() == 'ile':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'isoleucine')
              canvas79.create_image(0,0,image=ILETACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'isoleucine')
              canvas79.create_image(0,0,image=ILEGUM,anchor=NW)
        if name5.get() == 'm':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'methionine')
              canvas79.create_image(0,0,image=METTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'methionine')
              canvas79.create_image(0,0,image=METGUM,anchor=NW)
        if name5.get() == 'met':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'methionine')
              canvas79.create_image(0,0,image=METTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'methionine')
              canvas79.create_image(0,0,image=METGUM,anchor=NW)
        if name5.get() == 'r':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'arginine')
              canvas79.create_image(0,0,image=ARGTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'arginine')
              canvas79.create_image(0,0,image=ARGGUM,anchor=NW)
        if name5.get() == 'arg':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'arginine')
              canvas79.create_image(0,0,image=ARGTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'arginine')
              canvas79.create_image(0,0,image=ARGGUM,anchor=NW)
        if name5.get() == 'd':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'aspartate')
              canvas79.create_image(0,0,image=ASPTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'aspartate')
              canvas79.create_image(0,0,image=ASPGUM,anchor=NW)
        if name5.get() == 'asp':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'aspartate')
              canvas79.create_image(0,0,image=ASPTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'aspartate')
              canvas79.create_image(0,0,image=ASPGUM,anchor=NW)
        if name5.get() == 'c':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'cysteine')
              canvas79.create_image(0,0,image=CYSTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'cysteine')
              canvas79.create_image(0,0,image=CYSGUM,anchor=NW)
        if name5.get() == 'c':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'cysteine')
              canvas79.create_image(0,0,image=CYSTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'cysteine')
              canvas79.create_image(0,0,image=CYSGUM,anchor=NW)
        if name5.get() == 'e':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'glutamate')
              canvas79.create_image(0,0,image=GLUTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'glutamate')
              canvas79.create_image(0,0,image=GLUGUM,anchor=NW)
        if name5.get() == 'glu':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'glutamate')
              canvas79.create_image(0,0,image=GLUTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'glutamate')
              canvas79.create_image(0,0,image=GLUGUM,anchor=NW)
        if name5.get() == 'q':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'glutamine')
              canvas79.create_image(0,0,image=GLNTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'glutamine')
              canvas79.create_image(0,0,image=GLNGUM,anchor=NW)
        if name5.get() == 'gln':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'glutamine')
              canvas79.create_image(0,0,image=GLNTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'glutamine')
              canvas79.create_image(0,0,image=GLNGUM,anchor=NW)
        if name5.get() == 'h':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'histidine')
              canvas79.create_image(0,0,image=HISTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'histidine')
              canvas79.create_image(0,0,image=HISGUM,anchor=NW)
        if name5.get() == 'his':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'histidine')
              canvas79.create_image(0,0,image=HISTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'histidine')
              canvas79.create_image(0,0,image=HISGUM,anchor=NW)
        if name5.get() == 'k':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'lysine')
              canvas79.create_image(0,0,image=LYSTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'lysine')
              canvas79.create_image(0,0,image=LYSGUM,anchor=NW)
        if name5.get() == 'lys':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'lysine')
              canvas79.create_image(0,0,image=LYSTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'lysine')
              canvas79.create_image(0,0,image=LYSGUM,anchor=NW)
        if name5.get() == 'f':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'phenylalanine')
              canvas79.create_image(0,0,image=PHETACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'phenylalanine')
              canvas79.create_image(0,0,image=PHEGUM,anchor=NW)
        if name5.get() == 'phe':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'phenylalanine')
              canvas79.create_image(0,0,image=PHETACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'phenylalanine')
              canvas79.create_image(0,0,image=PHEGUM,anchor=NW)
        if name5.get() == 'p' :
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'proline')
              canvas79.create_image(0,0,image=PROTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'proline')
              canvas79.create_image(0,0,image=PROGUM,anchor=NW)
        if name5.get() == 'pro' :
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'proline')
              canvas79.create_image(0,0,image=PROTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'proline')
              canvas79.create_image(0,0,image=PROGUM,anchor=NW)
        if name5.get() == 's':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'serine')
              canvas79.create_image(0,0,image=SERTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'serine')
              canvas79.create_image(0,0,image=SERGUM,anchor=NW)
        if name5.get() == 'ser':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'serine')
              canvas79.create_image(0,0,image=SERTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'serine')
              canvas79.create_image(0,0,image=SERGUM,anchor=NW)
        if name5.get() == 't':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'threonine')
              canvas79.create_image(0,0,image=THRTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'threonine')
              canvas79.create_image(0,0,image=THRGUM,anchor=NW)
        if name5.get() == 'thr':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'threonine')
              canvas79.create_image(0,0,image=THRTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'threonine')
              canvas79.create_image(0,0,image=THRGUM,anchor=NW)
        if name5.get() == 'w':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'tryptophan')
              canvas79.create_image(0,0,image=TRPTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'tryptophan')
              canvas79.create_image(0,0,image=TRPGUM,anchor=NW)
        if name5.get() == 'trp':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0,'tryptophan')
              canvas79.create_image(0,0,image=TRPTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'tryptophan')
              canvas79.create_image(0,0,image=TRPGUM,anchor=NW)
        if name5.get() == 'y':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'tyrosine')
              canvas79.create_image(0,0,image=TYRTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'tyrosine')
              canvas79.create_image(0,0,image=TRYGUM,anchor=NW)
        if name5.get() == 'tyr':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'tyrosine')
              canvas79.create_image(0,0,image=TYRTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'tyrosine')
              canvas79.create_image(0,0,image=TRYGUM,anchor=NW)
        if name5.get() == 'n':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'asparagine')
              canvas79.create_image(0,0,image=ASNTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'asparagine')
              canvas79.create_image(0,0,image=ASNGUM,anchor=NW)
        if name5.get() == 'asn':
            if diment.get() == '2':
              name6.delete(0,30)
              name6.insert(0, 'asparagine')
              canvas79.create_image(0,0,image=ASNTACO,anchor=NW)
            else:
              name6.delete(0,30)
              name6.insert(0, 'asparagine')
              canvas79.create_image(0,0,image=ASNGUM,anchor=NW)
    except:
        name6.delete(0,30)
        name6.insert(0, '')
def getsequence(event):
    import webbrowser
    webbrowser.open('http://www.rcsb.org/pdb/downloadFile.do?fileFormat=FASTA&compression=NO&structureId='+ pdber.get())
def gotofasta(event):
    import webbrowser
    webbrowser.open('http://fasta.bioch.virginia.edu/')
def getabstract(event):
    import webbrowser
    webbrowser.open('http://www.rcsb.org/pdb/pubmed.do?structureId='+ pdber.get())
def gotorcsb():
    import webbrowser
    webbrowser.open('http://www.rcsb.org/pdb/Welcome.do')
    
def fetchurl():
    import webbrowser
    webbrowser.open('http://eds.bmc.uu.se/cgi-bin/eds/rama?pdbCode='+enterpdb.get())
def dis(event):
    cmd.wizard('Distance')
    
def selectresi(event):
    try:
        cmd.select('resi %s' % (xr.get()))
    except:
        print 'Invalid selection'
        
#----------Selection function for individual amino acids----------
#-----Experienced people just use Sequence viewer, which is recommended----
def selres(*args):
    if x.get() == 'ala' :
        cmd.select('alanine', 'resn ala')
    if x.get() == 'asn' :
        cmd.select('asparagine', 'resn asn')
    if x.get() == 'val' :
        cmd.select('valine', 'resn val')
    if x.get() == 'leu' :
        cmd.select('leucine', 'resn leu')
    if x.get() == 'ile' :
        cmd.select('isoleucine', 'resn ile')
    if x.get() == 'met' :
        cmd.select('methionine', 'resn met')
    if x.get() == 'pro' :
        cmd.select('proline', 'resn pro')
    if x.get() == 'phe' :
        cmd.select('phenylalanine', 'resn phe')
    if x.get() == 'tyr' :
        cmd.select('tyrosine', 'resn tyr')
    if x.get() == 'trp' :
        cmd.select('tryptophan', 'resn trp')
    if x.get() == 'ser' :
        cmd.select('serine', 'resn ser')
    if x.get() == 'thr' :
        cmd.select('threonine', 'resn thr')
    if x.get() == 'cys' :
        cmd.select('cysteine', 'resn cys')
    if x.get() == 'lys' :
        cmd.select('lysine', 'resn lys')
    if x.get() == 'arg' :
        cmd.select('arginine', 'resn arg')
    if x.get() == 'his' :
        cmd.select('histidine', 'resn his')
    if x.get() == 'asp' :
        cmd.select('aspartate', 'resn asp')
    if x.get() == 'glu' :
        cmd.select('glutamate', 'resn glu')
    if x.get() == 'gln' :
        cmd.select('glutamine', 'resn gln')
    if x.get() == 'a' :
        cmd.select('alanine', 'resn ala')
    if x.get() == 'n' :
        cmd.select('asparagine', 'resn asn')
    if x.get() == 'v' :
        cmd.select('valine', 'resn val')
    if x.get() == 'l' :
        cmd.select('leucine', 'resn leu')
    if x.get() == 'i' :
        cmd.select('isoleucine', 'resn ile')
    if x.get() == 'm' :
        cmd.select('methionine', 'resn met')
    if x.get() == 'p' :
        cmd.select('proline', 'resn pro')
    if x.get() == 'f' :
        cmd.select('phenylalanine', 'resn phe')
    if x.get() == 'y':
        cmd.select('tyrosine', 'resn tyr')
    if x.get() == 'w':
        cmd.select('tryptophan', 'resn trp')
    if x.get() == 's' :
        cmd.select('serine', 'resn ser')
    if x.get() == 't' :
        cmd.select('threonine', 'resn thr')
    if x.get() == 'c' :
        cmd.select('cysteine', 'resn cys')
    if x.get() == 'k' :
        cmd.select('lysine', 'resn lys')
    if x.get() == 'r' :
        cmd.select('arginine', 'resn arg')
    if x.get() == 'h' :
        cmd.select('histidine', 'resn his')
    if x.get() == 'd' :
        cmd.select('aspartate', 'resn asp')
    if x.get() == 'e' :
        cmd.select('glutamate', 'resn glu')
    if x.get() == 'q' :
        cmd.select('glutamine', 'resn gln')
cmd.extend('selres',selres)
def loadmapps(event):
    root = Tk()
    group = Pmw.Group(root, tag_text='Electron Density Mapping')#And a new group
    group.grid(row=0, column=0, padx=0, pady=0, sticky=NW)
    interior = group.interior()
    framemesh = Frame(interior)
    framemesh.grid(row=2, column=0, padx=0, pady=2, sticky=W)
    framesurf = Frame(interior)
    framesurf.grid(row=4, column=0, padx=0, pady=2, sticky=W)
    framedots = Frame(interior)
    framedots.grid(row=3, column=0, padx=0, pady=2, sticky=W)
    framemeshsel = Frame(interior)
    framemeshsel.grid(row=2, column=1, padx=0, pady=2, sticky=W)
    framedotsel = Frame(interior)
    framedotsel.grid(row=3, column=1, padx=0, pady=2, sticky=W)
    framesurfsel = Frame(interior)
    framesurfsel.grid(row=4, column=1, padx=0, pady=2, sticky=W)
    framenameit = Frame(interior)
    framenameit.grid(row=0, column=1, padx=0, pady=2, sticky=SW)
    framepdbname = Frame(interior)
    framepdbname.grid(row=1, column=1, padx=0, pady=2, sticky=SW)
    framemapper = Frame(interior)
    framemapper.grid(row=4, column=2, padx=0, pady=2, sticky=W)
    imesh = Button (framemesh)#Mesh Button
    imesh.grid(row=2, column=0, padx=0, pady=2, sticky=W)
    imesh.configure(text="Mesh")
    imesh.configure(width="10")
    nameit = Entry (framenameit, width = 8)#Name Object Entry
    nameit.grid(row=0, column=1, padx=0, pady=0, sticky=SW)
    pdbname = Entry (framepdbname, width = 8)#Map Filename Entry
    pdbname.grid(row=1, column=1, padx=0, pady=0, sticky=SW)
    labelno = Label(interior, text = 'Name Object:')#Label for Object
    labelno.grid(row=0, column=0, padx=0, pady=0, sticky=SW)
    labelid = Label(interior, text = 'Map Filename:')#Label for Filename
    labelid.grid(row=1, column=0, padx=0, pady=0, sticky=SW)
    ehelp = Button (interior)
    ehelp.grid(row=5, column=0, padx=0, pady=2, sticky=W)
    ehelp.configure(text="Help")
    ehelp.configure(width="10")
    getmapper = Entry(interior, width = 4)
    getmapper.grid(row=3, column=2, padx=2, pady=2, sticky=SW)
    loadbtn = Button(interior, text = "Load Map")
    loadbtn.grid(row=5, column=2, padx=4, pady=2, sticky=W)
    def loadccp4(event):      
        file = askopenfilename(defaultextension=".ccp4", initialdir=pglob.HOME)
        if len(file)>0:
            cmd.load(file)
        interior.mainloop()
    loadbtn.bind('<Button-1>', loadccp4)
    #go to upsalla website for maps
    def getmap():
        import webbrowser
        webbrowser.open('http://eds.bmc.uu.se/cgi-bin/eds/gen_maps_zip.pl?pdbCode='+ getmapper.get())
    mapper = Button (framemapper)
    mapper.grid(row=4, column=2, padx=0, pady=5, sticky=W)
    mapper.configure(text="Get Map")
    mapper.configure(width="10")
    
    labelcon = Label(interior, text = 'Input PDB code')
    labelcon.grid(row=2, column=2, padx=0, pady=2, sticky=SW)
    framecontour1 = Frame(interior)
    framecontour1.grid(row=1, column=2, padx=0, pady=0, sticky=NW)
    contour1  = Scale(framecontour1, width =8)
    contour1.configure(troughcolor="#ffffff")
    contour1.configure(length="65")
    contour1.configure(orient="horizontal")
    contour1.configure(resolution="0.05")
    contour1.configure(to="4.0")
    contour1.grid(row=1, column=2, padx=0, pady=0, sticky=NW)
    contour1.set(1.0)
    
    mapper.bind('<Button-1>', getmap)
    
    
    def elhelp(event):
        import webbrowser
        webbrowser.open(pglob.pathmaker('EDMHelp.htm'))
    ehelp.bind('<Button-1>', elhelp)
     #---isomesh function
    def emesh(event):
        delcrea()
        try:
            if len(nameit.get()) < 1:
                
                
                showinfo("Error", 'Enter a name for the object')
                interior.mainloop()
            elif len(pdbname.get()) < 1:
                
                
                showinfo('Error', "Enter the Map Filename")
                interior.mainloop()
            
            else:
                cmd.isomesh(nameit.get(),pdbname.get(), contour1.get())
        except:
            
            
            showinfo("Error", 'No map is present')
            interior.mainloop()

    
    
    imesh.bind('<Button-1>', emesh)
    idot = Button (framedots)
    idot.grid(row=3, column=0, padx=0, pady=5, sticky=W)
    idot.configure(text="Dots")
    idot.configure(width="10")
    #Isodot function
    def edot(event):
        delcrea()
        try:
            if len(nameit.get()) < 1:    
                showinfo("Error", 'Enter a name for the object')
                interior.mainloop()
            elif len(pdbname.get()) < 1:    
                showinfo('Error', "Enter the Map Filename")
                interior.mainloop()
            else:
                cmd.isodot(nameit.get(), pdbname.get(), contour1.get())
        except: 
            showinfo("Error", 'No map is present')
            interior.mainloop()
    idot.bind('<Button-1>', edot)
    isurf = Button(framesurf)
    isurf.grid(row=2, column=1, padx=0, pady=5, sticky=W)
    isurf.configure(text="Surface")
    isurf.configure(width="10")
    #Isosurface function
    def esurf(event):
        delcrea()
        try:
            if len(nameit.get()) < 1:
                
                
                showinfo("Error", 'Enter a name for the object')
                interior.mainloop()
            elif len(pdbname.get()) < 1:
                
                
                showinfo('Error', "Enter the Map Filename")
                interior.mainloop()
            else:
                cmd.isosurface(nameit.get(), pdbname.get(), contour1.get())
        except:
            
            
            showinfo("Error", 'No map is present')
            interior.mainloop()
    
    isurf.bind('<Button-1>', esurf)



#----------Electron Density Map on only Selection------------------------
    labelcon = Label(interior, text = '  Contour')
    labelcon.grid(row=0, column=2, padx=0, pady=2, sticky=SW)
    imesh1 = Button (framemeshsel)
    imesh1.grid(row=4, column=0, padx=0, pady=5, sticky=W)
    imesh1.configure(text="Mesh Select")
    imesh1.configure(width="10")
    #isomesh on only selection
    
    def emesh1(*args):
        delcrea()
        try:
            if len(nameit.get()) < 1:
                
                
                showinfo("Error", 'Enter a name for the object')
                interior.mainloop()
            elif len(pdbname.get()) < 1:
                
                
                showinfo('Error', "Enter the Map Filename")
                interior.mainloop()
            
            else:
                cmd.isomesh(nameit.get(),pdbname.get(), contour1.get(), ('sele'))
        except:
            cmd.orient('all')
            
            
            showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
            interior.mainloop()
    cmd.extend('emesh1',emesh1)
    imesh1.bind('<Button-1>', emesh1)
    idot1 = Button (framedotsel)
    idot1.grid(row=5, column=0, padx=0, pady=2, sticky=W)
    idot1.configure(text="Dots Select")
    idot1.configure(width="10")
    #isodot on only selection
    def edot1(event):
        delcrea()
        try:
            if len(nameit.get()) < 1:                
                showinfo("Error", 'Enter a name for the object')
                interior.mainloop()
            elif len(pdbname.get()) < 1:                
                showinfo('Error', "Enter the Map Filename")
                interior.mainloop()
            else:
                cmd.isodot(nameit.get(), pdbname.get(), contour1.get(), ('sele'))
        except:
            cmd.orient('all')            
            showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
            interior.mainloop()
    
    
    idot1.bind('<Button-1>', edot1)
    isurf1 = Button(framesurfsel)
    isurf1.grid(row=4, column=1, padx=0, pady=2, sticky=W)
    isurf1.configure(text="Surface Select")
    isurf1.configure(width="12")
    #isosurface on only selection
    def esurf1(event):
        delcrea()
        try:
            if len(nameit.get()) < 1:
                
                
                showinfo("Error", 'Enter a name for the object')
                interior.mainloop()
            elif len(pdbname.get()) < 1:
                
                
                showinfo('Error', "Enter the Map Filename")
                interior.mainloop()
            
            else:
                cmd.isosurface(nameit.get(), pdbname.get(), contour1.get(), ('sele'))
        except:
            cmd.orient('all')
            
            
            showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
            interior.mainloop()
    
    isurf1.bind('<Button-1>', esurf1)
    
    
    frame = Frame(interior)
    frame.grid(row=5, column=1, padx=0, pady=0, sticky=SW)
    doublemapbtn = Button(frame, text = 'Double resolution')
    doublemapbtn.grid(row=5, column=1, padx=0, pady=3, sticky=SW)
    
    balloon = Pmw.Balloon(interior)
    balloon.bind(frame, "Please be patient.\nButton should only be used once.\nPyMol will close if used twice.")
    
    #doubles map resolution (permanent because Pymol has errors associated
    #with halving the map resolution)
    def doublemapres(*args):
        try:
            cmd.map_double(pdbname.get(), '1')
        
        except:
            
            
            showinfo("Error", 'No map is present')
            interior.mainloop()
    doublemapbtn.bind('<Button-1>', doublemapres)
    cmd.extend('doublemapres',doublemapres)
    # 99 red balloons, floating in a summer sky
    balloon1 = Pmw.Balloon(interior)
    balloon1.bind(framemesh, "Display entire map as a mesh.")
    balloon2 = Pmw.Balloon(interior)
    balloon2.bind(framedots, "Display entire map as dots.")
    balloon3 = Pmw.Balloon(interior)
    balloon3.bind(framesurf, "Display entire map as surface.")
    balloon5 = Pmw.Balloon(interior)
    balloon5.bind(framemeshsel, "Must have PDB loaded.\n Display mesh on only selected residues (sele).")
    balloon6 = Pmw.Balloon(interior)
    balloon6.bind(framedotsel, "Must have PDB loaded.\n Display dots on only selected residues (sele).")
    balloon7 = Pmw.Balloon(interior)
    balloon7.bind(framesurfsel, "Must have PDB loaded.\n Display surface on only selected residues (sele).")
    balloon8 = Pmw.Balloon(interior)
    balloon8.bind(framenameit, "After loading map, must name the object\n to allow for more than one map instance.")
    balloon9 = Pmw.Balloon(interior)
    balloon9.bind(framepdbname, "After loading map, must enter filename\n of map to be viewed for PyMol to use it.")
    balloon10 = Pmw.Balloon(interior)
    balloon10.bind(framemapper, "View Help button for information on getting maps.")
    balloon11 = Pmw.Balloon(interior)
    balloon11.bind(framecontour1, "After altering countour click again\n on map view of choice for change to occur.")
