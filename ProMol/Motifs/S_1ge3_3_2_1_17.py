'''
FUNC:S_1ge3_3_2_1_17
PDB:1ge3
EC:3.2.1.17
RESI:glu,asp
LOCI:a-35,53;
'''
IDSpec[(('glu','CD'),('rasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.26,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','CD'),('rasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.54,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','CD'),('rasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.25,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE1'),('rasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.22,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE1'),('rasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.64,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE1'),('rasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.14,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE2'),('rasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.73,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE2'),('rasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.87,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE2'),('rasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.70,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('sglu','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.26,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.22,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.73,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.54,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.64,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.87,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.25,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.14,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.70,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_1ge3_3_2_1_17'] = cmd.select('S_1ge3_3_2_1_17', 'glu|asp')
cmd.delete('glu')
cmd.delete('asp')
