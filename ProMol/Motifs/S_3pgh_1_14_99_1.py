'''
FUNC:S_3pgh_1_14_99_1
PDB:3pgh
EC:1.14.99.1
RESI:gln,his,val,tyr
LOCI:a-203,207,291,385;
'''
IDSpec[(('val','CA'),('rhis','CE1'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+11.41,resSelectionSubs('his','CE1',subs)))
IDSpec[(('val','CA'),('rhis','ND1'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+11.26,resSelectionSubs('his','ND1',subs)))
IDSpec[(('val','CA'),('rhis','NE2'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+10.32,resSelectionSubs('his','NE2',subs)))
IDSpec[(('val','CB'),('rhis','CE1'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+10.38,resSelectionSubs('his','CE1',subs)))
IDSpec[(('val','CB'),('rhis','ND1'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+10.35,resSelectionSubs('his','ND1',subs)))
IDSpec[(('val','CB'),('rhis','NE2'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+9.21,resSelectionSubs('his','NE2',subs)))
IDSpec[(('val','CG1'),('rhis','CE1'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+8.97,resSelectionSubs('his','CE1',subs)))
IDSpec[(('val','CG1'),('rhis','ND1'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+8.89,resSelectionSubs('his','ND1',subs)))
IDSpec[(('val','CG1'),('rhis','NE2'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+7.87,resSelectionSubs('his','NE2',subs)))
IDSpec[(('val','CA'),('rtyr','CE1'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.00,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('val','CA'),('rtyr','CZ'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.76,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('val','CA'),('rtyr','OH'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+20.18,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('val','CB'),('rtyr','CE1'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.09,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('val','CB'),('rtyr','CZ'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.86,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('val','CB'),('rtyr','OH'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+19.38,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('val','CG1'),('rtyr','CE1'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+16.63,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('val','CG1'),('rtyr','CZ'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+17.41,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('val','CG1'),('rtyr','OH'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+17.90,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('val','CA'),('rgln','CD'))] = cmd.select('val19', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+11.28,resSelectionSubs('gln','CD',subs)))
IDSpec[(('val','CA'),('rgln','NE2'))] = cmd.select('val20', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+12.05,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('val','CA'),('rgln','OE1'))] = cmd.select('val21', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+10.44,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('val','CB'),('rgln','CD'))] = cmd.select('val22', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+10.77,resSelectionSubs('gln','CD',subs)))
IDSpec[(('val','CB'),('rgln','NE2'))] = cmd.select('val23', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+11.70,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('val','CB'),('rgln','OE1'))] = cmd.select('val24', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+9.86,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('val','CG1'),('rgln','CD'))] = cmd.select('val25', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+9.51,resSelectionSubs('gln','CD',subs)))
IDSpec[(('val','CG1'),('rgln','NE2'))] = cmd.select('val26', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+10.50,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('val','CG1'),('rgln','OE1'))] = cmd.select('val27', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+8.69,resSelectionSubs('gln','OE1',subs)))
IDSpec['val'] = cmd.select('val',' br. val1&br. val2&br. val3&br. val4&br. val5&br. val6&br. val7&br. val8&br. val9&br. val10&br. val11&br. val12&br. val13&br. val14&br. val15&br. val16&br. val17&br. val18&br. val19&br. val20&br. val21&br. val22&br. val23&br. val24&br. val25&br. val26&br. val27')
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
IDSpec[(('his','CE1'),('sval','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.41,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sval','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.38,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sval','CG1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.97,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('his','ND1'),('sval','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.26,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sval','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.35,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sval','CG1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.89,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('his','NE2'),('sval','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.32,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sval','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.21,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sval','CG1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.87,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('his','CE1'),('rtyr','CE1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.83,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','CE1'),('rtyr','CZ'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.76,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','CE1'),('rtyr','OH'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.44,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','ND1'),('rtyr','CE1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.75,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','ND1'),('rtyr','CZ'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.53,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','ND1'),('rtyr','OH'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.08,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','NE2'),('rtyr','CE1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.12,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','NE2'),('rtyr','CZ'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.04,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','NE2'),('rtyr','OH'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.75,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','CE1'),('rgln','CD'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.01,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','CE1'),('rgln','NE2'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.26,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','CE1'),('rgln','OE1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.00,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','ND1'),('rgln','CD'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.31,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','ND1'),('rgln','NE2'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.47,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','ND1'),('rgln','OE1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.45,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','NE2'),('rgln','CD'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.05,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','NE2'),('rgln','NE2'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.38,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','NE2'),('rgln','OE1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.72,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('tyr','CE1'),('sval','CA'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.00,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sval','CB'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+18.09,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sval','CG1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+16.63,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sval','CA'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.76,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sval','CB'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.86,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sval','CG1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+17.41,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sval','CA'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+20.18,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('sval','CB'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+19.38,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('tyr','OH'),('sval','CG1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+17.90,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','CE1'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.83,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','ND1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.75,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','NE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.12,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','CE1'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.76,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','ND1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.53,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','NE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.04,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','CE1'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.44,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','ND1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.08,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','NE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.75,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rgln','CD'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.35,resSelectionSubs('gln','CD',subs)))
IDSpec[(('tyr','CE1'),('rgln','NE2'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.88,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('tyr','CE1'),('rgln','OE1'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.10,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('tyr','CZ'),('rgln','CD'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+13.48,resSelectionSubs('gln','CD',subs)))
IDSpec[(('tyr','CZ'),('rgln','NE2'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.00,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('tyr','CZ'),('rgln','OE1'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.23,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('tyr','OH'),('rgln','CD'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+13.81,resSelectionSubs('gln','CD',subs)))
IDSpec[(('tyr','OH'),('rgln','NE2'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+14.22,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('tyr','OH'),('rgln','OE1'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+14.66,resSelectionSubs('gln','OE1',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27')
IDSpec['r_tyr'] = cmd.count_atoms(resSelectionSubs('tyr', subs=subs, selection=True))
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
cmd.delete('tyr19')
cmd.delete('tyr20')
cmd.delete('tyr21')
cmd.delete('tyr22')
cmd.delete('tyr23')
cmd.delete('tyr24')
cmd.delete('tyr25')
cmd.delete('tyr26')
cmd.delete('tyr27')
IDSpec[(('gln','CD'),('sval','CA'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.28,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sval','CB'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.77,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sval','CG1'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.51,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sval','CA'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.05,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sval','CB'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.70,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sval','CG1'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.50,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sval','CA'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.44,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sval','CB'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.86,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sval','CG1'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.69,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','CE1'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.01,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','ND1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.31,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','NE2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.05,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','CE1'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.26,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','ND1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.47,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','NE2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.38,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','CE1'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.00,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','ND1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.45,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','NE2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.72,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','CD'),('styr','CE1'))] = cmd.select('gln19', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.35,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gln','CD'),('styr','CZ'))] = cmd.select('gln20', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.48,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gln','CD'),('styr','OH'))] = cmd.select('gln21', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.81,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gln','NE2'),('styr','CE1'))] = cmd.select('gln22', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.88,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('styr','CZ'))] = cmd.select('gln23', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+14.00,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gln','NE2'),('styr','OH'))] = cmd.select('gln24', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+14.22,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gln','OE1'),('styr','CE1'))] = cmd.select('gln25', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.10,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('styr','CZ'))] = cmd.select('gln26', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.23,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gln','OE1'),('styr','OH'))] = cmd.select('gln27', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.66,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18&br. gln19&br. gln20&br. gln21&br. gln22&br. gln23&br. gln24&br. gln25&br. gln26&br. gln27')
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
cmd.delete('gln19')
cmd.delete('gln20')
cmd.delete('gln21')
cmd.delete('gln22')
cmd.delete('gln23')
cmd.delete('gln24')
cmd.delete('gln25')
cmd.delete('gln26')
cmd.delete('gln27')
IDSpec['S_3pgh_1_14_99_1'] = cmd.select('S_3pgh_1_14_99_1', 'val|his|tyr|gln')
cmd.delete('val')
cmd.delete('his')
cmd.delete('tyr')
cmd.delete('gln')
