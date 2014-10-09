'''
FUNC:S_2pfk_2_7_1_11
PDB:2pfk
EC:2.7.1.11
RESI:gly,arg,thr,asp,arg
LOCI:a-11,72,125,127,171;
'''
IDSpec[(('gly','CA'),('rasp','CG'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.19,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','CA'),('rasp','OD1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.59,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','CA'),('rasp','OD2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.37,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','N'),('rasp','CG'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.17,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','N'),('rasp','OD1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.57,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','N'),('rasp','OD2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.22,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','O'),('rasp','CG'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.75,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','O'),('rasp','OD1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.47,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','O'),('rasp','OD2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.67,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','CA'),('rthr','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.96,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','CA'),('rthr','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.08,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','CA'),('rthr','OG1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.59,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','N'),('rthr','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.96,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','N'),('rthr','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.83,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','N'),('rthr','OG1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.47,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','O'),('rthr','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.13,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','O'),('rthr','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.59,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','O'),('rthr','OG1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.51,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','CA'),('rarg','CZ'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.51,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','CA'),('rarg','NE'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.51,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','CA'),('rarg','NH1'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.51,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','N'),('rarg','CZ'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.51,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','N'),('rarg','NE'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.51,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','N'),('rarg','NH1'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.51,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','O'),('rarg','CZ'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.51,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','O'),('rarg','NE'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.51,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','O'),('rarg','NH1'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.51,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','CA'),('rarg','CZ'))] = cmd.select('gly28', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+16.23,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','CA'),('rarg','NE'))] = cmd.select('gly29', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+16.19,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','CA'),('rarg','NH1'))] = cmd.select('gly30', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+15.16,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','N'),('rarg','CZ'))] = cmd.select('gly31', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+16.13,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','N'),('rarg','NE'))] = cmd.select('gly32', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+16.07,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','N'),('rarg','NH1'))] = cmd.select('gly33', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+15.10,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','O'),('rarg','CZ'))] = cmd.select('gly34', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.71,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','O'),('rarg','NE'))] = cmd.select('gly35', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.50,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','O'),('rarg','NH1'))] = cmd.select('gly36', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.76,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('asp','CG'),('sgly','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.19,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','N'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.17,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','O'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.75,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.59,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','N'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.57,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','O'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.47,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.37,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','N'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.22,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','O'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.67,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','CG'),('rthr','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.70,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','CG'),('rthr','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.79,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','CG'),('rthr','OG1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.69,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD1'),('rthr','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.19,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD1'),('rthr','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.23,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD1'),('rthr','OG1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.94,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD2'),('rthr','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.12,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD2'),('rthr','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.06,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD2'),('rthr','OG1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.26,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.26,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.26,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.26,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.32,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.44,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.05,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.24,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.42,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.90,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.24,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.33,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.99,resSelectionSubs('arg','NH1',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36')
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
cmd.delete('asp28')
cmd.delete('asp29')
cmd.delete('asp30')
cmd.delete('asp31')
cmd.delete('asp32')
cmd.delete('asp33')
cmd.delete('asp34')
cmd.delete('asp35')
cmd.delete('asp36')
IDSpec[(('thr','CA'),('sgly','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.96,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','N'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.96,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','O'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.13,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.08,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','N'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.83,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','O'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.59,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.59,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','N'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.47,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','O'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.51,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','CG'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.19,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.12,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','CG'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.79,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.23,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.06,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','CG'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.94,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.26,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CA'),('rarg','CZ'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CA'),('rarg','NE'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.26,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CA'),('rarg','NH1'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','CB'),('rarg','CZ'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CB'),('rarg','NE'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.26,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CB'),('rarg','NH1'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','OG1'),('rarg','CZ'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','OG1'),('rarg','NE'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.26,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','OG1'),('rarg','NH1'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','CA'),('rarg','CZ'))] = cmd.select('thr28', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+17.91,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CA'),('rarg','NE'))] = cmd.select('thr29', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+17.28,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CA'),('rarg','NH1'))] = cmd.select('thr30', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+17.32,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','CB'),('rarg','CZ'))] = cmd.select('thr31', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+16.88,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CB'),('rarg','NE'))] = cmd.select('thr32', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+16.21,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CB'),('rarg','NH1'))] = cmd.select('thr33', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+16.34,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','OG1'),('rarg','CZ'))] = cmd.select('thr34', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+15.56,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','OG1'),('rarg','NE'))] = cmd.select('thr35', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+14.91,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','OG1'),('rarg','NH1'))] = cmd.select('thr36', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+15.00,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('sgly','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly','N'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly','O'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','N'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','O'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','N'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','O'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','OG1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','OG1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','OG1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','CZ'),('rarg','CZ'))] = cmd.select('arg28', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg','NE'))] = cmd.select('arg29', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','CZ'),('rarg','NH1'))] = cmd.select('arg30', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NE'),('rarg','CZ'))] = cmd.select('arg31', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NE'),('rarg','NE'))] = cmd.select('arg32', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NE'),('rarg','NH1'))] = cmd.select('arg33', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg','CZ'))] = cmd.select('arg34', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg','NE'))] = cmd.select('arg35', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NH1'),('rarg','NH1'))] = cmd.select('arg36', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('arg','NH1',subs)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27&br. arg28&br. arg29&br. arg30&br. arg31&br. arg32&br. arg33&br. arg34&br. arg35&br. arg36')
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
cmd.delete('arg28')
cmd.delete('arg29')
cmd.delete('arg30')
cmd.delete('arg31')
cmd.delete('arg32')
cmd.delete('arg33')
cmd.delete('arg34')
cmd.delete('arg35')
cmd.delete('arg36')
IDSpec[(('arg_i','CZ'),('sgly','CA'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.23,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sgly','N'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.13,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sgly','O'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.71,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sgly','CA'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.19,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sgly','N'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.07,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sgly','O'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.50,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sgly','CA'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.16,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sgly','N'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.10,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sgly','O'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.76,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','CG'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.32,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','OD1'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','OD2'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.24,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','CG'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','OD1'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.42,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','OD2'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.33,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','CG'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.05,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','OD1'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.90,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','OD2'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.99,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sthr','CA'))] = cmd.select('arg_i19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.91,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sthr','CB'))] = cmd.select('arg_i20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.88,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sthr','OG1'))] = cmd.select('arg_i21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.56,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sthr','CA'))] = cmd.select('arg_i22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.28,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sthr','CB'))] = cmd.select('arg_i23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.21,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sthr','OG1'))] = cmd.select('arg_i24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.91,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sthr','CA'))] = cmd.select('arg_i25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.32,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sthr','CB'))] = cmd.select('arg_i26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.34,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sthr','OG1'))] = cmd.select('arg_i27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i28', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i29', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i30', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.00,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i31', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i32', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i33', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.00,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i34', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i35', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i36', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.00,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['arg_i'] = cmd.select('arg_i',' br. arg_i1&br. arg_i2&br. arg_i3&br. arg_i4&br. arg_i5&br. arg_i6&br. arg_i7&br. arg_i8&br. arg_i9&br. arg_i10&br. arg_i11&br. arg_i12&br. arg_i13&br. arg_i14&br. arg_i15&br. arg_i16&br. arg_i17&br. arg_i18&br. arg_i19&br. arg_i20&br. arg_i21&br. arg_i22&br. arg_i23&br. arg_i24&br. arg_i25&br. arg_i26&br. arg_i27&br. arg_i28&br. arg_i29&br. arg_i30&br. arg_i31&br. arg_i32&br. arg_i33&br. arg_i34&br. arg_i35&br. arg_i36')
IDSpec['r_arg_i'] = cmd.count_atoms(resSelectionSubs('arg_i', subs=subs, selection=True))
cmd.delete('arg_i1')
cmd.delete('arg_i2')
cmd.delete('arg_i3')
cmd.delete('arg_i4')
cmd.delete('arg_i5')
cmd.delete('arg_i6')
cmd.delete('arg_i7')
cmd.delete('arg_i8')
cmd.delete('arg_i9')
cmd.delete('arg_i10')
cmd.delete('arg_i11')
cmd.delete('arg_i12')
cmd.delete('arg_i13')
cmd.delete('arg_i14')
cmd.delete('arg_i15')
cmd.delete('arg_i16')
cmd.delete('arg_i17')
cmd.delete('arg_i18')
cmd.delete('arg_i19')
cmd.delete('arg_i20')
cmd.delete('arg_i21')
cmd.delete('arg_i22')
cmd.delete('arg_i23')
cmd.delete('arg_i24')
cmd.delete('arg_i25')
cmd.delete('arg_i26')
cmd.delete('arg_i27')
cmd.delete('arg_i28')
cmd.delete('arg_i29')
cmd.delete('arg_i30')
cmd.delete('arg_i31')
cmd.delete('arg_i32')
cmd.delete('arg_i33')
cmd.delete('arg_i34')
cmd.delete('arg_i35')
cmd.delete('arg_i36')
IDSpec['S_2pfk_2_7_1_11'] = cmd.select('S_2pfk_2_7_1_11', 'gly|asp|thr|arg|arg_i')
cmd.delete('gly')
cmd.delete('asp')
cmd.delete('thr')
cmd.delete('arg')
cmd.delete('arg_i')
