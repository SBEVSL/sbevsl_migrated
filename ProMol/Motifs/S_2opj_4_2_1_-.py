'''
FUNC:S_2opj_4_2_1_-
PDB:2opj
EC:4.2.1.-
RESI:lys,ala,lys
LOCI:a-99,101,203;
'''
IDSpec[(('ala','CA'),('rlys','CD'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+19.37,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CA'),('rlys','CE'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+18.08,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CA'),('rlys','NZ'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+18.06,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CB'),('rlys','CD'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+18.92,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CB'),('rlys','CE'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+17.64,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CB'),('rlys','NZ'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+17.52,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CG'),('rlys','CD'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+17.52,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CG'),('rlys','CE'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+17.52,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CG'),('rlys','NZ'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+17.52,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CA'),('rlys_i','CD'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.68,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('ala','CA'),('rlys_i','CE'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.03,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('ala','CA'),('rlys_i','NZ'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.79,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('ala','CB'),('rlys_i','CD'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.10,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('ala','CB'),('rlys_i','CE'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.33,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('ala','CB'),('rlys_i','NZ'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.93,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('ala','CG'),('rlys_i','CD'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.93,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('ala','CG'),('rlys_i','CE'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.93,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('ala','CG'),('rlys_i','NZ'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.93,resSelectionSubs('lys_i','NZ',subs)))
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
IDSpec[(('lys','CD'),('sala','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+19.37,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sala','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.92,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sala','CG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.92,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.08,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.64,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.64,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.06,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.52,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.52,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.17,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.13,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.83,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.85,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.88,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.54,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.14,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.18,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.68,resSelectionSubs('lys_i','NZ',subs)))
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
IDSpec[(('lys_i','CD'),('sala','CA'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.68,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sala','CB'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.10,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sala','CG'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.10,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sala','CA'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.03,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sala','CB'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.33,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sala','CG'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.33,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sala','CA'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.79,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sala','CB'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.93,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sala','CG'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.93,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.17,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.85,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.14,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+14.13,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.88,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.18,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.83,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.54,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.68,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2opj_4_2_1_-'] = cmd.select('S_2opj_4_2_1_-', 'ala|lys|lys_i')
cmd.delete('ala')
cmd.delete('lys')
cmd.delete('lys_i')
