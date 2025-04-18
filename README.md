# 八字 (BaZi) - 四柱命理分析工具

这是一个精简版的八字（四柱命理）分析工具，主要包含以下功能：

- 八字排盘计算
- 五行强弱分析（五行分数）
- 吉凶神煞分析
- 喜用神计算
- 大运流年分析
- 性格特点分析

## 依赖安装

```
pip install -r requirements.txt
```

## 使用方法

### 八字排盘

```bash
# 使用公历
python bazi.py -g 年 月 日 时

# 使用农历
python bazi.py 年 月 日 时

# 使用农历闰月
python bazi.py -r 年 月 日 时

# 女命分析（默认为男命）
python bazi.py -n 年 月 日 时
```

### 示例

```bash
# 公历 1990年8月23日 12时 女命
python bazi.py -g 1990 8 23 12 -n

# 农历 1990年七月初三 12时 男命
python bazi.py 1990 7 3 12
```

## 输出内容说明

输出结果包括：

1. 基本信息：出生年月日时、干支纳音
2. 五行分数：计算日主五行强弱
3. 五行关系：生克冲合刑害等关系
4. 神煞分析：天罡、孤鸾等特殊神煞的影响
5. 大运分析：未来大运走向
6. 性格分析：基于八字的性格特点描述

## 注意事项

- 时辰对照表：子(23-1)、丑(1-3)、寅(3-5)、卯(5-7)、辰(7-9)、巳(9-11)、
  午(11-13)、未(13-15)、申(15-17)、酉(17-19)、戌(19-21)、亥(21-23)
- 输入时辰时，请使用24小时制的整数小时数

## 文件说明

该项目已经精简，仅保留核心功能文件：

- bazi.py - 主程序
- datas.py - 数据文件
- common.py - 通用函数
- ganzhi.py - 干支处理函数
- yue.py - 月令处理
- sizi.py - 四柱分析
