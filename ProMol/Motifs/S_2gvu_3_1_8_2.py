'''
FUNC:S_2gvu_3_1_8_2
PDB:2gvu
EC:3.1.8.2
RESI:glu,his
LOCI:a-37,287;
'''
IDSpec[(('his','CE1'),('rglu','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.81,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','CE1'),('rglu','OE1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.69,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','CE1'),('rglu','OE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.59,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('his','ND1'),('rglu','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.83,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','ND1'),('rglu','OE1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.50,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','ND1'),('rglu','OE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.60,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('his','NE2'),('rglu','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.96,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','NE2'),('rglu','OE1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.91,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','NE2'),('rglu','OE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.75,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('shis','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.81,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','ND1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.83,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','NE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.96,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.69,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','ND1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.50,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','NE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.91,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.59,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','ND1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.60,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','NE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.75,resSelectionSubs('his','NE2',subs,selection=True)))
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
IDSpec['S_2gvu_3_1_8_2'] = cmd.select('S_2gvu_3_1_8_2', 'his|glu')
cmd.delete('his')
cmd.delete('glu')
