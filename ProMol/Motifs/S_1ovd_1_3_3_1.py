'''
FUNC:S_1ovd_1_3_3_1
PDB:1ovd
EC:1.3.3.1
RESI:lys,cys
LOCI:a-43,130;
'''
IDSpec[(('lys','CD'),('rcys','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.33,resSelectionSubs('cys','CA',subs)))
IDSpec[(('lys','CD'),('rcys','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.51,resSelectionSubs('cys','CB',subs)))
IDSpec[(('lys','CD'),('rcys','SG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.00,resSelectionSubs('cys','SG',subs)))
IDSpec[(('lys','CE'),('rcys','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.34,resSelectionSubs('cys','CA',subs)))
IDSpec[(('lys','CE'),('rcys','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.41,resSelectionSubs('cys','CB',subs)))
IDSpec[(('lys','CE'),('rcys','SG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.75,resSelectionSubs('cys','SG',subs)))
IDSpec[(('lys','NZ'),('rcys','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.49,resSelectionSubs('cys','CA',subs)))
IDSpec[(('lys','NZ'),('rcys','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.71,resSelectionSubs('cys','CB',subs)))
IDSpec[(('lys','NZ'),('rcys','SG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.94,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys','CA'),('slys','CD'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.33,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('cys','CA'),('slys','CE'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.34,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('cys','CA'),('slys','NZ'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.49,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('cys','CB'),('slys','CD'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.51,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('cys','CB'),('slys','CE'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.41,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('cys','CB'),('slys','NZ'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.71,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('cys','SG'),('slys','CD'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.00,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('cys','SG'),('slys','CE'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.75,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('cys','SG'),('slys','NZ'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.94,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_1ovd_1_3_3_1'] = cmd.select('S_1ovd_1_3_3_1', 'lys|cys')
cmd.delete('lys')
cmd.delete('cys')
