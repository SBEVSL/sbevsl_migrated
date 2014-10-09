'''
FUNC:S_1nzf_2_4_1_27
PDB:1nzf
EC:2.4.1.27
RESI:glu,ala
LOCI:a-22,100;
'''
IDSpec[(('glu','CD'),('rala','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.91,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','CD'),('rala','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.61,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','CD'),('rala','CG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.61,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE1'),('rala','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.84,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE1'),('rala','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.61,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE1'),('rala','CG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.61,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE2'),('rala','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.01,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE2'),('rala','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.67,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE2'),('rala','CG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.67,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('ala','CA'),('sglu','CD'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.91,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.84,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','CD'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.61,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.61,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.67,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','CD'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.67,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.67,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.67,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_1nzf_2_4_1_27'] = cmd.select('S_1nzf_2_4_1_27', 'glu|ala')
cmd.delete('glu')
cmd.delete('ala')