'''
FUNC:S_2zz4_4_1_1_23
PDB:2zz4
EC:4.1.1.23
RESI:lys,asp,lys,asn
LOCI:a-42,70,72,75;
'''
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.01,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.09,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.11,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.46,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+4.90,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.30,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.45,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.37,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.79,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.19,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.10,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.57,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.91,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.86,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.56,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.45,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.00,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.65,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CD'),('rasn','CG'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.65,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CD'),('rasn','ND2'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.65,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CD'),('rasn','OD1'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.65,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','CE'),('rasn','CG'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.65,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CE'),('rasn','ND2'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.65,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CE'),('rasn','OD1'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.65,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','NZ'),('rasn','CG'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.65,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','NZ'),('rasn','ND2'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.65,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','NZ'),('rasn','OD1'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.65,resSelectionSubs('asn','OD1',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.01,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.46,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.45,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.09,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.90,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.37,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.11,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.30,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.79,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','CG'),('rlys_i','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.10,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('asp','CG'),('rlys_i','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.21,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('asp','CG'),('rlys_i','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.40,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys_i','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.16,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('asp','OD1'),('rlys_i','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.35,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('asp','OD1'),('rlys_i','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.61,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys_i','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.66,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('asp','OD2'),('rlys_i','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.39,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('asp','OD2'),('rlys_i','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.57,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+4.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+4.57,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+4.57,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.57,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.57,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.57,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.57,resSelectionSubs('asn','OD1',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
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
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.19,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.91,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.45,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.86,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.00,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.57,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.56,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.65,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','CG'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.10,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD1'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.16,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD2'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.66,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','CG'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.21,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD1'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.35,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD2'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.39,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','CG'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.40,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD1'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.61,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD2'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.57,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rasn','CG'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+4.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys_i','CD'),('rasn','ND2'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+4.57,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys_i','CD'),('rasn','OD1'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+4.57,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys_i','CE'),('rasn','CG'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+4.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys_i','CE'),('rasn','ND2'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+4.57,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys_i','CE'),('rasn','OD1'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+4.57,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys_i','NZ'),('rasn','CG'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys_i','NZ'),('rasn','ND2'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.57,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys_i','NZ'),('rasn','OD1'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.57,resSelectionSubs('asn','OD1',subs)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27')
IDSpec['r_lys_i'] = cmd.count_atoms(resSelectionSubs('lys_i', subs=subs, selection=True))
cmd.delete('lys_i1')
cmd.delete('lys_i2')
cmd.delete('lys_i3')
cmd.delete('lys_i4')
cmd.delete('lys_i5')
cmd.delete('lys_i6')
cmd.delete('lys_i7')
cmd.delete('lys_i8')
cmd.delete('lys_i9')
cmd.delete('lys_i10')
cmd.delete('lys_i11')
cmd.delete('lys_i12')
cmd.delete('lys_i13')
cmd.delete('lys_i14')
cmd.delete('lys_i15')
cmd.delete('lys_i16')
cmd.delete('lys_i17')
cmd.delete('lys_i18')
cmd.delete('lys_i19')
cmd.delete('lys_i20')
cmd.delete('lys_i21')
cmd.delete('lys_i22')
cmd.delete('lys_i23')
cmd.delete('lys_i24')
cmd.delete('lys_i25')
cmd.delete('lys_i26')
cmd.delete('lys_i27')
IDSpec[(('asn','CG'),('slys','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','CE'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','NZ'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CE'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','NZ'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CE'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','NZ'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','CG'),('slys_i','CD'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('slys_i','CE'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('slys_i','NZ'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+4.57,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys_i','CD'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys_i','CE'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys_i','NZ'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.57,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys_i','CD'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys_i','CE'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys_i','NZ'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.57,resSelectionSubs('lys_i','NZ',subs,selection=True)))
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
IDSpec['S_2zz4_4_1_1_23'] = cmd.select('S_2zz4_4_1_1_23', 'lys|asp|lys_i|asn')
cmd.delete('lys')
cmd.delete('asp')
cmd.delete('lys_i')
cmd.delete('asn')
