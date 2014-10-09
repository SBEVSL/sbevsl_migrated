'''
FUNC:S_1t38_2_1_1_63
PDB:1t38
EC:2.1.1.63
RESI:asn,ser,his,glu
LOCI:a-137,145,146,172;
'''
IDSpec[(('glu','CD'),('rser','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.55,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','CD'),('rser','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.68,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','CD'),('rser','OG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.48,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE1'),('rser','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.27,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE1'),('rser','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.52,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE1'),('rser','OG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.35,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE2'),('rser','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.00,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE2'),('rser','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.05,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE2'),('rser','OG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.76,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','CD'),('rasn','CG'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.07,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','CD'),('rasn','ND2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.88,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','CD'),('rasn','OD1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.82,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE1'),('rasn','CG'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.05,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE1'),('rasn','ND2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.77,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE1'),('rasn','OD1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.91,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE2'),('rasn','CG'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.17,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE2'),('rasn','ND2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.02,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE2'),('rasn','OD1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.86,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','CD'),('rhis','CE1'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.46,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','CD'),('rhis','ND1'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.47,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','CD'),('rhis','NE2'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.35,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis','CE1'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.79,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis','ND1'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.67,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis','NE2'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.69,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis','CE1'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.60,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis','ND1'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.76,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis','NE2'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.69,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('ser','CA'),('sglu','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.55,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.27,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.00,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.68,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.52,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.05,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.48,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.35,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.76,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CA'),('rasn','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.83,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ser','CA'),('rasn','ND2'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.69,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ser','CA'),('rasn','OD1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.21,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ser','CB'),('rasn','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.85,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ser','CB'),('rasn','ND2'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.00,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ser','CB'),('rasn','OD1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.22,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ser','OG'),('rasn','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.46,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ser','OG'),('rasn','ND2'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.59,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ser','OG'),('rasn','OD1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.92,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.77,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.78,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.62,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.53,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.55,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.36,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.38,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('asn','CG'),('sglu','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+16.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+16.05,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+15.17,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+15.88,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+15.77,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+15.02,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+15.82,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+15.91,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+14.86,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','CG'),('sser','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.83,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sser','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.85,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sser','OG'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.46,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sser','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.69,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sser','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.00,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sser','OG'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.59,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sser','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.21,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sser','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.22,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sser','OG'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.92,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asn','CG'),('rhis','CE1'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.80,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asn','CG'),('rhis','ND1'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.07,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asn','CG'),('rhis','NE2'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+13.02,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asn','ND2'),('rhis','CE1'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.78,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asn','ND2'),('rhis','ND1'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.14,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asn','ND2'),('rhis','NE2'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.99,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asn','OD1'),('rhis','CE1'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.49,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asn','OD1'),('rhis','ND1'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.83,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asn','OD1'),('rhis','NE2'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.76,resSelectionSubs('his','NE2',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27')
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
IDSpec[(('his','CE1'),('sglu','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.46,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.79,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.60,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.47,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.67,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.76,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.35,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.69,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.69,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.77,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.62,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.31,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.78,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.53,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.36,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.60,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.55,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.38,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasn','CG'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.80,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasn','ND2'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.78,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('his','CE1'),('sasn','OD1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.49,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasn','CG'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.07,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasn','ND2'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.14,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasn','OD1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.83,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasn','CG'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+13.02,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasn','ND2'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.99,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasn','OD1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.76,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27')
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
IDSpec['S_1t38_2_1_1_63'] = cmd.select('S_1t38_2_1_1_63', 'glu|ser|asn|his')
cmd.delete('glu')
cmd.delete('ser')
cmd.delete('asn')
cmd.delete('his')