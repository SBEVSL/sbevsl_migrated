'''
FUNC:S_1f3z_2_7_1_69
PDB:1f3z
EC:2.7.1.69
RESI:thr,his,his,gly
LOCI:a-73,75,90,92;
'''
IDSpec[(('his','CE1'),('rhis','CE1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.02,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','CE1'),('rhis','ND1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.66,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','CE1'),('rhis','NE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.69,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','ND1'),('rhis','CE1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.80,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','ND1'),('rhis','ND1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.28,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','ND1'),('rhis','NE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.48,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','NE2'),('rhis','CE1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.34,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','NE2'),('rhis','ND1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.19,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','NE2'),('rhis','NE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.07,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','CE1'),('rgly','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.06,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','CE1'),('rgly','N'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.92,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','CE1'),('rgly','O'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+4.96,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','ND1'),('rgly','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.79,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','ND1'),('rgly','N'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.36,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','ND1'),('rgly','O'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.80,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','NE2'),('rgly','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.32,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','NE2'),('rgly','N'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.10,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','NE2'),('rgly','O'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.28,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','CE1'),('rthr','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.00,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his','CE1'),('rthr','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.82,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his','CE1'),('rthr','OG1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.66,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('his','ND1'),('rthr','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.61,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his','ND1'),('rthr','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.55,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his','ND1'),('rthr','OG1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.48,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('his','NE2'),('rthr','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.39,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his','NE2'),('rthr','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.23,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his','NE2'),('rthr','OG1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.91,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.02,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.80,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.34,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.66,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.28,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.19,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.69,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.48,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.07,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('rgly','CA'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.19,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his_i','CE1'),('rgly','N'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.91,resSelectionSubs('gly','N',subs)))
IDSpec[(('his_i','CE1'),('rgly','O'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.14,resSelectionSubs('gly','O',subs)))
IDSpec[(('his_i','ND1'),('rgly','CA'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.07,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his_i','ND1'),('rgly','N'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.71,resSelectionSubs('gly','N',subs)))
IDSpec[(('his_i','ND1'),('rgly','O'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.40,resSelectionSubs('gly','O',subs)))
IDSpec[(('his_i','NE2'),('rgly','CA'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.16,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his_i','NE2'),('rgly','N'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.88,resSelectionSubs('gly','N',subs)))
IDSpec[(('his_i','NE2'),('rgly','O'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.92,resSelectionSubs('gly','O',subs)))
IDSpec[(('his_i','CE1'),('rthr','CA'))] = cmd.select('his_i19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.09,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his_i','CE1'),('rthr','CB'))] = cmd.select('his_i20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.89,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his_i','CE1'),('rthr','OG1'))] = cmd.select('his_i21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.68,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('his_i','ND1'),('rthr','CA'))] = cmd.select('his_i22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.37,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his_i','ND1'),('rthr','CB'))] = cmd.select('his_i23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.32,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his_i','ND1'),('rthr','OG1'))] = cmd.select('his_i24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.60,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('his_i','NE2'),('rthr','CA'))] = cmd.select('his_i25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.35,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his_i','NE2'),('rthr','CB'))] = cmd.select('his_i26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.18,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his_i','NE2'),('rthr','OG1'))] = cmd.select('his_i27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.01,resSelectionSubs('thr','OG1',subs)))
IDSpec['his_i'] = cmd.select('his_i',' br. his_i1&br. his_i2&br. his_i3&br. his_i4&br. his_i5&br. his_i6&br. his_i7&br. his_i8&br. his_i9&br. his_i10&br. his_i11&br. his_i12&br. his_i13&br. his_i14&br. his_i15&br. his_i16&br. his_i17&br. his_i18&br. his_i19&br. his_i20&br. his_i21&br. his_i22&br. his_i23&br. his_i24&br. his_i25&br. his_i26&br. his_i27')
IDSpec['r_his_i'] = cmd.count_atoms(resSelectionSubs('his_i', subs=subs, selection=True))
cmd.delete('his_i1')
cmd.delete('his_i2')
cmd.delete('his_i3')
cmd.delete('his_i4')
cmd.delete('his_i5')
cmd.delete('his_i6')
cmd.delete('his_i7')
cmd.delete('his_i8')
cmd.delete('his_i9')
cmd.delete('his_i10')
cmd.delete('his_i11')
cmd.delete('his_i12')
cmd.delete('his_i13')
cmd.delete('his_i14')
cmd.delete('his_i15')
cmd.delete('his_i16')
cmd.delete('his_i17')
cmd.delete('his_i18')
cmd.delete('his_i19')
cmd.delete('his_i20')
cmd.delete('his_i21')
cmd.delete('his_i22')
cmd.delete('his_i23')
cmd.delete('his_i24')
cmd.delete('his_i25')
cmd.delete('his_i26')
cmd.delete('his_i27')
IDSpec[(('gly','CA'),('shis','CE1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.06,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis','ND1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.79,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis','NE2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.32,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','N'),('shis','CE1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.92,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','N'),('shis','ND1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.36,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','N'),('shis','NE2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.10,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','O'),('shis','CE1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.96,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','O'),('shis','ND1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.80,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','O'),('shis','NE2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.28,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','CA'),('shis_i','CE1'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.19,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis_i','ND1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.07,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis_i','NE2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.16,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('gly','N'),('shis_i','CE1'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.91,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('gly','N'),('shis_i','ND1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.71,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('gly','N'),('shis_i','NE2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.88,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('gly','O'),('shis_i','CE1'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.14,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('gly','O'),('shis_i','ND1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.40,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('gly','O'),('shis_i','NE2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.92,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('gly','CA'),('rthr','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.07,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','CA'),('rthr','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.01,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','CA'),('rthr','OG1'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.45,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','N'),('rthr','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.70,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','N'),('rthr','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.76,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','N'),('rthr','OG1'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.23,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gly','O'),('rthr','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.69,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gly','O'),('rthr','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.52,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gly','O'),('rthr','OG1'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.68,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('thr','CA'),('shis','CE1'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.00,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('thr','CA'),('shis','ND1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.61,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('thr','CA'),('shis','NE2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.39,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('thr','CB'),('shis','CE1'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.82,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('thr','CB'),('shis','ND1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.55,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('thr','CB'),('shis','NE2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.23,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis','CE1'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.66,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis','ND1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.48,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis','NE2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.91,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('thr','CA'),('shis_i','CE1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.09,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('thr','CA'),('shis_i','ND1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.37,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('thr','CA'),('shis_i','NE2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.35,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('thr','CB'),('shis_i','CE1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.89,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('thr','CB'),('shis_i','ND1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.32,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('thr','CB'),('shis_i','NE2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.18,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis_i','CE1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.68,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis_i','ND1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.60,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis_i','NE2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.01,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','CA'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+14.07,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','N'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.70,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CA'),('sgly','O'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.69,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','CA'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+13.01,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','N'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.76,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','CB'),('sgly','O'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.52,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','CA'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.45,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','N'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.23,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgly','O'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.68,resSelectionSubs('gly','O',subs,selection=True)))
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
IDSpec['S_1f3z_2_7_1_69'] = cmd.select('S_1f3z_2_7_1_69', 'his|his_i|gly|thr')
cmd.delete('his')
cmd.delete('his_i')
cmd.delete('gly')
cmd.delete('thr')