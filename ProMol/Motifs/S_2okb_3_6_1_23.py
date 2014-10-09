'''
FUNC:S_2okb_3_6_1_23
PDB:2okb
EC:3.6.1.23
RESI:ser,leu,asp,asp
LOCI:a-70,74,85,87;
'''
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.36,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.69,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.24,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.77,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.24,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.69,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.84,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.16,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.62,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','CG'),('rleu','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.36,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','CG'),('rleu','CD2'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.43,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','CG'),('rleu','CG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+30.69,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','OD1'),('rleu','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+31.22,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','OD1'),('rleu','CD2'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+31.29,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','OD1'),('rleu','CG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.53,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','OD2'),('rleu','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+31.80,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','OD2'),('rleu','CD2'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+31.78,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','OD2'),('rleu','CG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+31.10,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+26.22,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+26.94,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+26.12,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.12,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.91,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.14,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+26.72,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.41,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+26.55,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.36,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.77,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.84,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.16,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.24,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.69,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.62,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rleu','CD1'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+36.98,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp_i','CG'),('rleu','CD2'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+37.49,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp_i','CG'),('rleu','CG'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+36.57,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp_i','OD1'),('rleu','CD1'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+36.06,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp_i','OD1'),('rleu','CD2'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+36.55,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp_i','OD1'),('rleu','CG'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+35.66,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp_i','OD2'),('rleu','CD1'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+38.18,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp_i','OD2'),('rleu','CD2'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+38.68,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp_i','OD2'),('rleu','CG'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+37.78,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp_i','CG'),('rser','CA'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.56,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp_i','CG'),('rser','CB'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+32.12,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp_i','CG'),('rser','OG'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.31,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp_i','OD1'),('rser','CA'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.64,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp_i','OD1'),('rser','CB'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+31.16,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp_i','OD1'),('rser','OG'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.32,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp_i','OD2'),('rser','CA'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+32.76,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp_i','OD2'),('rser','CB'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+33.31,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp_i','OD2'),('rser','OG'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+32.48,resSelectionSubs('ser','OG',subs)))
IDSpec['asp_i'] = cmd.select('asp_i',' br. asp_i1&br. asp_i2&br. asp_i3&br. asp_i4&br. asp_i5&br. asp_i6&br. asp_i7&br. asp_i8&br. asp_i9&br. asp_i10&br. asp_i11&br. asp_i12&br. asp_i13&br. asp_i14&br. asp_i15&br. asp_i16&br. asp_i17&br. asp_i18&br. asp_i19&br. asp_i20&br. asp_i21&br. asp_i22&br. asp_i23&br. asp_i24&br. asp_i25&br. asp_i26&br. asp_i27')
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
cmd.delete('asp_i19')
cmd.delete('asp_i20')
cmd.delete('asp_i21')
cmd.delete('asp_i22')
cmd.delete('asp_i23')
cmd.delete('asp_i24')
cmd.delete('asp_i25')
cmd.delete('asp_i26')
cmd.delete('asp_i27')
IDSpec[(('leu','CD1'),('sasp','CG'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+31.36,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp','OD1'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+31.22,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp','OD2'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+31.80,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','CG'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+31.43,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','OD1'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+31.29,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','OD2'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+31.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','CG'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+30.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','OD1'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+30.53,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','OD2'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+31.10,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp_i','CG'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+36.98,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp_i','OD1'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+36.06,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp_i','OD2'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+38.18,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp_i','CG'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+37.49,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp_i','OD1'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+36.55,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp_i','OD2'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+38.68,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp_i','CG'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+36.57,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp_i','OD1'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+35.66,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp_i','OD2'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+37.78,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('leu','CD1'),('rser','CA'))] = cmd.select('leu19', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.47,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD1'),('rser','CB'))] = cmd.select('leu20', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.33,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD1'),('rser','OG'))] = cmd.select('leu21', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.45,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CD2'),('rser','CA'))] = cmd.select('leu22', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.62,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD2'),('rser','CB'))] = cmd.select('leu23', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.59,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD2'),('rser','OG'))] = cmd.select('leu24', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.39,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CG'),('rser','CA'))] = cmd.select('leu25', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.44,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CG'),('rser','CB'))] = cmd.select('leu26', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.57,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CG'),('rser','OG'))] = cmd.select('leu27', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.57,resSelectionSubs('ser','OG',subs)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18&br. leu19&br. leu20&br. leu21&br. leu22&br. leu23&br. leu24&br. leu25&br. leu26&br. leu27')
IDSpec['r_leu'] = cmd.count_atoms(resSelectionSubs('leu', subs=subs, selection=True))
cmd.delete('leu1')
cmd.delete('leu2')
cmd.delete('leu3')
cmd.delete('leu4')
cmd.delete('leu5')
cmd.delete('leu6')
cmd.delete('leu7')
cmd.delete('leu8')
cmd.delete('leu9')
cmd.delete('leu10')
cmd.delete('leu11')
cmd.delete('leu12')
cmd.delete('leu13')
cmd.delete('leu14')
cmd.delete('leu15')
cmd.delete('leu16')
cmd.delete('leu17')
cmd.delete('leu18')
cmd.delete('leu19')
cmd.delete('leu20')
cmd.delete('leu21')
cmd.delete('leu22')
cmd.delete('leu23')
cmd.delete('leu24')
cmd.delete('leu25')
cmd.delete('leu26')
cmd.delete('leu27')
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+26.22,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+26.12,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+26.72,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+26.94,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+26.91,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+27.41,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+26.12,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+26.14,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+26.55,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp_i','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+31.56,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp_i','OD1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+30.64,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp_i','OD2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+32.76,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp_i','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+32.12,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp_i','OD1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+31.16,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp_i','OD2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+33.31,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp_i','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+31.31,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp_i','OD1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+30.32,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp_i','OD2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+32.48,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CD1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.47,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CD2'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.62,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.44,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.33,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD2'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.59,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.57,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.45,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD2'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.39,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.57,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
IDSpec['S_2okb_3_6_1_23'] = cmd.select('S_2okb_3_6_1_23', 'asp|asp_i|leu|ser')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('leu')
cmd.delete('ser')
