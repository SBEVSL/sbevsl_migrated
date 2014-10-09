'''
FUNC:S_1kyi_3_4_99_-
PDB:1kyi
EC:3.4.99.-
RESI:thr,lys,gly,gly,ser
LOCI:n-1,33,45,48,125;
'''
IDSpec[(('gly','CA'),('rlys','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.60,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','CA'),('rlys','CE'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.85,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','CA'),('rlys','NZ'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.00,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','N'),('rlys','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.28,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','N'),('rlys','CE'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.62,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','N'),('rlys','NZ'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.76,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','O'),('rlys','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.02,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','O'),('rlys','CE'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.15,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','O'),('rlys','NZ'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.41,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','CA'),('rthr','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.57,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','CA'),('rthr','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.91,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','CA'),('rthr','OG1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.54,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','N'),('rthr','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.46,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','N'),('rthr','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.65,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','N'),('rthr','OG1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.31,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','O'),('rthr','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.53,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','O'),('rthr','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.87,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','O'),('rthr','OG1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.45,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','CA'),('rser','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.10,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','CA'),('rser','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.14,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','CA'),('rser','OG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.15,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','N'),('rser','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.60,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','N'),('rser','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.70,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','N'),('rser','OG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.55,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','O'),('rser','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.15,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gly','O'),('rser','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.02,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gly','O'),('rser','OG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.04,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gly','CA'),('rgly','CA'))] = cmd.select('gly28', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.62,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','CA'),('rgly','N'))] = cmd.select('gly29', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.57,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','CA'),('rgly','O'))] = cmd.select('gly30', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.16,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','N'),('rgly','CA'))] = cmd.select('gly31', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.39,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','N'),('rgly','N'))] = cmd.select('gly32', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.42,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','N'),('rgly','O'))] = cmd.select('gly33', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.08,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','O'),('rgly','CA'))] = cmd.select('gly34', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.16,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','O'),('rgly','N'))] = cmd.select('gly35', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.01,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','O'),('rgly','O'))] = cmd.select('gly36', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.73,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('lys','CD'),('sgly','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.60,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sgly','N'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.28,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','CD'),('sgly','O'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.02,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.85,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','N'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.62,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','O'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.15,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.00,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','N'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.76,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','O'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.41,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','CD'),('rthr','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.10,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CD'),('rthr','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.86,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CD'),('rthr','OG1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.21,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CE'),('rthr','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.77,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CE'),('rthr','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CE'),('rthr','OG1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.23,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','NZ'),('rthr','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.72,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','NZ'),('rthr','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.17,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','NZ'),('rthr','OG1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.93,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CD'),('rser','CA'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CD'),('rser','CB'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.34,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CD'),('rser','OG'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.25,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CE'),('rser','CA'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.24,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CE'),('rser','CB'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.91,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CE'),('rser','OG'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.73,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','NZ'),('rser','CA'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.13,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','NZ'),('rser','CB'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.76,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','NZ'),('rser','OG'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.49,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.58,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.98,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.30,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.10,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.50,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.74,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.76,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.18,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.55,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('thr','CA'),('sgly','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.57,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','N'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.46,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','O'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.53,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.91,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','N'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.65,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','O'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.87,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.54,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','N'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.31,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','O'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.45,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CD'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CE'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.77,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','NZ'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.72,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CD'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.86,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CE'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.87,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','NZ'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.17,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CD'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.21,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CE'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.23,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','NZ'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.93,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CA'),('rser','CA'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.48,resSelectionSubs('ser','CA',subs)))
IDSpec[(('thr','CA'),('rser','CB'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.26,resSelectionSubs('ser','CB',subs)))
IDSpec[(('thr','CA'),('rser','OG'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.17,resSelectionSubs('ser','OG',subs)))
IDSpec[(('thr','CB'),('rser','CA'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.61,resSelectionSubs('ser','CA',subs)))
IDSpec[(('thr','CB'),('rser','CB'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.56,resSelectionSubs('ser','CB',subs)))
IDSpec[(('thr','CB'),('rser','OG'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.60,resSelectionSubs('ser','OG',subs)))
IDSpec[(('thr','OG1'),('rser','CA'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.82,resSelectionSubs('ser','CA',subs)))
IDSpec[(('thr','OG1'),('rser','CB'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.72,resSelectionSubs('ser','CB',subs)))
IDSpec[(('thr','OG1'),('rser','OG'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.94,resSelectionSubs('ser','OG',subs)))
IDSpec[(('thr','CA'),('rgly','CA'))] = cmd.select('thr28', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.24,resSelectionSubs('gly','CA',subs)))
IDSpec[(('thr','CA'),('rgly','N'))] = cmd.select('thr29', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.64,resSelectionSubs('gly','N',subs)))
IDSpec[(('thr','CA'),('rgly','O'))] = cmd.select('thr30', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.05,resSelectionSubs('gly','O',subs)))
IDSpec[(('thr','CB'),('rgly','CA'))] = cmd.select('thr31', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.85,resSelectionSubs('gly','CA',subs)))
IDSpec[(('thr','CB'),('rgly','N'))] = cmd.select('thr32', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.27,resSelectionSubs('gly','N',subs)))
IDSpec[(('thr','CB'),('rgly','O'))] = cmd.select('thr33', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.72,resSelectionSubs('gly','O',subs)))
IDSpec[(('thr','OG1'),('rgly','CA'))] = cmd.select('thr34', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.96,resSelectionSubs('gly','CA',subs)))
IDSpec[(('thr','OG1'),('rgly','N'))] = cmd.select('thr35', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.33,resSelectionSubs('gly','N',subs)))
IDSpec[(('thr','OG1'),('rgly','O'))] = cmd.select('thr36', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.56,resSelectionSubs('gly','O',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27&br. thr28&br. thr29&br. thr30&br. thr31&br. thr32&br. thr33&br. thr34&br. thr35&br. thr36')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
cmd.delete('thr19')
cmd.delete('thr20')
cmd.delete('thr21')
cmd.delete('thr22')
cmd.delete('thr23')
cmd.delete('thr24')
cmd.delete('thr25')
cmd.delete('thr26')
cmd.delete('thr27')
cmd.delete('thr28')
cmd.delete('thr29')
cmd.delete('thr30')
cmd.delete('thr31')
cmd.delete('thr32')
cmd.delete('thr33')
cmd.delete('thr34')
cmd.delete('thr35')
cmd.delete('thr36')
IDSpec[(('ser','CA'),('sgly','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.10,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','N'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.60,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CA'),('sgly','O'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.15,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.14,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','N'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.70,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','CB'),('sgly','O'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.02,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.15,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','N'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.55,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ser','OG'),('sgly','O'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.04,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.46,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.24,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','NZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.13,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.34,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.91,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','NZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.76,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.25,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.73,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','NZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.49,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CA'),('sthr','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.48,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('sthr','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.61,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('sthr','OG1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.82,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('ser','CB'),('sthr','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.26,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('sthr','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.56,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('sthr','OG1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.72,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('ser','OG'),('sthr','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.17,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('sthr','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.60,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('sthr','OG1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.94,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('ser','CA'),('rgly','CA'))] = cmd.select('ser28', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.65,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','CA'),('rgly','N'))] = cmd.select('ser29', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+16.86,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','CA'),('rgly','O'))] = cmd.select('ser30', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.76,resSelectionSubs('gly','O',subs)))
IDSpec[(('ser','CB'),('rgly','CA'))] = cmd.select('ser31', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+16.34,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','CB'),('rgly','N'))] = cmd.select('ser32', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+17.61,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','CB'),('rgly','O'))] = cmd.select('ser33', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.55,resSelectionSubs('gly','O',subs)))
IDSpec[(('ser','OG'),('rgly','CA'))] = cmd.select('ser34', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+15.76,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','OG'),('rgly','N'))] = cmd.select('ser35', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+17.08,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','OG'),('rgly','O'))] = cmd.select('ser36', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+15.18,resSelectionSubs('gly','O',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27&br. ser28&br. ser29&br. ser30&br. ser31&br. ser32&br. ser33&br. ser34&br. ser35&br. ser36')
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
cmd.delete('ser28')
cmd.delete('ser29')
cmd.delete('ser30')
cmd.delete('ser31')
cmd.delete('ser32')
cmd.delete('ser33')
cmd.delete('ser34')
cmd.delete('ser35')
cmd.delete('ser36')
IDSpec[(('gly_i','CA'),('sgly','CA'))] = cmd.select('gly_i1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.62,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','N'))] = cmd.select('gly_i2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.39,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','O'))] = cmd.select('gly_i3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.16,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','CA'))] = cmd.select('gly_i4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.57,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','N'))] = cmd.select('gly_i5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.42,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','O'))] = cmd.select('gly_i6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+15.01,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','CA'))] = cmd.select('gly_i7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.16,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','N'))] = cmd.select('gly_i8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.08,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','O'))] = cmd.select('gly_i9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.73,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','CD'))] = cmd.select('gly_i10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.58,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','CE'))] = cmd.select('gly_i11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','NZ'))] = cmd.select('gly_i12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.76,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','CD'))] = cmd.select('gly_i13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.98,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','CE'))] = cmd.select('gly_i14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.50,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','NZ'))] = cmd.select('gly_i15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.18,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','CD'))] = cmd.select('gly_i16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.30,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','CE'))] = cmd.select('gly_i17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.74,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','NZ'))] = cmd.select('gly_i18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.55,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sthr','CA'))] = cmd.select('gly_i19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.24,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sthr','CB'))] = cmd.select('gly_i20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.85,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sthr','OG1'))] = cmd.select('gly_i21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.96,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('gly_i','N'),('sthr','CA'))] = cmd.select('gly_i22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.64,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sthr','CB'))] = cmd.select('gly_i23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.27,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('gly_i','N'),('sthr','OG1'))] = cmd.select('gly_i24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.33,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('gly_i','O'),('sthr','CA'))] = cmd.select('gly_i25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.05,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sthr','CB'))] = cmd.select('gly_i26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.72,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('gly_i','O'),('sthr','OG1'))] = cmd.select('gly_i27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.56,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sser','CA'))] = cmd.select('gly_i28', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+15.65,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sser','CB'))] = cmd.select('gly_i29', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+16.34,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sser','OG'))] = cmd.select('gly_i30', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+15.76,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gly_i','N'),('sser','CA'))] = cmd.select('gly_i31', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+16.86,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sser','CB'))] = cmd.select('gly_i32', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+17.61,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly_i','N'),('sser','OG'))] = cmd.select('gly_i33', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+17.08,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gly_i','O'),('sser','CA'))] = cmd.select('gly_i34', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sser','CB'))] = cmd.select('gly_i35', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.55,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly_i','O'),('sser','OG'))] = cmd.select('gly_i36', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.18,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec['gly_i'] = cmd.select('gly_i',' br. gly_i1&br. gly_i2&br. gly_i3&br. gly_i4&br. gly_i5&br. gly_i6&br. gly_i7&br. gly_i8&br. gly_i9&br. gly_i10&br. gly_i11&br. gly_i12&br. gly_i13&br. gly_i14&br. gly_i15&br. gly_i16&br. gly_i17&br. gly_i18&br. gly_i19&br. gly_i20&br. gly_i21&br. gly_i22&br. gly_i23&br. gly_i24&br. gly_i25&br. gly_i26&br. gly_i27&br. gly_i28&br. gly_i29&br. gly_i30&br. gly_i31&br. gly_i32&br. gly_i33&br. gly_i34&br. gly_i35&br. gly_i36')
IDSpec['r_gly_i'] = cmd.count_atoms(resSelectionSubs('gly_i', subs=subs, selection=True))
cmd.delete('gly_i1')
cmd.delete('gly_i2')
cmd.delete('gly_i3')
cmd.delete('gly_i4')
cmd.delete('gly_i5')
cmd.delete('gly_i6')
cmd.delete('gly_i7')
cmd.delete('gly_i8')
cmd.delete('gly_i9')
cmd.delete('gly_i10')
cmd.delete('gly_i11')
cmd.delete('gly_i12')
cmd.delete('gly_i13')
cmd.delete('gly_i14')
cmd.delete('gly_i15')
cmd.delete('gly_i16')
cmd.delete('gly_i17')
cmd.delete('gly_i18')
cmd.delete('gly_i19')
cmd.delete('gly_i20')
cmd.delete('gly_i21')
cmd.delete('gly_i22')
cmd.delete('gly_i23')
cmd.delete('gly_i24')
cmd.delete('gly_i25')
cmd.delete('gly_i26')
cmd.delete('gly_i27')
cmd.delete('gly_i28')
cmd.delete('gly_i29')
cmd.delete('gly_i30')
cmd.delete('gly_i31')
cmd.delete('gly_i32')
cmd.delete('gly_i33')
cmd.delete('gly_i34')
cmd.delete('gly_i35')
cmd.delete('gly_i36')
IDSpec['S_1kyi_3_4_99_-'] = cmd.select('S_1kyi_3_4_99_-', 'gly|lys|thr|ser|gly_i')
cmd.delete('gly')
cmd.delete('lys')
cmd.delete('thr')
cmd.delete('ser')
cmd.delete('gly_i')
