# -*- coding: utf-8 -*-

# 日期：2020-3-12
# 作者：YangZai
# 功能：外星人游戏

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
#	初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
		ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
#	创建一艘飞船
	ship = Ship(ai_settings, screen)
#	创建一个用于存储子弹的编组
	bullets = Group()
#	创建一个外星人的编组
	aliens = Group()
#	创建外星人群
	gf.create_fleet(ai_settings, screen, aliens)
#	创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
#	创建记分牌
	score_board = Scoreboard(ai_settings, screen, stats)
#	创建Play按钮
	play_button = Button(ai_settings, screen, 'Play')
	
#	开始游戏主循环
	while True:
		# 监视鼠标和键盘事件：
		gf.check_events(ai_settings, screen, stats, ship, aliens, bullets,
			play_button, score_board)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, aliens, bullets,
				score_board)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets,
				score_board)

		# 更新屏幕
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
			play_button, score_board)
		
run_game()
