'''
FUNC:S_2j30_3_4_22_56
PDB:2j30
EC:3.4.22.56
RESI:his,gly,cys,val
LOCI:a-121,122,163,266;
'''
IDSpec[(('his','CE1'),('rgly','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.46,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','CE1'),('rgly','N'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.05,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','CE1'),('rgly','O'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.43,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','ND1'),('rgly','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.15,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','ND1'),('rgly','N'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.73,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','ND1'),('rgly','O'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.20,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','NE2'),('rgly','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.91,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','NE2'),('rgly','N'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.52,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','NE2'),('rgly','O'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.12,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','CE1'),('rcys','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.31,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','CE1'),('rcys','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.46,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','CE1'),('rcys','SG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.66,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','ND1'),('rcys','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.21,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','ND1'),('rcys','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.41,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','ND1'),('rcys','SG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.84,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','NE2'),('rcys','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.34,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','NE2'),('rcys','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.54,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','NE2'),('rcys','SG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.88,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','CE1'),('rval','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+25.12,resSelectionSubs('val','CA',subs)))
IDSpec[(('his','CE1'),('rval','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+24.20,resSelectionSubs('val','CB',subs)))
IDSpec[(('his','CE1'),('rval','CG1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+25.10,resSelectionSubs('val','CG1',subs)))
IDSpec[(('his','ND1'),('rval','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+23.96,resSelectionSubs('val','CA',subs)))
IDSpec[(('his','ND1'),('rval','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+23.01,resSelectionSubs('val','CB',subs)))
IDSpec[(('his','ND1'),('rval','CG1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+23.88,resSelectionSubs('val','CG1',subs)))
IDSpec[(('his','NE2'),('rval','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+25.88,resSelectionSubs('val','CA',subs)))
IDSpec[(('his','NE2'),('rval','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+24.93,resSelectionSubs('val','CB',subs)))
IDSpec[(('his','NE2'),('rval','CG1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+25.80,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('gly','CA'),('shis','CE1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.46,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis','ND1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.15,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis','NE2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.91,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','N'),('shis','CE1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.05,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','N'),('shis','ND1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.73,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','N'),('shis','NE2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.52,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','O'),('shis','CE1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.43,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','O'),('shis','ND1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.20,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','O'),('shis','NE2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.12,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','CA'),('rcys','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.75,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','CA'),('rcys','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.80,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','CA'),('rcys','SG'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.06,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','N'),('rcys','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.71,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','N'),('rcys','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.54,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','N'),('rcys','SG'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.41,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','O'),('rcys','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.92,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','O'),('rcys','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.37,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','O'),('rcys','SG'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.78,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','CA'),('rval','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+19.31,resSelectionSubs('val','CA',subs)))
IDSpec[(('gly','CA'),('rval','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.13,resSelectionSubs('val','CB',subs)))
IDSpec[(('gly','CA'),('rval','CG1'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.76,resSelectionSubs('val','CG1',subs)))
IDSpec[(('gly','N'),('rval','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+20.16,resSelectionSubs('val','CA',subs)))
IDSpec[(('gly','N'),('rval','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+19.05,resSelectionSubs('val','CB',subs)))
IDSpec[(('gly','N'),('rval','CG1'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+19.76,resSelectionSubs('val','CG1',subs)))
IDSpec[(('gly','O'),('rval','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.90,resSelectionSubs('val','CA',subs)))
IDSpec[(('gly','O'),('rval','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+18.74,resSelectionSubs('val','CB',subs)))
IDSpec[(('gly','O'),('rval','CG1'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.37,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('cys','CA'),('shis','CE1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.31,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','ND1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.21,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','NE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.34,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','CE1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.46,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','ND1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.41,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','NE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.54,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','CE1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.66,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','ND1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','NE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.88,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CA'),('sgly','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.75,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sgly','N'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.71,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','CA'),('sgly','O'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.92,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.80,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','N'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.54,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','O'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.37,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.06,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','N'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.41,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','O'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.78,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','CA'),('rval','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+17.67,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','CA'),('rval','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.73,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','CA'),('rval','CG1'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+17.62,resSelectionSubs('val','CG1',subs)))
IDSpec[(('cys','CB'),('rval','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+19.11,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','CB'),('rval','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+18.15,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','CB'),('rval','CG1'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+19.01,resSelectionSubs('val','CG1',subs)))
IDSpec[(('cys','SG'),('rval','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+20.16,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','SG'),('rval','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+19.30,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','SG'),('rval','CG1'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+20.26,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('val','CA'),('shis','CE1'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+25.12,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('val','CA'),('shis','ND1'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+23.96,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('val','CA'),('shis','NE2'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+25.88,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('val','CB'),('shis','CE1'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+24.20,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('val','CB'),('shis','ND1'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+23.01,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('val','CB'),('shis','NE2'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+24.93,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('val','CG1'),('shis','CE1'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+25.10,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('val','CG1'),('shis','ND1'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+23.88,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('val','CG1'),('shis','NE2'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+25.80,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('val','CA'),('sgly','CA'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.31,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('val','CA'),('sgly','N'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+20.16,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('val','CA'),('sgly','O'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.90,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('val','CB'),('sgly','CA'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.13,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('val','CB'),('sgly','N'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+19.05,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('val','CB'),('sgly','O'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.74,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('val','CG1'),('sgly','CA'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+18.76,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('val','CG1'),('sgly','N'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.76,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('val','CG1'),('sgly','O'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.37,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('val','CA'),('scys','CA'))] = cmd.select('val19', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+17.67,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CA'),('scys','CB'))] = cmd.select('val20', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.11,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CA'),('scys','SG'))] = cmd.select('val21', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+20.16,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CB'),('scys','CA'))] = cmd.select('val22', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+16.73,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CB'),('scys','CB'))] = cmd.select('val23', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.15,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CB'),('scys','SG'))] = cmd.select('val24', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+19.30,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','CA'))] = cmd.select('val25', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+17.62,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','CB'))] = cmd.select('val26', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.01,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','SG'))] = cmd.select('val27', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+20.26,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec['val'] = cmd.select('val',' br. val1&br. val2&br. val3&br. val4&br. val5&br. val6&br. val7&br. val8&br. val9&br. val10&br. val11&br. val12&br. val13&br. val14&br. val15&br. val16&br. val17&br. val18&br. val19&br. val20&br. val21&br. val22&br. val23&br. val24&br. val25&br. val26&br. val27')
IDSpec['r_val'] = cmd.count_atoms(resSelectionSubs('val', subs=subs, selection=True))
cmd.delete('val1')
cmd.delete('val2')
cmd.delete('val3')
cmd.delete('val4')
cmd.delete('val5')
cmd.delete('val6')
cmd.delete('val7')
cmd.delete('val8')
cmd.delete('val9')
cmd.delete('val10')
cmd.delete('val11')
cmd.delete('val12')
cmd.delete('val13')
cmd.delete('val14')
cmd.delete('val15')
cmd.delete('val16')
cmd.delete('val17')
cmd.delete('val18')
cmd.delete('val19')
cmd.delete('val20')
cmd.delete('val21')
cmd.delete('val22')
cmd.delete('val23')
cmd.delete('val24')
cmd.delete('val25')
cmd.delete('val26')
cmd.delete('val27')
IDSpec['S_2j30_3_4_22_56'] = cmd.select('S_2j30_3_4_22_56', 'his|gly|cys|val')
cmd.delete('his')
cmd.delete('gly')
cmd.delete('cys')
cmd.delete('val')
