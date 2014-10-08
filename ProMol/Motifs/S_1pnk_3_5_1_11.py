'''
FUNC:S_1pnk_3_5_1_11
PDB:1pnk
EC:3.5.1.11
RESI:ser,ala,asn
LOCI:b-1,69,241;
'''
IDSpec[(('asn','CG'),('rser','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.60,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','CG'),('rser','CB'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.74,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','CG'),('rser','OG'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.21,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','ND2'),('rser','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.32,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','ND2'),('rser','CB'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.04,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','ND2'),('rser','OG'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.51,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','OD1'),('rser','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.12,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','OD1'),('rser','CB'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.57,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','OD1'),('rser','OG'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.91,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','CG'),('rala','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.97,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asn','CG'),('rala','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.54,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asn','CG'),('rala','CG'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.54,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asn','ND2'),('rala','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.81,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asn','ND2'),('rala','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.60,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asn','ND2'),('rala','CG'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.60,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asn','OD1'),('rala','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.76,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asn','OD1'),('rala','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.09,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asn','OD1'),('rala','CG'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.09,resSelectionSubs('ala','CG',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18')
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
IDSpec[(('ser','CA'),('sasn','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.60,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','ND2'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.32,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','OD1'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.12,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.74,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','ND2'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.04,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','OD1'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.57,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.21,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','ND2'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.51,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','OD1'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.91,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('rala','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.76,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CA'),('rala','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.44,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CA'),('rala','CG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.44,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','CB'),('rala','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.63,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CB'),('rala','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.45,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CB'),('rala','CG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.45,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','OG'),('rala','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.52,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','OG'),('rala','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.09,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','OG'),('rala','CG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.09,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('ala','CA'),('sasn','CG'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.97,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ala','CA'),('sasn','ND2'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+5.81,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ala','CA'),('sasn','OD1'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.76,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ala','CB'),('sasn','CG'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.54,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ala','CB'),('sasn','ND2'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.60,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ala','CB'),('sasn','OD1'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.09,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ala','CG'),('sasn','CG'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.09,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ala','CG'),('sasn','ND2'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.09,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ala','CG'),('sasn','OD1'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.09,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','CA'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','CB'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.63,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','OG'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.52,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','CA'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.44,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','CB'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.45,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','OG'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.09,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','CA'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.09,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','CB'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.09,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','OG'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.09,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_1pnk_3_5_1_11'] = cmd.select('S_1pnk_3_5_1_11', 'asn|ser|ala')
cmd.delete('asn')
cmd.delete('ser')
cmd.delete('ala')
