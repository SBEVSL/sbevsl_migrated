'''
FUNC:S_1x10_3_4_19_3
PDB:1x10
EC:3.4.19.3
RESI:glu,arg,ser,his
LOCI:a-79,89,142,166;
'''
IDSpec[(('ser','CA'),('rglu','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.93,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CA'),('rglu','OE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.76,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CA'),('rglu','OE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.67,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CB'),('rglu','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.86,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CB'),('rglu','OE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.52,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CB'),('rglu','OE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.68,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','OG'),('rglu','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.57,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','OG'),('rglu','OE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.04,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','OG'),('rglu','OE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.49,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.91,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.09,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.72,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.45,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.66,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.21,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.65,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.77,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.89,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CA'),('rarg','CZ'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+16.29,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CA'),('rarg','NE'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+16.08,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CA'),('rarg','NH1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+16.27,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','CB'),('rarg','CZ'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.63,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CB'),('rarg','NE'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.51,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CB'),('rarg','NH1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.48,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','OG'),('rarg','CZ'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+15.23,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','OG'),('rarg','NE'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+15.23,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','OG'),('rarg','NH1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+15.08,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('glu','CD'),('sser','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.93,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.86,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','OG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.57,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.52,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','OG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.04,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.67,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.68,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','OG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.49,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','CD'),('rhis','CE1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.24,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','CD'),('rhis','ND1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.62,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','CD'),('rhis','NE2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.52,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis','CE1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.48,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis','ND1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+4.68,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis','NE2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.68,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis','CE1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.22,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis','ND1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.72,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis','NE2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.52,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+18.33,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+18.31,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+17.68,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+17.44,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+17.50,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.76,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+18.52,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+18.44,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.85,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.91,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.45,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.65,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.09,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.66,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.77,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.72,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.21,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.89,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.24,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.48,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.22,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.62,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.68,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.72,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.52,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.68,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.52,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','CE1'),('rarg','CZ'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.59,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','CE1'),('rarg','NE'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.66,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','CE1'),('rarg','NH1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.11,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','ND1'),('rarg','CZ'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+16.30,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','ND1'),('rarg','NE'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+16.45,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','ND1'),('rarg','NH1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.72,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','NE2'),('rarg','CZ'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.07,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','NE2'),('rarg','NE'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.22,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','NE2'),('rarg','NH1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+14.64,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('sser','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.29,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.63,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','OG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.23,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.08,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.51,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','OG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.23,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.27,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.48,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','OG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.08,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.33,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.44,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.52,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.44,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.68,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.76,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.85,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','CE1'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.59,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','ND1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.30,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','NE2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.07,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','CE1'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.66,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','ND1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.45,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','NE2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.22,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','CE1'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.11,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','ND1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.72,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','NE2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.64,resSelectionSubs('his','NE2',subs,selection=True)))
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
IDSpec['S_1x10_3_4_19_3'] = cmd.select('S_1x10_3_4_19_3', 'ser|glu|his|arg')
cmd.delete('ser')
cmd.delete('glu')
cmd.delete('his')
cmd.delete('arg')
