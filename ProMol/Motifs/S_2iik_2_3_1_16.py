'''
FUNC:S_2iik_2_3_1_16
PDB:2iik
EC:2.3.1.16
RESI:cys,his,cys,gly
LOCI:a-123,378,409,411;
'''
IDSpec[(('gly','CA'),('rcys','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.90,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','CA'),('rcys','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.86,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','CA'),('rcys','SG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.93,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','N'),('rcys','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.70,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','N'),('rcys','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.88,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','N'),('rcys','SG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.04,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','O'),('rcys','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.81,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','O'),('rcys','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.11,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','O'),('rcys','SG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.59,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','CA'),('rcys','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.65,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','CA'),('rcys','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.06,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','CA'),('rcys','SG'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.61,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','N'),('rcys','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.50,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','N'),('rcys','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.85,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','N'),('rcys','SG'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.62,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','O'),('rcys','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.22,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','O'),('rcys','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.04,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','O'),('rcys','SG'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.96,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','CA'),('rhis','CE1'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.28,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','CA'),('rhis','ND1'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.50,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','CA'),('rhis','NE2'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.46,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','N'),('rhis','CE1'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','N'),('rhis','ND1'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.58,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','N'),('rhis','NE2'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','O'),('rhis','CE1'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.68,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','O'),('rhis','ND1'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.97,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','O'),('rhis','NE2'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.08,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('cys','CA'),('sgly','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.90,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sgly','N'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.70,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','CA'),('sgly','O'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.81,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.86,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','N'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.88,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','O'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.11,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.93,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','N'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.04,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','O'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.59,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','CA'),('rcys','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.96,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CA'),('rcys','CB'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.78,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CA'),('rcys','SG'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.01,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CB'),('rcys','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.83,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CB'),('rcys','CB'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.50,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CB'),('rcys','SG'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.40,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','SG'),('rcys','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.51,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','SG'),('rcys','CB'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.04,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','SG'),('rcys','SG'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.80,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CA'),('rhis','CE1'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.33,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CA'),('rhis','ND1'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.35,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CA'),('rhis','NE2'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.90,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CB'),('rhis','CE1'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.72,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CB'),('rhis','ND1'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.67,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CB'),('rhis','NE2'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','SG'),('rhis','CE1'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.58,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','SG'),('rhis','ND1'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.43,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','SG'),('rhis','NE2'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.82,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('cys_i','CA'),('sgly','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.65,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sgly','N'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.50,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sgly','O'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.22,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sgly','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.06,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sgly','N'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.85,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sgly','O'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.04,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sgly','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.61,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sgly','N'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.62,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sgly','O'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.96,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.96,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.83,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.51,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.78,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.50,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.04,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.01,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.40,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.80,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rhis','CE1'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.43,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys_i','CA'),('rhis','ND1'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.69,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys_i','CA'),('rhis','NE2'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.63,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys_i','CB'),('rhis','CE1'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.97,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys_i','CB'),('rhis','ND1'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.29,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys_i','CB'),('rhis','NE2'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.85,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys_i','SG'),('rhis','CE1'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.74,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys_i','SG'),('rhis','ND1'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.02,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys_i','SG'),('rhis','NE2'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.15,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('sgly','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.28,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','N'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.31,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','O'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.68,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.50,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','N'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.58,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','O'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.97,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.46,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','N'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.60,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','O'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.08,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.33,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.72,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','SG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.58,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.35,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.67,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','SG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.43,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.90,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.10,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','SG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.82,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','CE1'),('scys_i','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.43,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('scys_i','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.97,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('scys_i','SG'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.74,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('his','ND1'),('scys_i','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.69,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('scys_i','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.29,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('scys_i','SG'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.02,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('his','NE2'),('scys_i','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.63,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('scys_i','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.85,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('scys_i','SG'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.15,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
IDSpec['S_2iik_2_3_1_16'] = cmd.select('S_2iik_2_3_1_16', 'gly|cys|cys_i|his')
cmd.delete('gly')
cmd.delete('cys')
cmd.delete('cys_i')
cmd.delete('his')
