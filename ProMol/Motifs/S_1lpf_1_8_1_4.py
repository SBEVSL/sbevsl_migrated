'''
FUNC:S_1lpf_1_8_1_4
PDB:1lpf
EC:1.8.1.4
RESI:cys,cys,ala,his,glu
LOCI:a-48,53,219,450,455;
'''
IDSpec[(('glu','CD'),('rhis','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.61,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','CD'),('rhis','ND1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.53,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','CD'),('rhis','NE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.03,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis','ND1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.18,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis','NE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.00,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.34,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis','ND1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.11,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis','NE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.26,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','CD'),('rcys','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+36.38,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','CD'),('rcys','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+35.77,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','CD'),('rcys','SG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+33.98,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE1'),('rcys','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+36.21,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE1'),('rcys','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+35.65,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE1'),('rcys','SG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+33.86,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE2'),('rcys','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+37.38,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE2'),('rcys','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+36.74,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE2'),('rcys','SG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+34.95,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','CD'),('rcys_i','CA'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+32.80,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('glu','CD'),('rcys_i','CB'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+32.52,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('glu','CD'),('rcys_i','SG'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+33.30,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('glu','OE1'),('rcys_i','CA'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+32.55,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('glu','OE1'),('rcys_i','CB'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+32.32,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('glu','OE1'),('rcys_i','SG'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+33.15,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('glu','OE2'),('rcys_i','CA'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+33.86,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('glu','OE2'),('rcys_i','CB'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+33.55,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('glu','OE2'),('rcys_i','SG'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+34.31,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('glu','CD'),('rala','CA'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+27.81,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','CD'),('rala','CB'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+27.36,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','CD'),('rala','CG'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+27.36,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE1'),('rala','CA'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+27.85,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE1'),('rala','CB'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+27.33,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE1'),('rala','CG'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+27.33,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE2'),('rala','CA'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+28.83,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE2'),('rala','CB'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+28.41,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE2'),('rala','CG'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+28.41,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('his','CE1'),('sglu','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.61,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.03,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.34,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.53,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.18,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.11,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.60,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.00,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.26,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','CE1'),('rcys','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+39.80,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','CE1'),('rcys','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+39.29,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','CE1'),('rcys','SG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+37.50,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','ND1'),('rcys','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+39.16,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','ND1'),('rcys','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+38.61,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','ND1'),('rcys','SG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+36.81,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','NE2'),('rcys','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+40.33,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','NE2'),('rcys','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+39.84,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','NE2'),('rcys','SG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+38.04,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','CE1'),('rcys_i','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+36.02,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('his','CE1'),('rcys_i','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+35.86,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('his','CE1'),('rcys_i','SG'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+36.78,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('his','ND1'),('rcys_i','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+35.47,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('his','ND1'),('rcys_i','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+35.25,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('his','ND1'),('rcys_i','SG'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+36.14,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('his','NE2'),('rcys_i','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+36.55,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('his','NE2'),('rcys_i','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+36.40,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('his','NE2'),('rcys_i','SG'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+37.36,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('his','CE1'),('rala','CA'))] = cmd.select('his28', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+31.34,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','CE1'),('rala','CB'))] = cmd.select('his29', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+30.76,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','CE1'),('rala','CG'))] = cmd.select('his30', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+30.76,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','ND1'),('rala','CA'))] = cmd.select('his31', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+30.86,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','ND1'),('rala','CB'))] = cmd.select('his32', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+30.33,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','ND1'),('rala','CG'))] = cmd.select('his33', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+30.33,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','NE2'),('rala','CA'))] = cmd.select('his34', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+32.46,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','NE2'),('rala','CB'))] = cmd.select('his35', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+31.85,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','NE2'),('rala','CG'))] = cmd.select('his36', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+31.85,resSelectionSubs('ala','CG',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
cmd.delete('his28')
cmd.delete('his29')
cmd.delete('his30')
cmd.delete('his31')
cmd.delete('his32')
cmd.delete('his33')
cmd.delete('his34')
cmd.delete('his35')
cmd.delete('his36')
IDSpec[(('cys','CA'),('sglu','CD'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.38,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.21,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+37.38,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','CD'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+35.77,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+35.65,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+36.74,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','CD'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+33.98,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+33.86,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+34.95,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','CE1'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+39.80,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','ND1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+39.16,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','NE2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+40.33,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','CE1'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+39.29,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','ND1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+38.61,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','NE2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+39.84,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','CE1'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+37.50,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','ND1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+36.81,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','NE2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+38.04,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CA'),('rcys_i','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.48,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CA'),('rcys_i','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.02,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CA'),('rcys_i','SG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.30,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CB'),('rcys_i','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.95,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CB'),('rcys_i','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.05,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CB'),('rcys_i','SG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.04,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','SG'),('rcys_i','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.05,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','SG'),('rcys_i','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.76,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','SG'),('rcys_i','SG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+3.99,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CA'),('rala','CA'))] = cmd.select('cys28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+23.91,resSelectionSubs('ala','CA',subs)))
IDSpec[(('cys','CA'),('rala','CB'))] = cmd.select('cys29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+23.63,resSelectionSubs('ala','CB',subs)))
IDSpec[(('cys','CA'),('rala','CG'))] = cmd.select('cys30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+23.63,resSelectionSubs('ala','CG',subs)))
IDSpec[(('cys','CB'),('rala','CA'))] = cmd.select('cys31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+23.65,resSelectionSubs('ala','CA',subs)))
IDSpec[(('cys','CB'),('rala','CB'))] = cmd.select('cys32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+23.44,resSelectionSubs('ala','CB',subs)))
IDSpec[(('cys','CB'),('rala','CG'))] = cmd.select('cys33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+23.44,resSelectionSubs('ala','CG',subs)))
IDSpec[(('cys','SG'),('rala','CA'))] = cmd.select('cys34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+22.70,resSelectionSubs('ala','CA',subs)))
IDSpec[(('cys','SG'),('rala','CB'))] = cmd.select('cys35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+22.46,resSelectionSubs('ala','CB',subs)))
IDSpec[(('cys','SG'),('rala','CG'))] = cmd.select('cys36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+22.46,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('cys_i','CA'),('sglu','CD'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+32.80,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sglu','OE1'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+32.55,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sglu','OE2'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+33.86,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sglu','CD'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+32.52,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sglu','OE1'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+32.32,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sglu','OE2'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+33.55,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sglu','CD'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+33.30,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sglu','OE1'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+33.15,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sglu','OE2'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+34.31,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_i','CA'),('shis','CE1'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.02,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('shis','ND1'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+35.47,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('shis','NE2'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+36.55,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys_i','CB'),('shis','CE1'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+35.86,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('shis','ND1'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+35.25,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('shis','NE2'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+36.40,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys_i','SG'),('shis','CE1'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+36.78,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('shis','ND1'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+36.14,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('shis','NE2'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+37.36,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.48,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.95,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.05,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.02,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.05,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+4.76,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.30,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.04,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+3.99,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rala','CA'))] = cmd.select('cys_i28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+21.53,resSelectionSubs('ala','CA',subs)))
IDSpec[(('cys_i','CA'),('rala','CB'))] = cmd.select('cys_i29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+21.02,resSelectionSubs('ala','CB',subs)))
IDSpec[(('cys_i','CA'),('rala','CG'))] = cmd.select('cys_i30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+21.02,resSelectionSubs('ala','CG',subs)))
IDSpec[(('cys_i','CB'),('rala','CA'))] = cmd.select('cys_i31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.62,resSelectionSubs('ala','CA',subs)))
IDSpec[(('cys_i','CB'),('rala','CB'))] = cmd.select('cys_i32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.19,resSelectionSubs('ala','CB',subs)))
IDSpec[(('cys_i','CB'),('rala','CG'))] = cmd.select('cys_i33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.19,resSelectionSubs('ala','CG',subs)))
IDSpec[(('cys_i','SG'),('rala','CA'))] = cmd.select('cys_i34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.09,resSelectionSubs('ala','CA',subs)))
IDSpec[(('cys_i','SG'),('rala','CB'))] = cmd.select('cys_i35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+20.78,resSelectionSubs('ala','CB',subs)))
IDSpec[(('cys_i','SG'),('rala','CG'))] = cmd.select('cys_i36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+20.78,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('ala','CA'),('sglu','CD'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+27.81,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+27.85,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+28.83,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','CD'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+27.36,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+27.33,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+28.41,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','CD'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+28.41,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+28.41,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+28.41,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','CE1'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+31.34,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','ND1'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+30.86,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','NE2'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+32.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','CE1'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+30.76,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','ND1'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+30.33,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','NE2'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+31.85,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','CE1'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+31.85,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','ND1'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+31.85,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','NE2'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+31.85,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CA'),('scys','CA'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+23.91,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('scys','CB'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+23.65,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ala','CA'),('scys','SG'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+22.70,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ala','CB'),('scys','CA'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+23.63,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('scys','CB'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+23.44,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ala','CB'),('scys','SG'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+22.46,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ala','CG'),('scys','CA'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+22.46,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('scys','CB'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+22.46,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ala','CG'),('scys','SG'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+22.46,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ala','CA'),('scys_i','CA'))] = cmd.select('ala28', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+21.53,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('scys_i','CB'))] = cmd.select('ala29', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+21.62,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('ala','CA'),('scys_i','SG'))] = cmd.select('ala30', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+21.09,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('ala','CB'),('scys_i','CA'))] = cmd.select('ala31', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+21.02,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('scys_i','CB'))] = cmd.select('ala32', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+21.19,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('ala','CB'),('scys_i','SG'))] = cmd.select('ala33', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+20.78,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('ala','CG'),('scys_i','CA'))] = cmd.select('ala34', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+20.78,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('scys_i','CB'))] = cmd.select('ala35', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+20.78,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('ala','CG'),('scys_i','SG'))] = cmd.select('ala36', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+20.78,resSelectionSubs('cys_i','SG',subs,selection=True)))
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
IDSpec['S_1lpf_1_8_1_4'] = cmd.select('S_1lpf_1_8_1_4', 'glu|his|cys|cys_i|ala')
cmd.delete('glu')
cmd.delete('his')
cmd.delete('cys')
cmd.delete('cys_i')
cmd.delete('ala')
