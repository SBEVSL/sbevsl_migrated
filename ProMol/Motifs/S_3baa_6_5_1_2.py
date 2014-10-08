'''
FUNC:S_3baa_6_5_1_2
PDB:3baa
EC:6.5.1.2
RESI:lys,asp,arg,lys
LOCI:a-120,122,202,315;
'''
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.20,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.55,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.52,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.02,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.26,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.86,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.51,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.23,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.60,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.66,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.99,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.45,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.81,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.90,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.72,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.62,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.57,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.64,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CD'),('rarg','CZ'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.27,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CD'),('rarg','NE'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.52,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CD'),('rarg','NH1'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.87,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','CE'),('rarg','CZ'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.41,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CE'),('rarg','NE'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.73,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CE'),('rarg','NH1'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.97,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','NZ'),('rarg','CZ'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.94,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','NZ'),('rarg','NE'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.24,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','NZ'),('rarg','NH1'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.54,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.20,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.02,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.51,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.55,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.26,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.23,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.52,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.86,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.60,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rasp','CG'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys_i','CD'),('rasp','OD1'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.24,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys_i','CD'),('rasp','OD2'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.51,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys_i','CE'),('rasp','CG'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.95,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys_i','CE'),('rasp','OD1'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.02,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys_i','CE'),('rasp','OD2'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.35,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys_i','NZ'),('rasp','CG'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.35,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys_i','NZ'),('rasp','OD1'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.19,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys_i','NZ'),('rasp','OD2'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.86,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys_i','CD'),('rarg','CZ'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.03,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_i','CD'),('rarg','NE'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.12,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_i','CD'),('rarg','NH1'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.96,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys_i','CE'),('rarg','CZ'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.82,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_i','CE'),('rarg','NE'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.84,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_i','CE'),('rarg','NH1'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.85,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys_i','NZ'),('rarg','CZ'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.16,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_i','NZ'),('rarg','NE'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.23,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_i','NZ'),('rarg','NH1'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.24,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.66,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.81,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.62,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.99,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.90,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.45,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.72,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.64,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','CG'),('slys_i','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.10,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys_i','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.95,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys_i','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.35,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys_i','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.24,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys_i','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.02,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys_i','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.19,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys_i','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.51,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys_i','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.35,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys_i','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.86,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.90,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.82,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.03,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.68,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.58,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.85,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.80,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.64,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.02,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('slys','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.27,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CE'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.41,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','NZ'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.94,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.52,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CE'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.73,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','NZ'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.24,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.87,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CE'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.97,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','NZ'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.54,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_i','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.03,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_i','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.82,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_i','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.16,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_i','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.12,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_i','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.84,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_i','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.23,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_i','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.96,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_i','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.85,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_i','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.24,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.90,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.68,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.80,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.82,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.58,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.64,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.03,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.85,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.02,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_3baa_6_5_1_2'] = cmd.select('S_3baa_6_5_1_2', 'lys|lys_i|asp|arg')
cmd.delete('lys')
cmd.delete('lys_i')
cmd.delete('asp')
cmd.delete('arg')
