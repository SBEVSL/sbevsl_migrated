'''
FUNC:S_1zx9_1_16_1_1
PDB:1zx9
EC:1.16.1.1
RESI:cys,cys,ile,tyr,glu
LOCI:a-42,47,218,441,446;
'''
IDSpec[(('tyr','CE1'),('rglu','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.45,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.03,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.90,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','CZ'),('rglu','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.88,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.42,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.37,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','OH'),('rglu','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.85,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','OH'),('rglu','OE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.41,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','OH'),('rglu','OE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.29,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','CE1'),('rcys','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+40.56,resSelectionSubs('cys','CA',subs)))
IDSpec[(('tyr','CE1'),('rcys','CB'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+39.96,resSelectionSubs('cys','CB',subs)))
IDSpec[(('tyr','CE1'),('rcys','SG'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+38.18,resSelectionSubs('cys','SG',subs)))
IDSpec[(('tyr','CZ'),('rcys','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+40.59,resSelectionSubs('cys','CA',subs)))
IDSpec[(('tyr','CZ'),('rcys','CB'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+39.99,resSelectionSubs('cys','CB',subs)))
IDSpec[(('tyr','CZ'),('rcys','SG'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+38.23,resSelectionSubs('cys','SG',subs)))
IDSpec[(('tyr','OH'),('rcys','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+41.30,resSelectionSubs('cys','CA',subs)))
IDSpec[(('tyr','OH'),('rcys','CB'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+40.74,resSelectionSubs('cys','CB',subs)))
IDSpec[(('tyr','OH'),('rcys','SG'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+38.99,resSelectionSubs('cys','SG',subs)))
IDSpec[(('tyr','CE1'),('rcys_i','CA'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+36.69,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('tyr','CE1'),('rcys_i','CB'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+36.37,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('tyr','CE1'),('rcys_i','SG'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+37.19,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('tyr','CZ'),('rcys_i','CA'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+36.70,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('tyr','CZ'),('rcys_i','CB'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+36.39,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('tyr','CZ'),('rcys_i','SG'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+37.17,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('tyr','OH'),('rcys_i','CA'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+37.34,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('tyr','OH'),('rcys_i','CB'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+37.08,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('tyr','OH'),('rcys_i','SG'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+37.88,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('tyr','CE1'),('rile','CD1'))] = cmd.select('tyr28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+29.28,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('tyr','CE1'),('rile','CG1'))] = cmd.select('tyr29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+28.59,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('tyr','CE1'),('rile','CG2'))] = cmd.select('tyr30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+29.42,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('tyr','CZ'),('rile','CD1'))] = cmd.select('tyr31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+28.51,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('tyr','CZ'),('rile','CG1'))] = cmd.select('tyr32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+27.78,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('tyr','CZ'),('rile','CG2'))] = cmd.select('tyr33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+28.68,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('tyr','OH'),('rile','CD1'))] = cmd.select('tyr34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+28.76,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('tyr','OH'),('rile','CG1'))] = cmd.select('tyr35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+27.96,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('tyr','OH'),('rile','CG2'))] = cmd.select('tyr36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+28.84,resSelectionSubs('ile','CG2',subs)))
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
IDSpec[(('glu','CD'),('styr','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.45,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','CZ'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.88,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','OH'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.85,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.03,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CZ'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.42,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','OH'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.41,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.90,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CZ'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.37,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','OH'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.29,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','CD'),('rcys','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+36.59,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','CD'),('rcys','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+35.86,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','CD'),('rcys','SG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+34.12,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE1'),('rcys','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+37.79,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE1'),('rcys','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+37.05,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE1'),('rcys','SG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+35.30,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE2'),('rcys','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+36.20,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE2'),('rcys','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+35.52,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE2'),('rcys','SG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+33.77,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','CD'),('rcys_i','CA'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+32.97,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('glu','CD'),('rcys_i','CB'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+32.51,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('glu','CD'),('rcys_i','SG'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+33.07,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('glu','OE1'),('rcys_i','CA'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+34.20,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('glu','OE1'),('rcys_i','CB'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+33.73,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('glu','OE1'),('rcys_i','SG'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+34.27,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('glu','OE2'),('rcys_i','CA'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.49,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('glu','OE2'),('rcys_i','CB'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.08,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('glu','OE2'),('rcys_i','SG'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.70,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('glu','CD'),('rile','CD1'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+24.13,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('glu','CD'),('rile','CG1'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+23.62,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('glu','CD'),('rile','CG2'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+24.77,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('glu','OE1'),('rile','CD1'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+25.15,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('glu','OE1'),('rile','CG1'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+24.63,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('glu','OE1'),('rile','CG2'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+25.83,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('glu','OE2'),('rile','CD1'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+23.98,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('glu','OE2'),('rile','CG1'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+23.43,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('glu','OE2'),('rile','CG2'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.46,resSelectionSubs('ile','CG2',subs)))
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
IDSpec[(('cys','CA'),('styr','CE1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+40.56,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('styr','CZ'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+40.59,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('cys','CA'),('styr','OH'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+41.30,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('cys','CB'),('styr','CE1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+39.96,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('styr','CZ'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+39.99,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('cys','CB'),('styr','OH'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+40.74,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('cys','SG'),('styr','CE1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+38.18,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('styr','CZ'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+38.23,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('cys','SG'),('styr','OH'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+38.99,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','CD'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.59,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+37.79,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.20,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','CD'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+35.86,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+37.05,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+35.52,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','CD'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+34.12,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+35.30,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+33.77,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','CA'),('rcys_i','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.57,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CA'),('rcys_i','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.28,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CA'),('rcys_i','SG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.62,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CB'),('rcys_i','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.95,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CB'),('rcys_i','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.19,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CB'),('rcys_i','SG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.11,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','SG'),('rcys_i','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.18,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','SG'),('rcys_i','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.98,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','SG'),('rcys_i','SG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.04,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CA'),('rile','CD1'))] = cmd.select('cys28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+24.56,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys','CA'),('rile','CG1'))] = cmd.select('cys29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+25.55,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys','CA'),('rile','CG2'))] = cmd.select('cys30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+24.11,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('cys','CB'),('rile','CD1'))] = cmd.select('cys31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+24.20,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys','CB'),('rile','CG1'))] = cmd.select('cys32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+25.24,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys','CB'),('rile','CG2'))] = cmd.select('cys33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+23.94,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('cys','SG'),('rile','CD1'))] = cmd.select('cys34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+23.26,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys','SG'),('rile','CG1'))] = cmd.select('cys35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+24.27,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys','SG'),('rile','CG2'))] = cmd.select('cys36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+23.03,resSelectionSubs('ile','CG2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27&br. cys28&br. cys29&br. cys30&br. cys31&br. cys32&br. cys33&br. cys34&br. cys35&br. cys36')
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
cmd.delete('cys28')
cmd.delete('cys29')
cmd.delete('cys30')
cmd.delete('cys31')
cmd.delete('cys32')
cmd.delete('cys33')
cmd.delete('cys34')
cmd.delete('cys35')
cmd.delete('cys36')
IDSpec[(('cys_i','CA'),('styr','CE1'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.69,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('styr','CZ'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.70,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('cys_i','CA'),('styr','OH'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+37.34,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('cys_i','CB'),('styr','CE1'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+36.37,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('styr','CZ'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+36.39,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('cys_i','CB'),('styr','OH'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+37.08,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('cys_i','SG'),('styr','CE1'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+37.19,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('styr','CZ'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+37.17,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('cys_i','SG'),('styr','OH'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+37.88,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sglu','CD'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+32.97,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sglu','OE1'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+34.20,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sglu','OE2'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+32.49,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sglu','CD'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+32.51,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sglu','OE1'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+33.73,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sglu','OE2'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+32.08,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sglu','CD'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+33.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sglu','OE1'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+34.27,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sglu','OE2'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+32.70,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.57,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.95,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.18,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.28,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.19,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+4.98,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.62,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.11,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.04,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rile','CD1'))] = cmd.select('cys_i28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+21.66,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys_i','CA'),('rile','CG1'))] = cmd.select('cys_i29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+22.45,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys_i','CA'),('rile','CG2'))] = cmd.select('cys_i30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+20.88,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('cys_i','CB'),('rile','CD1'))] = cmd.select('cys_i31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.62,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys_i','CB'),('rile','CG1'))] = cmd.select('cys_i32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+22.49,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys_i','CB'),('rile','CG2'))] = cmd.select('cys_i33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.07,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('cys_i','SG'),('rile','CD1'))] = cmd.select('cys_i34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.43,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('cys_i','SG'),('rile','CG1'))] = cmd.select('cys_i35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+22.40,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('cys_i','SG'),('rile','CG2'))] = cmd.select('cys_i36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.09,resSelectionSubs('ile','CG2',subs)))
IDSpec['cys_i'] = cmd.select('cys_i',' br. cys_i1&br. cys_i2&br. cys_i3&br. cys_i4&br. cys_i5&br. cys_i6&br. cys_i7&br. cys_i8&br. cys_i9&br. cys_i10&br. cys_i11&br. cys_i12&br. cys_i13&br. cys_i14&br. cys_i15&br. cys_i16&br. cys_i17&br. cys_i18&br. cys_i19&br. cys_i20&br. cys_i21&br. cys_i22&br. cys_i23&br. cys_i24&br. cys_i25&br. cys_i26&br. cys_i27&br. cys_i28&br. cys_i29&br. cys_i30&br. cys_i31&br. cys_i32&br. cys_i33&br. cys_i34&br. cys_i35&br. cys_i36')
IDSpec['r_cys_i'] = cmd.count_atoms(resSelectionSubs('cys_i', subs=subs, selection=True))
cmd.delete('cys_i1')
cmd.delete('cys_i2')
cmd.delete('cys_i3')
cmd.delete('cys_i4')
cmd.delete('cys_i5')
cmd.delete('cys_i6')
cmd.delete('cys_i7')
cmd.delete('cys_i8')
cmd.delete('cys_i9')
cmd.delete('cys_i10')
cmd.delete('cys_i11')
cmd.delete('cys_i12')
cmd.delete('cys_i13')
cmd.delete('cys_i14')
cmd.delete('cys_i15')
cmd.delete('cys_i16')
cmd.delete('cys_i17')
cmd.delete('cys_i18')
cmd.delete('cys_i19')
cmd.delete('cys_i20')
cmd.delete('cys_i21')
cmd.delete('cys_i22')
cmd.delete('cys_i23')
cmd.delete('cys_i24')
cmd.delete('cys_i25')
cmd.delete('cys_i26')
cmd.delete('cys_i27')
cmd.delete('cys_i28')
cmd.delete('cys_i29')
cmd.delete('cys_i30')
cmd.delete('cys_i31')
cmd.delete('cys_i32')
cmd.delete('cys_i33')
cmd.delete('cys_i34')
cmd.delete('cys_i35')
cmd.delete('cys_i36')
IDSpec[(('ile','CD1'),('styr','CE1'))] = cmd.select('ile1', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+29.28,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ile','CD1'),('styr','CZ'))] = cmd.select('ile2', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+28.51,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ile','CD1'),('styr','OH'))] = cmd.select('ile3', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+28.76,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ile','CG1'),('styr','CE1'))] = cmd.select('ile4', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+28.59,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ile','CG1'),('styr','CZ'))] = cmd.select('ile5', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+27.78,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ile','CG1'),('styr','OH'))] = cmd.select('ile6', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+27.96,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ile','CG2'),('styr','CE1'))] = cmd.select('ile7', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+29.42,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ile','CG2'),('styr','CZ'))] = cmd.select('ile8', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+28.68,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ile','CG2'),('styr','OH'))] = cmd.select('ile9', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+28.84,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ile','CD1'),('sglu','CD'))] = cmd.select('ile10', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+24.13,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ile','CD1'),('sglu','OE1'))] = cmd.select('ile11', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+25.15,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ile','CD1'),('sglu','OE2'))] = cmd.select('ile12', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+23.98,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ile','CG1'),('sglu','CD'))] = cmd.select('ile13', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+23.62,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ile','CG1'),('sglu','OE1'))] = cmd.select('ile14', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+24.63,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ile','CG1'),('sglu','OE2'))] = cmd.select('ile15', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+23.43,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ile','CG2'),('sglu','CD'))] = cmd.select('ile16', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+24.77,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ile','CG2'),('sglu','OE1'))] = cmd.select('ile17', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+25.83,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ile','CG2'),('sglu','OE2'))] = cmd.select('ile18', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+24.46,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys','CA'))] = cmd.select('ile19', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+24.56,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys','CB'))] = cmd.select('ile20', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+24.20,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys','SG'))] = cmd.select('ile21', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+23.26,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys','CA'))] = cmd.select('ile22', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+25.55,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys','CB'))] = cmd.select('ile23', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+25.24,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys','SG'))] = cmd.select('ile24', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+24.27,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys','CA'))] = cmd.select('ile25', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+24.11,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys','CB'))] = cmd.select('ile26', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+23.94,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys','SG'))] = cmd.select('ile27', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+23.03,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys_i','CA'))] = cmd.select('ile28', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+21.66,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys_i','CB'))] = cmd.select('ile29', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+21.62,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('ile','CD1'),('scys_i','SG'))] = cmd.select('ile30', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+21.43,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys_i','CA'))] = cmd.select('ile31', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+22.45,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys_i','CB'))] = cmd.select('ile32', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+22.49,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('ile','CG1'),('scys_i','SG'))] = cmd.select('ile33', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+22.40,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys_i','CA'))] = cmd.select('ile34', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+20.88,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys_i','CB'))] = cmd.select('ile35', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+21.07,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('ile','CG2'),('scys_i','SG'))] = cmd.select('ile36', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+21.09,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec['ile'] = cmd.select('ile',' br. ile1&br. ile2&br. ile3&br. ile4&br. ile5&br. ile6&br. ile7&br. ile8&br. ile9&br. ile10&br. ile11&br. ile12&br. ile13&br. ile14&br. ile15&br. ile16&br. ile17&br. ile18&br. ile19&br. ile20&br. ile21&br. ile22&br. ile23&br. ile24&br. ile25&br. ile26&br. ile27&br. ile28&br. ile29&br. ile30&br. ile31&br. ile32&br. ile33&br. ile34&br. ile35&br. ile36')
IDSpec['r_ile'] = cmd.count_atoms(resSelectionSubs('ile', subs=subs, selection=True))
cmd.delete('ile1')
cmd.delete('ile2')
cmd.delete('ile3')
cmd.delete('ile4')
cmd.delete('ile5')
cmd.delete('ile6')
cmd.delete('ile7')
cmd.delete('ile8')
cmd.delete('ile9')
cmd.delete('ile10')
cmd.delete('ile11')
cmd.delete('ile12')
cmd.delete('ile13')
cmd.delete('ile14')
cmd.delete('ile15')
cmd.delete('ile16')
cmd.delete('ile17')
cmd.delete('ile18')
cmd.delete('ile19')
cmd.delete('ile20')
cmd.delete('ile21')
cmd.delete('ile22')
cmd.delete('ile23')
cmd.delete('ile24')
cmd.delete('ile25')
cmd.delete('ile26')
cmd.delete('ile27')
cmd.delete('ile28')
cmd.delete('ile29')
cmd.delete('ile30')
cmd.delete('ile31')
cmd.delete('ile32')
cmd.delete('ile33')
cmd.delete('ile34')
cmd.delete('ile35')
cmd.delete('ile36')
IDSpec['S_1zx9_1_16_1_1'] = cmd.select('S_1zx9_1_16_1_1', 'tyr|glu|cys|cys_i|ile')
cmd.delete('tyr')
cmd.delete('glu')
cmd.delete('cys')
cmd.delete('cys_i')
cmd.delete('ile')
