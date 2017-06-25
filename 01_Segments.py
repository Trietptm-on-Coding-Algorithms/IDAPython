#from idaapi import *

# ScreeenEA()
print("ScreenEA is " + hex(ScreenEA()))
#-> ScreenEA is 0x401013

#GetInputFileMD5()
print("MD5 is " + GetInputFileMD5())
#-> MD5 is e89e8a79184596b17210ba976e83abac

#FirstSeg()
print("FirstSegment is " + hex(FirstSeg()))
#-> FirstSegment is 0x401000

#NextSeg()
print("NextSegment is " + hex(NextSeg(FirstSeg())))

#SegByName(str)
print("SegByName:" + hex(SegByName(".data")))
#-> SegByName:0x403000

#SegEnd(long Address)
print("SegEnd is " + hex(SegEnd(int(0x402000))))
#-> SegEnd is 0x402040
# SegEndは[Segmentの終了アドレス+1]の値を出力するようです。
  
#SegStart(long Address)
print("SegStart is " + hex(SegStart(int(0x40203F))))
#-> SegStart is 0x402000

#SegName(long Address)
print("SegmentName is " + SegName(int(0x402000)))
#-> SegmentName is .idata

#Segments()
print([hex(i) for i in Segments()])
#->['0x401000','0x402000','0x402040','0x403000']

#セグメント一覧
print([SegName(i) for i in Segments()])
#-> ['.text', '.idata', '.rdata', '.data']

#loop
cnt = len(Segments())
seg1 = FirstSeg()
for i in range(cnt):
  print(hex(seg1) + " " + SegName(seg1))
  seg1 = NextSeg(seg1)
  
