'''
FUNC:S_1axe_1_1_1_1
PDB:1axe
EC:1.1.1.1
RESI:ser,his,leu
LOCI:a-48,51,57;
'''
IDSpec[(('leu','CD1'),('rser','CA'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.98,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD1'),('rser','CB'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.61,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD1'),('rser','OG'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.99,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CD2'),('rser','CA'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.14,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD2'),('rser','CB'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.82,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD2'),('rser','OG'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.60,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CG'),('rser','CA'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.24,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CG'),('rser','CB'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.08,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CG'),('rser','OG'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.74,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CD1'),('rhis','CE1'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+10.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('leu','CD1'),('rhis','ND1'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.71,resSelectionSubs('his','ND1',subs)))
IDSpec[(('leu','CD1'),('rhis','NE2'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.61,resSelectionSubs('his','NE2',subs)))
IDSpec[(('leu','CD2'),('rhis','CE1'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.74,resSelectionSubs('his','CE1',subs)))
IDSpec[(('leu','CD2'),('rhis','ND1'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('leu','CD2'),('rhis','NE2'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.08,resSelectionSubs('his','NE2',subs)))
IDSpec[(('leu','CG'),('rhis','CE1'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.87,resSelectionSubs('his','CE1',subs)))
IDSpec[(('leu','CG'),('rhis','ND1'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.09,resSelectionSubs('his','ND1',subs)))
IDSpec[(('leu','CG'),('rhis','NE2'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.32,resSelectionSubs('his','NE2',subs)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18')
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
cmd.delete('leu10')
cmd.delete('leu11')
cmd.delete('leu12')
cmd.delete('leu13')
cmd.delete('leu14')
cmd.delete('leu15')
cmd.delete('leu16')
cmd.delete('leu17')
cmd.delete('leu18')
IDSpec[(('ser','CA'),('sleu','CD1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.98,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CD2'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.14,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CG'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.24,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.61,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD2'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.82,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CG'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.08,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.99,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD2'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.60,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CG'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.74,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.25,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.00,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.30,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.16,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.42,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.13,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.27,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.06,resSelectionSubs('his','NE2',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18')
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
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
IDSpec[(('his','CE1'),('sleu','CD1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.31,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sleu','CD2'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.74,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('his','CE1'),('sleu','CG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.87,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sleu','CD1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.71,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sleu','CD2'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.03,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sleu','CG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.09,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sleu','CD1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.61,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sleu','CD2'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.08,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sleu','CG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.32,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.25,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.30,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.13,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.00,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.16,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.27,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.60,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.42,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.06,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_1axe_1_1_1_1'] = cmd.select('S_1axe_1_1_1_1', 'leu|ser|his')
cmd.delete('leu')
cmd.delete('ser')
cmd.delete('his')
