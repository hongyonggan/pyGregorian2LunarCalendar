# 工具拓展模块
# author: cuba3
# github: https://github.com/cuba3/pyGregorian2LunarCalendar

# 去除空行
from config import encryptionVectorList


def not_empty(s):
    return s and s.strip()

# 两个List合并对应元素相加或者相减，a[i]+b[i]:tpye=1 a[i]-b[i]:tpye=-1
def abListMerge(a, b=encryptionVectorList, type=1):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i]*type)
    return c