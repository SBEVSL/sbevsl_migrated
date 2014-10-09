'''
FUNC:S_2icj_5_3_3_2
PDB:2icj
EC:5.3.3.2
RESI:cys,glu,glu,trp
LOCI:a-87,116,149,197;
'''
IDSpec[(('glu','CD'),('rcys','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.44,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','CD'),('rcys','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.90,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','CD'),('rcys','SG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.75,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE1'),('rcys','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.74,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE1'),('rcys','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.15,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE1'),('rcys','SG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.81,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE2'),('rcys','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.06,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE2'),('rcys','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.62,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE2'),('rcys','SG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.71,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','CD'),('rtrp','CE2'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.04,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','CD'),('rtrp','CZ2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.31,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','CD'),('rtrp','NE1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.75,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE1'),('rtrp','CE2'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.26,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE1'),('rtrp','CZ2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.72,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE1'),('rtrp','NE1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.81,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE2'),('rtrp','CE2'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.09,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE2'),('rtrp','CZ2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.12,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE2'),('rtrp','NE1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.90,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','CD'),('rglu','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.34,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','CD'),('rglu','OE1'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.35,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','CD'),('rglu','OE2'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.33,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.05,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE1'),('rglu','OE1'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.96,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu','OE2'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.11,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.51,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE2'),('rglu','OE1'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.61,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu','OE2'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.46,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('cys','CA'),('sglu','CD'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.44,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.74,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.06,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','CD'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.90,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.15,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.62,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','CD'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.75,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.81,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.71,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','CA'),('rtrp','CE2'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.07,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('cys','CA'),('rtrp','CZ2'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.96,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('cys','CA'),('rtrp','NE1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.94,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('cys','CB'),('rtrp','CE2'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.56,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('cys','CB'),('rtrp','CZ2'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.50,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('cys','CB'),('rtrp','NE1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.54,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('cys','SG'),('rtrp','CE2'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.04,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('cys','SG'),('rtrp','CZ2'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.50,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('cys','SG'),('rtrp','NE1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.37,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('cys','CA'),('rglu','CD'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.09,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CA'),('rglu','OE1'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.70,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CA'),('rglu','OE2'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.53,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','CB'),('rglu','CD'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.93,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CB'),('rglu','OE1'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.42,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CB'),('rglu','OE2'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.43,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','SG'),('rglu','CD'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.97,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','SG'),('rglu','OE1'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.25,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','SG'),('rglu','OE2'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.68,resSelectionSubs('glu','OE2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
cmd.delete('cys19')
cmd.delete('cys20')
cmd.delete('cys21')
cmd.delete('cys22')
cmd.delete('cys23')
cmd.delete('cys24')
cmd.delete('cys25')
cmd.delete('cys26')
cmd.delete('cys27')
IDSpec[(('trp','CE2'),('sglu','CD'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.04,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.26,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.09,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','CD'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.72,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.12,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','CD'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.75,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.81,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.90,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','CE2'),('scys','CA'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.07,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('trp','CE2'),('scys','CB'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+5.56,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('trp','CE2'),('scys','SG'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+5.04,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('trp','CZ2'),('scys','CA'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.96,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('trp','CZ2'),('scys','CB'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+5.50,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('trp','CZ2'),('scys','SG'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+5.50,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('trp','NE1'),('scys','CA'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.94,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('trp','NE1'),('scys','CB'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+5.54,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('trp','NE1'),('scys','SG'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+4.37,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('trp','CE2'),('rglu','CD'))] = cmd.select('trp19', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.67,resSelectionSubs('glu','CD',subs)))
IDSpec[(('trp','CE2'),('rglu','OE1'))] = cmd.select('trp20', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.00,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('trp','CE2'),('rglu','OE2'))] = cmd.select('trp21', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.30,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('trp','CZ2'),('rglu','CD'))] = cmd.select('trp22', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.80,resSelectionSubs('glu','CD',subs)))
IDSpec[(('trp','CZ2'),('rglu','OE1'))] = cmd.select('trp23', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.18,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('trp','CZ2'),('rglu','OE2'))] = cmd.select('trp24', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.43,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('trp','NE1'),('rglu','CD'))] = cmd.select('trp25', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+11.77,resSelectionSubs('glu','CD',subs)))
IDSpec[(('trp','NE1'),('rglu','OE1'))] = cmd.select('trp26', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+10.99,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('trp','NE1'),('rglu','OE2'))] = cmd.select('trp27', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+11.50,resSelectionSubs('glu','OE2',subs)))
IDSpec['trp'] = cmd.select('trp',' br. trp1&br. trp2&br. trp3&br. trp4&br. trp5&br. trp6&br. trp7&br. trp8&br. trp9&br. trp10&br. trp11&br. trp12&br. trp13&br. trp14&br. trp15&br. trp16&br. trp17&br. trp18&br. trp19&br. trp20&br. trp21&br. trp22&br. trp23&br. trp24&br. trp25&br. trp26&br. trp27')
IDSpec['r_trp'] = cmd.count_atoms(resSelectionSubs('trp', subs=subs, selection=True))
cmd.delete('trp1')
cmd.delete('trp2')
cmd.delete('trp3')
cmd.delete('trp4')
cmd.delete('trp5')
cmd.delete('trp6')
cmd.delete('trp7')
cmd.delete('trp8')
cmd.delete('trp9')
cmd.delete('trp10')
cmd.delete('trp11')
cmd.delete('trp12')
cmd.delete('trp13')
cmd.delete('trp14')
cmd.delete('trp15')
cmd.delete('trp16')
cmd.delete('trp17')
cmd.delete('trp18')
cmd.delete('trp19')
cmd.delete('trp20')
cmd.delete('trp21')
cmd.delete('trp22')
cmd.delete('trp23')
cmd.delete('trp24')
cmd.delete('trp25')
cmd.delete('trp26')
cmd.delete('trp27')
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.34,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.05,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.51,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.35,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.96,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.61,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.33,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.11,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.46,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('scys','CA'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.09,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu_i','CD'),('scys','CB'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.93,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu_i','CD'),('scys','SG'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.97,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('scys','CA'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.70,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('scys','CB'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.42,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('scys','SG'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.25,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('scys','CA'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.53,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('scys','CB'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.43,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('scys','SG'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.68,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu_i','CD'),('strp','CE2'))] = cmd.select('glu_i19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.67,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('strp','CZ2'))] = cmd.select('glu_i20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.80,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('strp','NE1'))] = cmd.select('glu_i21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.77,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('strp','CE2'))] = cmd.select('glu_i22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.00,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('strp','CZ2'))] = cmd.select('glu_i23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.18,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('strp','NE1'))] = cmd.select('glu_i24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.99,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('strp','CE2'))] = cmd.select('glu_i25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.30,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('strp','CZ2'))] = cmd.select('glu_i26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.43,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('strp','NE1'))] = cmd.select('glu_i27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.50,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec['glu_i'] = cmd.select('glu_i',' br. glu_i1&br. glu_i2&br. glu_i3&br. glu_i4&br. glu_i5&br. glu_i6&br. glu_i7&br. glu_i8&br. glu_i9&br. glu_i10&br. glu_i11&br. glu_i12&br. glu_i13&br. glu_i14&br. glu_i15&br. glu_i16&br. glu_i17&br. glu_i18&br. glu_i19&br. glu_i20&br. glu_i21&br. glu_i22&br. glu_i23&br. glu_i24&br. glu_i25&br. glu_i26&br. glu_i27')
IDSpec['r_glu_i'] = cmd.count_atoms(resSelectionSubs('glu_i', subs=subs, selection=True))
cmd.delete('glu_i1')
cmd.delete('glu_i2')
cmd.delete('glu_i3')
cmd.delete('glu_i4')
cmd.delete('glu_i5')
cmd.delete('glu_i6')
cmd.delete('glu_i7')
cmd.delete('glu_i8')
cmd.delete('glu_i9')
cmd.delete('glu_i10')
cmd.delete('glu_i11')
cmd.delete('glu_i12')
cmd.delete('glu_i13')
cmd.delete('glu_i14')
cmd.delete('glu_i15')
cmd.delete('glu_i16')
cmd.delete('glu_i17')
cmd.delete('glu_i18')
cmd.delete('glu_i19')
cmd.delete('glu_i20')
cmd.delete('glu_i21')
cmd.delete('glu_i22')
cmd.delete('glu_i23')
cmd.delete('glu_i24')
cmd.delete('glu_i25')
cmd.delete('glu_i26')
cmd.delete('glu_i27')
IDSpec['S_2icj_5_3_3_2'] = cmd.select('S_2icj_5_3_3_2', 'glu|cys|trp|glu_i')
cmd.delete('glu')
cmd.delete('cys')
cmd.delete('trp')
cmd.delete('glu_i')
