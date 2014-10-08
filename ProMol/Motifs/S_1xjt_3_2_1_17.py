'''
FUNC:S_1xjt_3_2_1_17
PDB:1xjt
EC:3.2.1.17
RESI:glu,cys
LOCI:a-42,51;
'''
IDSpec[(('glu','CD'),('rcys','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.89,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','CD'),('rcys','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.52,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','CD'),('rcys','SG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.19,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE1'),('rcys','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.72,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE1'),('rcys','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.39,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE1'),('rcys','SG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.99,resSelectionSubs('cys','SG',subs)))
IDSpec[(('glu','OE2'),('rcys','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.25,resSelectionSubs('cys','CA',subs)))
IDSpec[(('glu','OE2'),('rcys','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.81,resSelectionSubs('cys','CB',subs)))
IDSpec[(('glu','OE2'),('rcys','SG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.64,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys','CA'),('sglu','CD'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.89,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.72,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CA'),('sglu','OE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.25,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','CD'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.52,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.39,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','CB'),('sglu','OE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.81,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','CD'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.19,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.99,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('cys','SG'),('sglu','OE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.64,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_1xjt_3_2_1_17'] = cmd.select('S_1xjt_3_2_1_17', 'glu|cys')
cmd.delete('glu')
cmd.delete('cys')
