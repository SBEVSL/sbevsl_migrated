'''
FUNC:S_1pem_1_17_4_1
PDB:1pem
EC:1.17.4.1
RESI:cys,asn,cys,glu,cys
LOCI:a-178,386,388,390,415;
'''
IDSpec[(('cys','CA'),('rcys_i','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.17,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CA'),('rcys_i','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.17,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CA'),('rcys_i','SG'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.58,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CB'),('rcys_i','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.45,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','CB'),('rcys_i','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.50,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','CB'),('rcys_i','SG'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.80,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','SG'),('rcys_i','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.78,resSelectionSubs('cys_i','CA',subs)))
IDSpec[(('cys','SG'),('rcys_i','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.03,resSelectionSubs('cys_i','CB',subs)))
IDSpec[(('cys','SG'),('rcys_i','SG'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.46,resSelectionSubs('cys_i','SG',subs)))
IDSpec[(('cys','CA'),('rasn','CG'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.14,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys','CA'),('rasn','ND2'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.54,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys','CA'),('rasn','OD1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.29,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys','CB'),('rasn','CG'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.33,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys','CB'),('rasn','ND2'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.39,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys','CB'),('rasn','OD1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.55,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys','SG'),('rasn','CG'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.40,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys','SG'),('rasn','ND2'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.23,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys','SG'),('rasn','OD1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.92,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys','CA'),('rglu','CD'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.95,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CA'),('rglu','OE1'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.71,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CA'),('rglu','OE2'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.11,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','CB'),('rglu','CD'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.97,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CB'),('rglu','OE1'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.52,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CB'),('rglu','OE2'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.21,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','SG'),('rglu','CD'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.03,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','SG'),('rglu','OE1'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.17,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','SG'),('rglu','OE2'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.24,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','CA'),('rcys_ii','CA'))] = cmd.select('cys28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.37,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('cys','CA'),('rcys_ii','CB'))] = cmd.select('cys29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.72,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('cys','CA'),('rcys_ii','SG'))] = cmd.select('cys30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.27,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('cys','CB'),('rcys_ii','CA'))] = cmd.select('cys31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.85,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('cys','CB'),('rcys_ii','CB'))] = cmd.select('cys32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.04,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('cys','CB'),('rcys_ii','SG'))] = cmd.select('cys33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.72,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('cys','SG'),('rcys_ii','CA'))] = cmd.select('cys34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.47,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('cys','SG'),('rcys_ii','CB'))] = cmd.select('cys35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.79,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('cys','SG'),('rcys_ii','SG'))] = cmd.select('cys36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.78,resSelectionSubs('cys_ii','SG',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27&br. cys28&br. cys29&br. cys30&br. cys31&br. cys32&br. cys33&br. cys34&br. cys35&br. cys36')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
cmd.delete('cys19')
cmd.delete('cys20')
cmd.delete('cys21')
cmd.delete('cys22')
cmd.delete('cys23')
cmd.delete('cys24')
cmd.delete('cys25')
cmd.delete('cys26')
cmd.delete('cys27')
cmd.delete('cys28')
cmd.delete('cys29')
cmd.delete('cys30')
cmd.delete('cys31')
cmd.delete('cys32')
cmd.delete('cys33')
cmd.delete('cys34')
cmd.delete('cys35')
cmd.delete('cys36')
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.17,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.45,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.78,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.17,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.50,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.03,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.58,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.80,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.46,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rasn','CG'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.76,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys_i','CA'),('rasn','ND2'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.78,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys_i','CA'),('rasn','OD1'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.12,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys_i','CB'),('rasn','CG'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.71,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys_i','CB'),('rasn','ND2'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.83,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys_i','CB'),('rasn','OD1'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.92,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys_i','SG'),('rasn','CG'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.39,resSelectionSubs('asn','CG',subs)))
IDSpec[(('cys_i','SG'),('rasn','ND2'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.49,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('cys_i','SG'),('rasn','OD1'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.38,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('cys_i','CA'),('rglu','CD'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.36,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys_i','CA'),('rglu','OE1'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.39,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys_i','CA'),('rglu','OE2'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.48,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys_i','CB'),('rglu','CD'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.22,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys_i','CB'),('rglu','OE1'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.42,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys_i','CB'),('rglu','OE2'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.25,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys_i','SG'),('rglu','CD'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.13,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys_i','SG'),('rglu','OE1'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.52,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys_i','SG'),('rglu','OE2'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.00,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys_i','CA'),('rcys_ii','CA'))] = cmd.select('cys_i28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.05,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('cys_i','CA'),('rcys_ii','CB'))] = cmd.select('cys_i29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.24,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('cys_i','CA'),('rcys_ii','SG'))] = cmd.select('cys_i30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.64,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('cys_i','CB'),('rcys_ii','CA'))] = cmd.select('cys_i31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.35,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('cys_i','CB'),('rcys_ii','CB'))] = cmd.select('cys_i32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.35,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('cys_i','CB'),('rcys_ii','SG'))] = cmd.select('cys_i33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.25,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('cys_i','SG'),('rcys_ii','CA'))] = cmd.select('cys_i34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.88,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('cys_i','SG'),('rcys_ii','CB'))] = cmd.select('cys_i35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.70,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('cys_i','SG'),('rcys_ii','SG'))] = cmd.select('cys_i36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.49,resSelectionSubs('cys_ii','SG',subs)))
IDSpec['cys_i'] = cmd.select('cys_i',' br. cys_i1&br. cys_i2&br. cys_i3&br. cys_i4&br. cys_i5&br. cys_i6&br. cys_i7&br. cys_i8&br. cys_i9&br. cys_i10&br. cys_i11&br. cys_i12&br. cys_i13&br. cys_i14&br. cys_i15&br. cys_i16&br. cys_i17&br. cys_i18&br. cys_i19&br. cys_i20&br. cys_i21&br. cys_i22&br. cys_i23&br. cys_i24&br. cys_i25&br. cys_i26&br. cys_i27&br. cys_i28&br. cys_i29&br. cys_i30&br. cys_i31&br. cys_i32&br. cys_i33&br. cys_i34&br. cys_i35&br. cys_i36')
IDSpec['r_cys_i'] = cmd.count_atoms(resSelectionSubs('cys_i', subs=subs, selection=True))
cmd.delete('cys_i1')
cmd.delete('cys_i2')
cmd.delete('cys_i3')
cmd.delete('cys_i4')
cmd.delete('cys_i5')
cmd.delete('cys_i6')
cmd.delete('cys_i7')
cmd.delete('cys_i8')
cmd.delete('cys_i9')
cmd.delete('cys_i10')
cmd.delete('cys_i11')
cmd.delete('cys_i12')
cmd.delete('cys_i13')
cmd.delete('cys_i14')
cmd.delete('cys_i15')
cmd.delete('cys_i16')
cmd.delete('cys_i17')
cmd.delete('cys_i18')
cmd.delete('cys_i19')
cmd.delete('cys_i20')
cmd.delete('cys_i21')
cmd.delete('cys_i22')
cmd.delete('cys_i23')
cmd.delete('cys_i24')
cmd.delete('cys_i25')
cmd.delete('cys_i26')
cmd.delete('cys_i27')
cmd.delete('cys_i28')
cmd.delete('cys_i29')
cmd.delete('cys_i30')
cmd.delete('cys_i31')
cmd.delete('cys_i32')
cmd.delete('cys_i33')
cmd.delete('cys_i34')
cmd.delete('cys_i35')
cmd.delete('cys_i36')
IDSpec[(('asn','CG'),('scys','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.14,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('scys','CB'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.33,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('scys','SG'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.40,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.54,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys','CB'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.39,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys','SG'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.23,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.29,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys','CB'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.55,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys','SG'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.92,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asn','CG'),('scys_i','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.76,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('scys_i','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.71,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('scys_i','SG'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.39,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys_i','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.78,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys_i','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.83,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('scys_i','SG'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.49,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys_i','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.12,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys_i','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.92,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('scys_i','SG'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.38,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('asn','CG'),('rglu','CD'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.03,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','CG'),('rglu','OE1'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.18,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','CG'),('rglu','OE2'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.49,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','ND2'),('rglu','CD'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.48,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','ND2'),('rglu','OE1'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.26,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','ND2'),('rglu','OE2'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.18,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','OD1'),('rglu','CD'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.88,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','OD1'),('rglu','OE1'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.36,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','OD1'),('rglu','OE2'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.24,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','CG'),('rcys_ii','CA'))] = cmd.select('asn28', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.82,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('asn','CG'),('rcys_ii','CB'))] = cmd.select('asn29', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.15,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('asn','CG'),('rcys_ii','SG'))] = cmd.select('asn30', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.39,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('asn','ND2'),('rcys_ii','CA'))] = cmd.select('asn31', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.36,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('asn','ND2'),('rcys_ii','CB'))] = cmd.select('asn32', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.62,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('asn','ND2'),('rcys_ii','SG'))] = cmd.select('asn33', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.96,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('asn','OD1'),('rcys_ii','CA'))] = cmd.select('asn34', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.88,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('asn','OD1'),('rcys_ii','CB'))] = cmd.select('asn35', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.11,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('asn','OD1'),('rcys_ii','SG'))] = cmd.select('asn36', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.33,resSelectionSubs('cys_ii','SG',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32&br. asn33&br. asn34&br. asn35&br. asn36')
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
cmd.delete('asn28')
cmd.delete('asn29')
cmd.delete('asn30')
cmd.delete('asn31')
cmd.delete('asn32')
cmd.delete('asn33')
cmd.delete('asn34')
cmd.delete('asn35')
cmd.delete('asn36')
IDSpec[(('glu','CD'),('scys','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.95,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('scys','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.97,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('scys','SG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.03,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.71,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.52,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','SG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.17,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.11,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.21,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','SG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.24,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','CD'),('scys_i','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.36,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('scys_i','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.22,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('scys_i','SG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.13,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys_i','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.39,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys_i','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.42,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys_i','SG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.52,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys_i','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.48,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys_i','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.25,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys_i','SG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.00,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','CG'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.03,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','ND2'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.48,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','OD1'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.88,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','CG'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.18,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','ND2'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.26,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','OD1'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.36,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','CG'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.49,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','ND2'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.18,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','OD1'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.24,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('rcys_ii','CA'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.92,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('glu','CD'),('rcys_ii','CB'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.65,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('glu','CD'),('rcys_ii','SG'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.33,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('glu','OE1'),('rcys_ii','CA'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.23,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('glu','OE1'),('rcys_ii','CB'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.99,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('glu','OE1'),('rcys_ii','SG'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.82,resSelectionSubs('cys_ii','SG',subs)))
IDSpec[(('glu','OE2'),('rcys_ii','CA'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.92,resSelectionSubs('cys_ii','CA',subs)))
IDSpec[(('glu','OE2'),('rcys_ii','CB'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.57,resSelectionSubs('cys_ii','CB',subs)))
IDSpec[(('glu','OE2'),('rcys_ii','SG'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.32,resSelectionSubs('cys_ii','SG',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
IDSpec[(('cys_ii','CA'),('scys','CA'))] = cmd.select('cys_ii1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.37,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys','CB'))] = cmd.select('cys_ii2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.85,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys','SG'))] = cmd.select('cys_ii3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.47,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys','CA'))] = cmd.select('cys_ii4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.72,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys','CB'))] = cmd.select('cys_ii5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.04,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys','SG'))] = cmd.select('cys_ii6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.79,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys','CA'))] = cmd.select('cys_ii7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.27,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys','CB'))] = cmd.select('cys_ii8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.72,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys','SG'))] = cmd.select('cys_ii9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.78,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys_i','CA'))] = cmd.select('cys_ii10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.05,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys_i','CB'))] = cmd.select('cys_ii11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.35,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys_i','SG'))] = cmd.select('cys_ii12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.88,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys_i','CA'))] = cmd.select('cys_ii13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.24,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys_i','CB'))] = cmd.select('cys_ii14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.35,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys_i','SG'))] = cmd.select('cys_ii15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.70,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys_i','CA'))] = cmd.select('cys_ii16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.64,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys_i','CB'))] = cmd.select('cys_ii17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.25,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys_i','SG'))] = cmd.select('cys_ii18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.49,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sasn','CG'))] = cmd.select('cys_ii19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.82,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sasn','ND2'))] = cmd.select('cys_ii20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.36,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sasn','OD1'))] = cmd.select('cys_ii21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.88,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sasn','CG'))] = cmd.select('cys_ii22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.15,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sasn','ND2'))] = cmd.select('cys_ii23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.62,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sasn','OD1'))] = cmd.select('cys_ii24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.11,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sasn','CG'))] = cmd.select('cys_ii25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.39,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sasn','ND2'))] = cmd.select('cys_ii26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.96,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sasn','OD1'))] = cmd.select('cys_ii27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.33,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sglu','CD'))] = cmd.select('cys_ii28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.92,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sglu','OE1'))] = cmd.select('cys_ii29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.23,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sglu','OE2'))] = cmd.select('cys_ii30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.92,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sglu','CD'))] = cmd.select('cys_ii31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.65,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sglu','OE1'))] = cmd.select('cys_ii32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.99,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sglu','OE2'))] = cmd.select('cys_ii33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.57,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sglu','CD'))] = cmd.select('cys_ii34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.33,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sglu','OE1'))] = cmd.select('cys_ii35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.82,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sglu','OE2'))] = cmd.select('cys_ii36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.32,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['cys_ii'] = cmd.select('cys_ii',' br. cys_ii1&br. cys_ii2&br. cys_ii3&br. cys_ii4&br. cys_ii5&br. cys_ii6&br. cys_ii7&br. cys_ii8&br. cys_ii9&br. cys_ii10&br. cys_ii11&br. cys_ii12&br. cys_ii13&br. cys_ii14&br. cys_ii15&br. cys_ii16&br. cys_ii17&br. cys_ii18&br. cys_ii19&br. cys_ii20&br. cys_ii21&br. cys_ii22&br. cys_ii23&br. cys_ii24&br. cys_ii25&br. cys_ii26&br. cys_ii27&br. cys_ii28&br. cys_ii29&br. cys_ii30&br. cys_ii31&br. cys_ii32&br. cys_ii33&br. cys_ii34&br. cys_ii35&br. cys_ii36')
IDSpec['r_cys_ii'] = cmd.count_atoms(resSelectionSubs('cys_ii', subs=subs, selection=True))
cmd.delete('cys_ii1')
cmd.delete('cys_ii2')
cmd.delete('cys_ii3')
cmd.delete('cys_ii4')
cmd.delete('cys_ii5')
cmd.delete('cys_ii6')
cmd.delete('cys_ii7')
cmd.delete('cys_ii8')
cmd.delete('cys_ii9')
cmd.delete('cys_ii10')
cmd.delete('cys_ii11')
cmd.delete('cys_ii12')
cmd.delete('cys_ii13')
cmd.delete('cys_ii14')
cmd.delete('cys_ii15')
cmd.delete('cys_ii16')
cmd.delete('cys_ii17')
cmd.delete('cys_ii18')
cmd.delete('cys_ii19')
cmd.delete('cys_ii20')
cmd.delete('cys_ii21')
cmd.delete('cys_ii22')
cmd.delete('cys_ii23')
cmd.delete('cys_ii24')
cmd.delete('cys_ii25')
cmd.delete('cys_ii26')
cmd.delete('cys_ii27')
cmd.delete('cys_ii28')
cmd.delete('cys_ii29')
cmd.delete('cys_ii30')
cmd.delete('cys_ii31')
cmd.delete('cys_ii32')
cmd.delete('cys_ii33')
cmd.delete('cys_ii34')
cmd.delete('cys_ii35')
cmd.delete('cys_ii36')
IDSpec['S_1pem_1_17_4_1'] = cmd.select('S_1pem_1_17_4_1', 'cys|cys_i|asn|glu|cys_ii')
cmd.delete('cys')
cmd.delete('cys_i')
cmd.delete('asn')
cmd.delete('glu')
cmd.delete('cys_ii')
