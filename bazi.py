#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 钉钉、抖音或微信pythontesting 钉钉群21734177
# CreateDate: 2019-2-21

import argparse
import collections
import pprint
import datetime

from lunar_python import Lunar, Solar
from colorama import init

from datas import *
from sizi import summarys
from common import *
from yue import months

def get_gen(gan, zhis):
    zhus = []
    zhongs = []
    weis = []
    result = ""
    for item in zhis:
        zhu = zhi5_list[item][0]
        if ten_deities[gan]['本'] == ten_deities[zhu]['本']:
            zhus.append(item)

    for item in zhis:
        if len(zhi5_list[item]) ==1:
            continue
        zhong = zhi5_list[item][1]
        if ten_deities[gan]['本'] == ten_deities[zhong]['本']:
            zhongs.append(item)

    for item in zhis:
        if len(zhi5_list[item]) < 3:
            continue
        zhong = zhi5_list[item][2]
        if ten_deities[gan]['本'] == ten_deities[zhong]['本']:
            weis.append(item)

    if not (zhus or zhongs or weis):
        return "无根"
    else:
        result = result + "强：{}{}".format(''.join(zhus), chr(12288)) if zhus else result
        result = result + "中：{}{}".format(''.join(zhongs), chr(12288)) if zhongs else result
        result = result + "弱：{}".format(''.join(weis)) if weis else result
        return result


def gan_zhi_he(zhu):
    gan, zhi = zhu
    if ten_deities[gan]['合'] in zhi5[zhi]:
        return "|"
    return ""

