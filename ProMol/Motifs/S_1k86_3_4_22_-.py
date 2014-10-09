'''
FUNC:S_1k86_3_4_22_-
PDB:1k86
EC:3.4.22.-
RESI:his,gly,cys,val
LOCI:a-144,145,186,292;
'''
IDSpec[(('cys','CA'),('rgly','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.06,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CA'),('rgly','N'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.22,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CA'),('rgly','O'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.71,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','CB'),('rgly','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.27,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CB'),('rgly','N'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.23,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CB'),('rgly','O'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.99,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','SG'),('rgly','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.20,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','SG'),('rgly','N'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.94,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','SG'),('rgly','O'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.20,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','CA'),('rhis','CE1'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.56,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CA'),('rhis','ND1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.69,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CA'),('rhis','NE2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.68,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CB'),('rhis','CE1'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.09,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CB'),('rhis','ND1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.50,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CB'),('rhis','NE2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.27,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','SG'),('rhis','CE1'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.45,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','SG'),('rhis','ND1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.02,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','SG'),('rhis','NE2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.58,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CA'),('rval','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+19.32,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','CA'),('rval','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+18.69,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','CA'),('rval','CG1'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+19.82,resSelectionSubs('val','CG1',subs)))
IDSpec[(('cys','CB'),('rval','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+20.41,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','CB'),('rval','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+19.85,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','CB'),('rval','CG1'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.04,resSelectionSubs('val','CG1',subs)))
IDSpec[(('cys','SG'),('rval','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.76,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','SG'),('rval','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.14,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','SG'),('rval','CG1'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+22.29,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('gly','CA'),('scys','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.06,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.27,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','SG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.20,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.22,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.23,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','N'),('scys','SG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.94,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.71,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.99,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','O'),('scys','SG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.20,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','CA'),('rhis','CE1'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.60,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','CA'),('rhis','ND1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.28,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','CA'),('rhis','NE2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.01,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','N'),('rhis','CE1'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.18,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','N'),('rhis','ND1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.86,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','N'),('rhis','NE2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.63,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','O'),('rhis','CE1'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.72,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','O'),('rhis','ND1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.47,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','O'),('rhis','NE2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.38,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','CA'),('rval','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+19.12,resSelectionSubs('val','CA',subs)))
IDSpec[(('gly','CA'),('rval','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.03,resSelectionSubs('val','CB',subs)))
IDSpec[(('gly','CA'),('rval','CG1'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.77,resSelectionSubs('val','CG1',subs)))
IDSpec[(('gly','N'),('rval','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+19.99,resSelectionSubs('val','CA',subs)))
IDSpec[(('gly','N'),('rval','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+18.98,resSelectionSubs('val','CB',subs)))
IDSpec[(('gly','N'),('rval','CG1'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+19.79,resSelectionSubs('val','CG1',subs)))
IDSpec[(('gly','O'),('rval','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.54,resSelectionSubs('val','CA',subs)))
IDSpec[(('gly','O'),('rval','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+18.50,resSelectionSubs('val','CB',subs)))
IDSpec[(('gly','O'),('rval','CG1'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.25,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('his','CE1'),('scys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.56,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.09,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.45,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.69,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.50,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.02,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.68,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.27,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.58,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.60,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','N'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.18,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','O'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.72,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.28,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','N'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.86,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','O'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.47,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.01,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','N'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.63,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','O'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.38,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','CE1'),('rval','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+25.13,resSelectionSubs('val','CA',subs)))
IDSpec[(('his','CE1'),('rval','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+24.32,resSelectionSubs('val','CB',subs)))
IDSpec[(('his','CE1'),('rval','CG1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+25.31,resSelectionSubs('val','CG1',subs)))
IDSpec[(('his','ND1'),('rval','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+23.96,resSelectionSubs('val','CA',subs)))
IDSpec[(('his','ND1'),('rval','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+23.11,resSelectionSubs('val','CB',subs)))
IDSpec[(('his','ND1'),('rval','CG1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+24.08,resSelectionSubs('val','CG1',subs)))
IDSpec[(('his','NE2'),('rval','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+25.86,resSelectionSubs('val','CA',subs)))
IDSpec[(('his','NE2'),('rval','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+25.01,resSelectionSubs('val','CB',subs)))
IDSpec[(('his','NE2'),('rval','CG1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+25.97,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('val','CA'),('scys','CA'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.32,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CA'),('scys','CB'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+20.41,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CA'),('scys','SG'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+21.76,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CB'),('scys','CA'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.69,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CB'),('scys','CB'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+19.85,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CB'),('scys','SG'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+21.14,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','CA'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.82,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','CB'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+21.04,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','SG'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+22.29,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CA'),('sgly','CA'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.12,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('val','CA'),('sgly','N'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.99,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('val','CA'),('sgly','O'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.54,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('val','CB'),('sgly','CA'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.03,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('val','CB'),('sgly','N'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.98,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('val','CB'),('sgly','O'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.50,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('val','CG1'),('sgly','CA'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+18.77,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('val','CG1'),('sgly','N'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.79,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('val','CG1'),('sgly','O'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.25,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('val','CA'),('shis','CE1'))] = cmd.select('val19', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+25.13,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('val','CA'),('shis','ND1'))] = cmd.select('val20', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+23.96,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('val','CA'),('shis','NE2'))] = cmd.select('val21', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+25.86,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('val','CB'),('shis','CE1'))] = cmd.select('val22', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+24.32,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('val','CB'),('shis','ND1'))] = cmd.select('val23', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+23.11,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('val','CB'),('shis','NE2'))] = cmd.select('val24', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+25.01,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('val','CG1'),('shis','CE1'))] = cmd.select('val25', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+25.31,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('val','CG1'),('shis','ND1'))] = cmd.select('val26', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+24.08,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('val','CG1'),('shis','NE2'))] = cmd.select('val27', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+25.97,resSelectionSubs('his','NE2',subs,selection=True)))
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
IDSpec['S_1k86_3_4_22_-'] = cmd.select('S_1k86_3_4_22_-', 'cys|gly|his|val')
cmd.delete('cys')
cmd.delete('gly')
cmd.delete('his')
cmd.delete('val')