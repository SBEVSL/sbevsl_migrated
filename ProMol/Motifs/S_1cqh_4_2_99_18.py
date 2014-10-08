'''
FUNC:S_1cqh_4_2_99_18
PDB:1cqh
EC:4.2.99.18
RESI:cys,ala
LOCI:a-32,35;
'''
IDSpec[(('ala','CA'),('rcys','CA'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.49,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ala','CA'),('rcys','CB'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.89,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ala','CA'),('rcys','SG'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.01,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ala','CB'),('rcys','CA'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.91,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ala','CB'),('rcys','CB'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.02,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ala','CB'),('rcys','SG'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.40,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ala','CG'),('rcys','CA'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.40,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ala','CG'),('rcys','CB'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.40,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ala','CG'),('rcys','SG'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.40,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys','CA'),('sala','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.49,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sala','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.91,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('cys','CA'),('sala','CG'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.91,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sala','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.89,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sala','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.02,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('cys','CB'),('sala','CG'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.02,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sala','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.01,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sala','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.40,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('cys','SG'),('sala','CG'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.40,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9')
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
IDSpec['S_1cqh_4_2_99_18'] = cmd.select('S_1cqh_4_2_99_18', 'ala|cys')
cmd.delete('ala')
cmd.delete('cys')
