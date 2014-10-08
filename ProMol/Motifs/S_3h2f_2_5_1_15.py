'''
FUNC:S_3h2f_2_5_1_15
PDB:3h2f
EC:2.5.1.15
RESI:asn,arg
LOCI:a-27,254;
'''
IDSpec[(('arg','CZ'),('rasn','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.44,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','CZ'),('rasn','ND2'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.71,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','CZ'),('rasn','OD1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.23,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NE'),('rasn','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.09,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NE'),('rasn','ND2'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.37,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NE'),('rasn','OD1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.80,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('arg','NH1'),('rasn','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.67,resSelectionSubs('asn','CG',subs)))
IDSpec[(('arg','NH1'),('rasn','ND2'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.80,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('arg','NH1'),('rasn','OD1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.55,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sarg','CZ'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+13.44,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NE'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+14.09,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','CG'),('sarg','NH1'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+13.67,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','CZ'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.71,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NE'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+14.37,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','ND2'),('sarg','NH1'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.80,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','CZ'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+14.23,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NE'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+14.80,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asn','OD1'),('sarg','NH1'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+14.55,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9')
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
IDSpec['S_3h2f_2_5_1_15'] = cmd.select('S_3h2f_2_5_1_15', 'arg|asn')
cmd.delete('arg')
cmd.delete('asn')
