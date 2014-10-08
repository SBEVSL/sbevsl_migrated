'''
FUNC:S_1phz_1_14_16_1
PDB:1phz
EC:1.14.16.1
RESI:his,ser
LOCI:a-285,349;
'''
IDSpec[(('his','CE1'),('rser','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.71,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','CE1'),('rser','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.49,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','CE1'),('rser','OG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.36,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','ND1'),('rser','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.84,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','ND1'),('rser','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.56,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','ND1'),('rser','OG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.43,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','NE2'),('rser','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.59,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','NE2'),('rser','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.25,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','NE2'),('rser','OG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.29,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('shis','CE1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.71,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','ND1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','NE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.59,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','CE1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.49,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','ND1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.56,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','NE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.25,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','CE1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.36,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','ND1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.43,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','NE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.29,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9')
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
IDSpec['S_1phz_1_14_16_1'] = cmd.select('S_1phz_1_14_16_1', 'his|ser')
cmd.delete('his')
cmd.delete('ser')
