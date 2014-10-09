'''
FUNC:S_1kbr_2_7_6_3
PDB:1kbr
EC:2.7.6.3
RESI:arg,ala
LOCI:a-82,92;
'''
IDSpec[(('ala','CA'),('rarg','CZ'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ala','CA'),('rarg','NE'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ala','CA'),('rarg','NH1'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ala','CB'),('rarg','CZ'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ala','CB'),('rarg','NE'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ala','CB'),('rarg','NH1'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ala','CG'),('rarg','CZ'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ala','CG'),('rarg','NE'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ala','CG'),('rarg','NH1'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10,resSelectionSubs('arg','NH1',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9')
IDSpec['r_ala'] = cmd.count_atoms(resSelectionSubs('ala', subs=subs, selection=True))
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
IDSpec[(('arg','CZ'),('sala','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sala','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sala','CG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sala','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sala','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sala','CG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sala','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sala','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sala','CG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10,resSelectionSubs('ala','CG',subs,selection=True)))
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
IDSpec['S_1kbr_2_7_6_3'] = cmd.select('S_1kbr_2_7_6_3', 'ala|arg')
cmd.delete('ala')
cmd.delete('arg')