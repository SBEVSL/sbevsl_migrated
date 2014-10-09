'''
FUNC:S_2p9o_3_6_1_23
PDB:2p9o
EC:3.6.1.23
RESI:ser,trp,asp,asp
LOCI:a-89,93,105,107;
'''
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.54,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.43,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.67,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.31,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.25,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.44,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.18,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.00,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.22,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','CG'),('rtrp','CE2'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+39.70,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('asp','CG'),('rtrp','CZ2'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+40.58,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('asp','CG'),('rtrp','NE1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+40.01,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('asp','OD1'),('rtrp','CE2'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+38.60,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('asp','OD1'),('rtrp','CZ2'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+39.46,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('asp','OD1'),('rtrp','NE1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+38.91,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('asp','OD2'),('rtrp','CE2'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+40.70,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('asp','OD2'),('rtrp','CZ2'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+41.55,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('asp','OD2'),('rtrp','NE1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+41.03,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.13,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.57,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+32.41,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.12,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.57,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+31.44,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+32.19,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+32.60,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+33.47,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.54,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.31,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.18,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.43,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.25,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.67,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.22,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rtrp','CE2'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+34.97,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('asp_i','CG'),('rtrp','CZ2'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+35.75,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('asp_i','CG'),('rtrp','NE1'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+35.37,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('asp_i','OD1'),('rtrp','CE2'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+34.34,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('asp_i','OD1'),('rtrp','CZ2'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+35.10,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('asp_i','OD1'),('rtrp','NE1'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+34.78,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('asp_i','OD2'),('rtrp','CE2'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+35.43,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('asp_i','OD2'),('rtrp','CZ2'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+36.20,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('asp_i','OD2'),('rtrp','NE1'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+35.85,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('asp_i','CG'),('rser','CA'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+26.88,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp_i','CG'),('rser','CB'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+27.37,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp_i','CG'),('rser','OG'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.35,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp_i','OD1'),('rser','CA'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.30,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp_i','OD1'),('rser','CB'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.74,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp_i','OD1'),('rser','OG'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+27.75,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp_i','OD2'),('rser','CA'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.52,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp_i','OD2'),('rser','CB'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.06,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp_i','OD2'),('rser','OG'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+29.06,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('trp','CE2'),('sasp','CG'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+39.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('trp','CE2'),('sasp','OD1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+38.60,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('trp','CE2'),('sasp','OD2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+40.70,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sasp','CG'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+40.58,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sasp','OD1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+39.46,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sasp','OD2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+41.55,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sasp','CG'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+40.01,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('trp','NE1'),('sasp','OD1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+38.91,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sasp','OD2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+41.03,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('trp','CE2'),('sasp_i','CG'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+34.97,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('trp','CE2'),('sasp_i','OD1'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+34.34,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('trp','CE2'),('sasp_i','OD2'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+35.43,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sasp_i','CG'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+35.75,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sasp_i','OD1'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+35.10,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sasp_i','OD2'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+36.20,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sasp_i','CG'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+35.37,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('trp','NE1'),('sasp_i','OD1'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+34.78,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sasp_i','OD2'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+35.85,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('trp','CE2'),('rser','CA'))] = cmd.select('trp19', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.68,resSelectionSubs('ser','CA',subs)))
IDSpec[(('trp','CE2'),('rser','CB'))] = cmd.select('trp20', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.91,resSelectionSubs('ser','CB',subs)))
IDSpec[(('trp','CE2'),('rser','OG'))] = cmd.select('trp21', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.94,resSelectionSubs('ser','OG',subs)))
IDSpec[(('trp','CZ2'),('rser','CA'))] = cmd.select('trp22', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.86,resSelectionSubs('ser','CA',subs)))
IDSpec[(('trp','CZ2'),('rser','CB'))] = cmd.select('trp23', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+13.04,resSelectionSubs('ser','CB',subs)))
IDSpec[(('trp','CZ2'),('rser','OG'))] = cmd.select('trp24', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+13.15,resSelectionSubs('ser','OG',subs)))
IDSpec[(('trp','NE1'),('rser','CA'))] = cmd.select('trp25', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+11.64,resSelectionSubs('ser','CA',subs)))
IDSpec[(('trp','NE1'),('rser','CB'))] = cmd.select('trp26', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+11.88,resSelectionSubs('ser','CB',subs)))
IDSpec[(('trp','NE1'),('rser','OG'))] = cmd.select('trp27', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+11.74,resSelectionSubs('ser','OG',subs)))
IDSpec['trp'] = cmd.select('trp',' br. trp1&br. trp2&br. trp3&br. trp4&br. trp5&br. trp6&br. trp7&br. trp8&br. trp9&br. trp10&br. trp11&br. trp12&br. trp13&br. trp14&br. trp15&br. trp16&br. trp17&br. trp18&br. trp19&br. trp20&br. trp21&br. trp22&br. trp23&br. trp24&br. trp25&br. trp26&br. trp27')
IDSpec['r_trp'] = cmd.count_atoms(resSelectionSubs('trp', subs=subs, selection=True))
cmd.delete('trp1')
cmd.delete('trp2')
cmd.delete('trp3')
cmd.delete('trp4')
cmd.delete('trp5')
cmd.delete('trp6')
cmd.delete('trp7')
cmd.delete('trp8')
cmd.delete('trp9')
cmd.delete('trp10')
cmd.delete('trp11')
cmd.delete('trp12')
cmd.delete('trp13')
cmd.delete('trp14')
cmd.delete('trp15')
cmd.delete('trp16')
cmd.delete('trp17')
cmd.delete('trp18')
cmd.delete('trp19')
cmd.delete('trp20')
cmd.delete('trp21')
cmd.delete('trp22')
cmd.delete('trp23')
cmd.delete('trp24')
cmd.delete('trp25')
cmd.delete('trp26')
cmd.delete('trp27')
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+31.13,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+30.12,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+32.19,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+31.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+30.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+32.60,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+32.41,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+31.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+33.47,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp_i','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+26.88,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp_i','OD1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+26.30,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp_i','OD2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+27.52,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp_i','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+27.37,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp_i','OD1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+26.74,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp_i','OD2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+28.06,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp_i','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+28.35,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp_i','OD1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+27.75,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp_i','OD2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+29.06,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('strp','CE2'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.68,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('ser','CA'),('strp','CZ2'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.86,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('ser','CA'),('strp','NE1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.64,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('ser','CB'),('strp','CE2'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.91,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('ser','CB'),('strp','CZ2'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.04,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('ser','CB'),('strp','NE1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.88,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('ser','OG'),('strp','CE2'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.94,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('ser','OG'),('strp','CZ2'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.15,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('ser','OG'),('strp','NE1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.74,resSelectionSubs('trp','NE1',subs,selection=True)))
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
IDSpec['S_2p9o_3_6_1_23'] = cmd.select('S_2p9o_3_6_1_23', 'asp|asp_i|trp|ser')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('trp')
cmd.delete('ser')
