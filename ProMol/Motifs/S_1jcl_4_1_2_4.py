'''
FUNC:S_1jcl_4_1_2_4
PDB:1jcl
EC:4.1.2.4
RESI:asp,lys,lys
LOCI:a-102,167,201;
'''
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.04,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.94,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.95,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.38,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.44,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.39,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.06,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.77,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.83,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.38,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.85,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.10,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.39,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.00,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.25,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.50,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.05,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.04,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.38,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.06,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.94,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.77,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.95,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.39,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.83,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.69,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.50,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.51,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.72,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.01,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.68,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.09,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.23,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.41,resSelectionSubs('lys','NZ',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
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
IDSpec[(('lys_i','CD'),('sasp','CG'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.38,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD1'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.39,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD2'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.50,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','CG'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.85,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD1'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD2'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','CG'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.10,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD1'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.25,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD2'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.05,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.69,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.72,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.09,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.50,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.01,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.23,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.51,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.68,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.41,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18')
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
IDSpec['S_1jcl_4_1_2_4'] = cmd.select('S_1jcl_4_1_2_4', 'asp|lys|lys_i')
cmd.delete('asp')
cmd.delete('lys')
cmd.delete('lys_i')
