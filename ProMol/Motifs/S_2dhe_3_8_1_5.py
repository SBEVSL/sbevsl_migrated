'''
FUNC:S_2dhe_3_8_1_5
PDB:2dhe
EC:3.8.1.5
RESI:asp,asp,his
LOCI:a-124,260,289;
'''
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.90,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+4.98,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.14,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.25,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.33,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.20,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.34,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.29,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.61,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.52,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.88,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.43,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.39,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.82,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.57,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.33,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.98,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.90,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.14,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.20,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.98,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.25,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.34,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.10,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.33,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.29,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.50,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.37,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.69,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.56,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.33,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.82,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.71,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.51,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.92,resSelectionSubs('asp','OD2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
IDSpec['r_asp'] = cmd.count_atoms(resSelectionSubs('asp', subs=subs, selection=True))
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
IDSpec[(('asp_i','CG'),('shis','CE1'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.61,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('shis','ND1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.43,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('shis','NE2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.57,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('shis','CE1'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.52,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('shis','ND1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.39,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('shis','NE2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.33,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('shis','CE1'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.88,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('shis','ND1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.82,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('shis','NE2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.98,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.50,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.56,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.71,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.37,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.33,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.51,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.82,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.92,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['asp_i'] = cmd.select('asp_i',' br. asp_i1&br. asp_i2&br. asp_i3&br. asp_i4&br. asp_i5&br. asp_i6&br. asp_i7&br. asp_i8&br. asp_i9&br. asp_i10&br. asp_i11&br. asp_i12&br. asp_i13&br. asp_i14&br. asp_i15&br. asp_i16&br. asp_i17&br. asp_i18')
IDSpec['r_asp_i'] = cmd.count_atoms(resSelectionSubs('asp_i', subs=subs, selection=True))
cmd.delete('asp_i1')
cmd.delete('asp_i2')
cmd.delete('asp_i3')
cmd.delete('asp_i4')
cmd.delete('asp_i5')
cmd.delete('asp_i6')
cmd.delete('asp_i7')
cmd.delete('asp_i8')
cmd.delete('asp_i9')
cmd.delete('asp_i10')
cmd.delete('asp_i11')
cmd.delete('asp_i12')
cmd.delete('asp_i13')
cmd.delete('asp_i14')
cmd.delete('asp_i15')
cmd.delete('asp_i16')
cmd.delete('asp_i17')
cmd.delete('asp_i18')
IDSpec['S_2dhe_3_8_1_5'] = cmd.select('S_2dhe_3_8_1_5', 'his|asp|asp_i')
cmd.delete('his')
cmd.delete('asp')
cmd.delete('asp_i')
