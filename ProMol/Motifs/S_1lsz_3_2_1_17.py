'''
FUNC:S_1lsz_3_2_1_17
PDB:1lsz
EC:3.2.1.17
RESI:glu,ser
LOCI:a-35,52;
'''
IDSpec[(('glu','CD'),('rser','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.62,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','CD'),('rser','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.35,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','CD'),('rser','OG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.67,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE1'),('rser','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.66,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE1'),('rser','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.35,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE1'),('rser','OG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.70,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE2'),('rser','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.25,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE2'),('rser','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.93,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE2'),('rser','OG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.05,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('sglu','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.62,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.66,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.25,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.35,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.35,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.93,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.67,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.70,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.05,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
IDSpec['S_1lsz_3_2_1_17'] = cmd.select('S_1lsz_3_2_1_17', 'glu|ser')
cmd.delete('glu')
cmd.delete('ser')