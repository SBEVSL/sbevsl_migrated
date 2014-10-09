'''
FUNC:S_1gkf_3_5_1_11
PDB:1gkf
EC:3.5.1.11
RESI:ser,ala,ala
LOCI:b-1,69,241;
'''
IDSpec[(('ala','CA'),('rser','CA'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.12,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ala','CA'),('rser','CB'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.25,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ala','CA'),('rser','OG'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.21,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ala','CB'),('rser','CA'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.73,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ala','CB'),('rser','CB'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.98,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ala','CB'),('rser','OG'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.71,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ala','CG'),('rser','CA'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.71,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ala','CG'),('rser','CB'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.71,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ala','CG'),('rser','OG'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.71,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ala','CA'),('rala','CA'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.54,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ala','CA'),('rala','CB'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.58,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ala','CA'),('rala','CG'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.58,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ala','CB'),('rala','CA'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.56,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ala','CB'),('rala','CB'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.25,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ala','CB'),('rala','CG'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.25,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ala','CG'),('rala','CA'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ala','CG'),('rala','CB'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ala','CG'),('rala','CG'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('ala','CG',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18')
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
IDSpec[(('ser','CA'),('sala','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.12,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('sala','CB'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.73,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('sala','CG'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.73,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sala','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.25,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('sala','CB'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.98,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('sala','CG'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.98,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sala','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.21,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('sala','CB'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.71,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('sala','CG'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.71,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('rala','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.79,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CA'),('rala','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.66,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CA'),('rala','CG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.66,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','CB'),('rala','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.51,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CB'),('rala','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.52,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CB'),('rala','CG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.52,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','OG'),('rala','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.51,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','OG'),('rala','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.24,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','OG'),('rala','CG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.24,resSelectionSubs('ala','CG',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18')
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
IDSpec[(('ala_i','CA'),('sala','CA'))] = cmd.select('ala_i1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.54,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('ala_i','CA'),('sala','CB'))] = cmd.select('ala_i2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.56,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('ala_i','CA'),('sala','CG'))] = cmd.select('ala_i3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.56,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('ala_i','CB'),('sala','CA'))] = cmd.select('ala_i4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.58,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('ala_i','CB'),('sala','CB'))] = cmd.select('ala_i5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.25,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('ala_i','CB'),('sala','CG'))] = cmd.select('ala_i6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.25,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('ala_i','CG'),('sala','CA'))] = cmd.select('ala_i7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('ala_i','CG'),('sala','CB'))] = cmd.select('ala_i8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('ala_i','CG'),('sala','CG'))] = cmd.select('ala_i9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.25,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('ala_i','CA'),('sser','CA'))] = cmd.select('ala_i10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.79,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala_i','CA'),('sser','CB'))] = cmd.select('ala_i11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.51,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala_i','CA'),('sser','OG'))] = cmd.select('ala_i12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.51,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala_i','CB'),('sser','CA'))] = cmd.select('ala_i13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.66,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala_i','CB'),('sser','CB'))] = cmd.select('ala_i14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.52,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala_i','CB'),('sser','OG'))] = cmd.select('ala_i15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.24,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala_i','CG'),('sser','CA'))] = cmd.select('ala_i16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.24,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala_i','CG'),('sser','CB'))] = cmd.select('ala_i17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.24,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala_i','CG'),('sser','OG'))] = cmd.select('ala_i18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.24,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec['ala_i'] = cmd.select('ala_i',' br. ala_i1&br. ala_i2&br. ala_i3&br. ala_i4&br. ala_i5&br. ala_i6&br. ala_i7&br. ala_i8&br. ala_i9&br. ala_i10&br. ala_i11&br. ala_i12&br. ala_i13&br. ala_i14&br. ala_i15&br. ala_i16&br. ala_i17&br. ala_i18')
IDSpec['r_ala_i'] = cmd.count_atoms(resSelectionSubs('ala_i', subs=subs, selection=True))
cmd.delete('ala_i1')
cmd.delete('ala_i2')
cmd.delete('ala_i3')
cmd.delete('ala_i4')
cmd.delete('ala_i5')
cmd.delete('ala_i6')
cmd.delete('ala_i7')
cmd.delete('ala_i8')
cmd.delete('ala_i9')
cmd.delete('ala_i10')
cmd.delete('ala_i11')
cmd.delete('ala_i12')
cmd.delete('ala_i13')
cmd.delete('ala_i14')
cmd.delete('ala_i15')
cmd.delete('ala_i16')
cmd.delete('ala_i17')
cmd.delete('ala_i18')
IDSpec['S_1gkf_3_5_1_11'] = cmd.select('S_1gkf_3_5_1_11', 'ala|ser|ala_i')
cmd.delete('ala')
cmd.delete('ser')
cmd.delete('ala_i')
