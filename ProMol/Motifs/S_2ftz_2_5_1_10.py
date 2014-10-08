'''
FUNC:S_2ftz_2_5_1_10
PDB:2ftz
EC:2.5.1.10
RESI:arg,phe
LOCI:a-85,197;
'''
IDSpec[(('arg','CZ'),('rphe','CD1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.07,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('arg','CZ'),('rphe','CE1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.13,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('arg','CZ'),('rphe','CZ'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.65,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('arg','NE'),('rphe','CD1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.12,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('arg','NE'),('rphe','CE1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.12,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('arg','NE'),('rphe','CZ'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.55,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('arg','NH1'),('rphe','CD1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.98,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('arg','NH1'),('rphe','CE1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.99,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('arg','NH1'),('rphe','CZ'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.47,resSelectionSubs('phe','CZ',subs)))
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
IDSpec[(('phe','CD1'),('sarg','CZ'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+14.07,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('phe','CD1'),('sarg','NE'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+15.12,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('phe','CD1'),('sarg','NH1'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.98,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sarg','CZ'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+13.13,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('phe','CE1'),('sarg','NE'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+14.12,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('phe','CE1'),('sarg','NH1'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.99,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sarg','CZ'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+13.65,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('phe','CZ'),('sarg','NE'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+14.55,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('phe','CZ'),('sarg','NH1'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.47,resSelectionSubs('arg','NH1',subs,selection=True)))
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
IDSpec['S_2ftz_2_5_1_10'] = cmd.select('S_2ftz_2_5_1_10', 'arg|phe')
cmd.delete('arg')
cmd.delete('phe')
