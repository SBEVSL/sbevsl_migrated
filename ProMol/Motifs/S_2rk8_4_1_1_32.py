'''
FUNC:S_2rk8_4_1_1_32
PDB:2rk8
EC:4.1.1.32
RESI:his,lys,arg
LOCI:a-264,290,405;
'''
IDSpec[(('his','CE1'),('rlys','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','CE1'),('rlys','CE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','CE1'),('rlys','NZ'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','ND1'),('rlys','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','ND1'),('rlys','CE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','ND1'),('rlys','NZ'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','NE2'),('rlys','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','NE2'),('rlys','CE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','NE2'),('rlys','NZ'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','CE1'),('rarg','CZ'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.33,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','CE1'),('rarg','NE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.65,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','CE1'),('rarg','NH1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.70,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','ND1'),('rarg','CZ'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.64,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','ND1'),('rarg','NE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.96,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','ND1'),('rarg','NH1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.00,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','NE2'),('rarg','CZ'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.90,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','NE2'),('rarg','NE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.22,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','NE2'),('rarg','NH1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.13,resSelectionSubs('arg','NH1',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
IDSpec[(('lys','CD'),('shis','CE1'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.13,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('shis','ND1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.13,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','CD'),('shis','NE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.13,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','CE1'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.13,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','ND1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.13,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','NE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.13,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','CE1'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.13,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','ND1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.13,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','NE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.13,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','CD'),('rarg','CZ'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.13,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CD'),('rarg','NE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.13,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CD'),('rarg','NH1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.13,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','CE'),('rarg','CZ'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.13,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CE'),('rarg','NE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.13,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CE'),('rarg','NH1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.13,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','NZ'),('rarg','CZ'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.13,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','NZ'),('rarg','NE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.13,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','NZ'),('rarg','NH1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.13,resSelectionSubs('arg','NH1',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec[(('arg','CZ'),('shis','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.33,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','ND1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.64,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','NE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.90,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.65,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','ND1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.96,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','NE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.22,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.70,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','ND1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.00,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','NE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.13,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.13,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.13,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.13,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.13,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.13,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.13,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.13,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.13,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.13,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2rk8_4_1_1_32'] = cmd.select('S_2rk8_4_1_1_32', 'his|lys|arg')
cmd.delete('his')
cmd.delete('lys')
cmd.delete('arg')
