'''
FUNC:Jab_1bd4_2_4_2_9
PDB:1bd4
EC:2.4.2.9
RESI:arg,thr,asp
LOCI:a-137,141,235;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. arg'
jesstemp4 ='jessatom0 x. %s'%(1.531530+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp6 ='r. thr'
jesstemp7 ='r. ser'
jesstemp8 ='jessatom0 x. %s'%(7.947940+(d*0.050000))
jesstemp8 = '('+jesstemp8+') and not (jessatom0 x. %s)'%(max(0.05,7.932068-(d*0.050000)))
jesstemp9 ='jessatom1 x. %s'%(8.008000+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,7.992008-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(7.947940+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,7.932068-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(8.008000+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,7.992008-(d*0.050000))))
jesstemp10 ='jessatom0 x. %s'%(7.897890+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom0 x. %s)'%(max(0.05,7.882118-(d*0.050000)))
jesstemp11 ='jessatom1 x. %s'%(8.168160+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom1 x. %s)'%(max(0.05,8.151848-(d*0.050000)))
jesstemp12 ='jessatom2 x. %s'%(1.541540+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom2 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.897890+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,7.882118-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.168160+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,8.151848-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp14 ='r. asp'
jesstemp15 ='r. glu'
jesstemp16 ='jessatom0 x. %s'%(15.625610+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom0 x. %s)'%(max(0.05,15.594406-(d*0.050000)))
jesstemp17 ='jessatom1 x. %s'%(14.504490+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom1 x. %s)'%(max(0.05,14.475524-(d*0.050000)))
jesstemp18 ='jessatom2 x. %s'%(21.271250+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom2 x. %s)'%(max(0.05,21.228771-(d*0.050000)))
jesstemp19 ='jessatom3 x. %s'%(21.951930+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom3 x. %s)'%(max(0.05,21.908092-(d*0.050000)))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp14+'))|(('+jesstemp0+')&('+jesstemp15+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(15.625610+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,15.594406-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(14.504490+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,14.475524-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(21.271250+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,21.228771-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(21.951930+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,21.908092-(d*0.050000))))
jesstemp20 ='jessatom0 x. %s'%(15.065050+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom0 x. %s)'%(max(0.05,15.034965-(d*0.050000)))
jesstemp21 ='jessatom1 x. %s'%(13.973960+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom1 x. %s)'%(max(0.05,13.946054-(d*0.050000)))
jesstemp22 ='jessatom2 x. %s'%(20.670650+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom2 x. %s)'%(max(0.05,20.629371-(d*0.050000)))
jesstemp23 ='jessatom3 x. %s'%(21.391370+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom3 x. %s)'%(max(0.05,21.348651-(d*0.050000)))
jesstemp24 ='jessatom4 x. %s'%(1.531530+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom4 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp14+'))|(('+jesstemp2+')&('+jesstemp15+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(15.065050+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,15.034965-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.973960+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,13.946054-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(20.670650+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,20.629371-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(21.391370+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,21.348651-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
cmd.select('Jab_1bd4_2_4_2_9', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
