'''
FUNC:S_1ecj_2_4_2_14
PDB:1ecj
EC:2.4.2.14
RESI:cys,asn,gly,ser
LOCI:a-1,101,102,345;
'''
IDSpec[(('gly','CA'),('rcys','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.67,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','CA'),('rcys','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.80,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','CA'),('rcys','SG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.07,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','N'),('rcys','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.46,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','N'),('rcys','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.53,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','N'),('rcys','SG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.97,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','O'),('rcys','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.73,resSelectionSubs('cys','CA',subs)))
IDSpec[(('gly','O'),('rcys','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.62,resSelectionSubs('cys','CB',subs)))
IDSpec[(('gly','O'),('rcys','SG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.30,resSelectionSubs('cys','SG',subs)))
IDSpec[(('gly','CA'),('rasn','CG'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.59,resSelectionSubs('asn','CG',subs)))
IDSpec[(('gly','CA'),('rasn','ND2'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.20,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('gly','CA'),('rasn','OD1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.26,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('gly','N'),('rasn','CG'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.60,resSelectionSubs('asn','CG',subs)))
IDSpec[(('gly','N'),('rasn','ND2'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.24,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('gly','N'),('rasn','OD1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.50,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('gly','O'),('rasn','CG'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.02,resSelectionSubs('asn','CG',subs)))
IDSpec[(('gly','O'),('rasn','ND2'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.24,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('gly','O'),('rasn','OD1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.93,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('gly','CA'),('rser','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+32.82,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','CA'),('rser','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+33.71,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','CA'),('rser','OG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+35.08,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','N'),('rser','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+32.45,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','N'),('rser','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+33.28,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','N'),('rser','OG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+34.66,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','O'),('rser','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+31.89,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','O'),('rser','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+32.78,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','O'),('rser','OG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+34.15,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('cys','CA'),('sgly','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.67,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sgly','N'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.46,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','CA'),('sgly','O'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.73,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.80,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','N'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.53,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','CB'),('sgly','O'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.62,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.07,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','N'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.97,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('cys','SG'),('sgly','O'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.30,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('cys','CA'),('rasn','CG'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.62,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys','CA'),('rasn','ND2'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.05,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys','CA'),('rasn','OD1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.34,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys','CB'),('rasn','CG'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.50,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys','CB'),('rasn','ND2'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.84,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys','CB'),('rasn','OD1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.49,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys','SG'),('rasn','CG'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.76,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys','SG'),('rasn','ND2'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.79,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys','SG'),('rasn','OD1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.78,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys','CA'),('rser','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+28.01,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CA'),('rser','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+28.63,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CA'),('rser','OG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+30.04,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CB'),('rser','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+28.81,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CB'),('rser','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+29.45,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CB'),('rser','OG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+30.87,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','SG'),('rser','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+27.81,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','SG'),('rser','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+28.48,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','SG'),('rser','OG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+29.89,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('asn','CG'),('sgly','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.59,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sgly','N'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.60,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asn','CG'),('sgly','O'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.02,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asn','ND2'),('sgly','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.20,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sgly','N'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.24,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asn','ND2'),('sgly','O'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.24,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asn','OD1'),('sgly','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.26,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sgly','N'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.50,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asn','OD1'),('sgly','O'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.93,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asn','CG'),('scys','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.62,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('scys','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.50,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('scys','SG'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.76,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.05,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.84,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys','SG'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.79,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.34,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.49,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys','SG'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.78,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asn','CG'),('rser','CA'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+31.37,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','CG'),('rser','CB'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+32.13,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','CG'),('rser','OG'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+33.52,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','ND2'),('rser','CA'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+30.36,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','ND2'),('rser','CB'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+31.14,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','ND2'),('rser','OG'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+32.53,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','OD1'),('rser','CA'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+31.55,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','OD1'),('rser','CB'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+32.31,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','OD1'),('rser','OG'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+33.69,resSelectionSubs('ser','OG',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27')
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
cmd.delete('asn19')
cmd.delete('asn20')
cmd.delete('asn21')
cmd.delete('asn22')
cmd.delete('asn23')
cmd.delete('asn24')
cmd.delete('asn25')
cmd.delete('asn26')
cmd.delete('asn27')
IDSpec[(('ser','CA'),('sgly','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+32.82,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','N'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+32.45,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','O'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+31.89,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+33.71,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','N'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+33.28,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','O'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+32.78,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+35.08,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','N'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+34.66,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','O'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+34.15,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+28.01,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+28.81,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','SG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+27.81,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+28.63,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+29.45,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','SG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+28.48,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+30.04,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+30.87,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','SG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+29.89,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','CG'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+31.37,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','ND2'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+30.36,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','OD1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+31.55,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','CG'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+32.13,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','ND2'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+31.14,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','OD1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+32.31,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','CG'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+33.52,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','ND2'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+32.53,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','OD1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+33.69,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_1ecj_2_4_2_14'] = cmd.select('S_1ecj_2_4_2_14', 'gly|cys|asn|ser')
cmd.delete('gly')
cmd.delete('cys')
cmd.delete('asn')
cmd.delete('ser')