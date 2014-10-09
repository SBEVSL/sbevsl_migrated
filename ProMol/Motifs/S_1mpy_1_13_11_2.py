'''
FUNC:S_1mpy_1_13_11_2
PDB:1mpy
EC:1.13.11.2
RESI:his,his,tyr
LOCI:a-199,246,255;
'''
IDSpec[(('his','CE1'),('rhis','CE1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.86,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','CE1'),('rhis','ND1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.09,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','CE1'),('rhis','NE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.98,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','ND1'),('rhis','CE1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.84,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','ND1'),('rhis','ND1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.92,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','ND1'),('rhis','NE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.01,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','NE2'),('rhis','CE1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.51,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','NE2'),('rhis','ND1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.90,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','NE2'),('rhis','NE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','CE1'),('rtyr','CE1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.70,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','CE1'),('rtyr','CZ'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.45,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','CE1'),('rtyr','OH'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.17,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','ND1'),('rtyr','CE1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.98,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','ND1'),('rtyr','CZ'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.70,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','ND1'),('rtyr','OH'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.40,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','NE2'),('rtyr','CE1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.71,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','NE2'),('rtyr','CZ'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.52,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','NE2'),('rtyr','OH'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.29,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.86,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.51,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.09,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.92,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.90,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.98,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.01,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.60,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('rtyr','CE1'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.58,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his_i','CE1'),('rtyr','CZ'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.82,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his_i','CE1'),('rtyr','OH'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.31,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his_i','ND1'),('rtyr','CE1'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.85,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his_i','ND1'),('rtyr','CZ'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.14,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his_i','ND1'),('rtyr','OH'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.57,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his_i','NE2'),('rtyr','CE1'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.09,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his_i','NE2'),('rtyr','CZ'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.62,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his_i','NE2'),('rtyr','OH'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.97,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('shis','CE1'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.70,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','ND1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.98,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','NE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.71,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','CE1'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.45,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','ND1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.70,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','NE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.52,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','CE1'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.17,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','ND1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.40,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','NE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.29,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis_i','CE1'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.58,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis_i','ND1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.85,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis_i','NE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.09,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis_i','CE1'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.82,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis_i','ND1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.14,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis_i','NE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.62,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis_i','CE1'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.31,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis_i','ND1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.57,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis_i','NE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.97,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18')
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
IDSpec['S_1mpy_1_13_11_2'] = cmd.select('S_1mpy_1_13_11_2', 'his|his_i|tyr')
cmd.delete('his')
cmd.delete('his_i')
cmd.delete('tyr')
