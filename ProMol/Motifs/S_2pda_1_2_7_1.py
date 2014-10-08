'''
FUNC:S_2pda_1_2_7_1
PDB:2pda
EC:1.2.7.1
RESI:thr,glu,arg,met,asn
LOCI:a-31,64,114,746,996;
'''
IDSpec[(('met','CE'),('rthr','CA'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+24.95,resSelectionSubs('thr','CA',subs)))
IDSpec[(('met','CE'),('rthr','CB'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+23.51,resSelectionSubs('thr','CB',subs)))
IDSpec[(('met','CE'),('rthr','OG1'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+22.61,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('met','CG'),('rthr','CA'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+26.28,resSelectionSubs('thr','CA',subs)))
IDSpec[(('met','CG'),('rthr','CB'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+24.86,resSelectionSubs('thr','CB',subs)))
IDSpec[(('met','CG'),('rthr','OG1'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+23.87,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('met','SD'),('rthr','CA'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+26.14,resSelectionSubs('thr','CA',subs)))
IDSpec[(('met','SD'),('rthr','CB'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+24.68,resSelectionSubs('thr','CB',subs)))
IDSpec[(('met','SD'),('rthr','OG1'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+23.78,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('met','CE'),('rglu','CD'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+31.93,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','CE'),('rglu','OE1'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+31.27,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','CE'),('rglu','OE2'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+31.43,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','CG'),('rglu','CD'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+32.55,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','CG'),('rglu','OE1'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+31.98,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','CG'),('rglu','OE2'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+31.96,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','SD'),('rglu','CD'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+32.80,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','SD'),('rglu','OE1'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+32.20,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','SD'),('rglu','OE2'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+32.24,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','CE'),('rasn','CG'))] = cmd.select('met19', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+18.49,resSelectionSubs('asn','CG',subs)))
IDSpec[(('met','CE'),('rasn','ND2'))] = cmd.select('met20', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+19.66,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('met','CE'),('rasn','OD1'))] = cmd.select('met21', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+17.45,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('met','CG'),('rasn','CG'))] = cmd.select('met22', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+19.12,resSelectionSubs('asn','CG',subs)))
IDSpec[(('met','CG'),('rasn','ND2'))] = cmd.select('met23', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+20.32,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('met','CG'),('rasn','OD1'))] = cmd.select('met24', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+18.20,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('met','SD'),('rasn','CG'))] = cmd.select('met25', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+19.35,resSelectionSubs('asn','CG',subs)))
IDSpec[(('met','SD'),('rasn','ND2'))] = cmd.select('met26', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+20.50,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('met','SD'),('rasn','OD1'))] = cmd.select('met27', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+18.34,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('met','CE'),('rarg','CZ'))] = cmd.select('met28', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+26.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CE'),('rarg','NE'))] = cmd.select('met29', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+26.92,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CE'),('rarg','NH1'))] = cmd.select('met30', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+26.15,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','CG'),('rarg','CZ'))] = cmd.select('met31', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+27.39,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CG'),('rarg','NE'))] = cmd.select('met32', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+28.15,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CG'),('rarg','NH1'))] = cmd.select('met33', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+27.29,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','SD'),('rarg','CZ'))] = cmd.select('met34', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+27.16,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','SD'),('rarg','NE'))] = cmd.select('met35', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+27.84,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','SD'),('rarg','NH1'))] = cmd.select('met36', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+27.11,resSelectionSubs('arg','NH1',subs)))
IDSpec['met'] = cmd.select('met',' br. met1&br. met2&br. met3&br. met4&br. met5&br. met6&br. met7&br. met8&br. met9&br. met10&br. met11&br. met12&br. met13&br. met14&br. met15&br. met16&br. met17&br. met18&br. met19&br. met20&br. met21&br. met22&br. met23&br. met24&br. met25&br. met26&br. met27&br. met28&br. met29&br. met30&br. met31&br. met32&br. met33&br. met34&br. met35&br. met36')
IDSpec['r_met'] = cmd.count_atoms(resSelectionSubs('met', subs=subs, selection=True))
cmd.delete('met1')
cmd.delete('met2')
cmd.delete('met3')
cmd.delete('met4')
cmd.delete('met5')
cmd.delete('met6')
cmd.delete('met7')
cmd.delete('met8')
cmd.delete('met9')
cmd.delete('met10')
cmd.delete('met11')
cmd.delete('met12')
cmd.delete('met13')
cmd.delete('met14')
cmd.delete('met15')
cmd.delete('met16')
cmd.delete('met17')
cmd.delete('met18')
cmd.delete('met19')
cmd.delete('met20')
cmd.delete('met21')
cmd.delete('met22')
cmd.delete('met23')
cmd.delete('met24')
cmd.delete('met25')
cmd.delete('met26')
cmd.delete('met27')
cmd.delete('met28')
cmd.delete('met29')
cmd.delete('met30')
cmd.delete('met31')
cmd.delete('met32')
cmd.delete('met33')
cmd.delete('met34')
cmd.delete('met35')
cmd.delete('met36')
IDSpec[(('thr','CA'),('smet','CE'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+24.95,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('thr','CA'),('smet','CG'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+26.28,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('smet','SD'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+26.14,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('thr','CB'),('smet','CE'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+23.51,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('thr','CB'),('smet','CG'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+24.86,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('smet','SD'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+24.68,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('thr','OG1'),('smet','CE'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+22.61,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('thr','OG1'),('smet','CG'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+23.87,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('smet','SD'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+23.78,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('thr','CA'),('rglu','CD'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('thr','CA'),('rglu','OE1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.82,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('thr','CA'),('rglu','OE2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.21,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('thr','CB'),('rglu','CD'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.87,resSelectionSubs('glu','CD',subs)))
IDSpec[(('thr','CB'),('rglu','OE1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.85,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('thr','CB'),('rglu','OE2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+13.01,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('thr','OG1'),('rglu','CD'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.98,resSelectionSubs('glu','CD',subs)))
IDSpec[(('thr','OG1'),('rglu','OE1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.98,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('thr','OG1'),('rglu','OE2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.03,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('thr','CA'),('rasn','CG'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.69,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CA'),('rasn','ND2'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.87,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CA'),('rasn','OD1'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.98,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','CB'),('rasn','CG'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CB'),('rasn','ND2'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.80,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CB'),('rasn','OD1'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.72,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','OG1'),('rasn','CG'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.38,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','OG1'),('rasn','ND2'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.71,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','OG1'),('rasn','OD1'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.58,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','CA'),('rarg','CZ'))] = cmd.select('thr28', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.45,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CA'),('rarg','NE'))] = cmd.select('thr29', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.94,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CA'),('rarg','NH1'))] = cmd.select('thr30', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.31,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','CB'),('rarg','CZ'))] = cmd.select('thr31', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.30,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CB'),('rarg','NE'))] = cmd.select('thr32', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.88,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CB'),('rarg','NH1'))] = cmd.select('thr33', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.36,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','OG1'),('rarg','CZ'))] = cmd.select('thr34', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.18,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','OG1'),('rarg','NE'))] = cmd.select('thr35', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.95,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','OG1'),('rarg','NH1'))] = cmd.select('thr36', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.20,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('glu','CD'),('smet','CE'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+31.93,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('smet','CG'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+32.55,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('smet','SD'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+32.80,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','CE'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+31.27,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','CG'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+31.98,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','SD'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+32.20,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','CE'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+31.43,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','CG'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+31.96,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','SD'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.24,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','CD'),('sthr','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.92,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sthr','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.87,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sthr','OG1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.98,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sthr','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.82,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sthr','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.85,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sthr','OG1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.98,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sthr','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.21,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sthr','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.01,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sthr','OG1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.03,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('glu','CD'),('rasn','CG'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.46,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','CD'),('rasn','ND2'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.31,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','CD'),('rasn','OD1'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.49,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE1'),('rasn','CG'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.87,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE1'),('rasn','ND2'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.74,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE1'),('rasn','OD1'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.86,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE2'),('rasn','CG'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.95,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE2'),('rasn','ND2'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.79,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE2'),('rasn','OD1'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.01,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.32,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.03,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.59,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.72,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.42,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.87,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.07,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.61,resSelectionSubs('arg','NH1',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
IDSpec[(('asn','CG'),('smet','CE'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+18.49,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('smet','CG'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+19.12,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('smet','SD'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+19.35,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('asn','ND2'),('smet','CE'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+19.66,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('smet','CG'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+20.32,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('smet','SD'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+20.50,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('asn','OD1'),('smet','CE'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+17.45,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('smet','CG'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+18.20,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('smet','SD'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+18.34,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.69,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.57,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','OG1'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.38,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.87,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.80,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','OG1'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.71,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.98,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.72,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','OG1'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.58,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','CD'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+15.46,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE1'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+14.87,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE2'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+14.95,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','CD'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+14.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE1'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.74,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE2'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.79,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','CD'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+16.49,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE1'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+15.86,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE2'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+16.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','CG'),('rarg','CZ'))] = cmd.select('asn28', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.74,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asn','CG'),('rarg','NE'))] = cmd.select('asn29', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.87,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asn','CG'),('rarg','NH1'))] = cmd.select('asn30', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.25,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asn','ND2'),('rarg','CZ'))] = cmd.select('asn31', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.52,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asn','ND2'),('rarg','NE'))] = cmd.select('asn32', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.70,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asn','ND2'),('rarg','NH1'))] = cmd.select('asn33', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.04,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asn','OD1'),('rarg','CZ'))] = cmd.select('asn34', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.09,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asn','OD1'),('rarg','NE'))] = cmd.select('asn35', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+13.14,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asn','OD1'),('rarg','NH1'))] = cmd.select('asn36', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.67,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('smet','CE'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+26.26,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','CG'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+27.39,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','SD'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+27.16,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CE'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+26.92,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CG'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+28.15,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','SD'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+27.84,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CE'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.15,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CG'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+27.29,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','SD'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+27.11,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.45,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.30,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sthr','OG1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.18,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.94,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.88,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sthr','OG1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.95,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.31,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.36,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sthr','OG1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.20,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.32,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.72,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.26,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.03,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.42,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.07,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.59,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.87,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.61,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasn','CG'))] = cmd.select('arg28', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.74,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasn','ND2'))] = cmd.select('arg29', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.52,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasn','OD1'))] = cmd.select('arg30', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.09,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasn','CG'))] = cmd.select('arg31', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.87,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasn','ND2'))] = cmd.select('arg32', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.70,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasn','OD1'))] = cmd.select('arg33', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.14,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasn','CG'))] = cmd.select('arg34', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.25,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasn','ND2'))] = cmd.select('arg35', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.04,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasn','OD1'))] = cmd.select('arg36', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.67,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_2pda_1_2_7_1'] = cmd.select('S_2pda_1_2_7_1', 'met|thr|glu|asn|arg')
cmd.delete('met')
cmd.delete('thr')
cmd.delete('glu')
cmd.delete('asn')
cmd.delete('arg')
