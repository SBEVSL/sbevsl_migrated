'''
FUNC:S_5fiv_3_4_23_16
PDB:5fiv
EC:3.4.23.16
RESI:asp,thr
LOCI:a-30,31;
'''
IDSpec[(('thr','CA'),('rasp','CG'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.08,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CA'),('rasp','OD1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.39,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CA'),('rasp','OD2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.22,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','CB'),('rasp','CG'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.32,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CB'),('rasp','OD1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.51,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CB'),('rasp','OD2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.50,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','OG1'),('rasp','CG'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.25,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','OG1'),('rasp','OD1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.26,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','OG1'),('rasp','OD2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.42,resSelectionSubs('asp','OD2',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9')
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
IDSpec[(('asp','CG'),('sthr','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.08,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.32,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','OG1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.25,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.39,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.51,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','OG1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.26,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.22,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.50,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','OG1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.42,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9')
IDSpec['r_asp'] = cmd.count_atoms(resSelectionSubs('asp', subs=subs, selection=True))
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
IDSpec['S_5fiv_3_4_23_16'] = cmd.select('S_5fiv_3_4_23_16', 'thr|asp')
cmd.delete('thr')
cmd.delete('asp')
