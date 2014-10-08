'''
FUNC:S_1sck_4_1_2_39
PDB:1sck
EC:4.1.2.39
RESI:thr,ser,asp,his
LOCI:a-11,80,207,235;
'''
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','CG'),('rthr','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.68,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','CG'),('rthr','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.21,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','CG'),('rthr','OG1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.09,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD1'),('rthr','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.55,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD1'),('rthr','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.04,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD1'),('rthr','OG1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.85,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD2'),('rthr','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.78,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD2'),('rthr','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.36,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD2'),('rthr','OG1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.28,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.38,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.26,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.36,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.28,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.21,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.11,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.64,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.65,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.76,resSelectionSubs('his','NE2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
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
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('rthr','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','CA'),('rthr','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','CA'),('rthr','OG1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','CB'),('rthr','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','CB'),('rthr','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','CB'),('rthr','OG1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','OG'),('rthr','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','OG'),('rthr','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','OG'),('rthr','OG1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.76,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.76,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.76,resSelectionSubs('his','NE2',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27')
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
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
IDSpec[(('thr','CA'),('sasp','CG'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+14.68,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+14.55,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','CG'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+13.21,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+13.04,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.36,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','CG'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.09,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.85,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CA'),('sser','CA'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.28,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sser','CB'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.28,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','CA'),('sser','OG'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.28,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','CA'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.28,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','CB'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.28,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','OG'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.28,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','CA'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.28,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','CB'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.28,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','OG'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.28,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','CA'),('rhis','CE1'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.34,resSelectionSubs('his','CE1',subs)))
IDSpec[(('thr','CA'),('rhis','ND1'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.59,resSelectionSubs('his','ND1',subs)))
IDSpec[(('thr','CA'),('rhis','NE2'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.68,resSelectionSubs('his','NE2',subs)))
IDSpec[(('thr','CB'),('rhis','CE1'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.87,resSelectionSubs('his','CE1',subs)))
IDSpec[(('thr','CB'),('rhis','ND1'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.13,resSelectionSubs('his','ND1',subs)))
IDSpec[(('thr','CB'),('rhis','NE2'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.21,resSelectionSubs('his','NE2',subs)))
IDSpec[(('thr','OG1'),('rhis','CE1'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.86,resSelectionSubs('his','CE1',subs)))
IDSpec[(('thr','OG1'),('rhis','ND1'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.17,resSelectionSubs('his','ND1',subs)))
IDSpec[(('thr','OG1'),('rhis','NE2'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.35,resSelectionSubs('his','NE2',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27')
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
cmd.delete('thr19')
cmd.delete('thr20')
cmd.delete('thr21')
cmd.delete('thr22')
cmd.delete('thr23')
cmd.delete('thr24')
cmd.delete('thr25')
cmd.delete('thr26')
cmd.delete('thr27')
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.38,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.28,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.64,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.26,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.21,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.65,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.36,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.11,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.76,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.76,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.76,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.76,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.76,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.76,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.76,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','CE1'),('sthr','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.34,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sthr','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.87,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sthr','OG1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.86,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('his','ND1'),('sthr','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.59,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sthr','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.13,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sthr','OG1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.17,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('his','NE2'),('sthr','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.68,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sthr','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.21,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sthr','OG1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.35,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27')
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
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
IDSpec['S_1sck_4_1_2_39'] = cmd.select('S_1sck_4_1_2_39', 'asp|ser|thr|his')
cmd.delete('asp')
cmd.delete('ser')
cmd.delete('thr')
cmd.delete('his')
