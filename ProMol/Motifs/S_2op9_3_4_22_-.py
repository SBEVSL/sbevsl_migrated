'''
FUNC:S_2op9_3_4_22_-
PDB:2op9
EC:3.4.22.-
RESI:his,cys
LOCI:a-41,145;
'''
IDSpec[(('cys','CA'),('rhis','CE1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.88,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CA'),('rhis','ND1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.12,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CA'),('rhis','NE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.77,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CB'),('rhis','CE1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.47,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CB'),('rhis','ND1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.73,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CB'),('rhis','NE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.25,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','SG'),('rhis','CE1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.22,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','SG'),('rhis','ND1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.55,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','SG'),('rhis','NE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.96,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('scys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.88,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.47,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.22,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.12,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.73,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.55,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.77,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.25,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.96,resSelectionSubs('cys','SG',subs,selection=True)))
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
IDSpec['S_2op9_3_4_22_-'] = cmd.select('S_2op9_3_4_22_-', 'cys|his')
cmd.delete('cys')
cmd.delete('his')
