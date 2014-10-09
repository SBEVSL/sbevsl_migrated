'''
FUNC:S_1l0g_3_5_2_6
PDB:1l0g
EC:3.5.2.6
RESI:gly,lys,tyr,glu,lys
LOCI:a-64,67,150,272,315;
'''
IDSpec[(('glu','CD'),('rgly','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.38,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','CD'),('rgly','N'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.58,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','CD'),('rgly','O'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.28,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','OE1'),('rgly','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.50,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','OE1'),('rgly','N'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.73,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','OE1'),('rgly','O'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.51,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','OE2'),('rgly','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.84,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','OE2'),('rgly','N'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.94,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','OE2'),('rgly','O'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.91,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.43,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.17,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.04,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.10,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.37,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.98,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.52,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.56,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','CD'),('rtyr','CE1'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.60,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','CD'),('rtyr','CZ'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.62,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','CD'),('rtyr','OH'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.99,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE1'),('rtyr','CE1'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.42,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE1'),('rtyr','CZ'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.42,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE1'),('rtyr','OH'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.87,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE2'),('rtyr','CE1'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.01,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE2'),('rtyr','CZ'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.13,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE2'),('rtyr','OH'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.50,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.94,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.82,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.59,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.83,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.63,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.42,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.83,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.65,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.29,resSelectionSubs('lys','NZ',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36')
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
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
IDSpec[(('gly','CA'),('sglu','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.38,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('sglu','OE1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','CA'),('sglu','OE2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.84,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.58,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','OE1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.73,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','OE2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.94,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.28,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','OE1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.51,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','OE2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.91,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','CA'),('rlys','CD'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.69,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','CA'),('rlys','CE'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.67,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','CA'),('rlys','NZ'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.29,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','N'),('rlys','CD'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.90,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','N'),('rlys','CE'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.98,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','N'),('rlys','NZ'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.42,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','O'),('rlys','CD'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.18,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','O'),('rlys','CE'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.43,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','O'),('rlys','NZ'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.85,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','CA'),('rtyr','CE1'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.98,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','CA'),('rtyr','CZ'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.24,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','CA'),('rtyr','OH'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.87,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','N'),('rtyr','CE1'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.76,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','N'),('rtyr','CZ'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.24,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','N'),('rtyr','OH'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.89,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','O'),('rtyr','CE1'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.81,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','O'),('rtyr','CZ'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.69,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','O'),('rtyr','OH'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.46,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','CA'),('rlys','CD'))] = cmd.select('gly28', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.33,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','CA'),('rlys','CE'))] = cmd.select('gly29', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.67,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','CA'),('rlys','NZ'))] = cmd.select('gly30', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.75,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','N'),('rlys','CD'))] = cmd.select('gly31', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.65,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','N'),('rlys','CE'))] = cmd.select('gly32', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.76,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','N'),('rlys','NZ'))] = cmd.select('gly33', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.60,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','O'),('rlys','CD'))] = cmd.select('gly34', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.74,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','O'),('rlys','CE'))] = cmd.select('gly35', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.81,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','O'),('rlys','NZ'))] = cmd.select('gly36', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.58,resSelectionSubs('lys','NZ',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27&br. gly28&br. gly29&br. gly30&br. gly31&br. gly32&br. gly33&br. gly34&br. gly35&br. gly36')
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
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
cmd.delete('gly28')
cmd.delete('gly29')
cmd.delete('gly30')
cmd.delete('gly31')
cmd.delete('gly32')
cmd.delete('gly33')
cmd.delete('gly34')
cmd.delete('gly35')
cmd.delete('gly36')
IDSpec[(('lys','CD'),('sglu','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.43,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.04,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.98,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.87,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.10,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.52,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.17,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.37,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.56,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CD'),('sgly','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.69,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sgly','N'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.90,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','CD'),('sgly','O'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.18,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.67,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','N'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.98,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','O'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.43,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.29,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','N'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.42,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','O'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.85,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','CD'),('rtyr','CE1'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.95,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CD'),('rtyr','CZ'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.64,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CD'),('rtyr','OH'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.08,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','CE'),('rtyr','CE1'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.57,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CE'),('rtyr','CZ'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.23,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CE'),('rtyr','OH'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.61,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','NZ'),('rtyr','CE1'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.76,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','NZ'),('rtyr','CZ'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.57,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','NZ'),('rtyr','OH'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.88,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.47,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.71,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.09,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.09,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.22,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.61,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.57,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.35,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.44,resSelectionSubs('lys','NZ',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27&br. lys28&br. lys29&br. lys30&br. lys31&br. lys32&br. lys33&br. lys34&br. lys35&br. lys36')
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
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
cmd.delete('lys28')
cmd.delete('lys29')
cmd.delete('lys30')
cmd.delete('lys31')
cmd.delete('lys32')
cmd.delete('lys33')
cmd.delete('lys34')
cmd.delete('lys35')
cmd.delete('lys36')
IDSpec[(('tyr','CE1'),('sglu','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.60,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.42,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.62,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.42,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.13,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.99,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.87,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.50,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sgly','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.98,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sgly','N'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.76,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sgly','O'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.81,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.24,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','N'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.24,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','O'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.69,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.87,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','N'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.89,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','O'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.46,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','CD'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.95,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','CE'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.57,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','NZ'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.76,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CD'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.64,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CE'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.23,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','NZ'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CD'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.08,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CE'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.61,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','NZ'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.88,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rlys','CD'))] = cmd.select('tyr28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.85,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CE1'),('rlys','CE'))] = cmd.select('tyr29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.15,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CE1'),('rlys','NZ'))] = cmd.select('tyr30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.21,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CZ'),('rlys','CD'))] = cmd.select('tyr31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.85,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CZ'),('rlys','CE'))] = cmd.select('tyr32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.56,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CZ'),('rlys','NZ'))] = cmd.select('tyr33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.82,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','OH'),('rlys','CD'))] = cmd.select('tyr34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.31,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','OH'),('rlys','CE'))] = cmd.select('tyr35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.22,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','OH'),('rlys','NZ'))] = cmd.select('tyr36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.13,resSelectionSubs('lys','NZ',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27&br. tyr28&br. tyr29&br. tyr30&br. tyr31&br. tyr32&br. tyr33&br. tyr34&br. tyr35&br. tyr36')
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
cmd.delete('tyr19')
cmd.delete('tyr20')
cmd.delete('tyr21')
cmd.delete('tyr22')
cmd.delete('tyr23')
cmd.delete('tyr24')
cmd.delete('tyr25')
cmd.delete('tyr26')
cmd.delete('tyr27')
cmd.delete('tyr28')
cmd.delete('tyr29')
cmd.delete('tyr30')
cmd.delete('tyr31')
cmd.delete('tyr32')
cmd.delete('tyr33')
cmd.delete('tyr34')
cmd.delete('tyr35')
cmd.delete('tyr36')
IDSpec[(('lys_i','CD'),('sglu','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.94,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sglu','OE1'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.83,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sglu','OE2'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.83,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sglu','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.82,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sglu','OE1'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.63,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sglu','OE2'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.65,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sglu','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.59,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sglu','OE1'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.42,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sglu','OE2'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.29,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','CA'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.33,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','N'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.65,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','O'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.74,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','CA'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.67,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','N'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.76,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','O'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.81,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','CA'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.75,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','N'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.60,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','O'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.58,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.47,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.09,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.71,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.22,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.35,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.09,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.61,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.44,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('styr','CE1'))] = cmd.select('lys_i28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.85,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('styr','CZ'))] = cmd.select('lys_i29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.85,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('styr','OH'))] = cmd.select('lys_i30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.31,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys_i','CE'),('styr','CE1'))] = cmd.select('lys_i31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.15,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('styr','CZ'))] = cmd.select('lys_i32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.56,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('styr','OH'))] = cmd.select('lys_i33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.22,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('styr','CE1'))] = cmd.select('lys_i34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.21,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('styr','CZ'))] = cmd.select('lys_i35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.82,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('styr','OH'))] = cmd.select('lys_i36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.13,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27&br. lys_i28&br. lys_i29&br. lys_i30&br. lys_i31&br. lys_i32&br. lys_i33&br. lys_i34&br. lys_i35&br. lys_i36')
IDSpec['r_lys_i'] = cmd.count_atoms(resSelectionSubs('lys_i', subs=subs, selection=True))
cmd.delete('lys_i1')
cmd.delete('lys_i2')
cmd.delete('lys_i3')
cmd.delete('lys_i4')
cmd.delete('lys_i5')
cmd.delete('lys_i6')
cmd.delete('lys_i7')
cmd.delete('lys_i8')
cmd.delete('lys_i9')
cmd.delete('lys_i10')
cmd.delete('lys_i11')
cmd.delete('lys_i12')
cmd.delete('lys_i13')
cmd.delete('lys_i14')
cmd.delete('lys_i15')
cmd.delete('lys_i16')
cmd.delete('lys_i17')
cmd.delete('lys_i18')
cmd.delete('lys_i19')
cmd.delete('lys_i20')
cmd.delete('lys_i21')
cmd.delete('lys_i22')
cmd.delete('lys_i23')
cmd.delete('lys_i24')
cmd.delete('lys_i25')
cmd.delete('lys_i26')
cmd.delete('lys_i27')
cmd.delete('lys_i28')
cmd.delete('lys_i29')
cmd.delete('lys_i30')
cmd.delete('lys_i31')
cmd.delete('lys_i32')
cmd.delete('lys_i33')
cmd.delete('lys_i34')
cmd.delete('lys_i35')
cmd.delete('lys_i36')
IDSpec['S_1l0g_3_5_2_6'] = cmd.select('S_1l0g_3_5_2_6', 'glu|gly|lys|tyr|lys_i')
cmd.delete('glu')
cmd.delete('gly')
cmd.delete('lys')
cmd.delete('tyr')
cmd.delete('lys_i')