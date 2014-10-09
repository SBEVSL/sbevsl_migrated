'''
FUNC:S_2eer_1_1_1_1
PDB:2eer
EC:1.1.1.1
RESI:his,ser,his,phe
LOCI:a-39,40,43,49;
'''
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.20,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.68,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.41,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.52,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.88,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.82,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.61,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.94,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.99,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CA'),('rphe','CD1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.68,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('ser','CA'),('rphe','CE1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.53,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('ser','CA'),('rphe','CZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.91,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('ser','CB'),('rphe','CD1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.86,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('ser','CB'),('rphe','CE1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.59,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('ser','CB'),('rphe','CZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.74,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('ser','OG'),('rphe','CD1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.58,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('ser','OG'),('rphe','CE1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.47,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('ser','OG'),('rphe','CZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.86,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.78,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.66,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.92,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.00,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.89,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.01,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.95,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.05,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.79,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.20,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.52,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.61,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.68,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.88,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.94,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.41,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.82,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.99,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','CE1'),('rphe','CD1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.91,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('his','CE1'),('rphe','CE1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.65,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('his','CE1'),('rphe','CZ'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.68,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('his','ND1'),('rphe','CD1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.99,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('his','ND1'),('rphe','CE1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.60,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('his','ND1'),('rphe','CZ'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.59,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('his','NE2'),('rphe','CD1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.80,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('his','NE2'),('rphe','CE1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.57,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('his','NE2'),('rphe','CZ'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.58,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('his','CE1'),('rhis','CE1'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.22,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','CE1'),('rhis','ND1'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.07,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','CE1'),('rhis','NE2'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.30,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','ND1'),('rhis','CE1'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.80,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','ND1'),('rhis','ND1'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.66,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','ND1'),('rhis','NE2'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.57,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','NE2'),('rhis','CE1'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.04,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','NE2'),('rhis','ND1'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.79,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','NE2'),('rhis','NE2'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.26,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('phe','CD1'),('sser','CA'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.68,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('sser','CB'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.86,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('phe','CD1'),('sser','OG'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.58,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sser','CA'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.53,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('sser','CB'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.59,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('phe','CE1'),('sser','OG'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.47,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sser','CA'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.91,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('sser','CB'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.74,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('phe','CZ'),('sser','OG'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.86,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('phe','CD1'),('shis','CE1'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.91,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('phe','CD1'),('shis','ND1'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.99,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('phe','CD1'),('shis','NE2'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.80,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('phe','CE1'),('shis','CE1'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.65,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('phe','CE1'),('shis','ND1'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.60,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('phe','CE1'),('shis','NE2'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.57,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('phe','CZ'),('shis','CE1'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.68,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('phe','CZ'),('shis','ND1'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.59,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('phe','CZ'),('shis','NE2'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.58,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('phe','CD1'),('rhis','CE1'))] = cmd.select('phe19', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.30,resSelectionSubs('his','CE1',subs)))
IDSpec[(('phe','CD1'),('rhis','ND1'))] = cmd.select('phe20', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.84,resSelectionSubs('his','ND1',subs)))
IDSpec[(('phe','CD1'),('rhis','NE2'))] = cmd.select('phe21', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.76,resSelectionSubs('his','NE2',subs)))
IDSpec[(('phe','CE1'),('rhis','CE1'))] = cmd.select('phe22', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.52,resSelectionSubs('his','CE1',subs)))
IDSpec[(('phe','CE1'),('rhis','ND1'))] = cmd.select('phe23', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.02,resSelectionSubs('his','ND1',subs)))
IDSpec[(('phe','CE1'),('rhis','NE2'))] = cmd.select('phe24', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.84,resSelectionSubs('his','NE2',subs)))
IDSpec[(('phe','CZ'),('rhis','CE1'))] = cmd.select('phe25', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.69,resSelectionSubs('his','CE1',subs)))
IDSpec[(('phe','CZ'),('rhis','ND1'))] = cmd.select('phe26', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('phe','CZ'),('rhis','NE2'))] = cmd.select('phe27', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.09,resSelectionSubs('his','NE2',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9&br. phe10&br. phe11&br. phe12&br. phe13&br. phe14&br. phe15&br. phe16&br. phe17&br. phe18&br. phe19&br. phe20&br. phe21&br. phe22&br. phe23&br. phe24&br. phe25&br. phe26&br. phe27')
IDSpec['r_phe'] = cmd.count_atoms(resSelectionSubs('phe', subs=subs, selection=True))
cmd.delete('phe1')
cmd.delete('phe2')
cmd.delete('phe3')
cmd.delete('phe4')
cmd.delete('phe5')
cmd.delete('phe6')
cmd.delete('phe7')
cmd.delete('phe8')
cmd.delete('phe9')
cmd.delete('phe10')
cmd.delete('phe11')
cmd.delete('phe12')
cmd.delete('phe13')
cmd.delete('phe14')
cmd.delete('phe15')
cmd.delete('phe16')
cmd.delete('phe17')
cmd.delete('phe18')
cmd.delete('phe19')
cmd.delete('phe20')
cmd.delete('phe21')
cmd.delete('phe22')
cmd.delete('phe23')
cmd.delete('phe24')
cmd.delete('phe25')
cmd.delete('phe26')
cmd.delete('phe27')
IDSpec[(('his_i','CE1'),('sser','CA'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.78,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sser','CB'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.00,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sser','OG'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.95,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sser','CA'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.66,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sser','CB'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.89,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sser','OG'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.05,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sser','CA'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.92,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sser','CB'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.01,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sser','OG'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.79,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.22,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.80,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.04,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.07,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.66,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.79,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.30,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.57,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.26,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sphe','CD1'))] = cmd.select('his_i19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.30,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sphe','CE1'))] = cmd.select('his_i20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.52,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sphe','CZ'))] = cmd.select('his_i21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.69,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sphe','CD1'))] = cmd.select('his_i22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.84,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sphe','CE1'))] = cmd.select('his_i23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.02,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sphe','CZ'))] = cmd.select('his_i24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.03,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sphe','CD1'))] = cmd.select('his_i25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.76,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sphe','CE1'))] = cmd.select('his_i26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.84,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sphe','CZ'))] = cmd.select('his_i27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.09,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec['his_i'] = cmd.select('his_i',' br. his_i1&br. his_i2&br. his_i3&br. his_i4&br. his_i5&br. his_i6&br. his_i7&br. his_i8&br. his_i9&br. his_i10&br. his_i11&br. his_i12&br. his_i13&br. his_i14&br. his_i15&br. his_i16&br. his_i17&br. his_i18&br. his_i19&br. his_i20&br. his_i21&br. his_i22&br. his_i23&br. his_i24&br. his_i25&br. his_i26&br. his_i27')
IDSpec['r_his_i'] = cmd.count_atoms(resSelectionSubs('his_i', subs=subs, selection=True))
cmd.delete('his_i1')
cmd.delete('his_i2')
cmd.delete('his_i3')
cmd.delete('his_i4')
cmd.delete('his_i5')
cmd.delete('his_i6')
cmd.delete('his_i7')
cmd.delete('his_i8')
cmd.delete('his_i9')
cmd.delete('his_i10')
cmd.delete('his_i11')
cmd.delete('his_i12')
cmd.delete('his_i13')
cmd.delete('his_i14')
cmd.delete('his_i15')
cmd.delete('his_i16')
cmd.delete('his_i17')
cmd.delete('his_i18')
cmd.delete('his_i19')
cmd.delete('his_i20')
cmd.delete('his_i21')
cmd.delete('his_i22')
cmd.delete('his_i23')
cmd.delete('his_i24')
cmd.delete('his_i25')
cmd.delete('his_i26')
cmd.delete('his_i27')
IDSpec['S_2eer_1_1_1_1'] = cmd.select('S_2eer_1_1_1_1', 'ser|his|phe|his_i')
cmd.delete('ser')
cmd.delete('his')
cmd.delete('phe')
cmd.delete('his_i')