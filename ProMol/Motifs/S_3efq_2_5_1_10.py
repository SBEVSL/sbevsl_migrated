'''
FUNC:S_3efq_2_5_1_10
PDB:3efq
EC:2.5.1.10
RESI:arg,phe
LOCI:a-112,251;
'''
IDSpec[(('phe','CD1'),('rarg','CZ'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+14.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('phe','CD1'),('rarg','NE'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.59,resSelectionSubs('arg','NE',subs)))
IDSpec[(('phe','CD1'),('rarg','NH1'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+13.52,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('phe','CE1'),('rarg','CZ'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+13.62,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('phe','CE1'),('rarg','NE'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+14.48,resSelectionSubs('arg','NE',subs)))
IDSpec[(('phe','CE1'),('rarg','NH1'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+12.45,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('phe','CZ'),('rarg','CZ'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.35,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('phe','CZ'),('rarg','NE'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+13.24,resSelectionSubs('arg','NE',subs)))
IDSpec[(('phe','CZ'),('rarg','NH1'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.22,resSelectionSubs('arg','NH1',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9')
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
IDSpec[(('arg','CZ'),('sphe','CD1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.67,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sphe','CE1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.62,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sphe','CZ'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.35,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('arg','NE'),('sphe','CD1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.59,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sphe','CE1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.48,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sphe','CZ'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.24,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('sphe','CD1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.52,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sphe','CE1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.45,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sphe','CZ'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.22,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9')
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
IDSpec['S_3efq_2_5_1_10'] = cmd.select('S_3efq_2_5_1_10', 'phe|arg')
cmd.delete('phe')
cmd.delete('arg')
