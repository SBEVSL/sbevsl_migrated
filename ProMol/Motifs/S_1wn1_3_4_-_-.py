'''
FUNC:S_1wn1_3_4_-_-
PDB:1wn1
EC:3.4.-.-
RESI:his,glu
LOCI:a-297,319;
'''
IDSpec[(('glu','CD'),('rhis','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.39,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','CD'),('rhis','ND1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.26,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','CD'),('rhis','NE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.21,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis','ND1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.31,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis','NE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.20,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.59,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis','ND1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.35,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis','NE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.35,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('sglu','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.39,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.31,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.59,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.26,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.31,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.35,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.21,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.20,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.35,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
IDSpec['S_1wn1_3_4_-_-'] = cmd.select('S_1wn1_3_4_-_-', 'glu|his')
cmd.delete('glu')
cmd.delete('his')
