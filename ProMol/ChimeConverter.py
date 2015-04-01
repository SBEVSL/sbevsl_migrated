'''Converts chime commands to pymol commands'''
from pymol import cmd,util
class ChimeConverter:
    '''Converts chime commands to pymol commands'''
    def __init__(self):
        '''Construtor'''
        self.command = None
        self.args = []
        self.argsLength = 0
        self.rpsts = {'cartoon':'cartoon',
                    'cartoons':'cartoon',
                    'backbone':'ribbon',
                    'spacefill':'spheres',
                    'dots':'dots',
                    'wireframe':'lines',
                    'ribbons':'cartoon',
                    'ribbon':'cartoon'}
    
        self.coloring = {'colour':'color',
                     'color':'color',
                     'background':'bg_color'}
    
        self.individuals = {'center':'zoom',
                    'centre':'zoom'}
    
        self.selections = {'dna':'resn a+g+c+t+u',
                'protein':'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
                    'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+'+
                    'ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+'+
                    'TER+THY+UNK+MSE',
                'hydrophobic':'resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL',
                'hydrophilic':'resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS',
                'acidic':'resn ASP+GLU',
                'basic':'resn ARG+HIS+LYS'}

    def parse(self, x, y):
        '''Parse and store the command'''
        self.args.append(x.lower().strip())
        if y != None:
            self.args.append(y.lower().strip())
        self.argsLength = len(self.args)
        self.command = self.args[0]
        
        if self.command in self.rpsts.keys():
            self.on_off_conversions()
        elif self.command in self.coloring.keys():
            self.coloring_conversions()
        elif self.command in self.individuals.keys():
            self.convert_individual()
        elif self.command == 'spin':
            self.convert_spin()
        elif self.command == 'select':
            self.convert_selections()
        else:
            print 'Error: Chime command not recognized.'

    def on_off_conversions(self):
        '''handle on/off type commands'''
        if self.argsLength > 1 and self.args[1] == 'off':
            cmd.hide(self.rpsts[self.command], 'all')
            print 'PyMOL: hide %s, all'%self.rpsts[self.command]
        else:
            cmd.show(self.rpsts[self.command], 'all')
            print 'PyMOL: show %s, all'%self.rpsts[self.command]
    
    def coloring_conversions(self):
        '''coloring commands'''
        if 'sele' in cmd.get_names('all'):
            currentSel = 'sele'
        else:
            currentSel = 'all'
        if self.argsLength > 1:
            pymCmd = 'PyMOL: %s %s'%(self.coloring[self.command],self.args[1])
            if self.command == 'color' or self.command == 'colour':
                cmd.color(self.args[1], currentSel)
                pymCmd = '%s, %s'%(pymCmd,currentSel)
            elif self.command == 'background':
                cmd.bg_color(self.args[1])
            print pymCmd
        else:
            print 'Usage: %s [color]'%s
    
    def convert_spin(self):
        '''spin the protein'''
        if self.argsLength > 1 and self.args[1] == 'off':
            cmd.mstop()
            cmd.mset()
            pymSpin = 'PyMOL: mstop; mset\n\n'
        else:
            cmd.mset('1 x180')
            util.mroll(1,180,1)
            cmd.mplay()
            pymSpin = 'PyMOL: mset 1 x180; util.mroll(1,180,1); mplay'
        print pymSpin
    
    def convert_selections(self):
        '''select stuff'''
        try:
            if self.argsLength > 1:
                print 'PyMOL: select %s'%self.selections[self.args[1]]
                cmd.select(self.selections[self.args[1]])
            else:
                print 'Usage: select [selection]'
        except:
            print 'Error: Chime command not supported.'
    
    def convert_individual(self):
        '''other commands'''
        cmd.do(self.individuals[self.command])
        print 'PyMOL: %s'%self.individuals[self.command]
cmd.extend('c',lambda x,y=None:CC.ChimeConverter().parse(x,y))
cmd.extend('C',lambda x,y=None:CC.ChimeConverter().parse(x,y))