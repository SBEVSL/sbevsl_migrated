class ChimeConverter:
    
    #------Constructor----------
    def __init__(self):
        # initialize variables
        self.cmdLine = ' '
        self.command = ' '
        self.results = ' '
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
    
        selections = {'dna':'resn a+g+c+t+u',
                'protein':'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
                    'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+'+
                    'ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+'+
                    'TER+THY+UNK+MSE',
                'hydrophobic':'resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL',
                'hydrophilic':'resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS',
                'acidic':'resn ASP+GLU',
                'basic':'resn ARG+HIS+LYS'}
    # parse the command
    def parseIt(self, input, commLine, resultBox):
        
        self.cmdLine = commLine
        self.results = resultBox
    
    # get rid of capitalizations and leading/ending
    # white space
        ui = input.lower()
        ui = ui.strip()
        
        # store the command
        self.args = ui.split()
        self.argsLength = len(self.args)
        
        self.command = self.args[0]
        
        # representations
        if self.command in self.rpsts.keys():
            # repeat the command back to the user
            self.results.appendtext('Chime: ' + ui + '\n')
            self.on_off_conversions()
        # coloring stuff
        elif self.command in self.coloring.keys():
            # repeat the command back to the user
            self.results.appendtext('Chime: ' + ui + '\n')
            self.coloring_conversions()
        
        # commands without additional arguments
        elif self.command in self.individuals.keys():
            # repeat the command back to the user
            self.results.appendtext('Chime: ' + ui + '\n')
            self.convert_individual()
        
        # action commands ( such as spin )
        elif self.command == 'spin':
            self.results.appendtext('Chime: ' + ui + '\n')
            self.convert_spin()
        # selections from the user
        elif self.command == 'select':
            self.results.appendtext('Chime: ' + ui + '\n')
            self.convert_selections()
        # if the command is not recognized, let the user know
        else:
            self.results.appendtext('Error:Chime command not recognized.\n\n')
            self.cmdLine.clear()
            #self.cmdLine.focus_force()
    #-----------------------------------------#
    #        Chime Conversion Methods         #
    #-----------------------------------------#
    
    # handle on/off type commands
    def on_off_conversions(self):
        pymShow = 'PyMOL: show '+ self.rpsts[self.command] + ', all\n\n'
        pymHide = 'PyMOL: hide ' + self.rpsts[self.command]+ ', all\n\n'
        if self.args[0] == 'backbone':
            cmd.hide('everything')
            cmd.show('ribbon', 'all')
            pymShow = ('PyMOL: hide everything; show '+self.rpsts[self.command]
                +', all\n\n')
    
        if self.argsLength > 1:
            switch = self.args[1]
            if switch == 'on':
                cmd.show(self.rpsts[self.command], 'all')
                self.results.appendtext(pymShow)
            else:
                cmd.hide(self.rpsts[self.command], 'all')
                self.results.appendtext(pymHide)
        else:
            cmd.show(self.rpsts[self.command], 'all')
            self.results.appendtext(pymShow)
    
    # background command
    def coloring_conversions(self):
        selections = cmd.get_names('all')
        currentSel = selections[len(selections)-1]
        #print currentSel
        if self.argsLength > 1:
            pymCmd = 'PyMOL: '+self.coloring[self.command]+' '+self.args[1]
            if self.command == 'color' or self.command == 'colour':
                cmd.color(self.args[1], currentSel)
                pymCmd = pymCmd + ', '+currentSel+'\n\n'
            elif self.command == 'background':
                cmd.bg_color(self.args[1])
                pymCmd = pymCmd + '\n\n'
            self.results.appendtext(pymCmd)
        else:
            self.results.appendtext('Usage: '+self.command+' + [color]\n\n')
    
    def convert_spin(self):
        pymSpin = 'PyMOL: mset 1 x180; util.mroll(1,180,1); mplay\n\n'
        if self.argsLength > 1:
            if self.args[1] == 'off':
                cmd.do('mstop; mset')
                pymSpin = 'PyMOL: mstop; mset\n\n'
            else:
                cmd.do('mset 1 x180; util.mroll(1,180,1);mplay')
        else:
            cmd.do('mset 1 x180; util.mroll(1,180,1);mplay')
        self.results.appendtext(pymSpin)
    
    # convert chime selections
    def convert_selections(self):
        try:
            if self.argsLength > 1:
                pymSelect = 'PyMOL: select '+selections[self.args[1]]+'\n\n'
                self.results.appendtext(pymSelect)
                cmd.select(selections[self.args[1]])
            else:
                self.results.appendtext('Usage: select [selection]')
        except:
            showinfo('Error', 'That is not a supported command')
    
    # 'individual command' conversions
    def convert_individual(self):
        pymShow = 'PyMOL: '+self.individuals[self.command]+'\n\n'
        cmd.do(self.individuals[self.command])
        self.results.appendtext(pymShow)