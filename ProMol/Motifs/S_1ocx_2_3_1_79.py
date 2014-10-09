'''
FUNC:S_1ocx_2_3_1_79
PDB:1ocx
EC:2.3.1.79
RESI:leu,thr
LOCI:a-89,110;
'''
IDSpec[(('thr','CA'),('rleu','CD1'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.35,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('thr','CA'),('rleu','CD2'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.42,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('thr','CA'),('rleu','CG'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.16,resSelectionSubs('leu','CG',subs)))
IDSpec[(('thr','CB'),('rleu','CD1'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.92,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('thr','CB'),('rleu','CD2'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.59,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('thr','CB'),('rleu','CG'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.52,resSelectionSubs('leu','CG',subs)))
IDSpec[(('thr','OG1'),('rleu','CD1'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.15,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('thr','OG1'),('rleu','CD2'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.62,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('thr','OG1'),('rleu','CG'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.70,resSelectionSubs('leu','CG',subs)))
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
IDSpec[(('leu','CD1'),('sthr','CA'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.35,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('leu','CD1'),('sthr','CB'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.92,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('leu','CD1'),('sthr','OG1'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.15,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('leu','CD2'),('sthr','CA'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+10.42,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('leu','CD2'),('sthr','CB'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+10.59,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('leu','CD2'),('sthr','OG1'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.62,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('leu','CG'),('sthr','CA'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.16,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('leu','CG'),('sthr','CB'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.52,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('leu','CG'),('sthr','OG1'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.70,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9')
IDSpec['r_leu'] = cmd.count_atoms(resSelectionSubs('leu', subs=subs, selection=True))
cmd.delete('leu1')
cmd.delete('leu2')
cmd.delete('leu3')
cmd.delete('leu4')
cmd.delete('leu5')
cmd.delete('leu6')
cmd.delete('leu7')
cmd.delete('leu8')
cmd.delete('leu9')
IDSpec['S_1ocx_2_3_1_79'] = cmd.select('S_1ocx_2_3_1_79', 'thr|leu')
cmd.delete('thr')
cmd.delete('leu')