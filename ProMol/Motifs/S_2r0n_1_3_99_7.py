'''
FUNC:S_2r0n_1_3_99_7
PDB:2r0n
EC:1.3.99.7
RESI:ala,glu
LOCI:a-249,370;
'''
IDSpec[(('ala','CA'),('rglu','CD'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.18,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ala','CA'),('rglu','OE1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.75,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ala','CA'),('rglu','OE2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.40,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ala','CB'),('rglu','CD'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.05,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ala','CB'),('rglu','OE1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.46,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ala','CB'),('rglu','OE2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.29,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ala','CG'),('rglu','CD'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.29,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ala','CG'),('rglu','OE1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.29,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ala','CG'),('rglu','OE2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+6.29,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('sala','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.18,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sala','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.05,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sala','CG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.05,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sala','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.75,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sala','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.46,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sala','CG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.46,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sala','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.40,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sala','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.29,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sala','CG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.29,resSelectionSubs('ala','CG',subs,selection=True)))
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
IDSpec['S_2r0n_1_3_99_7'] = cmd.select('S_2r0n_1_3_99_7', 'ala|glu')
cmd.delete('ala')
cmd.delete('glu')
