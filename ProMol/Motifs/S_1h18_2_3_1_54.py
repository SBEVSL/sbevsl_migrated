'''
FUNC:S_1h18_2_3_1_54
PDB:1h18
EC:2.3.1.54
RESI:trp,cys,cys,gly
LOCI:a-333,418,419,734;
'''
IDSpec[(('cys','CA'),('rgly','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.62,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CA'),('rgly','N'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.91,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CA'),('rgly','O'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.23,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','CB'),('rgly','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.74,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CB'),('rgly','N'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.87,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CB'),('rgly','O'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.12,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','SG'),('rgly','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.72,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','SG'),('rgly','N'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.43,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','SG'),('rgly','O'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.17,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','CA'),('rtrp','CE2'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.00,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('cys','CA'),('rtrp','CZ2'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.92,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('cys','CA'),('rtrp','NE1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.86,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('cys','CB'),('rtrp','CE2'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.84,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('cys','CB'),('rtrp','CZ2'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.48,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('cys','CB'),('rtrp','NE1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.77,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('cys','SG'),('rtrp','CE2'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.36,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('cys','SG'),('rtrp','CZ2'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.83,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('cys','SG'),('rtrp','NE1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.43,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('cys','CA'),('rcys_i','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.82,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CA'),('rcys_i','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.14,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CA'),('rcys_i','SG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.36,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CB'),('rcys_i','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.82,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CB'),('rcys_i','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.73,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CB'),('rcys_i','SG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.44,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','SG'),('rcys_i','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.01,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','SG'),('rcys_i','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.77,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','SG'),('rcys_i','SG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.82,resSelectionSubs('cys_i','SG',subs)))
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
IDSpec[(('gly','CA'),('scys','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.62,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.74,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','SG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.72,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.91,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.87,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','N'),('scys','SG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.43,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.23,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.12,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','O'),('scys','SG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.17,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','CA'),('rtrp','CE2'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.02,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('gly','CA'),('rtrp','CZ2'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.39,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('gly','CA'),('rtrp','NE1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.88,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('gly','N'),('rtrp','CE2'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.28,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('gly','N'),('rtrp','CZ2'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.40,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('gly','N'),('rtrp','NE1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.30,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('gly','O'),('rtrp','CE2'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.73,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('gly','O'),('rtrp','CZ2'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.51,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('gly','O'),('rtrp','NE1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.40,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('gly','CA'),('rcys_i','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.95,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('gly','CA'),('rcys_i','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.14,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('gly','CA'),('rcys_i','SG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.46,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('gly','N'),('rcys_i','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.02,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('gly','N'),('rcys_i','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.10,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('gly','N'),('rcys_i','SG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.18,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('gly','O'),('rcys_i','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.07,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('gly','O'),('rcys_i','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.60,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('gly','O'),('rcys_i','SG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.16,resSelectionSubs('cys_i','SG',subs)))
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
IDSpec[(('trp','CE2'),('scys','CA'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.00,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('trp','CE2'),('scys','CB'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.84,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('trp','CE2'),('scys','SG'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+6.36,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('trp','CZ2'),('scys','CA'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.92,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('trp','CZ2'),('scys','CB'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.48,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('trp','CZ2'),('scys','SG'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.83,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('trp','NE1'),('scys','CA'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.86,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('trp','NE1'),('scys','CB'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.77,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('trp','NE1'),('scys','SG'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+5.43,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('trp','CE2'),('sgly','CA'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.02,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('trp','CE2'),('sgly','N'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.28,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('trp','CE2'),('sgly','O'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.73,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sgly','CA'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.39,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sgly','N'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.40,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sgly','O'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.51,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('trp','NE1'),('sgly','CA'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.88,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('trp','NE1'),('sgly','N'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.30,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('trp','NE1'),('sgly','O'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.40,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('trp','CE2'),('rcys_i','CA'))] = cmd.select('trp19', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.25,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('trp','CE2'),('rcys_i','CB'))] = cmd.select('trp20', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.20,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('trp','CE2'),('rcys_i','SG'))] = cmd.select('trp21', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+5.76,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('trp','CZ2'),('rcys_i','CA'))] = cmd.select('trp22', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.41,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('trp','CZ2'),('rcys_i','CB'))] = cmd.select('trp23', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.11,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('trp','CZ2'),('rcys_i','SG'))] = cmd.select('trp24', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.45,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('trp','NE1'),('rcys_i','CA'))] = cmd.select('trp25', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.68,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('trp','NE1'),('rcys_i','CB'))] = cmd.select('trp26', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.87,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('trp','NE1'),('rcys_i','SG'))] = cmd.select('trp27', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+5.65,resSelectionSubs('cys_i','SG',subs)))
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
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.82,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.82,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.01,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.14,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.73,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.77,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.36,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.44,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.82,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sgly','CA'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.95,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sgly','N'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.02,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sgly','O'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.07,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sgly','CA'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.14,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sgly','N'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.10,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sgly','O'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.60,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sgly','CA'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.46,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sgly','N'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.18,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sgly','O'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.16,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys_i','CA'),('strp','CE2'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.25,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('cys_i','CA'),('strp','CZ2'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.41,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('cys_i','CA'),('strp','NE1'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.68,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('strp','CE2'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.20,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('cys_i','CB'),('strp','CZ2'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.11,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('cys_i','CB'),('strp','NE1'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.87,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('strp','CE2'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.76,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('cys_i','SG'),('strp','CZ2'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.45,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('cys_i','SG'),('strp','NE1'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.65,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec['cys_i'] = cmd.select('cys_i',' br. cys_i1&br. cys_i2&br. cys_i3&br. cys_i4&br. cys_i5&br. cys_i6&br. cys_i7&br. cys_i8&br. cys_i9&br. cys_i10&br. cys_i11&br. cys_i12&br. cys_i13&br. cys_i14&br. cys_i15&br. cys_i16&br. cys_i17&br. cys_i18&br. cys_i19&br. cys_i20&br. cys_i21&br. cys_i22&br. cys_i23&br. cys_i24&br. cys_i25&br. cys_i26&br. cys_i27')
IDSpec['r_cys_i'] = cmd.count_atoms(resSelectionSubs('cys_i', subs=subs, selection=True))
cmd.delete('cys_i1')
cmd.delete('cys_i2')
cmd.delete('cys_i3')
cmd.delete('cys_i4')
cmd.delete('cys_i5')
cmd.delete('cys_i6')
cmd.delete('cys_i7')
cmd.delete('cys_i8')
cmd.delete('cys_i9')
cmd.delete('cys_i10')
cmd.delete('cys_i11')
cmd.delete('cys_i12')
cmd.delete('cys_i13')
cmd.delete('cys_i14')
cmd.delete('cys_i15')
cmd.delete('cys_i16')
cmd.delete('cys_i17')
cmd.delete('cys_i18')
cmd.delete('cys_i19')
cmd.delete('cys_i20')
cmd.delete('cys_i21')
cmd.delete('cys_i22')
cmd.delete('cys_i23')
cmd.delete('cys_i24')
cmd.delete('cys_i25')
cmd.delete('cys_i26')
cmd.delete('cys_i27')
IDSpec['S_1h18_2_3_1_54'] = cmd.select('S_1h18_2_3_1_54', 'cys|gly|trp|cys_i')
cmd.delete('cys')
cmd.delete('gly')
cmd.delete('trp')
cmd.delete('cys_i')
