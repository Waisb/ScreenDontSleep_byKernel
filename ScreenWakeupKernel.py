import ctypes
import time

# Флаги для windll.kernel32.SetThreadExecutionState
# SetThreadExecutionState отвечет за состояние потоков где потоки могут передавать состояние "пассивности" системы
# https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002
ES_UPDATE_TIMEOUT = 120 # Таймаут для перезаписи значений
HIDE_IN_TRAY = True

def prevent_sleep_and_display_off():
    print(f"[+] Forcing kernel.SetThreadExecutionState:\n\tES_CONTINUOUS - {hex(ES_CONTINUOUS)}\n\tES_SYSTEM_REQUIRED - {hex(ES_SYSTEM_REQUIRED)}\n\tES_DISPLAY_REQUIRED - {hex(ES_DISPLAY_REQUIRED)}\n")
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

try:
    while True:
        prevent_sleep_and_display_off()
        print(f"[+] Going sleep for {ES_UPDATE_TIMEOUT} seconds")
        time.sleep(ES_UPDATE_TIMEOUT)
except KeyboardInterrupt:
    pass
except Exception as ERROR:
    print(str(ERROR))
    input("Press any key")
