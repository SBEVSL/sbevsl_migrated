'''
FUNC:S_1tz3_2_7_1_4
PDB:1tz3
EC:2.7.1.4
RESI:gly,ala,gly,asp
LOCI:a-249,250,251,252;
'''
IDSpec[(('asp','CG'),('rgly','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.96,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','CG'),('rgly','N'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.75,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','CG'),('rgly','O'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.76,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD1'),('rgly','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.60,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD1'),('rgly','N'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.22,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD1'),('rgly','O'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.33,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD2'),('rgly','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.91,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD2'),('rgly','N'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.59,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD2'),('rgly','O'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.22,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','CG'),('rgly_i','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.97,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('asp','CG'),('rgly_i','N'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.26,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('asp','CG'),('rgly_i','O'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.81,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('asp','OD1'),('rgly_i','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.44,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('asp','OD1'),('rgly_i','N'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.99,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('asp','OD1'),('rgly_i','O'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.36,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('asp','OD2'),('rgly_i','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.00,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('asp','OD2'),('rgly_i','N'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.09,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('asp','OD2'),('rgly_i','O'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.04,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('asp','CG'),('rala','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.60,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','CG'),('rala','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.74,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','CG'),('rala','CG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.74,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','OD1'),('rala','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.72,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','OD1'),('rala','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.71,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','OD1'),('rala','CG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.71,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','OD2'),('rala','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.20,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','OD2'),('rala','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.32,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','OD2'),('rala','CG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.32,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('gly','CA'),('sasp','CG'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.96,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.60,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','CG'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.75,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.22,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.59,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','CG'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.33,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.22,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','CA'),('rgly_i','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.57,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','CA'),('rgly_i','N'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.50,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','CA'),('rgly_i','O'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.75,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','N'),('rgly_i','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.03,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','N'),('rgly_i','N'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.87,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','N'),('rgly_i','O'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.59,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','O'),('rgly_i','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.36,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','O'),('rgly_i','N'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.46,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','O'),('rgly_i','O'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.02,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','CA'),('rala','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.78,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly','CA'),('rala','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.79,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly','CA'),('rala','CG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.79,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gly','N'),('rala','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.16,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly','N'),('rala','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.76,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly','N'),('rala','CG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.76,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gly','O'),('rala','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.76,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly','O'),('rala','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.23,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly','O'),('rala','CG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.23,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('gly_i','CA'),('sasp','CG'))] = cmd.select('gly_i1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.97,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sasp','OD1'))] = cmd.select('gly_i2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sasp','OD2'))] = cmd.select('gly_i3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasp','CG'))] = cmd.select('gly_i4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.26,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasp','OD1'))] = cmd.select('gly_i5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.99,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasp','OD2'))] = cmd.select('gly_i6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.09,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasp','CG'))] = cmd.select('gly_i7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.81,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasp','OD1'))] = cmd.select('gly_i8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.36,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasp','OD2'))] = cmd.select('gly_i9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.04,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','CA'))] = cmd.select('gly_i10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.57,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','N'))] = cmd.select('gly_i11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.03,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','O'))] = cmd.select('gly_i12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.36,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','CA'))] = cmd.select('gly_i13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.50,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','N'))] = cmd.select('gly_i14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.87,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','O'))] = cmd.select('gly_i15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.46,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','CA'))] = cmd.select('gly_i16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.75,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','N'))] = cmd.select('gly_i17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.59,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','O'))] = cmd.select('gly_i18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.02,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','CA'),('rala','CA'))] = cmd.select('gly_i19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.80,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly_i','CA'),('rala','CB'))] = cmd.select('gly_i20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.35,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly_i','CA'),('rala','CG'))] = cmd.select('gly_i21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.35,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gly_i','N'),('rala','CA'))] = cmd.select('gly_i22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+4.43,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly_i','N'),('rala','CB'))] = cmd.select('gly_i23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.02,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly_i','N'),('rala','CG'))] = cmd.select('gly_i24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.02,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gly_i','O'),('rala','CA'))] = cmd.select('gly_i25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.35,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly_i','O'),('rala','CB'))] = cmd.select('gly_i26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.25,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly_i','O'),('rala','CG'))] = cmd.select('gly_i27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.25,resSelectionSubs('ala','CG',subs)))
IDSpec['gly_i'] = cmd.select('gly_i',' br. gly_i1&br. gly_i2&br. gly_i3&br. gly_i4&br. gly_i5&br. gly_i6&br. gly_i7&br. gly_i8&br. gly_i9&br. gly_i10&br. gly_i11&br. gly_i12&br. gly_i13&br. gly_i14&br. gly_i15&br. gly_i16&br. gly_i17&br. gly_i18&br. gly_i19&br. gly_i20&br. gly_i21&br. gly_i22&br. gly_i23&br. gly_i24&br. gly_i25&br. gly_i26&br. gly_i27')
IDSpec['r_gly_i'] = cmd.count_atoms(resSelectionSubs('gly_i', subs=subs, selection=True))
cmd.delete('gly_i1')
cmd.delete('gly_i2')
cmd.delete('gly_i3')
cmd.delete('gly_i4')
cmd.delete('gly_i5')
cmd.delete('gly_i6')
cmd.delete('gly_i7')
cmd.delete('gly_i8')
cmd.delete('gly_i9')
cmd.delete('gly_i10')
cmd.delete('gly_i11')
cmd.delete('gly_i12')
cmd.delete('gly_i13')
cmd.delete('gly_i14')
cmd.delete('gly_i15')
cmd.delete('gly_i16')
cmd.delete('gly_i17')
cmd.delete('gly_i18')
cmd.delete('gly_i19')
cmd.delete('gly_i20')
cmd.delete('gly_i21')
cmd.delete('gly_i22')
cmd.delete('gly_i23')
cmd.delete('gly_i24')
cmd.delete('gly_i25')
cmd.delete('gly_i26')
cmd.delete('gly_i27')
IDSpec[(('ala','CA'),('sasp','CG'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.60,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CA'),('sasp','OD1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.72,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CA'),('sasp','OD2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.20,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','CG'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.74,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','OD1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.71,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','OD2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10.32,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','CG'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.32,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','OD1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.32,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','OD2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.32,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly','CA'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+5.78,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly','N'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.16,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly','O'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+4.76,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly','CA'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.79,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly','N'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.76,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly','O'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.23,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly','CA'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.23,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly','N'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.23,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly','O'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.23,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly_i','CA'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+5.80,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly_i','N'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+4.43,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly_i','O'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.35,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly_i','CA'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.35,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly_i','N'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.02,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly_i','O'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.25,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly_i','CA'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly_i','N'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly_i','O'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18&br. ala19&br. ala20&br. ala21&br. ala22&br. ala23&br. ala24&br. ala25&br. ala26&br. ala27')
IDSpec['r_ala'] = cmd.count_atoms(resSelectionSubs('ala', subs=subs, selection=True))
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
cmd.delete('ala10')
cmd.delete('ala11')
cmd.delete('ala12')
cmd.delete('ala13')
cmd.delete('ala14')
cmd.delete('ala15')
cmd.delete('ala16')
cmd.delete('ala17')
cmd.delete('ala18')
cmd.delete('ala19')
cmd.delete('ala20')
cmd.delete('ala21')
cmd.delete('ala22')
cmd.delete('ala23')
cmd.delete('ala24')
cmd.delete('ala25')
cmd.delete('ala26')
cmd.delete('ala27')
IDSpec['S_1tz3_2_7_1_4'] = cmd.select('S_1tz3_2_7_1_4', 'asp|gly|gly_i|ala')
cmd.delete('asp')
cmd.delete('gly')
cmd.delete('gly_i')
cmd.delete('ala')
