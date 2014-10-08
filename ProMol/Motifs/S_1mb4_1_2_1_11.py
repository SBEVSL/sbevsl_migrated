'''
FUNC:S_1mb4_1_2_1_11
PDB:1mb4
EC:1.2.1.11
RESI:cys,gln,his
LOCI:a-134,161,274;
'''
IDSpec[(('his','CE1'),('rcys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.87,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','CE1'),('rcys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.72,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','CE1'),('rcys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.32,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','ND1'),('rcys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.22,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','ND1'),('rcys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.19,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','ND1'),('rcys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.98,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','NE2'),('rcys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.68,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','NE2'),('rcys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.61,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','NE2'),('rcys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.09,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','CE1'),('rgln','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.64,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','CE1'),('rgln','NE2'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.16,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','CE1'),('rgln','OE1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.81,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','ND1'),('rgln','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.90,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','ND1'),('rgln','NE2'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.76,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','ND1'),('rgln','OE1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.99,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','NE2'),('rgln','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.23,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','NE2'),('rgln','NE2'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.60,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','NE2'),('rgln','OE1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.31,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('cys','CA'),('shis','CE1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.87,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','ND1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.22,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','NE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.68,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','CE1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.72,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','ND1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.19,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','NE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.61,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','CE1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.32,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','ND1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.98,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','NE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.09,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CA'),('rgln','CD'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.98,resSelectionSubs('gln','CD',subs)))
IDSpec[(('cys','CA'),('rgln','NE2'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.32,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('cys','CA'),('rgln','OE1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.39,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('cys','CB'),('rgln','CD'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.56,resSelectionSubs('gln','CD',subs)))
IDSpec[(('cys','CB'),('rgln','NE2'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.78,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('cys','CB'),('rgln','OE1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.18,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('cys','SG'),('rgln','CD'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.89,resSelectionSubs('gln','CD',subs)))
IDSpec[(('cys','SG'),('rgln','NE2'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.02,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('cys','SG'),('rgln','OE1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.59,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('shis','CE1'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.64,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','ND1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.90,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','NE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.23,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','CE1'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.16,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','ND1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.76,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','NE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+5.60,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','CE1'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.81,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','ND1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.99,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','NE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.31,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','CD'),('scys','CA'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.98,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('scys','CB'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.56,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('scys','SG'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.89,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gln','NE2'),('scys','CA'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.32,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('scys','CB'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.78,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('scys','SG'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.02,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gln','OE1'),('scys','CA'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.39,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('scys','CB'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.18,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('scys','SG'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.59,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18')
IDSpec['r_gln'] = cmd.count_atoms(resSelectionSubs('gln', subs=subs, selection=True))
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
IDSpec['S_1mb4_1_2_1_11'] = cmd.select('S_1mb4_1_2_1_11', 'his|cys|gln')
cmd.delete('his')
cmd.delete('cys')
cmd.delete('gln')
