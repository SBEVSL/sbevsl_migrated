'''
FUNC:S_2hs8_1_3_1_42
PDB:2hs8
EC:1.3.1.42
RESI:his,his,tyr
LOCI:a-185,188,190;
'''
IDSpec[(('his','CE1'),('rtyr','CE1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.35,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','CE1'),('rtyr','CZ'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.62,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','CE1'),('rtyr','OH'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.49,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','ND1'),('rtyr','CE1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.12,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','ND1'),('rtyr','CZ'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.58,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','ND1'),('rtyr','OH'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.55,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','NE2'),('rtyr','CE1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.93,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','NE2'),('rtyr','CZ'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.14,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','NE2'),('rtyr','OH'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.87,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','CE1'),('rhis','CE1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.46,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','CE1'),('rhis','ND1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.77,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','CE1'),('rhis','NE2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','ND1'),('rhis','CE1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.53,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','ND1'),('rhis','ND1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.99,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','ND1'),('rhis','NE2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.07,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','NE2'),('rhis','CE1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.69,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','NE2'),('rhis','ND1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.94,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','NE2'),('rhis','NE2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.60,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('tyr','CE1'),('shis','CE1'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.35,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','ND1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.12,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','NE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.93,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','CE1'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.62,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','ND1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.58,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','NE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.14,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','CE1'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.49,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','ND1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.55,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','NE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.87,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rhis','CE1'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.34,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CE1'),('rhis','ND1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.04,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CE1'),('rhis','NE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.00,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','CZ'),('rhis','CE1'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CZ'),('rhis','ND1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.81,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CZ'),('rhis','NE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.82,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','OH'),('rhis','CE1'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.26,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','OH'),('rhis','ND1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','OH'),('rhis','NE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.05,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.46,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.53,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.69,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.77,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.99,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.94,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.10,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.07,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.60,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('styr','CE1'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.34,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('styr','CZ'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.10,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his_i','CE1'),('styr','OH'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.26,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his_i','ND1'),('styr','CE1'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.04,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('styr','CZ'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.81,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his_i','ND1'),('styr','OH'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.03,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his_i','NE2'),('styr','CE1'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.00,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('styr','CZ'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.82,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his_i','NE2'),('styr','OH'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.05,resSelectionSubs('tyr','OH',subs,selection=True)))
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
IDSpec['S_2hs8_1_3_1_42'] = cmd.select('S_2hs8_1_3_1_42', 'his|tyr|his_i')
cmd.delete('his')
cmd.delete('tyr')
cmd.delete('his_i')
