'''
FUNC:S_1al8_1_1_3_15
PDB:1al8
EC:1.1.3.15
RESI:tyr,tyr,asp,his,arg
LOCI:a-24,129,157,254,257;
'''
IDSpec[(('tyr','CE1'),('rhis','CE1'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.33,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CE1'),('rhis','ND1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.06,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CE1'),('rhis','NE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.05,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','CZ'),('rhis','CE1'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.32,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CZ'),('rhis','ND1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+13.14,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CZ'),('rhis','NE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.07,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','OH'),('rhis','CE1'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.40,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','OH'),('rhis','ND1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.32,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','OH'),('rhis','NE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.20,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','CE1'),('rarg','CZ'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.58,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CE1'),('rarg','NE'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.46,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CE1'),('rarg','NH1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CZ'),('rarg','CZ'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.07,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CZ'),('rarg','NE'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.84,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CZ'),('rarg','NH1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.80,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','OH'),('rarg','CZ'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.35,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','OH'),('rarg','NE'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.84,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','OH'),('rarg','NH1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.30,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CE1'),('rtyr_i','CE1'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.18,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','CE1'),('rtyr_i','CZ'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.02,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','CE1'),('rtyr_i','OH'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.08,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','CE1'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.00,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','CZ'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.76,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','OH'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.86,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','CE1'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.80,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','CZ'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.53,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','OH'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.68,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','CE1'),('rasp','CG'))] = cmd.select('tyr28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+16.47,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD1'))] = cmd.select('tyr29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+16.00,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD2'))] = cmd.select('tyr30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+16.64,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CZ'),('rasp','CG'))] = cmd.select('tyr31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+16.65,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD1'))] = cmd.select('tyr32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+16.10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD2'))] = cmd.select('tyr33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+16.79,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','OH'),('rasp','CG'))] = cmd.select('tyr34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.89,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','OH'),('rasp','OD1'))] = cmd.select('tyr35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.25,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','OH'),('rasp','OD2'))] = cmd.select('tyr36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+16.09,resSelectionSubs('asp','OD2',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27&br. tyr28&br. tyr29&br. tyr30&br. tyr31&br. tyr32&br. tyr33&br. tyr34&br. tyr35&br. tyr36')
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
cmd.delete('tyr28')
cmd.delete('tyr29')
cmd.delete('tyr30')
cmd.delete('tyr31')
cmd.delete('tyr32')
cmd.delete('tyr33')
cmd.delete('tyr34')
cmd.delete('tyr35')
cmd.delete('tyr36')
IDSpec[(('his','CE1'),('styr','CE1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.33,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','CE1'),('styr','CZ'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.32,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('styr','OH'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.40,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','CE1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.06,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','CZ'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.14,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','OH'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.32,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','CE1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.05,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','CZ'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','OH'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.20,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','CE1'),('rarg','CZ'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.14,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','CE1'),('rarg','NE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.90,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','CE1'),('rarg','NH1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.21,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','ND1'),('rarg','CZ'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.39,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','ND1'),('rarg','NE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.09,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','ND1'),('rarg','NH1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.34,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','NE2'),('rarg','CZ'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.85,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','NE2'),('rarg','NE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.64,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','NE2'),('rarg','NH1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.95,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','CE1'),('rtyr_i','CE1'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.77,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('his','CE1'),('rtyr_i','CZ'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.48,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('his','CE1'),('rtyr_i','OH'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.30,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('his','ND1'),('rtyr_i','CE1'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.77,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('his','ND1'),('rtyr_i','CZ'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.67,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('his','ND1'),('rtyr_i','OH'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.57,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('his','NE2'),('rtyr_i','CE1'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.46,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('his','NE2'),('rtyr_i','CZ'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.89,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('his','NE2'),('rtyr_i','OH'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.55,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his28', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.76,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his29', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.91,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his30', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.25,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his31', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.62,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his32', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.96,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his33', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.01,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his34', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.74,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his35', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.04,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his36', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.10,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('arg','CZ'),('styr','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.58,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','CZ'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.07,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','OH'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.35,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.46,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CZ'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.84,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','OH'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.84,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.26,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CZ'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.80,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','OH'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.30,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','CE1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.14,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','ND1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.39,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','NE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.85,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','CE1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.90,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','ND1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.09,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','NE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.64,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','CE1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.21,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','ND1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.34,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','NE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.95,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rtyr_i','CE1'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.63,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('arg','CZ'),('rtyr_i','CZ'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.66,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('arg','CZ'),('rtyr_i','OH'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.38,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('arg','NE'),('rtyr_i','CE1'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.63,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('arg','NE'),('rtyr_i','CZ'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.72,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('arg','NE'),('rtyr_i','OH'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.40,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('arg','NH1'),('rtyr_i','CE1'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.88,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('arg','NH1'),('rtyr_i','CZ'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.94,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('arg','NH1'),('rtyr_i','OH'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.64,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('arg','CZ'),('rasp','CG'))] = cmd.select('arg28', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.38,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','CZ'),('rasp','OD1'))] = cmd.select('arg29', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.19,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp','OD2'))] = cmd.select('arg30', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.26,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NE'),('rasp','CG'))] = cmd.select('arg31', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.06,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NE'),('rasp','OD1'))] = cmd.select('arg32', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.87,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NE'),('rasp','OD2'))] = cmd.select('arg33', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.94,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp','CG'))] = cmd.select('arg34', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.12,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NH1'),('rasp','OD1'))] = cmd.select('arg35', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.03,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp','OD2'))] = cmd.select('arg36', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.90,resSelectionSubs('asp','OD2',subs)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27&br. arg28&br. arg29&br. arg30&br. arg31&br. arg32&br. arg33&br. arg34&br. arg35&br. arg36')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
cmd.delete('arg28')
cmd.delete('arg29')
cmd.delete('arg30')
cmd.delete('arg31')
cmd.delete('arg32')
cmd.delete('arg33')
cmd.delete('arg34')
cmd.delete('arg35')
cmd.delete('arg36')
IDSpec[(('tyr_i','CE1'),('styr','CE1'))] = cmd.select('tyr_i1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.18,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('styr','CZ'))] = cmd.select('tyr_i2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.00,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('styr','OH'))] = cmd.select('tyr_i3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.80,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','CE1'))] = cmd.select('tyr_i4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+13.02,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','CZ'))] = cmd.select('tyr_i5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.76,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','OH'))] = cmd.select('tyr_i6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.53,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','CE1'))] = cmd.select('tyr_i7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.08,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','CZ'))] = cmd.select('tyr_i8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.86,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','OH'))] = cmd.select('tyr_i9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.68,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('shis','CE1'))] = cmd.select('tyr_i10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.77,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('shis','ND1'))] = cmd.select('tyr_i11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.77,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('shis','NE2'))] = cmd.select('tyr_i12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('shis','CE1'))] = cmd.select('tyr_i13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.48,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('shis','ND1'))] = cmd.select('tyr_i14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.67,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('shis','NE2'))] = cmd.select('tyr_i15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.89,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('shis','CE1'))] = cmd.select('tyr_i16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.30,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('shis','ND1'))] = cmd.select('tyr_i17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.57,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('shis','NE2'))] = cmd.select('tyr_i18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.55,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sarg','CZ'))] = cmd.select('tyr_i19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.63,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sarg','NE'))] = cmd.select('tyr_i20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.63,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sarg','NH1'))] = cmd.select('tyr_i21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.88,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sarg','CZ'))] = cmd.select('tyr_i22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.66,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sarg','NE'))] = cmd.select('tyr_i23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.72,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sarg','NH1'))] = cmd.select('tyr_i24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+13.94,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sarg','CZ'))] = cmd.select('tyr_i25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.38,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sarg','NE'))] = cmd.select('tyr_i26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.40,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sarg','NH1'))] = cmd.select('tyr_i27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.64,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('rasp','CG'))] = cmd.select('tyr_i28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.75,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr_i','CE1'),('rasp','OD1'))] = cmd.select('tyr_i29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.58,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr_i','CE1'),('rasp','OD2'))] = cmd.select('tyr_i30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.67,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr_i','CZ'),('rasp','CG'))] = cmd.select('tyr_i31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.20,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr_i','CZ'),('rasp','OD1'))] = cmd.select('tyr_i32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.04,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr_i','CZ'),('rasp','OD2'))] = cmd.select('tyr_i33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.00,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr_i','OH'),('rasp','CG'))] = cmd.select('tyr_i34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.49,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr_i','OH'),('rasp','OD1'))] = cmd.select('tyr_i35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.39,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr_i','OH'),('rasp','OD2'))] = cmd.select('tyr_i36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.19,resSelectionSubs('asp','OD2',subs)))
IDSpec['tyr_i'] = cmd.select('tyr_i',' br. tyr_i1&br. tyr_i2&br. tyr_i3&br. tyr_i4&br. tyr_i5&br. tyr_i6&br. tyr_i7&br. tyr_i8&br. tyr_i9&br. tyr_i10&br. tyr_i11&br. tyr_i12&br. tyr_i13&br. tyr_i14&br. tyr_i15&br. tyr_i16&br. tyr_i17&br. tyr_i18&br. tyr_i19&br. tyr_i20&br. tyr_i21&br. tyr_i22&br. tyr_i23&br. tyr_i24&br. tyr_i25&br. tyr_i26&br. tyr_i27&br. tyr_i28&br. tyr_i29&br. tyr_i30&br. tyr_i31&br. tyr_i32&br. tyr_i33&br. tyr_i34&br. tyr_i35&br. tyr_i36')
IDSpec['r_tyr_i'] = cmd.count_atoms(resSelectionSubs('tyr_i', subs=subs, selection=True))
cmd.delete('tyr_i1')
cmd.delete('tyr_i2')
cmd.delete('tyr_i3')
cmd.delete('tyr_i4')
cmd.delete('tyr_i5')
cmd.delete('tyr_i6')
cmd.delete('tyr_i7')
cmd.delete('tyr_i8')
cmd.delete('tyr_i9')
cmd.delete('tyr_i10')
cmd.delete('tyr_i11')
cmd.delete('tyr_i12')
cmd.delete('tyr_i13')
cmd.delete('tyr_i14')
cmd.delete('tyr_i15')
cmd.delete('tyr_i16')
cmd.delete('tyr_i17')
cmd.delete('tyr_i18')
cmd.delete('tyr_i19')
cmd.delete('tyr_i20')
cmd.delete('tyr_i21')
cmd.delete('tyr_i22')
cmd.delete('tyr_i23')
cmd.delete('tyr_i24')
cmd.delete('tyr_i25')
cmd.delete('tyr_i26')
cmd.delete('tyr_i27')
cmd.delete('tyr_i28')
cmd.delete('tyr_i29')
cmd.delete('tyr_i30')
cmd.delete('tyr_i31')
cmd.delete('tyr_i32')
cmd.delete('tyr_i33')
cmd.delete('tyr_i34')
cmd.delete('tyr_i35')
cmd.delete('tyr_i36')
IDSpec[(('asp','CG'),('styr','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.47,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CZ'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.65,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','OH'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.89,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.00,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CZ'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.10,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','OH'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.25,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.64,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CZ'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.79,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','OH'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.09,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.76,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.62,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.74,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.91,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.96,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.04,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.25,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.01,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.10,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','CZ'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.38,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.06,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NH1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.12,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','CZ'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.19,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.87,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NH1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.03,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','CZ'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.26,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.94,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NH1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.90,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr_i','CE1'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.75,resSelectionSubs('tyr_i','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr_i','CZ'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.20,resSelectionSubs('tyr_i','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('styr_i','OH'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.49,resSelectionSubs('tyr_i','OH',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr_i','CE1'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.58,resSelectionSubs('tyr_i','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr_i','CZ'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.04,resSelectionSubs('tyr_i','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr_i','OH'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.39,resSelectionSubs('tyr_i','OH',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr_i','CE1'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.67,resSelectionSubs('tyr_i','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr_i','CZ'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.00,resSelectionSubs('tyr_i','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr_i','OH'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.19,resSelectionSubs('tyr_i','OH',subs,selection=True)))
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
IDSpec['S_1al8_1_1_3_15'] = cmd.select('S_1al8_1_1_3_15', 'tyr|his|arg|tyr_i|asp')
cmd.delete('tyr')
cmd.delete('his')
cmd.delete('arg')
cmd.delete('tyr_i')
cmd.delete('asp')