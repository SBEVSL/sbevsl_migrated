'''
FUNC:S_1qao_2_1_1_48
PDB:1qao
EC:2.1.1.48
RESI:gly,glu,asn
LOCI:a-38,59,101;
'''
IDSpec[(('gly','CA'),('rasn','CG'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.83,resSelectionSubs('asn','CG',subs)))
IDSpec[(('gly','CA'),('rasn','ND2'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.87,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('gly','CA'),('rasn','OD1'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.65,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('gly','N'),('rasn','CG'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.43,resSelectionSubs('asn','CG',subs)))
IDSpec[(('gly','N'),('rasn','ND2'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.66,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('gly','N'),('rasn','OD1'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.18,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('gly','O'),('rasn','CG'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.22,resSelectionSubs('asn','CG',subs)))
IDSpec[(('gly','O'),('rasn','ND2'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.05,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('gly','O'),('rasn','OD1'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.24,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('gly','CA'),('rglu','CD'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.46,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','CA'),('rglu','OE1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.43,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','CA'),('rglu','OE2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.12,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','N'),('rglu','CD'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.47,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','N'),('rglu','OE1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.60,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','N'),('rglu','OE2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.12,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','O'),('rglu','CD'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.42,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','O'),('rglu','OE1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.18,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','O'),('rglu','OE2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.22,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('asn','CG'),('sgly','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.83,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sgly','N'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.43,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asn','CG'),('sgly','O'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.22,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asn','ND2'),('sgly','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.87,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sgly','N'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.66,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asn','ND2'),('sgly','O'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.05,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asn','OD1'),('sgly','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.65,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sgly','N'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.18,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asn','OD1'),('sgly','O'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.24,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asn','CG'),('rglu','CD'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','CG'),('rglu','OE1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.74,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','CG'),('rglu','OE2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+13.32,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','ND2'),('rglu','CD'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.50,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','ND2'),('rglu','OE1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.34,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','ND2'),('rglu','OE2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.89,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','OD1'),('rglu','CD'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+13.78,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','OD1'),('rglu','OE1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.63,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','OD1'),('rglu','OE2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+14.09,resSelectionSubs('glu','OE2',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18')
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
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
IDSpec[(('glu','CD'),('sgly','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.46,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','N'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.47,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','O'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.42,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.43,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','N'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.60,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','O'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.18,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.12,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','N'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.12,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','O'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.22,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','CG'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.92,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','ND2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.50,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','OD1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.78,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','CG'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.74,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','ND2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.34,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','OD1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.63,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','CG'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.32,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','ND2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.89,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','OD1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.09,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_1qao_2_1_1_48'] = cmd.select('S_1qao_2_1_1_48', 'gly|asn|glu')
cmd.delete('gly')
cmd.delete('asn')
cmd.delete('glu')
