'''
FUNC:S_3foc_6_1_1_2
PDB:3foc
EC:6.1.1.2
RESI:lys,ala
LOCI:a-311,314;
'''
IDSpec[(('lys','CD'),('rala','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.56,resSelectionSubs('ala','CA',subs)))
IDSpec[(('lys','CD'),('rala','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.09,resSelectionSubs('ala','CB',subs)))
IDSpec[(('lys','CD'),('rala','CG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.09,resSelectionSubs('ala','CG',subs)))
IDSpec[(('lys','CE'),('rala','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+14.82,resSelectionSubs('ala','CA',subs)))
IDSpec[(('lys','CE'),('rala','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.26,resSelectionSubs('ala','CB',subs)))
IDSpec[(('lys','CE'),('rala','CG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.26,resSelectionSubs('ala','CG',subs)))
IDSpec[(('lys','NZ'),('rala','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.37,resSelectionSubs('ala','CA',subs)))
IDSpec[(('lys','NZ'),('rala','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.70,resSelectionSubs('ala','CB',subs)))
IDSpec[(('lys','NZ'),('rala','CG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.70,resSelectionSubs('ala','CG',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9')
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
IDSpec[(('ala','CA'),('slys','CD'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+13.56,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ala','CA'),('slys','CE'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+14.82,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ala','CA'),('slys','NZ'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+15.37,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ala','CB'),('slys','CD'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+14.09,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ala','CB'),('slys','CE'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+15.26,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ala','CB'),('slys','NZ'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+15.70,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ala','CG'),('slys','CD'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+15.70,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ala','CG'),('slys','CE'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+15.70,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ala','CG'),('slys','NZ'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+15.70,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9')
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
IDSpec['S_3foc_6_1_1_2'] = cmd.select('S_3foc_6_1_1_2', 'lys|ala')
cmd.delete('lys')
cmd.delete('ala')
