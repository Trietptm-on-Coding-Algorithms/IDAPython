# *** Function ***

#Functions(StartAddress, EndAddress)
print(Functions(0x401000, 0x402000))
#-> [4198400, 4198443, 4198553, 4199366, 4199372, 4199378, 4199384, 4199390, 4199396, 4199402, 4199408, 4199414, 4199420, 4199426, 4199432, 4199438, 4199444, 4199456]

#GetFunctionName(Address)
print([GetFunctionName(i) for i in Functions(0x401000 ,0x402000)])
#-> ['start', 'sub_40102B', 'DialogFunc', 'CallWindowProcA', 'DialogBoxParamA', 'EndDialog', 'GetDlgItem', 'GetDlgItemInt', 'GetWindowTextA', 'LoadIconA', 'MessageBoxA', 'SendMessageA', 'SetWindowLongA', 'SetWindowTextA', 'ShowWindow', 'ExitProcess', 'GetModuleHandleA', 'sub_401420']

#Chunks(FunctionAddress)
print(Chunks(4198400))
#-> [(4198400, 4198443)]

#print([hex(i) for i in Chunks(LocByName("CallWindowProcA"))])
print(Chunks(LocByName("CallWindowProcA")))
#-> [(4199366, 4199372)]

#LocByName(FunctionName)
print(hex(LocByName("CallWindowProcA")))
#-> 0x4013c6

#GetFuncOffset(Address)
print(GetFuncOffset(4198402))
#-> start+2