def get_gong(zhis):
    result = []
    for i in range(3):
        if  gans[i] != gans[i+1]:
            continue
        zhi1 = zhis[i]
        zhi2 = zhis[i+1]
        if abs(Zhi.index(zhi1) - Zhi.index(zhi2)) == 2:
            value = Zhi[(Zhi.index(zhi1) + Zhi.index(zhi2))//2]
            #if value in ("丑", "辰", "未", "戌"):
            result.append(value)
        if (zhi1 + zhi2 in gong_he) and (gong_he[zhi1 + zhi2] not in zhis):
            result.append(gong_he[zhi1 + zhi2]) 
            
        #if (zhi1 + zhi2 in gong_hui) and (gong_hui[zhi1 + zhi2] not in zhis):
            #result.append(gong_hui[zhi1 + zhi2])             
        
    return result


def get_shens(gans, zhis, gan_, zhi_):
    
    all_shens = []
    for item in year_shens:
        if zhi_ in year_shens[item][zhis.year]:    
            all_shens.append(item)
                
    for item in month_shens:
        if gan_ in month_shens[item][zhis.month] or zhi_ in month_shens[item][zhis.month]:     
            all_shens.append(item)
                
    for item in day_shens:
        if zhi_ in day_shens[item][zhis.day]:     
            all_shens.append(item)
                
    for item in g_shens:
        if zhi_ in g_shens[item][me]:    
            all_shens.append(item) 
    if all_shens:  
        return "  神:" + ' '.join(all_shens)
    else:
        return ""
                
def jin_jiao(first, second):
    return True if Zhi.index(second) - Zhi.index(first) == 1 else False

def is_ku(zhi):
    return True if zhi in "辰戌丑未" else False  

def zhi_ku(zhi, items):
    return True if is_ku(zhi) and min(zhi5[zhi], key=zhi5[zhi].get) in items else False

def is_yang():
    return True if Gan.index(me) % 2 == 0 else False

def not_yang():
    return False if Gan.index(me) % 2 == 0 else True

def gan_ke(gan1, gan2):
    return True if ten_deities[gan1]['克'] == ten_deities[gan2]['本'] or ten_deities[gan2]['克'] == ten_deities[gan1]['本'] else False
    
description = '''

'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('year', action="store", help=u'year')
parser.add_argument('month', action="store", help=u'month')
parser.add_argument('day', action="store", help=u'day')
parser.add_argument('time', action="store",help=u'time')    
parser.add_argument("--start", help="start year", type=int, default=1850)
parser.add_argument("--end", help="end year", default='2030')
parser.add_argument('-b', action="store_true", default=False, help=u'直接输入八字')
parser.add_argument('-g', action="store_true", default=False, help=u'是否采用公历')
parser.add_argument('-r', action="store_true", default=False, help=u'是否为闰月，仅仅使用于农历')
parser.add_argument('-n', action="store_true", default=False, help=u'是否为女，默认为男')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2022 06 15')
options = parser.parse_args()

Gans = collections.namedtuple("Gans", "year month day time")
Zhis = collections.namedtuple("Zhis", "year month day time")

print("-"*120)

if options.b:
    import sxtwl
    gans = Gans(year=options.year[0], month=options.month[0], 
                day=options.day[0],  time=options.time[0])
    zhis = Gans(year=options.year[1], month=options.month[1], 
                day=options.day[1],  time=options.time[1])
    jds = sxtwl.siZhu2Year(getGZ(options.year), getGZ(options.month), getGZ(options.day), getGZ(options.time), options.start, int(options.end));
    for jd in jds:
        t = sxtwl.JD2DD(jd )
        print("可能出生时间: python bazi.py -g %d %d %d %d :%d:%d"%(t.Y, t.M, t.D, t.h, t.m, round(t.s)))   
    
else:

    if options.g:
        solar = Solar.fromYmdHms(int(options.year), int(options.month), int(options.day), int(options.time), 0, 0)
        lunar = solar.getLunar()
    else:
        month_ = int(options.month)*-1 if options.r else int(options.month)
        lunar = Lunar.fromYmdHms(int(options.year), month_, int(options.day),int(options.time), 0, 0)
        solar = lunar.getSolar()

    day = lunar
    ba = lunar.getEightChar() 
    gans = Gans(year=ba.getYearGan(), month=ba.getMonthGan(), day=ba.getDayGan(), time=ba.getTimeGan())
    zhis = Zhis(year=ba.getYearZhi(), month=ba.getMonthZhi(), day=ba.getDayZhi(), time=ba.getTimeZhi())


me = gans.day
month = zhis.month
alls = list(gans) + list(zhis)
zhus = [item for item in zip(gans, zhis)]

gan_shens = []
for seq, item in enumerate(gans):    
    if seq == 2:
        gan_shens.append('--')
    else:
        gan_shens.append(ten_deities[me][item])

zhi_shens = [] # The main gods of the terrestrial branches
for item in zhis:
    d = zhi5[item]
    zhi_shens.append(ten_deities[me][max(d, key=d.get)])

shens = gan_shens + zhi_shens

zhi_shens2 = [] # All gods of the terrestrial branches, including residual and tail gas, mixed together
zhi_shen3 = [] # All gods of the terrestrial branches, string format
for item in zhis:
    d = zhi5[item]
    tmp = ''
    for item2 in d:
        zhi_shens2.append(ten_deities[me][item2])
        tmp += ten_deities[me][item2]
    zhi_shen3.append(tmp)
shens2 = gan_shens + zhi_shens2

# Calculate minggong and taiyuan
minggong = Zhi[(Zhi.index(zhis.month) + 1) % 12]
taiyuan = Gan[(Gan.index(gans.month) + 1) % 10] + Zhi[(Zhi.index(zhis.month) + 3) % 12]

# Get shang operation time
def get_shang(yZhi, yGan, mZhi, mGan):
    # This is a placeholder - the real implementation would need the actual algorithm
    return "10岁"

# Only keep the output for the basic four pillar information and dayun section

sex = "女" if options.n else "男"
print("{}命".format(sex), end=' ')
print("\t公历:", end=' ')
print("{}年{}月{}日".format(solar.getYear(), solar.getMonth(), solar.getDay()), end=' ')

print("  农历:", end=' ')
print("{}年{}月{}日 穿=害 上运时间：{} 命宫:{} 胎元:{}".format(lunar.getYear(), lunar.getMonth(),
    lunar.getDay(), get_shang(zhis[0], gans[0], zhis[1], gans[1]), minggong, taiyuan))
    
print("\t", siling[zhis.month], lunar.getPrevJieQi(True), lunar.getPrevJieQi(True).getSolar().toYmdHms(),lunar.getNextJieQi(True),
      lunar.getNextJieQi(True).getSolar().toYmdHms())

print("-"*120)

# Print gans and zhis with their corresponding gods
out = " ".join(["{}{}{} ".format(alls[i], ten_deities[me][alls[i]], gan_zhi_he(zhus[i//2])) for i in range(4)])
print('\033[1;36;40m' + ' '.join(list(gans)), ' '*5, ' '.join(list(gan_shens)) + '\033[0m',' '*5, out)

out = " 四柱：" + ' '.join([''.join(item) for item in zip(gans, zhis)])
print('\033[1;36;40m' + ' '.join(list(zhis)), ' '*5, ' '.join(list(zhi_shens)) + '\033[0m', ' '*5, out)
print("-"*120)

# Display the Dayun information
print()
print("-"*120)
print("大运：", end=' ')
running_age = 10
for i in range(8):
    dayun = Gan[(Gan.index(gans.month) + i + 1) % 10] + Zhi[(Zhi.index(zhis.month) + i + 1) % 12]
    print("{}~{}{}".format(running_age, running_age+9, dayun), end=' ')
    running_age += 10
print()

# Display the Dayun detailed information
dayun_ages = [(i * 10 + 10, i * 10 + 19) for i in range(8)]  # (start_age, end_age) pairs

# Calculate current age based on birth year and current year
birth_year = solar.getYear()
current_year = datetime.datetime.now().year
current_age = current_year - birth_year

# Determine which dayun the person is currently in
current_dayun_index = -1
for i, (start_age, end_age) in enumerate(dayun_ages):
    if start_age <= current_age <= end_age:
        current_dayun_index = i
        break

# Display details for each dayun
for i in range(8):
    start_age, end_age = dayun_ages[i]
    dayun_gan = Gan[(Gan.index(gans.month) + i + 1) % 10]
    dayun_zhi = Zhi[(Zhi.index(zhis.month) + i + 1) % 12]
    
    # Calculate years for this dayun period
    start_year = birth_year + start_age
    end_year = birth_year + end_age
    
    # Format and display the dayun information
    current_marker = "◎" if i == current_dayun_index else "　"
    
    # Display elements for this dayun
    elements_str = ""
    for element in zhi5[dayun_zhi]:
        elements_str += f"{element}{ten_deities[me][element]} "
    
    # Fix the nayin lookup - use tuple (dayun_gan, dayun_zhi) instead of string concatenation
    nayin_str = nayins.get((dayun_gan, dayun_zhi), "未知")
    
    print(f"{current_marker}{start_age}~{end_age}岁 {start_year}~{end_year}年 {dayun_gan}{dayun_zhi} {nayin_str} {ten_deities[me][dayun_gan]} - {elements_str.strip()}")
