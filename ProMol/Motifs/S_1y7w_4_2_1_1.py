'''
FUNC:S_1y7w_4_2_1_1
PDB:1y7w
EC:4.2.1.1
RESI:glu,thr
LOCI:a-122,217;
'''
IDSpec[(('glu','CD'),('rthr','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.15,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','CD'),('rthr','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.74,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','CD'),('rthr','OG1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.32,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE1'),('rthr','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.58,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE1'),('rthr','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.10,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE1'),('rthr','OG1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+4.51,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE2'),('rthr','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.92,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE2'),('rthr','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.74,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE2'),('rthr','OG1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.39,resSelectionSubs('thr','OG1',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
IDSpec[(('thr','CA'),('sglu','CD'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.15,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.58,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.92,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','CD'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.74,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.10,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.74,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','CD'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.32,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+4.51,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.39,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_1y7w_4_2_1_1'] = cmd.select('S_1y7w_4_2_1_1', 'glu|thr')
cmd.delete('glu')
cmd.delete('thr')