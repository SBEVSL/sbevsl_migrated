'''
FUNC:S_3gf0_3_5_4_30
PDB:3gf0
EC:3.5.4.30
RESI:ser,arg,asp,gly
LOCI:a-118,122,135,137;
'''
IDSpec[(('asp','CG'),('rgly','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.21,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','CG'),('rgly','N'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.65,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','CG'),('rgly','O'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.82,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD1'),('rgly','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.89,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD1'),('rgly','N'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.34,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD1'),('rgly','O'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.24,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD2'),('rgly','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.81,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD2'),('rgly','N'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.29,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD2'),('rgly','O'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.52,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+26.44,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+26.88,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.10,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+25.57,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.06,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+27.28,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.30,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.71,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.90,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+32.27,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+30.42,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.85,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+31.42,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+29.61,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+32.44,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+33.06,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+31.21,resSelectionSubs('arg','NH1',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
IDSpec['r_asp'] = cmd.count_atoms(resSelectionSubs('asp', subs=subs, selection=True))
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
IDSpec[(('gly','CA'),('sasp','CG'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.21,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.89,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.81,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','CG'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.65,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.34,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.29,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','CG'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.82,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','CA'),('rser','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+29.17,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','CA'),('rser','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+29.53,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','CA'),('rser','OG'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+30.90,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','N'),('rser','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+28.11,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','N'),('rser','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+28.42,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','N'),('rser','OG'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+29.78,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','O'),('rser','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+29.57,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','O'),('rser','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+30.05,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','O'),('rser','OG'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+31.44,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','CA'),('rarg','CZ'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+34.45,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','CA'),('rarg','NE'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+35.17,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','CA'),('rarg','NH1'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+33.12,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','N'),('rarg','CZ'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+33.32,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','N'),('rarg','NE'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+34.06,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','N'),('rarg','NH1'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+31.99,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','O'),('rarg','CZ'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+35.02,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','O'),('rarg','NE'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+35.66,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','O'),('rarg','NH1'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+33.69,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+26.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+25.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+27.30,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+26.88,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+26.06,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+27.71,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+28.10,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+27.28,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+28.90,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+29.17,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','N'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+28.11,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','O'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+29.57,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+29.53,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','N'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+28.42,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','O'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+30.05,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+30.90,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','N'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+29.78,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','O'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+31.44,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','CA'),('rarg','CZ'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.80,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CA'),('rarg','NE'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.16,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CA'),('rarg','NH1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.58,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','CB'),('rarg','CZ'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.99,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CB'),('rarg','NE'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.66,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CB'),('rarg','NH1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.67,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','OG'),('rarg','CZ'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.62,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','OG'),('rarg','NE'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.30,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','OG'),('rarg','NH1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.36,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+31.67,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+30.85,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+32.44,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+32.27,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+31.42,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+33.06,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+30.42,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+29.61,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+31.21,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+34.45,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly','N'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+33.32,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly','O'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+35.02,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+35.17,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','N'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+34.06,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','O'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+35.66,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+33.12,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','N'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+31.99,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','O'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+33.69,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.80,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.99,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','OG'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.62,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.16,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.66,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','OG'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.30,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.58,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.67,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','OG'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+4.36,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
IDSpec['S_3gf0_3_5_4_30'] = cmd.select('S_3gf0_3_5_4_30', 'asp|gly|ser|arg')
cmd.delete('asp')
cmd.delete('gly')
cmd.delete('ser')
cmd.delete('arg')
