# -*- coding: utf-8 -*-
# @BY       : 爱读书的番茄君
# @Time     : 2022/3/21 23:11

from datetime import datetime
import time
import pymysql
import requests
import json


# 连接数据库
def mysql():

    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='lpl',
        charset='utf-8')
    cur = db.cursor()
    return db, cur


def get_html(url, headers):
    """
    连接网页
    :param headers: 请求头
    :param url: 网页URL
    :return: 返回网页文本
    """
    r = requests.get(url=url, headers=headers, timeout=30)
    # 判断是否连接成功
    if not r.raise_for_status():
        r.encoding = 'utf-8'  # utf-8格式
        return r.text
    return None


# 获取队伍排名信息
def team_ranking():

    # 构造请求头
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/34.0.1847.137 Safari/537.36 LBBROWSER',
               "origin": "https://lpl.qq.com",
               "referer": "https://lpl.qq.com",
               "accept-encoding": "gzip, deflate, br",
               "accept-language": "zh-CN,zh;q=0.9",
               "authorization": "7935be4c41d8760a28c05581a7b1f570",
               "content-type": "application/json"
               }
    team_ranking_url = "https://open.tjstats.com/match-auth-app/open/v1/compound/team?seasonId=167&stageIds=1%2C5"
    team_ranking_info = get_html(team_ranking_url, headers)  # 发起请求
    team_ranking_info = json.loads(team_ranking_info)  # 转为json格式
    # print(team_ranking_info)
    team_ranking_info = team_ranking_info["data"]
    # print(team_ranking_info)

    for info in team_ranking_info:
        print(info)
        teamId = info["teamId"]  # 队伍ID
        teamName = info["teamName"]  # 队伍名称
        matchCount = info["matchCount"]  # 出场次数
        teamLogo = info["teamLogo"]  # 队伍Logo下载地址
        matchWinCount = info["matchWinCount"]  # 胜场次数
        winningRate = info["winningRate"]  # 胜率
        totalKills = info["totalKills"]  # 总击杀人数
        killPerGameTeam = info["killPerGameTeam"]  # 场均击杀
        totalDeath = info["totalDeath"]  # 总死亡
        deathPerGameTeam = info["deathPerGameTeam"]  # 场均死亡
        wardPlacedPerGameTeam = info["wardPlacedPerGameTeam"]  # 场均插眼数量
        wardKilledPerGameTeam = info["wardKilledPerGameTeam"]  # 场均排眼数量
        goldPerGameTeam = info["goldPerGameTeam"]  # 场均金钱
        baronKillPerGameTeam = info["baronKillPerGameTeam"]  # 场均大龙
        drakeKillPerGameTeam = info["drakeKillPerGameTeam"]  # 场均小龙
        kad = info["kda"]  # kda
        timePerGameTeam = info["timePerGameTeam"]  # 场均时长
        timePerGameWinTeam = info["timePerGameWinTeam"]  # 胜时场均时长
        timePerGameLoseTeam = info["timePerGameLoseTeam"]  # 负时场均时长
        firstBloodWinRate = info["firstBloodWinRate"]  # 一血胜率
        blueGameCount = info["blueGameCount"]  # 蓝方小场胜场数量
        blueGameWinRate = info["blueGameWinRate"]  # 蓝方小场胜场胜率
        redGameCount = info["redGameCount"]  # 红方小场胜场数量
        redGameWinRate = info["redGameWinRate"]  # 红方小场胜场胜率
        baronControlRate = info["baronControlRate"]  # 男爵大龙控制率

        break


team_ranking()