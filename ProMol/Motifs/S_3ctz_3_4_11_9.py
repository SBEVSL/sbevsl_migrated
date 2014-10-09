'''
FUNC:S_3ctz_3_4_11_9
PDB:3ctz
EC:3.4.11.9
RESI:his,pro,glu
LOCI:a-498,501,523;
'''
IDSpec[(('glu','CD'),('rpro','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+17.31,resSelectionSubs('pro','CA',subs)))
IDSpec[(('glu','CD'),('rpro','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+18.81,resSelectionSubs('pro','CB',subs)))
IDSpec[(('glu','CD'),('rpro','CD'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+18.50,resSelectionSubs('pro','CD',subs)))
IDSpec[(('glu','OE1'),('rpro','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+18.38,resSelectionSubs('pro','CA',subs)))
IDSpec[(('glu','OE1'),('rpro','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+19.89,resSelectionSubs('pro','CB',subs)))
IDSpec[(('glu','OE1'),('rpro','CD'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+19.58,resSelectionSubs('pro','CD',subs)))
IDSpec[(('glu','OE2'),('rpro','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.24,resSelectionSubs('pro','CA',subs)))
IDSpec[(('glu','OE2'),('rpro','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.75,resSelectionSubs('pro','CB',subs)))
IDSpec[(('glu','OE2'),('rpro','CD'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.38,resSelectionSubs('pro','CD',subs)))
IDSpec[(('glu','CD'),('rhis','CE1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.32,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','CD'),('rhis','ND1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.12,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','CD'),('rhis','NE2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.09,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis','CE1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.27,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis','ND1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.22,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis','NE2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.12,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis','CE1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.44,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis','ND1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.14,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis','NE2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.16,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('pro','CA'),('sglu','CD'))] = cmd.select('pro1', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+17.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('pro','CA'),('sglu','OE1'))] = cmd.select('pro2', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+18.38,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('pro','CA'),('sglu','OE2'))] = cmd.select('pro3', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+16.24,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('pro','CB'),('sglu','CD'))] = cmd.select('pro4', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+18.81,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('pro','CB'),('sglu','OE1'))] = cmd.select('pro5', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+19.89,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('pro','CB'),('sglu','OE2'))] = cmd.select('pro6', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+17.75,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('pro','CD'),('sglu','CD'))] = cmd.select('pro7', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+18.50,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('pro','CD'),('sglu','OE1'))] = cmd.select('pro8', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+19.58,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('pro','CD'),('sglu','OE2'))] = cmd.select('pro9', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+17.38,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('pro','CA'),('rhis','CE1'))] = cmd.select('pro10', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+15.98,resSelectionSubs('his','CE1',subs)))
IDSpec[(('pro','CA'),('rhis','ND1'))] = cmd.select('pro11', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+15.01,resSelectionSubs('his','ND1',subs)))
IDSpec[(('pro','CA'),('rhis','NE2'))] = cmd.select('pro12', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+15.55,resSelectionSubs('his','NE2',subs)))
IDSpec[(('pro','CB'),('rhis','CE1'))] = cmd.select('pro13', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+17.40,resSelectionSubs('his','CE1',subs)))
IDSpec[(('pro','CB'),('rhis','ND1'))] = cmd.select('pro14', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+16.40,resSelectionSubs('his','ND1',subs)))
IDSpec[(('pro','CB'),('rhis','NE2'))] = cmd.select('pro15', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+17.01,resSelectionSubs('his','NE2',subs)))
IDSpec[(('pro','CD'),('rhis','CE1'))] = cmd.select('pro16', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+16.89,resSelectionSubs('his','CE1',subs)))
IDSpec[(('pro','CD'),('rhis','ND1'))] = cmd.select('pro17', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+15.88,resSelectionSubs('his','ND1',subs)))
IDSpec[(('pro','CD'),('rhis','NE2'))] = cmd.select('pro18', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+16.48,resSelectionSubs('his','NE2',subs)))
IDSpec['pro'] = cmd.select('pro',' br. pro1&br. pro2&br. pro3&br. pro4&br. pro5&br. pro6&br. pro7&br. pro8&br. pro9&br. pro10&br. pro11&br. pro12&br. pro13&br. pro14&br. pro15&br. pro16&br. pro17&br. pro18')
IDSpec['r_pro'] = cmd.count_atoms(resSelectionSubs('pro', subs=subs, selection=True))
cmd.delete('pro1')
cmd.delete('pro2')
cmd.delete('pro3')
cmd.delete('pro4')
cmd.delete('pro5')
cmd.delete('pro6')
cmd.delete('pro7')
cmd.delete('pro8')
cmd.delete('pro9')
cmd.delete('pro10')
cmd.delete('pro11')
cmd.delete('pro12')
cmd.delete('pro13')
cmd.delete('pro14')
cmd.delete('pro15')
cmd.delete('pro16')
cmd.delete('pro17')
cmd.delete('pro18')
IDSpec[(('his','CE1'),('sglu','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.32,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.27,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.44,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.12,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.22,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.14,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.09,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.12,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.16,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','CE1'),('spro','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.98,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('spro','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+17.40,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('spro','CD'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.89,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('spro','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.01,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('spro','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+16.40,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('spro','CD'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.88,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('spro','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.55,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('spro','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+17.01,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('spro','CD'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.48,resSelectionSubs('pro','CD',subs,selection=True)))
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
IDSpec['S_3ctz_3_4_11_9'] = cmd.select('S_3ctz_3_4_11_9', 'glu|pro|his')
cmd.delete('glu')
cmd.delete('pro')
cmd.delete('his')