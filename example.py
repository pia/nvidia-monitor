from pynvml import *

nvmlInit()
print("Driver: ".format(nvmlSystemGetDriverVersion()))  # 显示驱动信息
# >>> Driver: 384.xxx

# 查看设备
deviceCount = nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = nvmlDeviceGetHandleByIndex(i)
    print("GPU", i, ":", nvmlDeviceGetName(handle))
# >>>
# GPU 0 : b'GeForce GTX 1080 Ti'
# GPU 1 : b'GeForce GTX 1080 Ti'

# 查看显存、温度、风扇、电源
handle = nvmlDeviceGetHandleByIndex(0)
info = nvmlDeviceGetMemoryInfo(handle)
print("Memory Total: ", info.total)
print("Memory Free: ", info.free)
print("Memory Used: ", info.used)

print("Temperature is %d C" % nvmlDeviceGetTemperature(handle, 0))
print("Fan speed is {}".format(nvmlDeviceGetFanSpeed(handle)))
print("Power ststus {}".format(nvmlDeviceGetPowerState(handle)))

# 最后要关闭管理工具
nvmlShutdown()
