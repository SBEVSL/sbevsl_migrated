'''
FUNC:S_2e9e_1_11_1_7
PDB:2e9e
EC:1.11.1.7
RESI:gln,his,arg
LOCI:a-105,109,255;
'''
IDSpec[(('his','CE1'),('rarg','CZ'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.29,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','CE1'),('rarg','NE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.09,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','CE1'),('rarg','NH1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.66,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','ND1'),('rarg','CZ'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.24,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','ND1'),('rarg','NE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.28,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','ND1'),('rarg','NH1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.22,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','NE2'),('rarg','CZ'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.86,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','NE2'),('rarg','NE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.89,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','NE2'),('rarg','NH1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.43,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','CE1'),('rgln','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.09,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','CE1'),('rgln','NE2'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.91,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','CE1'),('rgln','OE1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.05,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','ND1'),('rgln','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.75,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','ND1'),('rgln','NE2'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.88,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','ND1'),('rgln','OE1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.55,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','NE2'),('rgln','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.46,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','NE2'),('rgln','NE2'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.20,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','NE2'),('rgln','OE1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.58,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('arg','CZ'),('shis','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.29,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','ND1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.24,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','NE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.86,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.09,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','ND1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.28,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','NE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.89,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.66,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','ND1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.22,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','NE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.43,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rgln','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.26,resSelectionSubs('gln','CD',subs)))
IDSpec[(('arg','CZ'),('rgln','NE2'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.90,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('arg','CZ'),('rgln','OE1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.30,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('arg','NE'),('rgln','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.04,resSelectionSubs('gln','CD',subs)))
IDSpec[(('arg','NE'),('rgln','NE2'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.52,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('arg','NE'),('rgln','OE1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.05,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('arg','NH1'),('rgln','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.67,resSelectionSubs('gln','CD',subs)))
IDSpec[(('arg','NH1'),('rgln','NE2'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.49,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('arg','NH1'),('rgln','OE1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.63,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('shis','CE1'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.09,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','ND1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.75,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','NE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','CE1'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+5.91,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','ND1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.88,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','NE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.20,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','CE1'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.05,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','ND1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.55,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','NE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.58,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','CD'),('sarg','CZ'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.26,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gln','CD'),('sarg','NE'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.04,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gln','CD'),('sarg','NH1'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.67,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sarg','CZ'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.90,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gln','NE2'),('sarg','NE'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.52,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gln','NE2'),('sarg','NH1'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.49,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sarg','CZ'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.30,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gln','OE1'),('sarg','NE'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.05,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gln','OE1'),('sarg','NH1'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.63,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18')
IDSpec['r_gln'] = cmd.count_atoms(resSelectionSubs('gln', subs=subs, selection=True))
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
IDSpec['S_2e9e_1_11_1_7'] = cmd.select('S_2e9e_1_11_1_7', 'his|arg|gln')
cmd.delete('his')
cmd.delete('arg')
cmd.delete('gln')
