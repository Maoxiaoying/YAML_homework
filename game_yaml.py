#!/usr/bin/env python
# —*— coding: utf-8 —*—

#!/usr/bin/env python
# —*— coding: utf-8 —*—
import yaml

class Game:
    def __init__(self):
        self.character_info = yaml.safe_load(open("./game_character.yml"))  #读取角色信息的yml文件，并存入character_info中
        #print(character_info)  #打印结果为：{'Sunshangxiang': {'hp': 1000, 'power': 150, 'skill': 2}, 'Xiaoqiao': {'hp': 800, 'power': 180, 'skill': 2.5}, 'Hanxin': {'hp': 1500, 'power': 200, 'skill': 1.5}, 'Yase': {'hp': 2000, 'power': 100, 'skill': 1.2}, 'default': ['Sunshangxiang', 'Xiaoqiao', 'Hanxin', 'Yase']}
        self.group1 = [self.character_info["default"][0],self.character_info["default"][1]]  #分组pk，第一轮为1,2pk
        #print(group1)  #打印结果：['Sunshangxiang', 'Xiaoqiao']
        self.group2 = [self.character_info["default"][2],self.character_info["default"][3]]  #第二轮为3,4pk
        #print(group2)  #打印结果：['Hanxin', 'Yase']
        self.group3 = []   #第三轮为第一、二轮中胜利的两个进行pk

    def bi_fight(self,group):  #定义一个两两pk函数，传入pk的两人信息，返回胜者信息
        man1_hp = self.character_info[group[0]]["hp"]      #传入选手1的血量
        man1_power = self.character_info[group[0]]["power"] #传入选手1的power
        man1_skill = self.character_info[group[0]]["skill"]  ##传入选手1的技能
        man2_hp = self.character_info[group[1]]["hp"]  #传入选手2的血量
        man2_power = self.character_info[group[1]]["power"]  #传入选手2的power
        man2_skill = self.character_info[group[1]]["skill"]  ##传入选手2的技能
        round = 0  #定义轮数
        while man1_hp > 0 and man2_hp >0:  #双方血量都大于0时进行对打，直到一方血量小于等于0停止
            if round % 3 == 0:  #每三轮会进行一次技能
                man1_hp = man1_hp - man2_power * man2_skill   #血量公式
                man2_hp = man2_hp - man1_power * man1_skill
            else:
                man1_hp = man1_hp - man2_power
                man2_hp = man2_hp - man1_power
        if man1_hp > 0:   #若结束时选手1血量为正，则他胜利
            return group[0]   #返回胜者姓名
        else:
            return group[1]

    def fight(self):  #定义游戏流程：两两pk，选出最终胜利的一方
        print("比赛正式开始，首先介绍今天的参赛选手，他们分别是：{}，{}，{}，{}".format(self.group1[0],self.group1[1],self.group2[0],self.group2[1]))
        print("----------------------------------------------------------------------------")
        print("第一轮，参赛选手：{}和{}".format(self.group1[0],self.group1[1]))
        print("第一轮胜利的是：{}".format(self.bi_fight(self.group1)))
        self.group3.append(self.bi_fight(self.group1))
        print("-----------------------------中场休息--------------------------------------")
        print("第二轮，参赛选手：{}和{}".format(self.group2[0],self.group2[1]))
        print("第二轮胜利的是：{}".format(self.bi_fight(self.group2)))
        self.group3.append(self.bi_fight(self.group2))
        print("-----------------------------中场休息--------------------------------------")
        print("第三轮，参赛选手：{}和{}".format(self.group3[0],self.group3[1]))
        print("第三轮胜利的是：{}".format(self.bi_fight(self.group3)))
        print("-----------------------------颁奖环节--------------------------------------")
        print("比赛结束，最终获胜的选手是{}".format(self.bi_fight(self.group3)))

game = Game()
game.fight()