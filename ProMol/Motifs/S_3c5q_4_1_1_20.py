'''
FUNC:S_3c5q_4_1_1_20
PDB:3c5q
EC:4.1.1.20
RESI:lys,his,glu
LOCI:a-46,185,259;
'''
IDSpec[(('glu','CD'),('rhis','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.79,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','CD'),('rhis','ND1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.98,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','CD'),('rhis','NE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.61,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.70,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis','ND1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.89,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis','NE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.44,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.88,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis','ND1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.01,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis','NE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.62,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.71,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.01,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.74,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.97,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.28,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.14,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.43,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.58,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.27,resSelectionSubs('lys','NZ',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18')
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
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
IDSpec[(('his','CE1'),('sglu','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.79,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.70,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.88,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.98,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.89,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.61,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.44,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.62,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','CE1'),('rlys','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.22,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','CE1'),('rlys','CE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.38,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','CE1'),('rlys','NZ'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.22,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','ND1'),('rlys','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.88,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','ND1'),('rlys','CE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.81,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','ND1'),('rlys','NZ'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.48,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','NE2'),('rlys','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.98,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','NE2'),('rlys','CE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.12,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','NE2'),('rlys','NZ'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.20,resSelectionSubs('lys','NZ',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
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
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
IDSpec[(('lys','CD'),('sglu','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.71,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.97,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.43,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.01,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.28,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.58,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.74,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.14,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.27,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CD'),('shis','CE1'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.22,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('shis','ND1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.88,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','CD'),('shis','NE2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.98,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','CE1'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.38,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','ND1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.81,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','NE2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.12,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','CE1'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.22,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','ND1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.48,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','NE2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.20,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec['S_3c5q_4_1_1_20'] = cmd.select('S_3c5q_4_1_1_20', 'glu|his|lys')
cmd.delete('glu')
cmd.delete('his')
cmd.delete('lys')