'''
FUNC:S_3e31_4_2_1_1
PDB:3e31
EC:4.2.1.1
RESI:asp,arg
LOCI:a-44,46;
'''
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.96,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.58,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.82,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.27,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.09,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.13,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.73,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.26,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.51,resSelectionSubs('arg','NH1',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9')
IDSpec['r_asp'] = cmd.count_atoms(resSelectionSubs('asp', subs=subs, selection=True))
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.96,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.27,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.58,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.09,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.26,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.82,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.13,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.51,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_3e31_4_2_1_1'] = cmd.select('S_3e31_4_2_1_1', 'asp|arg')
cmd.delete('asp')
cmd.delete('arg')
