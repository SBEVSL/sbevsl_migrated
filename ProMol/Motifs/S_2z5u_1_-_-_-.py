'''
FUNC:S_2z5u_1_-_-_-
PDB:2z5u
EC:1.-.-.-
RESI:thr,his,lys
LOCI:a-335,551,661;
'''
IDSpec[(('thr','CA'),('rlys','CD'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+17.56,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CA'),('rlys','CE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+16.19,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CA'),('rlys','NZ'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+15.35,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','CB'),('rlys','CD'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+17.70,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CB'),('rlys','CE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+16.27,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CB'),('rlys','NZ'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+15.53,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','OG1'),('rlys','CD'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+18.48,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','OG1'),('rlys','CE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+17.05,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','OG1'),('rlys','NZ'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+16.26,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','CA'),('rhis','CE1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+25.47,resSelectionSubs('his','CE1',subs)))
IDSpec[(('thr','CA'),('rhis','ND1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+24.19,resSelectionSubs('his','ND1',subs)))
IDSpec[(('thr','CA'),('rhis','NE2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+26.16,resSelectionSubs('his','NE2',subs)))
IDSpec[(('thr','CB'),('rhis','CE1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+23.97,resSelectionSubs('his','CE1',subs)))
IDSpec[(('thr','CB'),('rhis','ND1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+22.69,resSelectionSubs('his','ND1',subs)))
IDSpec[(('thr','CB'),('rhis','NE2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+24.66,resSelectionSubs('his','NE2',subs)))
IDSpec[(('thr','OG1'),('rhis','CE1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+23.71,resSelectionSubs('his','CE1',subs)))
IDSpec[(('thr','OG1'),('rhis','ND1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+22.46,resSelectionSubs('his','ND1',subs)))
IDSpec[(('thr','OG1'),('rhis','NE2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+24.42,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('lys','CD'),('sthr','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.56,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.70,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','OG1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.48,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.19,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.27,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','OG1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.05,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.35,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.53,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','OG1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.26,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CD'),('rhis','CE1'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+31.54,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','CD'),('rhis','ND1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+30.30,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','CD'),('rhis','NE2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+31.54,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','CE'),('rhis','CE1'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+30.24,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','CE'),('rhis','ND1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+29.00,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','CE'),('rhis','NE2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+30.28,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','NZ'),('rhis','CE1'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+30.59,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','NZ'),('rhis','ND1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+29.33,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','NZ'),('rhis','NE2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+30.68,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('sthr','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+25.47,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sthr','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+23.97,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sthr','OG1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+23.71,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('his','ND1'),('sthr','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+24.19,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sthr','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+22.69,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sthr','OG1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+22.46,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('his','NE2'),('sthr','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+26.16,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sthr','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+24.66,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sthr','OG1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+24.42,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('his','CE1'),('slys','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+31.54,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('slys','CE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+30.24,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','CE1'),('slys','NZ'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+30.59,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+30.30,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','CE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+29.00,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','NZ'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+29.33,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+31.54,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','CE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+30.28,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','NZ'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+30.68,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2z5u_1_-_-_-'] = cmd.select('S_2z5u_1_-_-_-', 'thr|lys|his')
cmd.delete('thr')
cmd.delete('lys')
cmd.delete('his')
