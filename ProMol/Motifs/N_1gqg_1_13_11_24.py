'''
FUNC:N_1gqg_1_13_11_24
PDB:1gqg
EC:1.13.11.24
RESI:glu,cu
LOCI:a-73,1352;
'''
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CU&r. cu'%(d*7.47))
cmd.select('glu2', 'n. CG&r. glu w. %s of n. CU&r. cu'%(d*6.61))
cmd.select('glu3', 'n. CD&r. glu w. %s of n. CU&r. cu'%(d*6.71))
cmd.select('glu4', 'n. OE1&r. glu w. %s of n. CU&r. cu'%(d*6.63))
cmd.select('glu5', 'n. OE2&r. glu w. %s of n. CU&r. cu'%(d*7.35))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.select('cu1', 'n. CU&r. cu w. %s of n. CB&glu'%(d*7.47))
cmd.select('cu2', 'n. CU&r. cu w. %s of n. CG&glu'%(d*6.61))
cmd.select('cu3', 'n. CU&r. cu w. %s of n. CD&glu'%(d*6.71))
cmd.select('cu4', 'n. CU&r. cu w. %s of n. OE1&glu'%(d*6.63))
cmd.select('cu5', 'n. CU&r. cu w. %s of n. OE2&glu'%(d*7.35))
cmd.select('cu',' br. cu1&br. cu2&br. cu3&br. cu4&br. cu5')
cmd.delete('cu1')
cmd.delete('cu2')
cmd.delete('cu3')
cmd.delete('cu4')
cmd.delete('cu5')
cmd.select('N_1gqg_1_13_11_24', 'glu|cu')
cmd.delete('glu')
cmd.delete('cu')
