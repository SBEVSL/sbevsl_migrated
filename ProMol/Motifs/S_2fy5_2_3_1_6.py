'''
FUNC:S_2fy5_2_3_1_6
PDB:2fy5
EC:2.3.1.6
RESI:tyr,pro,his,ser
LOCI:a-85,98,324,540;
'''
IDSpec[(('pro','CA'),('rtyr','CE1'))] = cmd.select('pro1', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+12.38,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('pro','CA'),('rtyr','CZ'))] = cmd.select('pro2', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+11.09,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('pro','CA'),('rtyr','OH'))] = cmd.select('pro3', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+10.59,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('pro','CB'),('rtyr','CE1'))] = cmd.select('pro4', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+11.66,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('pro','CB'),('rtyr','CZ'))] = cmd.select('pro5', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+10.39,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('pro','CB'),('rtyr','OH'))] = cmd.select('pro6', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+9.72,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('pro','CD'),('rtyr','CE1'))] = cmd.select('pro7', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+10.30,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('pro','CD'),('rtyr','CZ'))] = cmd.select('pro8', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+9.08,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('pro','CD'),('rtyr','OH'))] = cmd.select('pro9', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+8.76,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('pro','CA'),('rser','CA'))] = cmd.select('pro10', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+13.66,resSelectionSubs('ser','CA',subs)))
IDSpec[(('pro','CA'),('rser','CB'))] = cmd.select('pro11', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+12.39,resSelectionSubs('ser','CB',subs)))
IDSpec[(('pro','CA'),('rser','OG'))] = cmd.select('pro12', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+11.35,resSelectionSubs('ser','OG',subs)))
IDSpec[(('pro','CB'),('rser','CA'))] = cmd.select('pro13', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+12.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('pro','CB'),('rser','CB'))] = cmd.select('pro14', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+11.14,resSelectionSubs('ser','CB',subs)))
IDSpec[(('pro','CB'),('rser','OG'))] = cmd.select('pro15', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+10.11,resSelectionSubs('ser','OG',subs)))
IDSpec[(('pro','CD'),('rser','CA'))] = cmd.select('pro16', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+13.95,resSelectionSubs('ser','CA',subs)))
IDSpec[(('pro','CD'),('rser','CB'))] = cmd.select('pro17', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+12.53,resSelectionSubs('ser','CB',subs)))
IDSpec[(('pro','CD'),('rser','OG'))] = cmd.select('pro18', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+11.70,resSelectionSubs('ser','OG',subs)))
IDSpec[(('pro','CA'),('rhis','CE1'))] = cmd.select('pro19', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+9.19,resSelectionSubs('his','CE1',subs)))
IDSpec[(('pro','CA'),('rhis','ND1'))] = cmd.select('pro20', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+9.17,resSelectionSubs('his','ND1',subs)))
IDSpec[(('pro','CA'),('rhis','NE2'))] = cmd.select('pro21', '%s w. %s of %s'%(resSelectionSubs('pro','CA',subs),d+8.36,resSelectionSubs('his','NE2',subs)))
IDSpec[(('pro','CB'),('rhis','CE1'))] = cmd.select('pro22', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+8.04,resSelectionSubs('his','CE1',subs)))
IDSpec[(('pro','CB'),('rhis','ND1'))] = cmd.select('pro23', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+8.21,resSelectionSubs('his','ND1',subs)))
IDSpec[(('pro','CB'),('rhis','NE2'))] = cmd.select('pro24', '%s w. %s of %s'%(resSelectionSubs('pro','CB',subs),d+7.26,resSelectionSubs('his','NE2',subs)))
IDSpec[(('pro','CD'),('rhis','CE1'))] = cmd.select('pro25', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+7.41,resSelectionSubs('his','CE1',subs)))
IDSpec[(('pro','CD'),('rhis','ND1'))] = cmd.select('pro26', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+7.09,resSelectionSubs('his','ND1',subs)))
IDSpec[(('pro','CD'),('rhis','NE2'))] = cmd.select('pro27', '%s w. %s of %s'%(resSelectionSubs('pro','CD',subs),d+6.78,resSelectionSubs('his','NE2',subs)))
IDSpec['pro'] = cmd.select('pro',' br. pro1&br. pro2&br. pro3&br. pro4&br. pro5&br. pro6&br. pro7&br. pro8&br. pro9&br. pro10&br. pro11&br. pro12&br. pro13&br. pro14&br. pro15&br. pro16&br. pro17&br. pro18&br. pro19&br. pro20&br. pro21&br. pro22&br. pro23&br. pro24&br. pro25&br. pro26&br. pro27')
IDSpec['r_pro'] = cmd.count_atoms(resSelectionSubs('pro', subs=subs, selection=True))
cmd.delete('pro1')
cmd.delete('pro2')
cmd.delete('pro3')
cmd.delete('pro4')
cmd.delete('pro5')
cmd.delete('pro6')
cmd.delete('pro7')
cmd.delete('pro8')
cmd.delete('pro9')
cmd.delete('pro10')
cmd.delete('pro11')
cmd.delete('pro12')
cmd.delete('pro13')
cmd.delete('pro14')
cmd.delete('pro15')
cmd.delete('pro16')
cmd.delete('pro17')
cmd.delete('pro18')
cmd.delete('pro19')
cmd.delete('pro20')
cmd.delete('pro21')
cmd.delete('pro22')
cmd.delete('pro23')
cmd.delete('pro24')
cmd.delete('pro25')
cmd.delete('pro26')
cmd.delete('pro27')
IDSpec[(('tyr','CE1'),('spro','CA'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.38,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('spro','CB'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.66,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('tyr','CE1'),('spro','CD'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.30,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('spro','CA'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.09,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('spro','CB'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.39,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('tyr','CZ'),('spro','CD'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.08,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('spro','CA'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.59,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('spro','CB'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.72,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('tyr','OH'),('spro','CD'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.76,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rser','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('tyr','CE1'),('rser','CB'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.09,resSelectionSubs('ser','CB',subs)))
IDSpec[(('tyr','CE1'),('rser','OG'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.31,resSelectionSubs('ser','OG',subs)))
IDSpec[(('tyr','CZ'),('rser','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+13.68,resSelectionSubs('ser','CA',subs)))
IDSpec[(('tyr','CZ'),('rser','CB'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.27,resSelectionSubs('ser','CB',subs)))
IDSpec[(('tyr','CZ'),('rser','OG'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.38,resSelectionSubs('ser','OG',subs)))
IDSpec[(('tyr','OH'),('rser','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.33,resSelectionSubs('ser','CA',subs)))
IDSpec[(('tyr','OH'),('rser','CB'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.92,resSelectionSubs('ser','CB',subs)))
IDSpec[(('tyr','OH'),('rser','OG'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.03,resSelectionSubs('ser','OG',subs)))
IDSpec[(('tyr','CE1'),('rhis','CE1'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.54,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CE1'),('rhis','ND1'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.14,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CE1'),('rhis','NE2'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.91,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','CZ'),('rhis','CE1'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.69,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CZ'),('rhis','ND1'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.34,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CZ'),('rhis','NE2'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.78,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','OH'),('rhis','CE1'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.75,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','OH'),('rhis','ND1'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.90,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','OH'),('rhis','NE2'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.74,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('ser','CA'),('spro','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.66,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('spro','CB'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.46,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('spro','CD'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.95,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('spro','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.39,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('spro','CB'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.14,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('spro','CD'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.53,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('spro','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.35,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('spro','CB'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.11,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('spro','CD'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.70,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('styr','CE1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.46,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('styr','CZ'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.68,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('styr','OH'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.33,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ser','CB'),('styr','CE1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.09,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('styr','CZ'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.27,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('styr','OH'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.92,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ser','OG'),('styr','CE1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.31,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('styr','CZ'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.38,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('styr','OH'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.03,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.68,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.98,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.11,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.16,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.46,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.59,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.96,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.22,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.33,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('spro','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.19,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('spro','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.04,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('spro','CD'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.41,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('spro','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.17,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('spro','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.21,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('spro','CD'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.09,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('spro','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.36,resSelectionSubs('pro','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('spro','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.26,resSelectionSubs('pro','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('spro','CD'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.78,resSelectionSubs('pro','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('styr','CE1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.54,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','CE1'),('styr','CZ'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.69,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('styr','OH'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+4.75,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','CE1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.14,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','CZ'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.34,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','OH'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.90,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','CE1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.91,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','CZ'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.78,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','OH'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.74,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.68,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.16,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.96,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.98,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.46,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.22,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.11,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.59,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.33,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_2fy5_2_3_1_6'] = cmd.select('S_2fy5_2_3_1_6', 'pro|tyr|ser|his')
cmd.delete('pro')
cmd.delete('tyr')
cmd.delete('ser')
cmd.delete('his')
