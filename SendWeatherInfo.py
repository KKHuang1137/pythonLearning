# -*- coding: utf-8 -*-
import random

import requests
from datetime import datetime
import time


class DailyTips(object):

    def __init__(self, city):
        self.key = 自己的key,
        self.city = city
        self.headers = {'Content-type': 'application/x-www-form-urlencoded'}
        self.weather = ""

    def weathers(self):

        try:
            params = {"key": self.key, "city": self.city}
            url = "http://api.tianapi.com/tianqi/index"
            r = requests.post(url=url, params=params, headers=self.headers).json()  # 访问API，获取数据
            info = r["newslist"][0]  # 当天数据
            # print(info)
            now = datetime.now()  # 当前时间
            now_time = datetime.strftime(now, "北京时间%Y年%m月%d日 %H:%M")  # 格式化输出时间
            # print(now_time)

            """
            现在是(星期一)，(北京时间 2022年3月18日 20：50)，(宝安)实时天气为(23°)，最低温度(18°)，最高温度(24°)，(晴转多云)。
            目前风力是(1-2级)，降雨概率为(50)%，紫外线强度指数(9)，相对湿度(23)%。温馨小tips：(天气暖和，适合外出)
            """
            week = info["week"]  # 星期
            area = info["area"]  # 地区
            real = info["real"]  # 实时温度
            lowest = info["lowest"]  # 最低温度
            highest = info["real"]  # 最高温度
            self.weather = info["weather"]  # 天气，该值可用来获取对应的天气诗句
            windsc = info["windsc"]  # 风力
            pop = info["pop"]  # 降雨概率
            uv_index = info["uv_index"]  # 紫外线强度指数
            humidity = info["humidity"]  # 相对湿度
            tips = info["tips"]  # 生活指数提示

            text = "现在是{}，{}，{}实时天气为{}，最低温度{}，最高温度{}，{}。目前风力是{}，降雨概率为{}%，紫外线强度指数{}，" \
                   "相对湿度{}。温馨小tips：{}"  # 输出文本
            # 格式化输出
            text = text.format(week, now_time, area, real, lowest, highest,
                               self.weather, windsc, pop, uv_index, humidity, tips)

            # print(text)
            return text

        except AttributeError as a:
            return "天气字典信息获取失败..."


    def weather_type(self):
        """1 = 风、2 = 云、3 = 雨、4 = 雪、5 = 霜、6 = 露 、7 = 雾、8 = 雷、9 = 晴、10 = 阴"""
        dict_item = {
            "风": 1, "云": 2, "雨": 3, "雪": 4, "霜": 5, "露": 6, "雾": 7, "雷": 8, "晴": 9, "阴": 10}
        if self.weather != "":  # 判断天气是否为空，
            for key in dict_item.keys():  # 遍历字典
                if key in self.weather:
                    return dict_item[key]  # 获取天气对应的数值
            return None  # 不在字典内，返回空值
        else:
            return None


    def weather_poems(self):
        """获取天气对应的诗句"""
        try:
            tqtype = self.weather_type()  # 天气类型
            params = {"key": self.key, "tqtype": tqtype}  # key号
            url = "http://api.tianapi.com/tianqishiju/index"
            r = requests.get(url=url, params=params, headers=self.headers).json()
            return r["newslist"][0]["content"]
        except AttributeError as a:
            return "天气诗句获取失败..."


    def love_poems(self):
        """获取情诗"""
        try:
            url = "http://api.tianapi.com/qingshi/index"
            params = {"key": self.key}
            r = requests.get(url=url, params=params).json()
            return r["newslist"][0]["content"]
        except AttributeError as a:
            return "情诗获取失败..."

    def combine_text(self):
        """合并文本"""
        nameList = ["亲爱的小宝贝儿", "小宝", "小宝儿", "宝贝儿", "亲爱的老婆", "亲爱的", "小宝贝儿", "老婆"]
        name = random.choice(nameList)
        # love_poem = self.love_poems()  # 企业微信API信息太长，字符串超过230个就发不出去，取消情诗
        love_poem = ""
        weather = self.weathers()

        now_day = datetime.now().strftime('%Y-%m-%d')  # 当前的天数
        start_day = "2021-10-06"

        # 计算两个日期中的时间差天数
        time_array1 = time.strptime(start_day, "%Y-%m-%d")
        timestamp_day1 = int(time.mktime(time_array1))
        time_array2 = time.strptime(now_day, "%Y-%m-%d")
        timestamp_day2 = int(time.mktime(time_array2))
        interval = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24

        """
        (众里寻他千百度，那人却在灯火阑珊处。)
        (小宝儿)，该起床啦。(天气描述)
        （宝贝儿），今天是我们在一起的第(161)天，也是我们未来在一起很多很多天的一天。爱你哟，我的小宝贝儿，mua~
        """
        text_total = "{}\n{}，该起床啦。\n{}\n{}，今天是我们在一起的第{}天，" \
                     "也是我们未来在一起很多很多天的一天。爱你哟，我的小宝贝儿，mua~"

        text_total = text_total.format(love_poem, name, weather, name, interval)  # 格式化输出
        return text_total


class SendInfo(object):

    def __init__(self, text):
        self.text = text


    def sendByWechat(self):

        url_vx = "https://api.htm.fun/api/Wechat/text/"
        params = {
            "corpid": 企业微信corpid,
            "corpsecret": 企业微信secret,
            "agentid": 企业微信应用id,
            "text": self.text
        }
        r = requests.post(url_vx, params=params)
        print("发送成功")





def main():
    dailytips = DailyTips("宝安")
    text = dailytips.combine_text()
    sendInfo = SendInfo(text)
    sendInfo.sendByWechat()



if __name__ == '__main__':
    main()
