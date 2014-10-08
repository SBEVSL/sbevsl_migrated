'''
FUNC:S_6fit_3_6_1_29
PDB:6fit
EC:3.6.1.29
RESI:gln,his,his
LOCI:a-83,94,96;
'''
IDSpec[(('gln','CD'),('rhis','CE1'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+8.70,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','CD'),('rhis','ND1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.68,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','CD'),('rhis','NE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.74,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gln','NE2'),('rhis','CE1'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.91,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','NE2'),('rhis','ND1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','NE2'),('rhis','NE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.06,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gln','OE1'),('rhis','CE1'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.82,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','OE1'),('rhis','ND1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.81,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','OE1'),('rhis','NE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.80,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gln','CD'),('rhis_i','CE1'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.76,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('gln','CD'),('rhis_i','ND1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.97,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('gln','CD'),('rhis_i','NE2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.15,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('gln','NE2'),('rhis_i','CE1'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('gln','NE2'),('rhis_i','ND1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+15.23,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('gln','NE2'),('rhis_i','NE2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+15.58,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('gln','OE1'),('rhis_i','CE1'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.93,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('gln','OE1'),('rhis_i','ND1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.15,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('gln','OE1'),('rhis_i','NE2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.31,resSelectionSubs('his_i','NE2',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18')
IDSpec['r_gln'] = cmd.count_atoms(resSelectionSubs('gln', subs=subs, selection=True))
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
IDSpec[(('his','CE1'),('sgln','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.70,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','NE2'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.91,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','OE1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.82,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.68,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','NE2'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.03,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','OE1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.81,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.74,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','NE2'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.06,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','OE1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.80,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('rhis_i','CE1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.30,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','CE1'),('rhis_i','ND1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.44,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','CE1'),('rhis_i','NE2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.89,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('his','ND1'),('rhis_i','CE1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.20,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','ND1'),('rhis_i','ND1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.47,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','ND1'),('rhis_i','NE2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.69,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('his','NE2'),('rhis_i','CE1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.34,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','NE2'),('rhis_i','ND1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.58,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','NE2'),('rhis_i','NE2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.85,resSelectionSubs('his_i','NE2',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
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
IDSpec[(('his_i','CE1'),('sgln','CD'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.76,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sgln','NE2'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.10,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sgln','OE1'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+17.93,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sgln','CD'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.97,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sgln','NE2'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.23,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sgln','OE1'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+17.15,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sgln','CD'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.15,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sgln','NE2'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.58,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sgln','OE1'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+17.31,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.30,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.20,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.34,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.44,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.47,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.58,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.89,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.69,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.85,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['his_i'] = cmd.select('his_i',' br. his_i1&br. his_i2&br. his_i3&br. his_i4&br. his_i5&br. his_i6&br. his_i7&br. his_i8&br. his_i9&br. his_i10&br. his_i11&br. his_i12&br. his_i13&br. his_i14&br. his_i15&br. his_i16&br. his_i17&br. his_i18')
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
IDSpec['S_6fit_3_6_1_29'] = cmd.select('S_6fit_3_6_1_29', 'gln|his|his_i')
cmd.delete('gln')
cmd.delete('his')
cmd.delete('his_i')
