'''
FUNC:S_2h6e_1_1_1_117
PDB:2h6e
EC:1.1.1.117
RESI:arg,thr
LOCI:a-42,43;
'''
IDSpec[(('arg','CZ'),('rthr','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','CZ'),('rthr','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','CZ'),('rthr','OG1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NE'),('rthr','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NE'),('rthr','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NE'),('rthr','OG1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NH1'),('rthr','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NH1'),('rthr','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NH1'),('rthr','OG1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('thr','CA'),('sarg','CZ'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NH1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','CZ'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NH1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','CZ'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NH1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
IDSpec['S_2h6e_1_1_1_117'] = cmd.select('S_2h6e_1_1_1_117', 'arg|thr')
cmd.delete('arg')
cmd.delete('thr')
