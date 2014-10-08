'''
FUNC:S_2b94_2_4_2_1
PDB:2b94
EC:2.4.2.1
RESI:asp,cys
LOCI:a-203,205;
'''
IDSpec[(('asp','CG'),('rcys','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.79,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','CG'),('rcys','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.00,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','CG'),('rcys','SG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.23,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD1'),('rcys','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.63,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD1'),('rcys','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.89,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD1'),('rcys','SG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.19,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD2'),('rcys','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.77,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD2'),('rcys','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.05,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD2'),('rcys','SG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.37,resSelectionSubs('cys','SG',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9')
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
IDSpec[(('cys','CA'),('sasp','CG'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.79,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.63,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.77,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','CG'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.89,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.05,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','CG'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.23,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.19,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.37,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_2b94_2_4_2_1'] = cmd.select('S_2b94_2_4_2_1', 'asp|cys')
cmd.delete('asp')
cmd.delete('cys')
