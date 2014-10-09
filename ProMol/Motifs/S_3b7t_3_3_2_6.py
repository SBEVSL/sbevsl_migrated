'''
FUNC:S_3b7t_3_3_2_6
PDB:3b7t
EC:3.3.2.6
RESI:glu,gln,tyr
LOCI:a-271,296,383;
'''
IDSpec[(('tyr','CE1'),('rgln','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.58,resSelectionSubs('gln','CD',subs)))
IDSpec[(('tyr','CE1'),('rgln','NE2'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.48,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('tyr','CE1'),('rgln','OE1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.70,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('tyr','CZ'),('rgln','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.22,resSelectionSubs('gln','CD',subs)))
IDSpec[(('tyr','CZ'),('rgln','NE2'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.11,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('tyr','CZ'),('rgln','OE1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.37,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('tyr','OH'),('rgln','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.67,resSelectionSubs('gln','CD',subs)))
IDSpec[(('tyr','OH'),('rgln','NE2'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.44,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('tyr','OH'),('rgln','OE1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.88,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('tyr','CE1'),('rglu','CD'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.12,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.79,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.53,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','CZ'),('rglu','CD'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.86,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.61,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.22,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','OH'),('rglu','CD'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.01,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','OH'),('rglu','OE1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.75,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','OH'),('rglu','OE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.32,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('gln','CD'),('styr','CE1'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.58,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gln','CD'),('styr','CZ'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.22,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gln','CD'),('styr','OH'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.67,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gln','NE2'),('styr','CE1'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.48,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('styr','CZ'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.11,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gln','NE2'),('styr','OH'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.44,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gln','OE1'),('styr','CE1'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.70,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('styr','CZ'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.37,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gln','OE1'),('styr','OH'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.88,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gln','CD'),('rglu','CD'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.69,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gln','CD'),('rglu','OE1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+8.79,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gln','CD'),('rglu','OE2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.75,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gln','NE2'),('rglu','CD'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.41,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gln','NE2'),('rglu','OE1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.56,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gln','NE2'),('rglu','OE2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+5.52,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gln','OE1'),('rglu','CD'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.24,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gln','OE1'),('rglu','OE1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.22,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gln','OE1'),('rglu','OE2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.19,resSelectionSubs('glu','OE2',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18')
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
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
IDSpec[(('glu','CD'),('styr','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.12,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','CZ'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.86,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','OH'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.01,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.79,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CZ'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.61,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','OH'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.75,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.53,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CZ'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.22,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','OH'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.32,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','CD'),('sgln','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.69,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('sgln','NE2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.41,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('glu','CD'),('sgln','OE1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.24,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgln','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.79,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgln','NE2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.56,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgln','OE1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.22,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgln','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.75,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgln','NE2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.52,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgln','OE1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.19,resSelectionSubs('gln','OE1',subs,selection=True)))
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
IDSpec['S_3b7t_3_3_2_6'] = cmd.select('S_3b7t_3_3_2_6', 'tyr|gln|glu')
cmd.delete('tyr')
cmd.delete('gln')
cmd.delete('glu')