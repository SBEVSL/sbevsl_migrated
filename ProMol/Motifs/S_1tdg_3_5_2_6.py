'''
FUNC:S_1tdg_3_5_2_6
PDB:1tdg
EC:3.5.2.6
RESI:ser,lys,gly,glu
LOCI:a-70,73,130,166;
'''
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.75,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.31,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.56,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.78,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.31,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.36,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.78,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.43,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.94,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','CD'),('rgly','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.21,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','CD'),('rgly','N'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.52,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','CD'),('rgly','O'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.82,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','OE1'),('rgly','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.66,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','OE1'),('rgly','N'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.04,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','OE1'),('rgly','O'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.11,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','OE2'),('rgly','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.67,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','OE2'),('rgly','N'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.95,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','OE2'),('rgly','O'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.62,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','CD'),('rser','CA'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.91,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','CD'),('rser','CB'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.32,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','CD'),('rser','OG'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.46,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE1'),('rser','CA'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.33,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE1'),('rser','CB'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.63,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE1'),('rser','OG'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.60,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE2'),('rser','CA'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.75,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE2'),('rser','CB'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.26,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE2'),('rser','OG'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.57,resSelectionSubs('ser','OG',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27')
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
IDSpec[(('lys','CD'),('sglu','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.75,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.78,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.78,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.31,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.43,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.56,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.36,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.94,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.29,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.00,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.72,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.25,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.24,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.05,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.08,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.19,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.58,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CD'),('rser','CA'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.73,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CD'),('rser','CB'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.83,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CD'),('rser','OG'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.07,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CE'),('rser','CA'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.56,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CE'),('rser','CB'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.64,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CE'),('rser','OG'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.47,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','NZ'),('rser','CA'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.27,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','NZ'),('rser','CB'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.94,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','NZ'),('rser','OG'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.46,resSelectionSubs('ser','OG',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
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
IDSpec[(('gly','CA'),('sglu','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.21,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('sglu','OE1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.66,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','CA'),('sglu','OE2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.67,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.52,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','OE1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.04,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','OE2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.95,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.82,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','OE1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.11,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','OE2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.62,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','CD'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.29,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','CE'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.25,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','NZ'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.08,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CD'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.00,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CE'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.24,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','N'),('slys','NZ'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.19,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CD'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.72,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CE'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.05,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','O'),('slys','NZ'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.58,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','CA'),('rser','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.33,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','CA'),('rser','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.21,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','CA'),('rser','OG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.83,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','N'),('rser','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.36,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','N'),('rser','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.25,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','N'),('rser','OG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.06,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','O'),('rser','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.63,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','O'),('rser','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.66,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','O'),('rser','OG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.81,resSelectionSubs('ser','OG',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27')
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
IDSpec[(('ser','CA'),('sglu','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.91,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.33,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.75,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.32,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.63,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.26,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.46,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.60,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.57,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.73,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.56,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','NZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.27,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.83,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.64,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','NZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.94,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.47,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','NZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.46,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.33,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','N'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.36,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','O'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.63,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.21,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','N'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.25,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','O'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.66,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.83,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','N'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.06,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','O'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.81,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27')
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
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
IDSpec['S_1tdg_3_5_2_6'] = cmd.select('S_1tdg_3_5_2_6', 'glu|lys|gly|ser')
cmd.delete('glu')
cmd.delete('lys')
cmd.delete('gly')
cmd.delete('ser')
