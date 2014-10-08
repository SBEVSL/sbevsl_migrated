'''
FUNC:S_1tlu_4_1_1_50
PDB:1tlu
EC:4.1.1.50
RESI:ser,ser,his,cys
LOCI:a-55,63,68,83;
'''
IDSpec[(('his','CE1'),('rcys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+21.89,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','CE1'),('rcys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+21.84,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','CE1'),('rcys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+20.73,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','ND1'),('rcys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+22.82,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','ND1'),('rcys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+22.84,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','ND1'),('rcys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+21.76,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','NE2'),('rcys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+21.02,resSelectionSubs('cys','CA',subs)))
IDSpec[(('his','NE2'),('rcys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+21.01,resSelectionSubs('cys','CB',subs)))
IDSpec[(('his','NE2'),('rcys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+19.86,resSelectionSubs('cys','SG',subs)))
IDSpec[(('his','CE1'),('rser','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.49,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','CE1'),('rser','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.83,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','CE1'),('rser','OG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.82,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','ND1'),('rser','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.84,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','ND1'),('rser','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.27,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','ND1'),('rser','OG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.92,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','NE2'),('rser','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.57,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','NE2'),('rser','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.07,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','NE2'),('rser','OG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.99,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','CE1'),('rser_i','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.42,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('his','CE1'),('rser_i','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+17.01,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('his','CE1'),('rser_i','OG'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+17.72,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('his','ND1'),('rser_i','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+17.51,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('his','ND1'),('rser_i','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+18.04,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('his','ND1'),('rser_i','OG'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+18.69,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('his','NE2'),('rser_i','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.73,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('his','NE2'),('rser_i','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.24,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('his','NE2'),('rser_i','OG'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.99,resSelectionSubs('ser_i','OG',subs)))
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
IDSpec[(('cys','CA'),('shis','CE1'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+21.89,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','ND1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+22.82,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CA'),('shis','NE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+21.02,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','CE1'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.84,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','ND1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+22.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','CB'),('shis','NE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+21.01,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','CE1'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+20.73,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','ND1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.76,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('cys','SG'),('shis','NE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+19.86,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('cys','CA'),('rser','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+24.18,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CA'),('rser','CB'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+24.52,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CA'),('rser','OG'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+25.21,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CB'),('rser','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+24.23,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CB'),('rser','CB'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+24.48,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CB'),('rser','OG'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+25.21,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','SG'),('rser','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+23.37,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','SG'),('rser','CB'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+23.53,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','SG'),('rser','OG'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+24.20,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CA'),('rser_i','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.57,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('cys','CA'),('rser_i','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.30,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('cys','CA'),('rser_i','OG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.73,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('cys','CB'),('rser_i','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.95,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('cys','CB'),('rser_i','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.91,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('cys','CB'),('rser_i','OG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.52,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('cys','SG'),('rser_i','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.01,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('cys','SG'),('rser_i','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.05,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('cys','SG'),('rser_i','OG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.19,resSelectionSubs('ser_i','OG',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27')
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
IDSpec[(('ser','CA'),('shis','CE1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.49,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','ND1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','NE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.57,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','CE1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.83,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','ND1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.27,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','NE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.07,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','CE1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.82,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','ND1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.92,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','NE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.99,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+24.18,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+24.23,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','SG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+23.37,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+24.52,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+24.48,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','SG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+23.53,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+25.21,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+25.21,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','SG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+24.20,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CA'),('rser_i','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+18.83,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','CA'),('rser_i','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+19.43,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','CA'),('rser_i','OG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+19.83,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('ser','CB'),('rser_i','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+18.94,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','CB'),('rser_i','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+19.62,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','CB'),('rser_i','OG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+20.13,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('ser','OG'),('rser_i','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+19.74,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','OG'),('rser_i','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+20.36,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','OG'),('rser_i','OG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+20.92,resSelectionSubs('ser_i','OG',subs)))
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
IDSpec[(('ser_i','CA'),('shis','CE1'))] = cmd.select('ser_i1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+16.42,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser_i','CA'),('shis','ND1'))] = cmd.select('ser_i2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+17.51,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser_i','CA'),('shis','NE2'))] = cmd.select('ser_i3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.73,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser_i','CB'),('shis','CE1'))] = cmd.select('ser_i4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+17.01,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser_i','CB'),('shis','ND1'))] = cmd.select('ser_i5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+18.04,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser_i','CB'),('shis','NE2'))] = cmd.select('ser_i6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+16.24,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser_i','OG'),('shis','CE1'))] = cmd.select('ser_i7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+17.72,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser_i','OG'),('shis','ND1'))] = cmd.select('ser_i8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.69,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser_i','OG'),('shis','NE2'))] = cmd.select('ser_i9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+16.99,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser_i','CA'),('scys','CA'))] = cmd.select('ser_i10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.57,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('scys','CB'))] = cmd.select('ser_i11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.95,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('scys','SG'))] = cmd.select('ser_i12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.01,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('scys','CA'))] = cmd.select('ser_i13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.30,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('scys','CB'))] = cmd.select('ser_i14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.91,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('scys','SG'))] = cmd.select('ser_i15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.05,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('scys','CA'))] = cmd.select('ser_i16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.73,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('scys','CB'))] = cmd.select('ser_i17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.52,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('scys','SG'))] = cmd.select('ser_i18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.19,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CA'))] = cmd.select('ser_i19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+18.83,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CB'))] = cmd.select('ser_i20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+18.94,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','OG'))] = cmd.select('ser_i21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+19.74,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CA'))] = cmd.select('ser_i22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+19.43,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CB'))] = cmd.select('ser_i23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+19.62,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','OG'))] = cmd.select('ser_i24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+20.36,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CA'))] = cmd.select('ser_i25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+19.83,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CB'))] = cmd.select('ser_i26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+20.13,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','OG'))] = cmd.select('ser_i27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+20.92,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec['ser_i'] = cmd.select('ser_i',' br. ser_i1&br. ser_i2&br. ser_i3&br. ser_i4&br. ser_i5&br. ser_i6&br. ser_i7&br. ser_i8&br. ser_i9&br. ser_i10&br. ser_i11&br. ser_i12&br. ser_i13&br. ser_i14&br. ser_i15&br. ser_i16&br. ser_i17&br. ser_i18&br. ser_i19&br. ser_i20&br. ser_i21&br. ser_i22&br. ser_i23&br. ser_i24&br. ser_i25&br. ser_i26&br. ser_i27')
IDSpec['r_ser_i'] = cmd.count_atoms(resSelectionSubs('ser_i', subs=subs, selection=True))
cmd.delete('ser_i1')
cmd.delete('ser_i2')
cmd.delete('ser_i3')
cmd.delete('ser_i4')
cmd.delete('ser_i5')
cmd.delete('ser_i6')
cmd.delete('ser_i7')
cmd.delete('ser_i8')
cmd.delete('ser_i9')
cmd.delete('ser_i10')
cmd.delete('ser_i11')
cmd.delete('ser_i12')
cmd.delete('ser_i13')
cmd.delete('ser_i14')
cmd.delete('ser_i15')
cmd.delete('ser_i16')
cmd.delete('ser_i17')
cmd.delete('ser_i18')
cmd.delete('ser_i19')
cmd.delete('ser_i20')
cmd.delete('ser_i21')
cmd.delete('ser_i22')
cmd.delete('ser_i23')
cmd.delete('ser_i24')
cmd.delete('ser_i25')
cmd.delete('ser_i26')
cmd.delete('ser_i27')
IDSpec['S_1tlu_4_1_1_50'] = cmd.select('S_1tlu_4_1_1_50', 'his|cys|ser|ser_i')
cmd.delete('his')
cmd.delete('cys')
cmd.delete('ser')
cmd.delete('ser_i')
