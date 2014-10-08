'''
FUNC:S_2gmw_3_1_3_-
PDB:2gmw
EC:3.1.3.-
RESI:thr,ala,lys
LOCI:a-73,100,131;
'''
IDSpec[(('ala','CA'),('rlys','CD'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+24.93,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CA'),('rlys','CE'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+24.39,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CA'),('rlys','NZ'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+23.42,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CB'),('rlys','CD'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+25.14,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CB'),('rlys','CE'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+24.61,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CB'),('rlys','NZ'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+23.72,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CG'),('rlys','CD'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+23.72,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ala','CG'),('rlys','CE'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+23.72,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ala','CG'),('rlys','NZ'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+23.72,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ala','CA'),('rthr','CA'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+20.90,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ala','CA'),('rthr','CB'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+19.85,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ala','CA'),('rthr','OG1'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+20.55,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ala','CB'),('rthr','CA'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+21.01,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ala','CB'),('rthr','CB'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+19.97,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ala','CB'),('rthr','OG1'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+20.71,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ala','CG'),('rthr','CA'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+20.71,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ala','CG'),('rthr','CB'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+20.71,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ala','CG'),('rthr','OG1'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+20.71,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('lys','CD'),('sala','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+24.93,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sala','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+25.14,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sala','CG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+25.14,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+24.39,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+24.61,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sala','CG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+24.61,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+23.42,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+23.72,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sala','CG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+23.72,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('rthr','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.46,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CD'),('rthr','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.91,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CD'),('rthr','OG1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.35,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CE'),('rthr','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.36,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CE'),('rthr','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.72,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CE'),('rthr','OG1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.99,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','NZ'),('rthr','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.15,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','NZ'),('rthr','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.27,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','NZ'),('rthr','OG1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.53,resSelectionSubs('thr','OG1',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec[(('thr','CA'),('sala','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+20.90,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sala','CB'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+21.01,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('thr','CA'),('sala','CG'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+21.01,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sala','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+19.85,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sala','CB'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+19.97,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('thr','CB'),('sala','CG'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+19.97,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sala','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+20.55,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sala','CB'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+20.71,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('thr','OG1'),('sala','CG'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+20.71,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CD'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.46,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CE'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.36,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','NZ'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.15,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CD'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.91,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CE'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.72,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','NZ'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.27,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CD'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.35,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CE'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.99,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','NZ'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.53,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
IDSpec['S_2gmw_3_1_3_-'] = cmd.select('S_2gmw_3_1_3_-', 'ala|lys|thr')
cmd.delete('ala')
cmd.delete('lys')
cmd.delete('thr')
