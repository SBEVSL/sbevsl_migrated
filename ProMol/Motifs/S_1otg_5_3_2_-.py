'''
FUNC:S_1otg_5_3_2_-
PDB:1otg
EC:5.3.2.-
RESI:pro,phe,arg
LOCI:a-2,35,41;
'''
IDSpec[(('pro','CA'),('rphe','CD1'))] = cmd.select('pro1', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+7.24,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('pro','CA'),('rphe','CE1'))] = cmd.select('pro2', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+7.70,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('pro','CA'),('rphe','CZ'))] = cmd.select('pro3', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.79,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('pro','CB'),('rphe','CD1'))] = cmd.select('pro4', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+5.99,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('pro','CB'),('rphe','CE1'))] = cmd.select('pro5', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+6.37,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('pro','CB'),('rphe','CZ'))] = cmd.select('pro6', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+7.36,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('pro','CD'),('rphe','CD1'))] = cmd.select('pro7', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+6.09,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('pro','CD'),('rphe','CE1'))] = cmd.select('pro8', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+7.08,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('pro','CD'),('rphe','CZ'))] = cmd.select('pro9', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+8.24,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('pro','CA'),('rarg','CZ'))] = cmd.select('pro10', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.30,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('pro','CA'),('rarg','NE'))] = cmd.select('pro11', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.07,resSelectionSubs('arg','NE',subs)))
IDSpec[(('pro','CA'),('rarg','NH1'))] = cmd.select('pro12', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+9.50,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('pro','CB'),('rarg','CZ'))] = cmd.select('pro13', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+9.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('pro','CB'),('rarg','NE'))] = cmd.select('pro14', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+9.39,resSelectionSubs('arg','NE',subs)))
IDSpec[(('pro','CB'),('rarg','NH1'))] = cmd.select('pro15', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+10.91,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('pro','CD'),('rarg','CZ'))] = cmd.select('pro16', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+8.54,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('pro','CD'),('rarg','NE'))] = cmd.select('pro17', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+8.43,resSelectionSubs('arg','NE',subs)))
IDSpec[(('pro','CD'),('rarg','NH1'))] = cmd.select('pro18', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+9.79,resSelectionSubs('arg','NH1',subs)))
IDSpec['pro'] = cmd.select('pro',' br. pro1&br. pro2&br. pro3&br. pro4&br. pro5&br. pro6&br. pro7&br. pro8&br. pro9&br. pro10&br. pro11&br. pro12&br. pro13&br. pro14&br. pro15&br. pro16&br. pro17&br. pro18')
IDSpec['r_pro'] = cmd.count_atoms(resSelectionSubs('pro', subs=subs, selection=True))
cmd.delete('pro1')
cmd.delete('pro2')
cmd.delete('pro3')
cmd.delete('pro4')
cmd.delete('pro5')
cmd.delete('pro6')
cmd.delete('pro7')
cmd.delete('pro8')
cmd.delete('pro9')
cmd.delete('pro10')
cmd.delete('pro11')
cmd.delete('pro12')
cmd.delete('pro13')
cmd.delete('pro14')
cmd.delete('pro15')
cmd.delete('pro16')
cmd.delete('pro17')
cmd.delete('pro18')
IDSpec[(('phe','CD1'),('spro','CA'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.24,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('spro','CB'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+5.99,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('phe','CD1'),('spro','CD'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.09,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('phe','CE1'),('spro','CA'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.70,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('spro','CB'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.37,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('phe','CE1'),('spro','CD'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.08,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('phe','CZ'),('spro','CA'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.79,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('spro','CB'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.36,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('phe','CZ'),('spro','CD'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.24,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('phe','CD1'),('rarg','CZ'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.58,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('phe','CD1'),('rarg','NE'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.51,resSelectionSubs('arg','NE',subs)))
IDSpec[(('phe','CD1'),('rarg','NH1'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+13.79,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('phe','CE1'),('rarg','CZ'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+13.45,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('phe','CE1'),('rarg','NE'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+13.38,resSelectionSubs('arg','NE',subs)))
IDSpec[(('phe','CE1'),('rarg','NH1'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+14.65,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('phe','CZ'),('rarg','CZ'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+14.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('phe','CZ'),('rarg','NE'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+14.51,resSelectionSubs('arg','NE',subs)))
IDSpec[(('phe','CZ'),('rarg','NH1'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+15.90,resSelectionSubs('arg','NH1',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9&br. phe10&br. phe11&br. phe12&br. phe13&br. phe14&br. phe15&br. phe16&br. phe17&br. phe18')
IDSpec['r_phe'] = cmd.count_atoms(resSelectionSubs('phe', subs=subs, selection=True))
cmd.delete('phe1')
cmd.delete('phe2')
cmd.delete('phe3')
cmd.delete('phe4')
cmd.delete('phe5')
cmd.delete('phe6')
cmd.delete('phe7')
cmd.delete('phe8')
cmd.delete('phe9')
cmd.delete('phe10')
cmd.delete('phe11')
cmd.delete('phe12')
cmd.delete('phe13')
cmd.delete('phe14')
cmd.delete('phe15')
cmd.delete('phe16')
cmd.delete('phe17')
cmd.delete('phe18')
IDSpec[(('arg','CZ'),('spro','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.30,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('spro','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.67,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('spro','CD'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.54,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('spro','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.07,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('spro','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.39,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('spro','CD'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.43,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('spro','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.50,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('spro','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.91,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('spro','CD'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.79,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sphe','CD1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.58,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sphe','CE1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.45,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sphe','CZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.67,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('arg','NE'),('sphe','CD1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.51,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sphe','CE1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.38,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sphe','CZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.51,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('sphe','CD1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.79,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sphe','CE1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.65,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sphe','CZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.90,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
IDSpec['S_1otg_5_3_2_-'] = cmd.select('S_1otg_5_3_2_-', 'pro|phe|arg')
cmd.delete('pro')
cmd.delete('phe')
cmd.delete('arg')
