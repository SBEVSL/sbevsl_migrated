'''
FUNC:S_1s1m_6_3_4_2
PDB:1s1m
EC:6.3.4.2
RESI:cys,his,glu
LOCI:a-379,515,517;
'''
IDSpec[(('cys','CA'),('rhis','CE1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.59,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CA'),('rhis','ND1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.24,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CA'),('rhis','NE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.41,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CB'),('rhis','CE1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.29,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CB'),('rhis','ND1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.13,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CB'),('rhis','NE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.09,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','SG'),('rhis','CE1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.69,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','SG'),('rhis','ND1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.71,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','SG'),('rhis','NE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.03,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CA'),('rglu','CD'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.64,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CA'),('rglu','OE1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.20,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CA'),('rglu','OE2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.03,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','CB'),('rglu','CD'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.94,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CB'),('rglu','OE1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.67,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CB'),('rglu','OE2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.16,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','SG'),('rglu','CD'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','SG'),('rglu','OE1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.70,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','SG'),('rglu','OE2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.09,resSelectionSubs('glu','OE2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18')
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
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
IDSpec[(('his','CE1'),('scys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.59,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.29,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.69,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.24,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.13,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.71,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.41,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.09,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.03,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','CE1'),('rglu','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.82,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','CE1'),('rglu','OE1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.07,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','CE1'),('rglu','OE2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.76,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('his','ND1'),('rglu','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.56,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','ND1'),('rglu','OE1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.80,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','ND1'),('rglu','OE2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.61,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('his','NE2'),('rglu','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.69,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','NE2'),('rglu','OE1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.77,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','NE2'),('rglu','OE2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.78,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('scys','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.64,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('scys','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.94,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('scys','SG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.92,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.20,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.67,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','SG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.70,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.03,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.16,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','SG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.09,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','CE1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.82,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','ND1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.56,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','NE2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.69,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','CE1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.07,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','ND1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.80,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','NE2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.77,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','CE1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.76,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','ND1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.61,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','NE2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.78,resSelectionSubs('his','NE2',subs,selection=True)))
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
IDSpec['S_1s1m_6_3_4_2'] = cmd.select('S_1s1m_6_3_4_2', 'cys|his|glu')
cmd.delete('cys')
cmd.delete('his')
cmd.delete('glu')
