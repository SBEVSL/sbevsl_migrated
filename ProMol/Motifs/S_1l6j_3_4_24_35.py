'''
FUNC:S_1l6j_3_4_24_35
PDB:1l6j
EC:3.4.24.35
RESI:arg,ala,glu,met
LOCI:a-221,228,402,419;
'''
IDSpec[(('met','CE'),('rglu','CD'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+9.17,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','CE'),('rglu','OE1'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+9.32,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','CE'),('rglu','OE2'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.90,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','CG'),('rglu','CD'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.58,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','CG'),('rglu','OE1'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.65,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','CG'),('rglu','OE2'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.50,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','SD'),('rglu','CD'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+9.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','SD'),('rglu','OE1'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+10.08,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','SD'),('rglu','OE2'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+9.88,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','CE'),('rarg','CZ'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+39.77,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CE'),('rarg','NE'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+39.55,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CE'),('rarg','NH1'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+38.83,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','CG'),('rarg','CZ'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+40.33,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CG'),('rarg','NE'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+40.02,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CG'),('rarg','NH1'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+39.46,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','SD'),('rarg','CZ'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+38.87,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','SD'),('rarg','NE'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+38.60,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','SD'),('rarg','NH1'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+37.98,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','CE'),('rala','CA'))] = cmd.select('met19', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+33.15,resSelectionSubs('ala','CA',subs)))
IDSpec[(('met','CE'),('rala','CB'))] = cmd.select('met20', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+33.49,resSelectionSubs('ala','CB',subs)))
IDSpec[(('met','CE'),('rala','CG'))] = cmd.select('met21', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+33.49,resSelectionSubs('ala','CG',subs)))
IDSpec[(('met','CG'),('rala','CA'))] = cmd.select('met22', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+32.94,resSelectionSubs('ala','CA',subs)))
IDSpec[(('met','CG'),('rala','CB'))] = cmd.select('met23', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+33.16,resSelectionSubs('ala','CB',subs)))
IDSpec[(('met','CG'),('rala','CG'))] = cmd.select('met24', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+33.16,resSelectionSubs('ala','CG',subs)))
IDSpec[(('met','SD'),('rala','CA'))] = cmd.select('met25', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+31.85,resSelectionSubs('ala','CA',subs)))
IDSpec[(('met','SD'),('rala','CB'))] = cmd.select('met26', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+32.14,resSelectionSubs('ala','CB',subs)))
IDSpec[(('met','SD'),('rala','CG'))] = cmd.select('met27', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+32.14,resSelectionSubs('ala','CG',subs)))
IDSpec['met'] = cmd.select('met',' br. met1&br. met2&br. met3&br. met4&br. met5&br. met6&br. met7&br. met8&br. met9&br. met10&br. met11&br. met12&br. met13&br. met14&br. met15&br. met16&br. met17&br. met18&br. met19&br. met20&br. met21&br. met22&br. met23&br. met24&br. met25&br. met26&br. met27')
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
IDSpec[(('glu','CD'),('smet','CE'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.17,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('smet','CG'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.58,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('smet','SD'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.92,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','CE'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.32,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','CG'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.65,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','SD'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.08,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','CE'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.90,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','CG'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.50,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','SD'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.88,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+35.20,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+35.17,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+34.13,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+35.41,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+35.35,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+34.34,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+36.12,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+36.10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+35.04,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','CD'),('rala','CA'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+30.33,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','CD'),('rala','CB'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+30.94,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','CD'),('rala','CG'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+30.94,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE1'),('rala','CA'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+30.35,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE1'),('rala','CB'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+30.93,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE1'),('rala','CG'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+30.93,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE2'),('rala','CA'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+31.39,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE2'),('rala','CB'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.01,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE2'),('rala','CG'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.01,resSelectionSubs('ala','CG',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27')
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
IDSpec[(('arg','CZ'),('smet','CE'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+39.77,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','CG'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+40.33,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','SD'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+38.87,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CE'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+39.55,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CG'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+40.02,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','SD'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+38.60,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CE'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+38.83,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CG'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+39.46,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','SD'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+37.98,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+35.20,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+35.41,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+36.12,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+35.17,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+35.35,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+36.10,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+34.13,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+34.34,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+35.04,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rala','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.17,resSelectionSubs('ala','CA',subs)))
IDSpec[(('arg','CZ'),('rala','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.43,resSelectionSubs('ala','CB',subs)))
IDSpec[(('arg','CZ'),('rala','CG'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.43,resSelectionSubs('ala','CG',subs)))
IDSpec[(('arg','NE'),('rala','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.05,resSelectionSubs('ala','CA',subs)))
IDSpec[(('arg','NE'),('rala','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.26,resSelectionSubs('ala','CB',subs)))
IDSpec[(('arg','NE'),('rala','CG'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.26,resSelectionSubs('ala','CG',subs)))
IDSpec[(('arg','NH1'),('rala','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.25,resSelectionSubs('ala','CA',subs)))
IDSpec[(('arg','NH1'),('rala','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.57,resSelectionSubs('ala','CB',subs)))
IDSpec[(('arg','NH1'),('rala','CG'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.57,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('ala','CA'),('smet','CE'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+33.15,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('ala','CA'),('smet','CG'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+32.94,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('ala','CA'),('smet','SD'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+31.85,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('ala','CB'),('smet','CE'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+33.49,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('ala','CB'),('smet','CG'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+33.16,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('ala','CB'),('smet','SD'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+32.14,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('ala','CG'),('smet','CE'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+32.14,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('ala','CG'),('smet','CG'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+32.14,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('ala','CG'),('smet','SD'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+32.14,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','CD'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+30.33,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE1'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+30.35,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE2'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+31.39,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','CD'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+30.94,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE1'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+30.93,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE2'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+32.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','CD'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+32.01,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE1'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+32.01,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE2'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+32.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CA'),('sarg','CZ'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+14.17,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ala','CA'),('sarg','NE'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+13.05,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ala','CA'),('sarg','NH1'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+14.25,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ala','CB'),('sarg','CZ'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+15.43,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ala','CB'),('sarg','NE'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+14.26,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ala','CB'),('sarg','NH1'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+15.57,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ala','CG'),('sarg','CZ'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+15.57,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ala','CG'),('sarg','NE'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+15.57,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ala','CG'),('sarg','NH1'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+15.57,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18&br. ala19&br. ala20&br. ala21&br. ala22&br. ala23&br. ala24&br. ala25&br. ala26&br. ala27')
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
IDSpec['S_1l6j_3_4_24_35'] = cmd.select('S_1l6j_3_4_24_35', 'met|glu|arg|ala')
cmd.delete('met')
cmd.delete('glu')
cmd.delete('arg')
cmd.delete('ala')