'''
FUNC:S_1mka_4_2_1_60
PDB:1mka
EC:4.2.1.60
RESI:his,val,gly,cys,asp
LOCI:a-70,76,79,80,84;
'''
IDSpec[(('cys','CA'),('rval','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.47,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','CA'),('rval','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.42,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','CA'),('rval','CG1'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.92,resSelectionSubs('val','CG1',subs)))
IDSpec[(('cys','CB'),('rval','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.84,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','CB'),('rval','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.78,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','CB'),('rval','CG1'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.11,resSelectionSubs('val','CG1',subs)))
IDSpec[(('cys','SG'),('rval','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.08,resSelectionSubs('val','CA',subs)))
IDSpec[(('cys','SG'),('rval','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.20,resSelectionSubs('val','CB',subs)))
IDSpec[(('cys','SG'),('rval','CG1'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.49,resSelectionSubs('val','CG1',subs)))
IDSpec[(('cys','CA'),('rgly','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.81,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CA'),('rgly','N'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.17,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CA'),('rgly','O'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+4.81,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','CB'),('rgly','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.88,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','CB'),('rgly','N'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.87,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','CB'),('rgly','O'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.31,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','SG'),('rgly','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.44,resSelectionSubs('gly','CA',subs)))
IDSpec[(('cys','SG'),('rgly','N'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.98,resSelectionSubs('gly','N',subs)))
IDSpec[(('cys','SG'),('rgly','O'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.25,resSelectionSubs('gly','O',subs)))
IDSpec[(('cys','CA'),('rhis','CE1'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.71,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CA'),('rhis','ND1'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.45,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CA'),('rhis','NE2'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.87,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CB'),('rhis','CE1'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.09,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CB'),('rhis','ND1'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.80,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CB'),('rhis','NE2'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.49,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','SG'),('rhis','CE1'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.06,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','SG'),('rhis','ND1'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.53,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','SG'),('rhis','NE2'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.64,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CA'),('rasp','CG'))] = cmd.select('cys28', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.03,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CA'),('rasp','OD1'))] = cmd.select('cys29', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.97,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CA'),('rasp','OD2'))] = cmd.select('cys30', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.12,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CB'),('rasp','CG'))] = cmd.select('cys31', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.19,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CB'),('rasp','OD1'))] = cmd.select('cys32', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.00,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CB'),('rasp','OD2'))] = cmd.select('cys33', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.27,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','SG'),('rasp','CG'))] = cmd.select('cys34', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.40,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','SG'),('rasp','OD1'))] = cmd.select('cys35', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.38,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','SG'),('rasp','OD2'))] = cmd.select('cys36', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.28,resSelectionSubs('asp','OD2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27&br. cys28&br. cys29&br. cys30&br. cys31&br. cys32&br. cys33&br. cys34&br. cys35&br. cys36')
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
cmd.delete('cys19')
cmd.delete('cys20')
cmd.delete('cys21')
cmd.delete('cys22')
cmd.delete('cys23')
cmd.delete('cys24')
cmd.delete('cys25')
cmd.delete('cys26')
cmd.delete('cys27')
cmd.delete('cys28')
cmd.delete('cys29')
cmd.delete('cys30')
cmd.delete('cys31')
cmd.delete('cys32')
cmd.delete('cys33')
cmd.delete('cys34')
cmd.delete('cys35')
cmd.delete('cys36')
IDSpec[(('val','CA'),('scys','CA'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+13.47,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CA'),('scys','CB'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+13.84,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CA'),('scys','SG'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+13.08,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CB'),('scys','CA'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+13.42,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CB'),('scys','CB'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+13.78,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CB'),('scys','SG'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+13.20,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','CA'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+12.92,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','CB'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+13.11,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('val','CG1'),('scys','SG'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+12.49,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('val','CA'),('rgly','CA'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+10.59,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val','CA'),('rgly','N'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+9.53,resSelectionSubs('gly','N',subs)))
IDSpec[(('val','CA'),('rgly','O'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+12.60,resSelectionSubs('gly','O',subs)))
IDSpec[(('val','CB'),('rgly','CA'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+10.34,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val','CB'),('rgly','N'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+9.34,resSelectionSubs('gly','N',subs)))
IDSpec[(('val','CB'),('rgly','O'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+12.53,resSelectionSubs('gly','O',subs)))
IDSpec[(('val','CG1'),('rgly','CA'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+10.11,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val','CG1'),('rgly','N'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+8.98,resSelectionSubs('gly','N',subs)))
IDSpec[(('val','CG1'),('rgly','O'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+12.37,resSelectionSubs('gly','O',subs)))
IDSpec[(('val','CA'),('rhis','CE1'))] = cmd.select('val19', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+9.47,resSelectionSubs('his','CE1',subs)))
IDSpec[(('val','CA'),('rhis','ND1'))] = cmd.select('val20', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+9.38,resSelectionSubs('his','ND1',subs)))
IDSpec[(('val','CA'),('rhis','NE2'))] = cmd.select('val21', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+8.36,resSelectionSubs('his','NE2',subs)))
IDSpec[(('val','CB'),('rhis','CE1'))] = cmd.select('val22', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+9.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('val','CB'),('rhis','ND1'))] = cmd.select('val23', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+9.45,resSelectionSubs('his','ND1',subs)))
IDSpec[(('val','CB'),('rhis','NE2'))] = cmd.select('val24', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+8.06,resSelectionSubs('his','NE2',subs)))
IDSpec[(('val','CG1'),('rhis','CE1'))] = cmd.select('val25', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+8.05,resSelectionSubs('his','CE1',subs)))
IDSpec[(('val','CG1'),('rhis','ND1'))] = cmd.select('val26', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+8.25,resSelectionSubs('his','ND1',subs)))
IDSpec[(('val','CG1'),('rhis','NE2'))] = cmd.select('val27', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+6.80,resSelectionSubs('his','NE2',subs)))
IDSpec[(('val','CA'),('rasp','CG'))] = cmd.select('val28', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+18.73,resSelectionSubs('asp','CG',subs)))
IDSpec[(('val','CA'),('rasp','OD1'))] = cmd.select('val29', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.26,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('val','CA'),('rasp','OD2'))] = cmd.select('val30', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.33,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('val','CB'),('rasp','CG'))] = cmd.select('val31', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+19.16,resSelectionSubs('asp','CG',subs)))
IDSpec[(('val','CB'),('rasp','OD1'))] = cmd.select('val32', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+19.60,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('val','CB'),('rasp','OD2'))] = cmd.select('val33', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+19.85,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('val','CG1'),('rasp','CG'))] = cmd.select('val34', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+18.87,resSelectionSubs('asp','CG',subs)))
IDSpec[(('val','CG1'),('rasp','OD1'))] = cmd.select('val35', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.23,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('val','CG1'),('rasp','OD2'))] = cmd.select('val36', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+19.60,resSelectionSubs('asp','OD2',subs)))
IDSpec['val'] = cmd.select('val',' br. val1&br. val2&br. val3&br. val4&br. val5&br. val6&br. val7&br. val8&br. val9&br. val10&br. val11&br. val12&br. val13&br. val14&br. val15&br. val16&br. val17&br. val18&br. val19&br. val20&br. val21&br. val22&br. val23&br. val24&br. val25&br. val26&br. val27&br. val28&br. val29&br. val30&br. val31&br. val32&br. val33&br. val34&br. val35&br. val36')
IDSpec['r_val'] = cmd.count_atoms(resSelectionSubs('val', subs=subs, selection=True))
cmd.delete('val1')
cmd.delete('val2')
cmd.delete('val3')
cmd.delete('val4')
cmd.delete('val5')
cmd.delete('val6')
cmd.delete('val7')
cmd.delete('val8')
cmd.delete('val9')
cmd.delete('val10')
cmd.delete('val11')
cmd.delete('val12')
cmd.delete('val13')
cmd.delete('val14')
cmd.delete('val15')
cmd.delete('val16')
cmd.delete('val17')
cmd.delete('val18')
cmd.delete('val19')
cmd.delete('val20')
cmd.delete('val21')
cmd.delete('val22')
cmd.delete('val23')
cmd.delete('val24')
cmd.delete('val25')
cmd.delete('val26')
cmd.delete('val27')
cmd.delete('val28')
cmd.delete('val29')
cmd.delete('val30')
cmd.delete('val31')
cmd.delete('val32')
cmd.delete('val33')
cmd.delete('val34')
cmd.delete('val35')
cmd.delete('val36')
IDSpec[(('gly','CA'),('scys','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.81,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.88,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('scys','SG'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.44,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.17,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','N'),('scys','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.87,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','N'),('scys','SG'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.98,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.81,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('gly','O'),('scys','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.31,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('gly','O'),('scys','SG'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.25,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('gly','CA'),('sval','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.59,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('sval','CB'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.34,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('sval','CG1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.11,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gly','N'),('sval','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.53,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gly','N'),('sval','CB'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.34,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gly','N'),('sval','CG1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.98,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gly','O'),('sval','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.60,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gly','O'),('sval','CB'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.53,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gly','O'),('sval','CG1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.37,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gly','CA'),('rhis','CE1'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.14,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','CA'),('rhis','ND1'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.00,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','CA'),('rhis','NE2'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.63,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','N'),('rhis','CE1'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.78,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','N'),('rhis','ND1'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.59,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','N'),('rhis','NE2'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.25,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','O'),('rhis','CE1'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.82,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gly','O'),('rhis','ND1'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.57,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gly','O'),('rhis','NE2'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.56,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gly','CA'),('rasp','CG'))] = cmd.select('gly28', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.14,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','CA'),('rasp','OD1'))] = cmd.select('gly29', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.34,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','CA'),('rasp','OD2'))] = cmd.select('gly30', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.12,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','N'),('rasp','CG'))] = cmd.select('gly31', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.53,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','N'),('rasp','OD1'))] = cmd.select('gly32', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.76,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','N'),('rasp','OD2'))] = cmd.select('gly33', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.45,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','O'),('rasp','CG'))] = cmd.select('gly34', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.14,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','O'),('rasp','OD1'))] = cmd.select('gly35', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.34,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','O'),('rasp','OD2'))] = cmd.select('gly36', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.15,resSelectionSubs('asp','OD2',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27&br. gly28&br. gly29&br. gly30&br. gly31&br. gly32&br. gly33&br. gly34&br. gly35&br. gly36')
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
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
cmd.delete('gly28')
cmd.delete('gly29')
cmd.delete('gly30')
cmd.delete('gly31')
cmd.delete('gly32')
cmd.delete('gly33')
cmd.delete('gly34')
cmd.delete('gly35')
cmd.delete('gly36')
IDSpec[(('his','CE1'),('scys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.71,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.09,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.06,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.45,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.80,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.53,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.87,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.49,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.64,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','CE1'),('sval','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.47,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sval','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.31,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sval','CG1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.05,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('his','ND1'),('sval','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.38,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sval','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.45,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sval','CG1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.25,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('his','NE2'),('sval','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.36,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sval','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.06,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sval','CG1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.80,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.14,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','N'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.78,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','CE1'),('sgly','O'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.82,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.00,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','N'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.59,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','ND1'),('sgly','O'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.57,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.63,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','N'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.25,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('his','NE2'),('sgly','O'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.56,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his28', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.32,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his29', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.41,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his30', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.08,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his31', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.55,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his32', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.72,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his33', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+16.22,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his34', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.81,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his35', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.95,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his36', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.60,resSelectionSubs('asp','OD2',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36')
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
cmd.delete('his28')
cmd.delete('his29')
cmd.delete('his30')
cmd.delete('his31')
cmd.delete('his32')
cmd.delete('his33')
cmd.delete('his34')
cmd.delete('his35')
cmd.delete('his36')
IDSpec[(('asp','CG'),('scys','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.03,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.19,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','SG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.40,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.97,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.00,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','SG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.38,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.12,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.27,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','SG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.28,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','CG'),('sval','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+18.73,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sval','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+19.16,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sval','CG1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+18.87,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sval','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.26,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sval','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.60,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sval','CG1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.23,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sval','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.33,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sval','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.85,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sval','CG1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.60,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.14,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','N'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.53,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','O'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.14,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.34,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','N'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.76,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','O'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.34,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.12,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','N'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.45,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','O'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.15,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.32,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.55,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.81,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.41,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.72,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.95,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.08,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.22,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.60,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36')
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
cmd.delete('asp28')
cmd.delete('asp29')
cmd.delete('asp30')
cmd.delete('asp31')
cmd.delete('asp32')
cmd.delete('asp33')
cmd.delete('asp34')
cmd.delete('asp35')
cmd.delete('asp36')
IDSpec['S_1mka_4_2_1_60'] = cmd.select('S_1mka_4_2_1_60', 'cys|val|gly|his|asp')
cmd.delete('cys')
cmd.delete('val')
cmd.delete('gly')
cmd.delete('his')
cmd.delete('asp')