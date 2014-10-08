'''
FUNC:S_1w8o_3_2_1_18
PDB:1w8o
EC:3.2.1.18
RESI:gly,glu,tyr
LOCI:a-92,260,370;
'''
IDSpec[(('gly','CA'),('rtyr','CE1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.05,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','CA'),('rtyr','CZ'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.12,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','CA'),('rtyr','OH'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.52,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','N'),('rtyr','CE1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.34,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','N'),('rtyr','CZ'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.56,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','N'),('rtyr','OH'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.99,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','O'),('rtyr','CE1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.40,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','O'),('rtyr','CZ'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.46,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','O'),('rtyr','OH'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.78,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','CA'),('rglu','CD'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.26,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','CA'),('rglu','OE1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.02,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','CA'),('rglu','OE2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.00,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','N'),('rglu','CD'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.04,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','N'),('rglu','OE1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.69,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','N'),('rglu','OE2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.80,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','O'),('rglu','CD'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.33,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','O'),('rglu','OE1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.15,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','O'),('rglu','OE2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.09,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('tyr','CE1'),('sgly','CA'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.05,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sgly','N'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.34,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sgly','O'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+15.40,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','CA'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.12,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','N'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.56,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','O'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.46,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','CA'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.52,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','N'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.99,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','O'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+13.78,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rglu','CD'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.75,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.15,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.57,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','CZ'),('rglu','CD'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.77,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.51,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.35,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','OH'),('rglu','CD'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.18,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','OH'),('rglu','OE1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.12,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','OH'),('rglu','OE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.60,resSelectionSubs('glu','OE2',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18')
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
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
IDSpec[(('glu','CD'),('sgly','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.26,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','N'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.04,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','O'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.33,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.02,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','N'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.69,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','O'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.15,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.00,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','N'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.80,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','O'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.09,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','CE1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.75,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','CZ'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.77,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','OH'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.18,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CE1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.15,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CZ'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.51,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','OH'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.12,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CE1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.57,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CZ'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.35,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','OH'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.60,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
IDSpec['S_1w8o_3_2_1_18'] = cmd.select('S_1w8o_3_2_1_18', 'gly|tyr|glu')
cmd.delete('gly')
cmd.delete('tyr')
cmd.delete('glu')
