'''
FUNC:S_1bem_1_11_1_5
PDB:1bem
EC:1.11.1.5
RESI:arg,his,asn
LOCI:a-48,52,82;
'''
IDSpec[(('arg','CZ'),('rhis','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.67,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','CZ'),('rhis','ND1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.60,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','CZ'),('rhis','NE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.65,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NE'),('rhis','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.19,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NE'),('rhis','ND1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.97,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NE'),('rhis','NE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.84,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NH1'),('rhis','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.87,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NH1'),('rhis','ND1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.59,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NH1'),('rhis','NE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.28,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','CZ'),('rasn','CG'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.30,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','CZ'),('rasn','ND2'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.61,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','CZ'),('rasn','OD1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.44,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NE'),('rasn','CG'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.92,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NE'),('rasn','ND2'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.19,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NE'),('rasn','OD1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.98,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NH1'),('rasn','CG'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.65,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NH1'),('rasn','ND2'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.99,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NH1'),('rasn','OD1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.98,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('his','CE1'),('sarg','CZ'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.67,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.19,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NH1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.87,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','CZ'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.60,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.97,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NH1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.59,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','CZ'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.65,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.84,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NH1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.28,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','CE1'),('rasn','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.66,resSelectionSubs('asn','CG',subs)))
IDSpec[(('his','CE1'),('rasn','ND2'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.77,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('his','CE1'),('rasn','OD1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.52,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('his','ND1'),('rasn','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.68,resSelectionSubs('asn','CG',subs)))
IDSpec[(('his','ND1'),('rasn','ND2'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.72,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('his','ND1'),('rasn','OD1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.46,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('his','NE2'),('rasn','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.83,resSelectionSubs('asn','CG',subs)))
IDSpec[(('his','NE2'),('rasn','ND2'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.87,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('his','NE2'),('rasn','OD1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.63,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sarg','CZ'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.30,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NE'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.92,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NH1'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.65,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','CZ'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.61,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NE'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.19,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NH1'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.99,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','CZ'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.44,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NE'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.98,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NH1'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.98,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','CG'),('shis','CE1'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.66,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asn','CG'),('shis','ND1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.68,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asn','CG'),('shis','NE2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.83,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('shis','CE1'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.77,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('shis','ND1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.72,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asn','ND2'),('shis','NE2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.87,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('shis','CE1'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.52,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('shis','ND1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.46,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asn','OD1'),('shis','NE2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.63,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18')
IDSpec['r_asn'] = cmd.count_atoms(resSelectionSubs('asn', subs=subs, selection=True))
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
IDSpec['S_1bem_1_11_1_5'] = cmd.select('S_1bem_1_11_1_5', 'arg|his|asn')
cmd.delete('arg')
cmd.delete('his')
cmd.delete('asn')
