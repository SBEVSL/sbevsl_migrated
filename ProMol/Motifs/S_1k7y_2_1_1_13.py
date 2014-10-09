'''
FUNC:S_1k7y_2_1_1_13
PDB:1k7y
EC:2.1.1.13
RESI:asp,gly,leu,ser
LOCI:a-757,759,770,810;
'''
IDSpec[(('ser','CA'),('rasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.40,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CA'),('rasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.95,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CA'),('rasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.29,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CB'),('rasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.32,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CB'),('rasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.65,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CB'),('rasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.26,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','OG'),('rasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.30,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','OG'),('rasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.84,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','OG'),('rasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.05,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CA'),('rgly','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.20,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','CA'),('rgly','N'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.49,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','CA'),('rgly','O'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.15,resSelectionSubs('gly','O',subs)))
IDSpec[(('ser','CB'),('rgly','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.88,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','CB'),('rgly','N'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.28,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','CB'),('rgly','O'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.87,resSelectionSubs('gly','O',subs)))
IDSpec[(('ser','OG'),('rgly','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.02,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ser','OG'),('rgly','N'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.33,resSelectionSubs('gly','N',subs)))
IDSpec[(('ser','OG'),('rgly','O'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.30,resSelectionSubs('gly','O',subs)))
IDSpec[(('ser','CA'),('rleu','CD1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+21.64,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('ser','CA'),('rleu','CD2'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+23.72,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('ser','CA'),('rleu','CG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+22.76,resSelectionSubs('leu','CG',subs)))
IDSpec[(('ser','CB'),('rleu','CD1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+20.62,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('ser','CB'),('rleu','CD2'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+22.67,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('ser','CB'),('rleu','CG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+21.68,resSelectionSubs('leu','CG',subs)))
IDSpec[(('ser','OG'),('rleu','CD1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+21.23,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('ser','OG'),('rleu','CD2'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+23.29,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('ser','OG'),('rleu','CG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+22.24,resSelectionSubs('leu','CG',subs)))
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
IDSpec[(('asp','CG'),('sser','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.40,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.32,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','OG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.30,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.95,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.65,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','OG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.84,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.29,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.26,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','OG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.05,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','CG'),('rgly','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.03,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','CG'),('rgly','N'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.12,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','CG'),('rgly','O'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.38,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD1'),('rgly','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.25,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD1'),('rgly','N'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.65,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD1'),('rgly','O'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.48,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD2'),('rgly','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.61,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD2'),('rgly','N'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.62,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD2'),('rgly','O'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.47,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','CG'),('rleu','CD1'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+20.25,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','CG'),('rleu','CD2'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+22.38,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','CG'),('rleu','CG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+21.18,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','OD1'),('rleu','CD1'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.54,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','OD1'),('rleu','CD2'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+21.62,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','OD1'),('rleu','CG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+20.46,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','OD2'),('rleu','CD1'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+21.05,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','OD2'),('rleu','CD2'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+23.15,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','OD2'),('rleu','CG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+21.91,resSelectionSubs('leu','CG',subs)))
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
IDSpec[(('gly','CA'),('sser','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.20,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('sser','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.88,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('sser','OG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.02,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gly','N'),('sser','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.49,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly','N'),('sser','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.28,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly','N'),('sser','OG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.33,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gly','O'),('sser','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.15,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gly','O'),('sser','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.87,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gly','O'),('sser','OG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.30,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','CG'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.03,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.25,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.61,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','CG'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.12,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.65,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.62,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','CG'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.38,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.48,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.47,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','CA'),('rleu','CD1'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.73,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gly','CA'),('rleu','CD2'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+20.68,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gly','CA'),('rleu','CG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+19.34,resSelectionSubs('leu','CG',subs)))
IDSpec[(('gly','N'),('rleu','CD1'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+19.49,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gly','N'),('rleu','CD2'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+21.53,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gly','N'),('rleu','CG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+20.19,resSelectionSubs('leu','CG',subs)))
IDSpec[(('gly','O'),('rleu','CD1'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.85,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gly','O'),('rleu','CD2'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+18.93,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gly','O'),('rleu','CG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.56,resSelectionSubs('leu','CG',subs)))
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
IDSpec[(('leu','CD1'),('sser','CA'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+21.64,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('leu','CD1'),('sser','CB'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+20.62,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('leu','CD1'),('sser','OG'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+21.23,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('leu','CD2'),('sser','CA'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+23.72,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('leu','CD2'),('sser','CB'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+22.67,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('leu','CD2'),('sser','OG'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+23.29,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('leu','CG'),('sser','CA'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+22.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('leu','CG'),('sser','CB'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+21.68,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('leu','CG'),('sser','OG'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+22.24,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp','CG'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+20.25,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp','OD1'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+19.54,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp','OD2'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+21.05,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','CG'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+22.38,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','OD1'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+21.62,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','OD2'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+23.15,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','CG'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+21.18,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','OD1'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+20.46,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','OD2'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+21.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgly','CA'))] = cmd.select('leu19', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+18.73,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgly','N'))] = cmd.select('leu20', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+19.49,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgly','O'))] = cmd.select('leu21', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+16.85,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgly','CA'))] = cmd.select('leu22', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+20.68,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgly','N'))] = cmd.select('leu23', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+21.53,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgly','O'))] = cmd.select('leu24', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+18.93,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('leu','CG'),('sgly','CA'))] = cmd.select('leu25', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+19.34,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('leu','CG'),('sgly','N'))] = cmd.select('leu26', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+20.19,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('leu','CG'),('sgly','O'))] = cmd.select('leu27', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+17.56,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18&br. leu19&br. leu20&br. leu21&br. leu22&br. leu23&br. leu24&br. leu25&br. leu26&br. leu27')
IDSpec['r_leu'] = cmd.count_atoms(resSelectionSubs('leu', subs=subs, selection=True))
cmd.delete('leu1')
cmd.delete('leu2')
cmd.delete('leu3')
cmd.delete('leu4')
cmd.delete('leu5')
cmd.delete('leu6')
cmd.delete('leu7')
cmd.delete('leu8')
cmd.delete('leu9')
cmd.delete('leu10')
cmd.delete('leu11')
cmd.delete('leu12')
cmd.delete('leu13')
cmd.delete('leu14')
cmd.delete('leu15')
cmd.delete('leu16')
cmd.delete('leu17')
cmd.delete('leu18')
cmd.delete('leu19')
cmd.delete('leu20')
cmd.delete('leu21')
cmd.delete('leu22')
cmd.delete('leu23')
cmd.delete('leu24')
cmd.delete('leu25')
cmd.delete('leu26')
cmd.delete('leu27')
IDSpec['S_1k7y_2_1_1_13'] = cmd.select('S_1k7y_2_1_1_13', 'ser|asp|gly|leu')
cmd.delete('ser')
cmd.delete('asp')
cmd.delete('gly')
cmd.delete('leu')