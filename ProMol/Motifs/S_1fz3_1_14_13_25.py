'''
FUNC:S_1fz3_1_14_13_25
PDB:1fz3
EC:1.14.13.25
RESI:cys,thr
LOCI:a-151,213;
'''
IDSpec[(('cys','CA'),('rthr','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+15.34,resSelectionSubs('thr','CA',subs)))
IDSpec[(('cys','CA'),('rthr','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.62,resSelectionSubs('thr','CB',subs)))
IDSpec[(('cys','CA'),('rthr','OG1'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+15.45,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('cys','CB'),('rthr','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+14.37,resSelectionSubs('thr','CA',subs)))
IDSpec[(('cys','CB'),('rthr','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.59,resSelectionSubs('thr','CB',subs)))
IDSpec[(('cys','CB'),('rthr','OG1'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+14.44,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('cys','SG'),('rthr','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.66,resSelectionSubs('thr','CA',subs)))
IDSpec[(('cys','SG'),('rthr','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.89,resSelectionSubs('thr','CB',subs)))
IDSpec[(('cys','SG'),('rthr','OG1'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.74,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('thr','CA'),('scys','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+15.34,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('scys','CB'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+14.37,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('thr','CA'),('scys','SG'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.66,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('thr','CB'),('scys','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+14.62,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('scys','CB'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+13.59,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('thr','CB'),('scys','SG'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.89,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('thr','OG1'),('scys','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+15.45,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('scys','CB'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+14.44,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('thr','OG1'),('scys','SG'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.74,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
IDSpec['S_1fz3_1_14_13_25'] = cmd.select('S_1fz3_1_14_13_25', 'cys|thr')
cmd.delete('cys')
cmd.delete('thr')
