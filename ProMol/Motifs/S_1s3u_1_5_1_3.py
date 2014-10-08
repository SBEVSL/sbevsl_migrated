'''
FUNC:S_1s3u_1_5_1_3
PDB:1s3u
EC:1.5.1.3
RESI:leu,glu
LOCI:a-22,30;
'''
IDSpec[(('leu','CD1'),('rglu','CD'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.31,resSelectionSubs('glu','CD',subs)))
IDSpec[(('leu','CD1'),('rglu','OE1'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+10.29,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('leu','CD1'),('rglu','OE2'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.30,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('leu','CD2'),('rglu','CD'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.61,resSelectionSubs('glu','CD',subs)))
IDSpec[(('leu','CD2'),('rglu','OE1'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+10.32,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('leu','CD2'),('rglu','OE2'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.56,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('leu','CG'),('rglu','CD'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+10.21,resSelectionSubs('glu','CD',subs)))
IDSpec[(('leu','CG'),('rglu','OE1'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+11.06,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('leu','CG'),('rglu','OE2'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.16,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('sleu','CD1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.31,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sleu','CD2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.61,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('glu','CD'),('sleu','CG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.21,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sleu','CD1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.29,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sleu','CD2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.32,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sleu','CG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.06,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sleu','CD1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.30,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sleu','CD2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.56,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sleu','CG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.16,resSelectionSubs('leu','CG',subs,selection=True)))
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
IDSpec['S_1s3u_1_5_1_3'] = cmd.select('S_1s3u_1_5_1_3', 'leu|glu')
cmd.delete('leu')
cmd.delete('glu')
