'''
FUNC:S_2zkx_1_15_1_1
PDB:2zkx
EC:1.15.1.1
RESI:his,arg
LOCI:a-63,143;
'''
IDSpec[(('arg','CZ'),('rhis','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','CZ'),('rhis','ND1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.59,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','CZ'),('rhis','NE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.79,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NE'),('rhis','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.22,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NE'),('rhis','ND1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.89,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NE'),('rhis','NE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.92,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NH1'),('rhis','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.79,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NH1'),('rhis','ND1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.15,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NH1'),('rhis','NE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.48,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('sarg','CZ'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.10,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.22,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NH1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.79,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','CZ'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.59,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.89,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NH1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.15,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','CZ'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.79,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.92,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NH1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.48,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9')
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
IDSpec['S_2zkx_1_15_1_1'] = cmd.select('S_2zkx_1_15_1_1', 'arg|his')
cmd.delete('arg')
cmd.delete('his')
