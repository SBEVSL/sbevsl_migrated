'''
FUNC:S_3ie7_2_7_1_-
PDB:3ie7
EC:2.7.1.-
RESI:gly,ala,gly,asp
LOCI:a-248,249,250,251;
'''
IDSpec[(('gly','CA'),('rala','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.81,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly','CA'),('rala','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.88,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly','CA'),('rala','CG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.88,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gly','N'),('rala','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.19,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly','N'),('rala','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.87,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly','N'),('rala','CG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.87,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gly','O'),('rala','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.74,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gly','O'),('rala','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.24,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gly','O'),('rala','CG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.24,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gly','CA'),('rasp','CG'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.42,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','CA'),('rasp','OD1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.26,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','CA'),('rasp','OD2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.95,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','N'),('rasp','CG'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.43,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','N'),('rasp','OD1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','N'),('rasp','OD2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.86,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','O'),('rasp','CG'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.31,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','O'),('rasp','OD1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.13,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','O'),('rasp','OD2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.45,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','CA'),('rgly','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.28,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','CA'),('rgly','N'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.23,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','CA'),('rgly','O'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.53,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','N'),('rgly','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.82,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','N'),('rgly','N'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.68,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','N'),('rgly','O'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.43,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','O'),('rgly','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.17,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','O'),('rgly','N'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.24,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','O'),('rgly','O'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.91,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('ala','CA'),('sgly','CA'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+5.81,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly','N'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.19,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ala','CA'),('sgly','O'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+4.74,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly','CA'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.88,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly','N'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.87,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ala','CB'),('sgly','O'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.24,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly','CA'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.24,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly','N'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.24,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('ala','CG'),('sgly','O'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.24,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('ala','CA'),('rasp','CG'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.47,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CA'),('rasp','OD1'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.95,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CA'),('rasp','OD2'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.70,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ala','CB'),('rasp','CG'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.78,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CB'),('rasp','OD1'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10.15,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CB'),('rasp','OD2'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.98,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ala','CG'),('rasp','CG'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.98,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CG'),('rasp','OD1'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.98,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CG'),('rasp','OD2'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.98,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ala','CA'),('rgly','CA'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+5.79,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ala','CA'),('rgly','N'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+4.43,resSelectionSubs('gly','N',subs)))
IDSpec[(('ala','CA'),('rgly','O'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.39,resSelectionSubs('gly','O',subs)))
IDSpec[(('ala','CB'),('rgly','CA'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.47,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ala','CB'),('rgly','N'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.16,resSelectionSubs('gly','N',subs)))
IDSpec[(('ala','CB'),('rgly','O'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.35,resSelectionSubs('gly','O',subs)))
IDSpec[(('ala','CG'),('rgly','CA'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.35,resSelectionSubs('gly','CA',subs)))
IDSpec[(('ala','CG'),('rgly','N'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.35,resSelectionSubs('gly','N',subs)))
IDSpec[(('ala','CG'),('rgly','O'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.35,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('asp','CG'),('sgly','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.42,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','N'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.43,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','O'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.31,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.26,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','N'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.10,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','O'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.13,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.95,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','N'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.86,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','O'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.45,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.47,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.78,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.78,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.95,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.15,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.15,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.70,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.98,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.98,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asp','CG'),('rgly','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.06,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','CG'),('rgly','N'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.22,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','CG'),('rgly','O'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.85,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD1'),('rgly','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.85,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD1'),('rgly','N'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.31,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD1'),('rgly','O'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.56,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD2'),('rgly','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.84,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD2'),('rgly','N'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.75,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD2'),('rgly','O'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.96,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('gly_i','CA'),('sgly','CA'))] = cmd.select('gly_i1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.28,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','N'))] = cmd.select('gly_i2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.82,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','O'))] = cmd.select('gly_i3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.17,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','CA'))] = cmd.select('gly_i4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.23,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','N'))] = cmd.select('gly_i5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.68,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','O'))] = cmd.select('gly_i6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.24,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','CA'))] = cmd.select('gly_i7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.53,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','N'))] = cmd.select('gly_i8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.43,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','O'))] = cmd.select('gly_i9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.91,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sala','CA'))] = cmd.select('gly_i10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.79,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sala','CB'))] = cmd.select('gly_i11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.47,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sala','CG'))] = cmd.select('gly_i12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.47,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('gly_i','N'),('sala','CA'))] = cmd.select('gly_i13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+4.43,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sala','CB'))] = cmd.select('gly_i14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.16,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('gly_i','N'),('sala','CG'))] = cmd.select('gly_i15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+5.16,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('gly_i','O'),('sala','CA'))] = cmd.select('gly_i16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.39,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sala','CB'))] = cmd.select('gly_i17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.35,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('gly_i','O'),('sala','CG'))] = cmd.select('gly_i18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.35,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sasp','CG'))] = cmd.select('gly_i19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.06,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sasp','OD1'))] = cmd.select('gly_i20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.85,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sasp','OD2'))] = cmd.select('gly_i21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.84,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasp','CG'))] = cmd.select('gly_i22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.22,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasp','OD1'))] = cmd.select('gly_i23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.31,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasp','OD2'))] = cmd.select('gly_i24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.75,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasp','CG'))] = cmd.select('gly_i25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.85,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasp','OD1'))] = cmd.select('gly_i26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.56,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasp','OD2'))] = cmd.select('gly_i27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.96,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_3ie7_2_7_1_-'] = cmd.select('S_3ie7_2_7_1_-', 'gly|ala|asp|gly_i')
cmd.delete('gly')
cmd.delete('ala')
cmd.delete('asp')
cmd.delete('gly_i')
