'''
FUNC:S_2quh_6_1_1_2
PDB:2quh
EC:6.1.1.2
RESI:lys,ala
LOCI:a-349,352;
'''
IDSpec[(('ala','CA'),('rlys','CD'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CA'),('rlys','CE'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CA'),('rlys','NZ'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CB'),('rlys','CD'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CB'),('rlys','CE'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CB'),('rlys','NZ'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CG'),('rlys','CD'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CG'),('rlys','CE'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CG'),('rlys','NZ'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sala','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sala','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sala','CG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('ala','CG',subs,selection=True)))
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
IDSpec['S_2quh_6_1_1_2'] = cmd.select('S_2quh_6_1_1_2', 'ala|lys')
cmd.delete('ala')
cmd.delete('lys')