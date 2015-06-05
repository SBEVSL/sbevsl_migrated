'''
FUNC:Jab_1nwc
PDB:1nwc
EC:1.2.1.11
PFAM:PF01118,PF02774
RESI:cys,gln,his
LOCI:a-136,163,277;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. cys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. cys'
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. gln'
jesstemp7 ='r. asn'
jesstemp8 ='jessatom0 x. %s'%(9.706100+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(8.776900+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(9.706100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(8.776900+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(8.978900+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(8.100200+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.978900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.100200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp14 ='r. his'
jesstemp15 ='jessatom0 x. %s'%(8.150700+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(7.393200+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(4.423800+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(5.231800+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.150700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.393200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.423800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(5.231800+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(6.716500+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(6.060000+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(4.595500+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(4.949000+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.716500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.060000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1nwc', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
