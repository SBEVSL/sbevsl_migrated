'''
FUNC:S_1ggo_2_7_9_1
PDB:1ggo
EC:2.7.9.1
RESI:his,cys
LOCI:a-455,831;
'''
IDSpec[(('his','CE1'),('rcys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+37.12,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','CE1'),('rcys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+38.20,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','CE1'),('rcys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+39.50,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','ND1'),('rcys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+37.81,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','ND1'),('rcys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+38.90,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','ND1'),('rcys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+40.16,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','NE2'),('rcys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+37.62,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','NE2'),('rcys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+38.73,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','NE2'),('rcys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+40.04,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys','CA'),('shis','CE1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+37.12,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','ND1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+37.81,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','NE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+37.62,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','CE1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+38.20,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','ND1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+38.90,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','NE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+38.73,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','CE1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+39.50,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','ND1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+40.16,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','NE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+40.04,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9')
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
IDSpec['S_1ggo_2_7_9_1'] = cmd.select('S_1ggo_2_7_9_1', 'his|cys')
cmd.delete('his')
cmd.delete('cys')
