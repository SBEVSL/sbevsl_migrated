'''
FUNC:S_1r3s_4_1_1_37
PDB:1r3s
EC:4.1.1.37
RESI:gly,tyr
LOCI:a-86,164;
'''
IDSpec[(('tyr','CE1'),('rgly','CA'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.74,resSelectionSubs('gly','CA',subs)))
IDSpec[(('tyr','CE1'),('rgly','N'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.18,resSelectionSubs('gly','N',subs)))
IDSpec[(('tyr','CE1'),('rgly','O'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.78,resSelectionSubs('gly','O',subs)))
IDSpec[(('tyr','CZ'),('rgly','CA'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.84,resSelectionSubs('gly','CA',subs)))
IDSpec[(('tyr','CZ'),('rgly','N'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+13.29,resSelectionSubs('gly','N',subs)))
IDSpec[(('tyr','CZ'),('rgly','O'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.18,resSelectionSubs('gly','O',subs)))
IDSpec[(('tyr','OH'),('rgly','CA'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.84,resSelectionSubs('gly','CA',subs)))
IDSpec[(('tyr','OH'),('rgly','N'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+13.28,resSelectionSubs('gly','N',subs)))
IDSpec[(('tyr','OH'),('rgly','O'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.40,resSelectionSubs('gly','O',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9')
IDSpec['r_tyr'] = cmd.count_atoms(resSelectionSubs('tyr', subs=subs, selection=True))
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
IDSpec[(('gly','CA'),('styr','CE1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.74,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gly','CA'),('styr','CZ'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.84,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gly','CA'),('styr','OH'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.84,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gly','N'),('styr','CE1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.18,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gly','N'),('styr','CZ'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.29,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gly','N'),('styr','OH'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.28,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gly','O'),('styr','CE1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.78,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gly','O'),('styr','CZ'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.18,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gly','O'),('styr','OH'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.40,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9')
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
IDSpec['S_1r3s_4_1_1_37'] = cmd.select('S_1r3s_4_1_1_37', 'tyr|gly')
cmd.delete('tyr')
cmd.delete('gly')