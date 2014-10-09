'''
FUNC:S_2gmj_1_5_5_1
PDB:2gmj
EC:1.5.5.1
RESI:thr,cys
LOCI:a-80,85;
'''
IDSpec[(('thr','CA'),('rcys','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+16.05,resSelectionSubs('cys','CA',subs)))
IDSpec[(('thr','CA'),('rcys','CB'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+17.05,resSelectionSubs('cys','CB',subs)))
IDSpec[(('thr','CA'),('rcys','SG'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+18.70,resSelectionSubs('cys','SG',subs)))
IDSpec[(('thr','CB'),('rcys','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+15.43,resSelectionSubs('cys','CA',subs)))
IDSpec[(('thr','CB'),('rcys','CB'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+16.54,resSelectionSubs('cys','CB',subs)))
IDSpec[(('thr','CB'),('rcys','SG'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+18.12,resSelectionSubs('cys','SG',subs)))
IDSpec[(('thr','OG1'),('rcys','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+16.31,resSelectionSubs('cys','CA',subs)))
IDSpec[(('thr','OG1'),('rcys','CB'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+17.47,resSelectionSubs('cys','CB',subs)))
IDSpec[(('thr','OG1'),('rcys','SG'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+18.98,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys','CA'),('sthr','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.05,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sthr','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+15.43,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('cys','CA'),('sthr','OG1'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.31,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('cys','CB'),('sthr','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+17.05,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sthr','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+16.54,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('cys','CB'),('sthr','OG1'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+17.47,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('cys','SG'),('sthr','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+18.70,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sthr','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+18.12,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('cys','SG'),('sthr','OG1'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+18.98,resSelectionSubs('thr','OG1',subs,selection=True)))
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
IDSpec['S_2gmj_1_5_5_1'] = cmd.select('S_2gmj_1_5_5_1', 'thr|cys')
cmd.delete('thr')
cmd.delete('cys')