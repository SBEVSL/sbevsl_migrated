'''
FUNC:S_2p9q_2_7_2_3
PDB:2p9q
EC:2.7.2.3
RESI:arg,lys,gly
LOCI:a-38,215,396;
'''
IDSpec[(('arg','CZ'),('rlys','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.76,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','CZ'),('rlys','CE'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+20.89,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','CZ'),('rlys','NZ'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+20.26,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NE'),('rlys','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+22.61,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NE'),('rlys','CE'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.69,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NE'),('rlys','NZ'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+20.99,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NH1'),('rlys','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+22.29,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NH1'),('rlys','CE'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.47,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NH1'),('rlys','NZ'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+20.91,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','CZ'),('rgly','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.07,resSelectionSubs('gly','CA',subs)))
IDSpec[(('arg','CZ'),('rgly','N'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.81,resSelectionSubs('gly','N',subs)))
IDSpec[(('arg','CZ'),('rgly','O'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.05,resSelectionSubs('gly','O',subs)))
IDSpec[(('arg','NE'),('rgly','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.24,resSelectionSubs('gly','CA',subs)))
IDSpec[(('arg','NE'),('rgly','N'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.94,resSelectionSubs('gly','N',subs)))
IDSpec[(('arg','NE'),('rgly','O'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.19,resSelectionSubs('gly','O',subs)))
IDSpec[(('arg','NH1'),('rgly','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.99,resSelectionSubs('gly','CA',subs)))
IDSpec[(('arg','NH1'),('rgly','N'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.83,resSelectionSubs('gly','N',subs)))
IDSpec[(('arg','NH1'),('rgly','O'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.93,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('lys','CD'),('sarg','CZ'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.76,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+22.61,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NH1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+22.29,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','CZ'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+20.89,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+21.69,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NH1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+21.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','CZ'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+20.26,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+20.99,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NH1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+20.91,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.66,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.90,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.16,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+14.60,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+14.70,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.37,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.32,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.28,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.10,resSelectionSubs('gly','O',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec[(('gly','CA'),('sarg','CZ'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.07,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gly','CA'),('sarg','NE'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.24,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gly','CA'),('sarg','NH1'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.99,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gly','N'),('sarg','CZ'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.81,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gly','N'),('sarg','NE'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.94,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gly','N'),('sarg','NH1'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.83,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gly','O'),('sarg','CZ'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.05,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('gly','O'),('sarg','NE'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.19,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('gly','O'),('sarg','NH1'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.93,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','CD'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.66,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','CE'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.60,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','NZ'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.32,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CD'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.90,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CE'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.70,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','N'),('slys','NZ'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.28,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CD'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.16,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CE'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.37,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','O'),('slys','NZ'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
IDSpec['S_2p9q_2_7_2_3'] = cmd.select('S_2p9q_2_7_2_3', 'arg|lys|gly')
cmd.delete('arg')
cmd.delete('lys')
cmd.delete('gly')
