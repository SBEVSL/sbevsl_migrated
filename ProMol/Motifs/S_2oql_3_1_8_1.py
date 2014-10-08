'''
FUNC:S_2oql_3_1_8_1
PDB:2oql
EC:3.1.8.1
RESI:asp,gln,asp
LOCI:a-233,254,301;
'''
IDSpec[(('gln','CD'),('rasp','CG'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.06,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gln','CD'),('rasp','OD1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.75,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gln','CD'),('rasp','OD2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.29,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gln','NE2'),('rasp','CG'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.90,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gln','NE2'),('rasp','OD1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.63,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gln','NE2'),('rasp','OD2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.96,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gln','OE1'),('rasp','CG'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.85,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gln','OE1'),('rasp','OD1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.59,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gln','OE1'),('rasp','OD2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.07,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gln','CD'),('rasp_i','CG'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.65,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('gln','CD'),('rasp_i','OD1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.80,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('gln','CD'),('rasp_i','OD2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+5.74,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('gln','NE2'),('rasp_i','CG'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+5.99,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('gln','NE2'),('rasp_i','OD1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.07,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('gln','NE2'),('rasp_i','OD2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+4.89,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('gln','OE1'),('rasp_i','CG'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.87,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('gln','OE1'),('rasp_i','OD1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.00,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('gln','OE1'),('rasp_i','OD2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.93,resSelectionSubs('asp_i','OD2',subs)))
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
IDSpec[(('asp','CG'),('sgln','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.06,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('sgln','NE2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.90,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('asp','CG'),('sgln','OE1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.85,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgln','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.75,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgln','NE2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.63,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgln','OE1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.59,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgln','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.29,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgln','NE2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.96,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgln','OE1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.07,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('asp','CG'),('rasp_i','CG'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.71,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.84,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.74,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp_i','CG'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.37,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.54,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.44,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp_i','CG'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.88,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.97,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.83,resSelectionSubs('asp_i','OD2',subs)))
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
IDSpec[(('asp_i','CG'),('sgln','CD'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.65,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sgln','NE2'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.99,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sgln','OE1'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.87,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sgln','CD'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.80,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sgln','NE2'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.07,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sgln','OE1'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.00,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sgln','CD'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.74,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sgln','NE2'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.89,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sgln','OE1'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.93,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.71,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.37,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.88,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.84,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.54,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.97,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.74,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.83,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_2oql_3_1_8_1'] = cmd.select('S_2oql_3_1_8_1', 'gln|asp|asp_i')
cmd.delete('gln')
cmd.delete('asp')
cmd.delete('asp_i')
