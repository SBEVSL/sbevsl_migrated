'''
FUNC:S_3bc1_3_6_5_2
PDB:3bc1
EC:3.6.5.2
RESI:gly,leu
LOCI:a-19,78;
'''
IDSpec[(('leu','CD1'),('rgly','CA'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+10.87,resSelectionSubs('gly','CA',subs)))
IDSpec[(('leu','CD1'),('rgly','N'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.84,resSelectionSubs('gly','N',subs)))
IDSpec[(('leu','CD1'),('rgly','O'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+13.24,resSelectionSubs('gly','O',subs)))
IDSpec[(('leu','CD2'),('rgly','CA'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.81,resSelectionSubs('gly','CA',subs)))
IDSpec[(('leu','CD2'),('rgly','N'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.74,resSelectionSubs('gly','N',subs)))
IDSpec[(('leu','CD2'),('rgly','O'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+12.15,resSelectionSubs('gly','O',subs)))
IDSpec[(('leu','CG'),('rgly','CA'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+10.10,resSelectionSubs('gly','CA',subs)))
IDSpec[(('leu','CG'),('rgly','N'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.94,resSelectionSubs('gly','N',subs)))
IDSpec[(('leu','CG'),('rgly','O'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+12.48,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('gly','CA'),('sleu','CD1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.87,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('gly','CA'),('sleu','CD2'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.81,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('gly','CA'),('sleu','CG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.10,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('gly','N'),('sleu','CD1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.84,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('gly','N'),('sleu','CD2'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.74,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('gly','N'),('sleu','CG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.94,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('gly','O'),('sleu','CD1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.24,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('gly','O'),('sleu','CD2'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.15,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('gly','O'),('sleu','CG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.48,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
IDSpec['S_3bc1_3_6_5_2'] = cmd.select('S_3bc1_3_6_5_2', 'leu|gly')
cmd.delete('leu')
cmd.delete('gly')
