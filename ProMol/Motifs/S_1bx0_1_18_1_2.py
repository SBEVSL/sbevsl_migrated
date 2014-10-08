'''
FUNC:S_1bx0_1_18_1_2
PDB:1bx0
EC:1.18.1.2
RESI:tyr,ser,cys,leu
LOCI:a-95,96,272,312;
'''
IDSpec[(('cys','CA'),('rser','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.70,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CA'),('rser','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.27,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CA'),('rser','OG'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.32,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CB'),('rser','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.49,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CB'),('rser','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.01,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CB'),('rser','OG'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.18,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','SG'),('rser','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.86,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','SG'),('rser','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.44,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','SG'),('rser','OG'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.49,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CA'),('rleu','CD1'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.07,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('cys','CA'),('rleu','CD2'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.37,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('cys','CA'),('rleu','CG'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.79,resSelectionSubs('leu','CG',subs)))
IDSpec[(('cys','CB'),('rleu','CD1'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.87,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('cys','CB'),('rleu','CD2'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.66,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('cys','CB'),('rleu','CG'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.44,resSelectionSubs('leu','CG',subs)))
IDSpec[(('cys','SG'),('rleu','CD1'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.88,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('cys','SG'),('rleu','CD2'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.45,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('cys','SG'),('rleu','CG'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.41,resSelectionSubs('leu','CG',subs)))
IDSpec[(('cys','CA'),('rtyr','CE1'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+17.34,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('cys','CA'),('rtyr','CZ'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.99,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('cys','CA'),('rtyr','OH'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+17.78,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('cys','CB'),('rtyr','CE1'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+16.69,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('cys','CB'),('rtyr','CZ'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+16.42,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('cys','CB'),('rtyr','OH'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+17.31,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('cys','SG'),('rtyr','CE1'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+14.90,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('cys','SG'),('rtyr','CZ'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+14.66,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('cys','SG'),('rtyr','OH'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+15.58,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('ser','CA'),('scys','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.70,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CB'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.49,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','SG'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.86,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.27,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CB'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.01,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','SG'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.44,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.32,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CB'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.18,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','SG'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.49,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CA'),('rleu','CD1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.98,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('ser','CA'),('rleu','CD2'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.99,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('ser','CA'),('rleu','CG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.21,resSelectionSubs('leu','CG',subs)))
IDSpec[(('ser','CB'),('rleu','CD1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.44,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('ser','CB'),('rleu','CD2'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.30,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('ser','CB'),('rleu','CG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.45,resSelectionSubs('leu','CG',subs)))
IDSpec[(('ser','OG'),('rleu','CD1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.09,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('ser','OG'),('rleu','CD2'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.03,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('ser','OG'),('rleu','CG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.08,resSelectionSubs('leu','CG',subs)))
IDSpec[(('ser','CA'),('rtyr','CE1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.24,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('ser','CA'),('rtyr','CZ'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.58,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('ser','CA'),('rtyr','OH'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.87,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('ser','CB'),('rtyr','CE1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.25,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('ser','CB'),('rtyr','CZ'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.40,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('ser','CB'),('rtyr','OH'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.63,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('ser','OG'),('rtyr','CE1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.41,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('ser','OG'),('rtyr','CZ'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.52,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('ser','OG'),('rtyr','OH'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.67,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('leu','CD1'),('scys','CA'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.07,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('leu','CD1'),('scys','CB'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.87,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('leu','CD1'),('scys','SG'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.88,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('leu','CD2'),('scys','CA'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.37,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('leu','CD2'),('scys','CB'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.66,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('leu','CD2'),('scys','SG'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.45,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('leu','CG'),('scys','CA'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.79,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('leu','CG'),('scys','CB'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.44,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('leu','CG'),('scys','SG'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+6.41,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('leu','CD1'),('sser','CA'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.98,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('leu','CD1'),('sser','CB'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.44,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('leu','CD1'),('sser','OG'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.09,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('leu','CD2'),('sser','CA'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.99,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('leu','CD2'),('sser','CB'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.30,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('leu','CD2'),('sser','OG'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.03,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('leu','CG'),('sser','CA'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.21,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('leu','CG'),('sser','CB'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.45,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('leu','CG'),('sser','OG'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.08,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('leu','CD1'),('rtyr','CE1'))] = cmd.select('leu19', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+14.53,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('leu','CD1'),('rtyr','CZ'))] = cmd.select('leu20', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+14.70,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('leu','CD1'),('rtyr','OH'))] = cmd.select('leu21', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+15.49,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('leu','CD2'),('rtyr','CE1'))] = cmd.select('leu22', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+13.92,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('leu','CD2'),('rtyr','CZ'))] = cmd.select('leu23', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+14.11,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('leu','CD2'),('rtyr','OH'))] = cmd.select('leu24', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+15.08,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('leu','CG'),('rtyr','CE1'))] = cmd.select('leu25', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+14.46,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('leu','CG'),('rtyr','CZ'))] = cmd.select('leu26', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+14.55,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('leu','CG'),('rtyr','OH'))] = cmd.select('leu27', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+15.41,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('scys','CA'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+17.34,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('scys','CB'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+16.69,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('tyr','CE1'),('scys','SG'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.90,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('scys','CA'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+16.99,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('scys','CB'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+16.42,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('tyr','CZ'),('scys','SG'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.66,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('tyr','OH'),('scys','CA'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+17.78,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('scys','CB'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+17.31,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('tyr','OH'),('scys','SG'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.58,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sser','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.24,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sser','CB'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.25,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sser','OG'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.41,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sser','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.58,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sser','CB'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.40,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sser','OG'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.52,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sser','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.87,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('sser','CB'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.63,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('tyr','OH'),('sser','OG'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.67,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sleu','CD1'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.53,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sleu','CD2'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.92,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sleu','CG'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.46,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sleu','CD1'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.70,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sleu','CD2'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.11,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sleu','CG'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.55,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sleu','CD1'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.49,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sleu','CD2'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.08,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sleu','CG'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.41,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27')
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
IDSpec['S_1bx0_1_18_1_2'] = cmd.select('S_1bx0_1_18_1_2', 'cys|ser|leu|tyr')
cmd.delete('cys')
cmd.delete('ser')
cmd.delete('leu')
cmd.delete('tyr')