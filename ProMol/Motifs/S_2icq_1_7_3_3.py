'''
FUNC:S_2icq_1_7_3_3
PDB:2icq
EC:1.7.3.3
RESI:arg,gln
LOCI:a-176,228;
'''
IDSpec[(('gln','CD'),('rarg','CZ'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.74,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gln','CD'),('rarg','NE'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.94,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gln','CD'),('rarg','NH1'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.72,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gln','NE2'),('rarg','CZ'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.17,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gln','NE2'),('rarg','NE'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.42,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gln','NE2'),('rarg','NH1'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.95,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gln','OE1'),('rarg','CZ'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.57,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gln','OE1'),('rarg','NE'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.75,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gln','OE1'),('rarg','NH1'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.63,resSelectionSubs('arg','NH1',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9')
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
IDSpec[(('arg','CZ'),('sgln','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.74,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgln','NE2'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.17,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgln','OE1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.57,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sgln','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.94,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sgln','NE2'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.42,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sgln','OE1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.75,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgln','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.72,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgln','NE2'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.95,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgln','OE1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.63,resSelectionSubs('gln','OE1',subs,selection=True)))
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
IDSpec['S_2icq_1_7_3_3'] = cmd.select('S_2icq_1_7_3_3', 'gln|arg')
cmd.delete('gln')
cmd.delete('arg')
