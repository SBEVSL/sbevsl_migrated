'''
FUNC:S_1hzf_3_4_21_43
PDB:1hzf
EC:3.4.21.43
RESI:cys,gln,ala
LOCI:a-991,994,1292;
'''
IDSpec[(('ala','CA'),('rcys','CA'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+30.13,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ala','CA'),('rcys','CB'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+30.60,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ala','CA'),('rcys','SG'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+29.55,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ala','CB'),('rcys','CA'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+30.19,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ala','CB'),('rcys','CB'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+30.59,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ala','CB'),('rcys','SG'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+29.46,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ala','CG'),('rcys','CA'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+29.46,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ala','CG'),('rcys','CB'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+29.46,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ala','CG'),('rcys','SG'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+29.46,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ala','CA'),('rgln','CD'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+26.85,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ala','CA'),('rgln','NE2'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+26.78,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ala','CA'),('rgln','OE1'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+26.41,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ala','CB'),('rgln','CD'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+26.65,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ala','CB'),('rgln','NE2'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+26.52,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ala','CB'),('rgln','OE1'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+26.20,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ala','CG'),('rgln','CD'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+26.20,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ala','CG'),('rgln','NE2'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+26.20,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ala','CG'),('rgln','OE1'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+26.20,resSelectionSubs('gln','OE1',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18')
IDSpec['r_ala'] = cmd.count_atoms(resSelectionSubs('ala', subs=subs, selection=True))
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
cmd.delete('ala10')
cmd.delete('ala11')
cmd.delete('ala12')
cmd.delete('ala13')
cmd.delete('ala14')
cmd.delete('ala15')
cmd.delete('ala16')
cmd.delete('ala17')
cmd.delete('ala18')
IDSpec[(('cys','CA'),('sala','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+30.13,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sala','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+30.19,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('cys','CA'),('sala','CG'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+30.19,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sala','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+30.60,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sala','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+30.59,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('cys','CB'),('sala','CG'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+30.59,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sala','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+29.55,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sala','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+29.46,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('cys','SG'),('sala','CG'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+29.46,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('rgln','CD'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.56,resSelectionSubs('gln','CD',subs)))
IDSpec[(('cys','CA'),('rgln','NE2'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.93,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('cys','CA'),('rgln','OE1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.50,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('cys','CB'),('rgln','CD'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.42,resSelectionSubs('gln','CD',subs)))
IDSpec[(('cys','CB'),('rgln','NE2'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.53,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('cys','CB'),('rgln','OE1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.50,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('cys','SG'),('rgln','CD'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.93,resSelectionSubs('gln','CD',subs)))
IDSpec[(('cys','SG'),('rgln','NE2'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.85,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('cys','SG'),('rgln','OE1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.10,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('sala','CA'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+26.85,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sala','CB'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+26.65,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sala','CG'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+26.65,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sala','CA'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+26.78,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sala','CB'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+26.52,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sala','CG'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+26.52,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sala','CA'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+26.41,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sala','CB'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+26.20,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sala','CG'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+26.20,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('gln','CD'),('scys','CA'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+8.56,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('scys','CB'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+8.42,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('scys','SG'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.93,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gln','NE2'),('scys','CA'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.93,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('scys','CB'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.53,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('scys','SG'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.85,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gln','OE1'),('scys','CA'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.50,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('scys','CB'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.50,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('scys','SG'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.10,resSelectionSubs('cys','SG',subs,selection=True)))
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
IDSpec['S_1hzf_3_4_21_43'] = cmd.select('S_1hzf_3_4_21_43', 'ala|cys|gln')
cmd.delete('ala')
cmd.delete('cys')
cmd.delete('gln')