'''
FUNC:S_2zjf_3_3_2_10
PDB:2zjf
EC:3.3.2.10
RESI:asp,asp,his
LOCI:a-104,302,333;
'''
IDSpec[(('asp','CG'),('rasp_i','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.17,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.25,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.31,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp_i','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.47,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.48,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.55,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp_i','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.95,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.10,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.15,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.94,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.92,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.00,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.11,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.16,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.12,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.35,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.26,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.47,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.95,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.25,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.48,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.10,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.31,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.55,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.15,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rhis','CE1'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.70,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp_i','CG'),('rhis','ND1'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.01,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp_i','CG'),('rhis','NE2'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.61,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp_i','OD1'),('rhis','CE1'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.92,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rhis','ND1'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.19,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp_i','OD1'),('rhis','NE2'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.16,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp_i','OD2'),('rhis','CE1'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.65,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rhis','ND1'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.96,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp_i','OD2'),('rhis','NE2'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.30,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.94,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.11,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.12,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.92,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.03,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.35,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.16,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.26,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp_i','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.70,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp_i','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+4.92,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp_i','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.65,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp_i','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.01,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp_i','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.19,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp_i','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.96,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp_i','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.61,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp_i','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.16,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp_i','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.30,resSelectionSubs('asp_i','OD2',subs,selection=True)))
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
IDSpec['S_2zjf_3_3_2_10'] = cmd.select('S_2zjf_3_3_2_10', 'asp|asp_i|his')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('his')
