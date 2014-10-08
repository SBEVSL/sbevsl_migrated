'''
FUNC:S_1urb_3_1_3_1
PDB:1urb
EC:3.1.3.1
RESI:ser,arg
LOCI:a-102,166;
'''
IDSpec[(('ser','CA'),('rarg','CZ'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.10,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CA'),('rarg','NE'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CA'),('rarg','NH1'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.52,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','CB'),('rarg','CZ'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.59,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CB'),('rarg','NE'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.67,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CB'),('rarg','NH1'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.35,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','OG'),('rarg','CZ'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.85,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','OG'),('rarg','NE'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','OG'),('rarg','NH1'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.54,resSelectionSubs('arg','NH1',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
IDSpec[(('arg','CZ'),('sser','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.10,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.59,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','OG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.85,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.10,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.67,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','OG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.10,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.52,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.35,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','OG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.54,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_1urb_3_1_3_1'] = cmd.select('S_1urb_3_1_3_1', 'ser|arg')
cmd.delete('ser')
cmd.delete('arg')
