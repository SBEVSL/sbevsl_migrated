'''
FUNC:S_2prl_1_3_99_11
PDB:2prl
EC:1.3.99.11
RESI:phe,ser,thr,lys
LOCI:a-149,215,218,255;
'''
IDSpec[(('ser','CA'),('rthr','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.25,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','CA'),('rthr','CB'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.14,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','CA'),('rthr','OG1'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.37,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','CB'),('rthr','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.40,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','CB'),('rthr','CB'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.09,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','CB'),('rthr','OG1'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.35,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','OG'),('rthr','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.09,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','OG'),('rthr','CB'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.01,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','OG'),('rthr','OG1'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.40,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','CA'),('rphe','CD1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.47,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('ser','CA'),('rphe','CE1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.54,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('ser','CA'),('rphe','CZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.25,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('ser','CB'),('rphe','CD1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.08,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('ser','CB'),('rphe','CE1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.26,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('ser','CB'),('rphe','CZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.02,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('ser','OG'),('rphe','CD1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.02,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('ser','OG'),('rphe','CE1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.52,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('ser','OG'),('rphe','CZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.60,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('ser','CA'),('rlys','CD'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.01,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CA'),('rlys','CE'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.01,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CA'),('rlys','NZ'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.41,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CB'),('rlys','CD'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.48,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CB'),('rlys','CE'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.55,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CB'),('rlys','NZ'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.76,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','OG'),('rlys','CD'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.31,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','OG'),('rlys','CE'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.22,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','OG'),('rlys','NZ'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.27,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('thr','CA'),('sser','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.25,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sser','CB'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.40,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','CA'),('sser','OG'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.09,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.14,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','CB'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.09,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','OG'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.01,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.37,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','CB'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.35,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','OG'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.40,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','CA'),('rphe','CD1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.04,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','CA'),('rphe','CE1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.11,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','CA'),('rphe','CZ'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.58,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','CB'),('rphe','CD1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.96,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','CB'),('rphe','CE1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.02,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','CB'),('rphe','CZ'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.34,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','OG1'),('rphe','CD1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.74,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('thr','OG1'),('rphe','CE1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.86,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('thr','OG1'),('rphe','CZ'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.05,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('thr','CA'),('rlys','CD'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+15.76,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CA'),('rlys','CE'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+15.94,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CA'),('rlys','NZ'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+16.11,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','CB'),('rlys','CD'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+15.08,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CB'),('rlys','CE'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+15.41,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CB'),('rlys','NZ'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+15.54,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','OG1'),('rlys','CD'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+16.05,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','OG1'),('rlys','CE'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+16.47,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','OG1'),('rlys','NZ'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+16.63,resSelectionSubs('lys','NZ',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27')
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
IDSpec[(('phe','CD1'),('sser','CA'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.47,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('sser','CB'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.08,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('phe','CD1'),('sser','OG'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.02,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sser','CA'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.54,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('sser','CB'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.26,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('phe','CE1'),('sser','OG'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.52,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sser','CA'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.25,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('sser','CB'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.02,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('phe','CZ'),('sser','OG'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.60,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','CA'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.04,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','CB'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.96,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CD1'),('sthr','OG1'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.74,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','CA'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.11,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','CB'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+8.02,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CE1'),('sthr','OG1'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+8.86,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','CA'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.58,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','CB'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.34,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('phe','CZ'),('sthr','OG1'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.05,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('phe','CD1'),('rlys','CD'))] = cmd.select('phe19', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.93,resSelectionSubs('lys','CD',subs)))
IDSpec[(('phe','CD1'),('rlys','CE'))] = cmd.select('phe20', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.22,resSelectionSubs('lys','CE',subs)))
IDSpec[(('phe','CD1'),('rlys','NZ'))] = cmd.select('phe21', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.80,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('phe','CE1'),('rlys','CD'))] = cmd.select('phe22', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.70,resSelectionSubs('lys','CD',subs)))
IDSpec[(('phe','CE1'),('rlys','CE'))] = cmd.select('phe23', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.08,resSelectionSubs('lys','CE',subs)))
IDSpec[(('phe','CE1'),('rlys','NZ'))] = cmd.select('phe24', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.78,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('phe','CZ'),('rlys','CD'))] = cmd.select('phe25', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.82,resSelectionSubs('lys','CD',subs)))
IDSpec[(('phe','CZ'),('rlys','CE'))] = cmd.select('phe26', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.36,resSelectionSubs('lys','CE',subs)))
IDSpec[(('phe','CZ'),('rlys','NZ'))] = cmd.select('phe27', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.26,resSelectionSubs('lys','NZ',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9&br. phe10&br. phe11&br. phe12&br. phe13&br. phe14&br. phe15&br. phe16&br. phe17&br. phe18&br. phe19&br. phe20&br. phe21&br. phe22&br. phe23&br. phe24&br. phe25&br. phe26&br. phe27')
IDSpec['r_phe'] = cmd.count_atoms(resSelectionSubs('phe', subs=subs, selection=True))
cmd.delete('phe1')
cmd.delete('phe2')
cmd.delete('phe3')
cmd.delete('phe4')
cmd.delete('phe5')
cmd.delete('phe6')
cmd.delete('phe7')
cmd.delete('phe8')
cmd.delete('phe9')
cmd.delete('phe10')
cmd.delete('phe11')
cmd.delete('phe12')
cmd.delete('phe13')
cmd.delete('phe14')
cmd.delete('phe15')
cmd.delete('phe16')
cmd.delete('phe17')
cmd.delete('phe18')
cmd.delete('phe19')
cmd.delete('phe20')
cmd.delete('phe21')
cmd.delete('phe22')
cmd.delete('phe23')
cmd.delete('phe24')
cmd.delete('phe25')
cmd.delete('phe26')
cmd.delete('phe27')
IDSpec[(('lys','CD'),('sser','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.01,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.48,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','OG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.31,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.01,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.55,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','OG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.22,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.41,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.76,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','OG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.27,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.76,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.08,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','OG1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.05,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.94,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.41,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','OG1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.47,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.11,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.54,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','OG1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.63,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CD'),('sphe','CD1'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.93,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sphe','CE1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.70,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sphe','CZ'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.82,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sphe','CD1'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.22,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sphe','CE1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.08,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sphe','CZ'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.36,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sphe','CD1'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.80,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sphe','CE1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.78,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sphe','CZ'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.26,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
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
IDSpec['S_2prl_1_3_99_11'] = cmd.select('S_2prl_1_3_99_11', 'ser|thr|phe|lys')
cmd.delete('ser')
cmd.delete('thr')
cmd.delete('phe')
cmd.delete('lys')
