'''
FUNC:S_2ixb_3_2_1_49
PDB:2ixb
EC:3.2.1.49
RESI:his,pro
LOCI:a-181,185;
'''
IDSpec[(('his','CE1'),('rpro','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.42,resSelectionSubs('pro','CA',subs)))
IDSpec[(('his','CE1'),('rpro','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.05,resSelectionSubs('pro','CB',subs)))
IDSpec[(('his','CE1'),('rpro','CD'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.12,resSelectionSubs('pro','CD',subs)))
IDSpec[(('his','ND1'),('rpro','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.07,resSelectionSubs('pro','CA',subs)))
IDSpec[(('his','ND1'),('rpro','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.83,resSelectionSubs('pro','CB',subs)))
IDSpec[(('his','ND1'),('rpro','CD'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.64,resSelectionSubs('pro','CD',subs)))
IDSpec[(('his','NE2'),('rpro','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.89,resSelectionSubs('pro','CA',subs)))
IDSpec[(('his','NE2'),('rpro','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.37,resSelectionSubs('pro','CB',subs)))
IDSpec[(('his','NE2'),('rpro','CD'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.38,resSelectionSubs('pro','CD',subs)))
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
IDSpec[(('pro','CA'),('shis','CE1'))] = cmd.select('pro1', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+11.42,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('pro','CA'),('shis','ND1'))] = cmd.select('pro2', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+12.07,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('pro','CA'),('shis','NE2'))] = cmd.select('pro3', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+10.89,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('pro','CB'),('shis','CE1'))] = cmd.select('pro4', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+11.05,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('pro','CB'),('shis','ND1'))] = cmd.select('pro5', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+11.83,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('pro','CB'),('shis','NE2'))] = cmd.select('pro6', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+10.37,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('pro','CD'),('shis','CE1'))] = cmd.select('pro7', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+10.12,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('pro','CD'),('shis','ND1'))] = cmd.select('pro8', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+10.64,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('pro','CD'),('shis','NE2'))] = cmd.select('pro9', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+9.38,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['pro'] = cmd.select('pro',' br. pro1&br. pro2&br. pro3&br. pro4&br. pro5&br. pro6&br. pro7&br. pro8&br. pro9')
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
IDSpec['S_2ixb_3_2_1_49'] = cmd.select('S_2ixb_3_2_1_49', 'his|pro')
cmd.delete('his')
cmd.delete('pro')
