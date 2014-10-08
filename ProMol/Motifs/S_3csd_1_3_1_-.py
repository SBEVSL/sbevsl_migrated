'''
FUNC:S_3csd_1_3_1_-
PDB:3csd
EC:1.3.1.-
RESI:asn,ser,ala,tyr,lys
LOCI:a-114,144,154,157,161;
'''
IDSpec[(('asn','CG'),('rlys','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.92,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asn','CG'),('rlys','CE'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.47,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asn','CG'),('rlys','NZ'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asn','ND2'),('rlys','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.91,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asn','ND2'),('rlys','CE'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.21,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asn','ND2'),('rlys','NZ'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.32,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asn','OD1'),('rlys','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.55,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asn','OD1'),('rlys','CE'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.07,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asn','OD1'),('rlys','NZ'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.81,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asn','CG'),('rser','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.67,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','CG'),('rser','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.60,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','CG'),('rser','OG'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.31,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','ND2'),('rser','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','ND2'),('rser','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.43,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','ND2'),('rser','OG'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.12,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','OD1'),('rser','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.06,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','OD1'),('rser','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.88,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','OD1'),('rser','OG'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.45,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','CG'),('rtyr','CE1'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.90,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','CG'),('rtyr','CZ'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.03,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','CG'),('rtyr','OH'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.46,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asn','ND2'),('rtyr','CE1'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.51,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','ND2'),('rtyr','CZ'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.68,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','ND2'),('rtyr','OH'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.96,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asn','OD1'),('rtyr','CE1'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.80,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','OD1'),('rtyr','CZ'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.98,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','OD1'),('rtyr','OH'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.58,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asn','CG'),('rala','CA'))] = cmd.select('asn28', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.85,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asn','CG'),('rala','CB'))] = cmd.select('asn29', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.39,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asn','CG'),('rala','CG'))] = cmd.select('asn30', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.39,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asn','ND2'),('rala','CA'))] = cmd.select('asn31', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.67,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asn','ND2'),('rala','CB'))] = cmd.select('asn32', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.18,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asn','ND2'),('rala','CG'))] = cmd.select('asn33', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.18,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asn','OD1'),('rala','CA'))] = cmd.select('asn34', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.69,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asn','OD1'),('rala','CB'))] = cmd.select('asn35', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.18,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asn','OD1'),('rala','CG'))] = cmd.select('asn36', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.18,resSelectionSubs('ala','CG',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32&br. asn33&br. asn34&br. asn35&br. asn36')
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
cmd.delete('asn28')
cmd.delete('asn29')
cmd.delete('asn30')
cmd.delete('asn31')
cmd.delete('asn32')
cmd.delete('asn33')
cmd.delete('asn34')
cmd.delete('asn35')
cmd.delete('asn36')
IDSpec[(('lys','CD'),('sasn','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.92,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasn','ND2'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.91,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('lys','CD'),('sasn','OD1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.55,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasn','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.47,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasn','ND2'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.21,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasn','OD1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.07,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasn','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.87,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasn','ND2'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.32,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasn','OD1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.81,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('rser','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.07,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CD'),('rser','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.28,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CD'),('rser','OG'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.39,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CE'),('rser','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.27,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CE'),('rser','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.38,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CE'),('rser','OG'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.34,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','NZ'),('rser','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.67,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','NZ'),('rser','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.11,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','NZ'),('rser','OG'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.18,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CD'),('rtyr','CE1'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.59,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CD'),('rtyr','CZ'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.56,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CD'),('rtyr','OH'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.58,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','CE'),('rtyr','CE1'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.74,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CE'),('rtyr','CZ'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.78,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CE'),('rtyr','OH'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.54,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','NZ'),('rtyr','CE1'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.89,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','NZ'),('rtyr','CZ'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.93,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','NZ'),('rtyr','OH'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.35,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','CD'),('rala','CA'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.88,resSelectionSubs('ala','CA',subs)))
IDSpec[(('lys','CD'),('rala','CB'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.08,resSelectionSubs('ala','CB',subs)))
IDSpec[(('lys','CD'),('rala','CG'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.08,resSelectionSubs('ala','CG',subs)))
IDSpec[(('lys','CE'),('rala','CA'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.94,resSelectionSubs('ala','CA',subs)))
IDSpec[(('lys','CE'),('rala','CB'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.02,resSelectionSubs('ala','CB',subs)))
IDSpec[(('lys','CE'),('rala','CG'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.02,resSelectionSubs('ala','CG',subs)))
IDSpec[(('lys','NZ'),('rala','CA'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.38,resSelectionSubs('ala','CA',subs)))
IDSpec[(('lys','NZ'),('rala','CB'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.43,resSelectionSubs('ala','CB',subs)))
IDSpec[(('lys','NZ'),('rala','CG'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.43,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('ser','CA'),('sasn','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.67,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','ND2'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.46,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','OD1'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.06,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.60,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','ND2'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.43,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','OD1'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.88,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.31,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','ND2'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.12,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','OD1'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.45,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.27,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','NZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.67,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.28,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.38,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','NZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.11,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.39,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.34,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','NZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.18,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CA'),('rtyr','CE1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.96,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('ser','CA'),('rtyr','CZ'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.88,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('ser','CA'),('rtyr','OH'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.23,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('ser','CB'),('rtyr','CE1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.54,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('ser','CB'),('rtyr','CZ'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.43,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('ser','CB'),('rtyr','OH'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.96,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('ser','OG'),('rtyr','CE1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.58,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('ser','OG'),('rtyr','CZ'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.30,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('ser','OG'),('rtyr','OH'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.92,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('ser','CA'),('rala','CA'))] = cmd.select('ser28', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.18,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CA'),('rala','CB'))] = cmd.select('ser29', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.00,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CA'),('rala','CG'))] = cmd.select('ser30', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.00,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','CB'),('rala','CA'))] = cmd.select('ser31', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.76,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CB'),('rala','CB'))] = cmd.select('ser32', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.57,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CB'),('rala','CG'))] = cmd.select('ser33', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.57,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','OG'),('rala','CA'))] = cmd.select('ser34', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.06,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','OG'),('rala','CB'))] = cmd.select('ser35', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.79,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','OG'),('rala','CG'))] = cmd.select('ser36', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.79,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('tyr','CE1'),('sasn','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.90,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasn','ND2'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.51,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasn','OD1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.80,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.03,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','ND2'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.68,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','OD1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.98,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.46,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','ND2'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.96,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','OD1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.58,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','CD'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.59,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','CE'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.74,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','NZ'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.89,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CD'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.56,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CE'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.78,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','NZ'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.93,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CD'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.58,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CE'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.54,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','NZ'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.35,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sser','CA'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.96,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sser','CB'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.54,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sser','OG'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.58,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sser','CA'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.88,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sser','CB'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.43,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sser','OG'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.30,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sser','CA'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.23,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('sser','CB'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.96,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('tyr','OH'),('sser','OG'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.92,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rala','CA'))] = cmd.select('tyr28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.90,resSelectionSubs('ala','CA',subs)))
IDSpec[(('tyr','CE1'),('rala','CB'))] = cmd.select('tyr29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.88,resSelectionSubs('ala','CB',subs)))
IDSpec[(('tyr','CE1'),('rala','CG'))] = cmd.select('tyr30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.88,resSelectionSubs('ala','CG',subs)))
IDSpec[(('tyr','CZ'),('rala','CA'))] = cmd.select('tyr31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.04,resSelectionSubs('ala','CA',subs)))
IDSpec[(('tyr','CZ'),('rala','CB'))] = cmd.select('tyr32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.85,resSelectionSubs('ala','CB',subs)))
IDSpec[(('tyr','CZ'),('rala','CG'))] = cmd.select('tyr33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.85,resSelectionSubs('ala','CG',subs)))
IDSpec[(('tyr','OH'),('rala','CA'))] = cmd.select('tyr34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.34,resSelectionSubs('ala','CA',subs)))
IDSpec[(('tyr','OH'),('rala','CB'))] = cmd.select('tyr35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.09,resSelectionSubs('ala','CB',subs)))
IDSpec[(('tyr','OH'),('rala','CG'))] = cmd.select('tyr36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.09,resSelectionSubs('ala','CG',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27&br. tyr28&br. tyr29&br. tyr30&br. tyr31&br. tyr32&br. tyr33&br. tyr34&br. tyr35&br. tyr36')
IDSpec['r_tyr'] = cmd.count_atoms(resSelectionSubs('tyr', subs=subs, selection=True))
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
cmd.delete('tyr19')
cmd.delete('tyr20')
cmd.delete('tyr21')
cmd.delete('tyr22')
cmd.delete('tyr23')
cmd.delete('tyr24')
cmd.delete('tyr25')
cmd.delete('tyr26')
cmd.delete('tyr27')
cmd.delete('tyr28')
cmd.delete('tyr29')
cmd.delete('tyr30')
cmd.delete('tyr31')
cmd.delete('tyr32')
cmd.delete('tyr33')
cmd.delete('tyr34')
cmd.delete('tyr35')
cmd.delete('tyr36')
IDSpec[(('ala','CA'),('sasn','CG'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+12.85,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ala','CA'),('sasn','ND2'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+13.67,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ala','CA'),('sasn','OD1'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+11.69,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ala','CB'),('sasn','CG'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+12.39,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ala','CB'),('sasn','ND2'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+13.18,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ala','CB'),('sasn','OD1'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+11.18,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ala','CG'),('sasn','CG'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+11.18,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ala','CG'),('sasn','ND2'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+11.18,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ala','CG'),('sasn','OD1'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+11.18,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ala','CA'),('slys','CD'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+12.88,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ala','CA'),('slys','CE'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+12.94,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ala','CA'),('slys','NZ'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+14.38,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ala','CB'),('slys','CD'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+12.08,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ala','CB'),('slys','CE'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+12.02,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ala','CB'),('slys','NZ'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+13.43,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ala','CG'),('slys','CD'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+13.43,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ala','CG'),('slys','CE'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+13.43,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ala','CG'),('slys','NZ'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+13.43,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','CA'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+14.18,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','CB'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+12.76,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','OG'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+12.06,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','CA'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+13.00,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','CB'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+11.57,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','OG'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10.79,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','CA'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.79,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','CB'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.79,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','OG'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.79,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CA'),('styr','CE1'))] = cmd.select('ala28', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.90,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ala','CA'),('styr','CZ'))] = cmd.select('ala29', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.04,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ala','CA'),('styr','OH'))] = cmd.select('ala30', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+11.34,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ala','CB'),('styr','CE1'))] = cmd.select('ala31', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.88,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ala','CB'),('styr','CZ'))] = cmd.select('ala32', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.85,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ala','CB'),('styr','OH'))] = cmd.select('ala33', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10.09,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ala','CG'),('styr','CE1'))] = cmd.select('ala34', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.09,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ala','CG'),('styr','CZ'))] = cmd.select('ala35', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.09,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ala','CG'),('styr','OH'))] = cmd.select('ala36', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.09,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18&br. ala19&br. ala20&br. ala21&br. ala22&br. ala23&br. ala24&br. ala25&br. ala26&br. ala27&br. ala28&br. ala29&br. ala30&br. ala31&br. ala32&br. ala33&br. ala34&br. ala35&br. ala36')
IDSpec['r_ala'] = cmd.count_atoms(resSelectionSubs('ala', subs=subs, selection=True))
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
cmd.delete('ala10')
cmd.delete('ala11')
cmd.delete('ala12')
cmd.delete('ala13')
cmd.delete('ala14')
cmd.delete('ala15')
cmd.delete('ala16')
cmd.delete('ala17')
cmd.delete('ala18')
cmd.delete('ala19')
cmd.delete('ala20')
cmd.delete('ala21')
cmd.delete('ala22')
cmd.delete('ala23')
cmd.delete('ala24')
cmd.delete('ala25')
cmd.delete('ala26')
cmd.delete('ala27')
cmd.delete('ala28')
cmd.delete('ala29')
cmd.delete('ala30')
cmd.delete('ala31')
cmd.delete('ala32')
cmd.delete('ala33')
cmd.delete('ala34')
cmd.delete('ala35')
cmd.delete('ala36')
IDSpec['S_3csd_1_3_1_-'] = cmd.select('S_3csd_1_3_1_-', 'asn|lys|ser|tyr|ala')
cmd.delete('asn')
cmd.delete('lys')
cmd.delete('ser')
cmd.delete('tyr')
cmd.delete('ala')
