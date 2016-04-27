# -*- coding: utf-8 -*-
import unittest
from time import sleep
from driver import Driver

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass'
        cls.driver = Driver().sgDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()
        print 'tearDownClass'

    # def setUp(self):
    #     print "setup"
    #
    # def tearDown(self):
    #     print 'teardown'

    # def switchContext(self,type):
    #     contexts = self.driver.contexts
    #     for context in contexts:
    #         log.myLog(context)
    #
    #     if type == 'n':
    #         return self.driver.switch_to.context('NATIVE_APP')
    #     elif type == 'w':
    #         n = len(contexts)
    #         log.myLog(n)
    #         return self.driver.switch_to.context(contexts[n-1])
    #     else:
    #         return

    def test_sg_register(self):
        print '注册'
        sleep(2)
        positions = []
        positions.append((170,300))
        self.driver.tap(positions)
        sleep(40)
        self.driver.tap(positions)
        sleep(40)
        self.driver.tap(positions)
        sleep(2)
        self.driver.tap(positions)
        sleep(2)
        positions = []
        positions.append((90,480))
        self.driver.tap(positions)
        sleep(2)
        positions = []
        positions.append((1,1))
        self.driver.swipe(1,1,1,1,500)
        self.driver.tap(positions)
        self.driver.swipe(1,1,1,1,500)
        self.driver.tap(positions)

    def test_sg_logout(self):
        print '退出游戏'
        sleep(2)
        self.driver.swipe(275,500,-250,0,1000)
        # self.switchContext('w')
        # context = self.driver.contexts[4]
        sleep(2)
        self.driver.switch_to.context(self.driver.contexts[4])
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("btn-settings").click()
        sleep(1)
        tap_account = self.driver.find_elements_by_tag_name('li')
        sleep(1)
        tap_account[1].click()
        sleep(1)
        change_character = self.driver.find_elements_by_class_name("button-big-red")
        change_character[10].click()
        sleep(1)
        quit_game = self.driver.find_elements_by_class_name("mojo-ui-button")
        quit_game[18].click()

    def test_sg_login(self):
        print '登陆'
        sleep(1)
        self.driver.switch_to.context('NATIVE_APP')
        sleep(2)
        positions = []
        positions.append((170,360))
        self.driver.tap(positions)
        sleep(1)
        positions = []
        positions.append((170,300))
        self.driver.tap(positions)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_accessibility_id('shift').click()
        self.driver.find_element_by_accessibility_id('h').click()
        self.driver.find_element_by_accessibility_id('t').click()
        self.driver.find_element_by_accessibility_id('d').click()
        self.driver.find_element_by_accessibility_id("more, numbers").click()
        self.driver.find_element_by_accessibility_id('@').click()
        self.driver.find_element_by_accessibility_id('more, letters').click()
        self.driver.find_element_by_accessibility_id('q').click()
        self.driver.find_element_by_accessibility_id("more, numbers").click()
        self.driver.find_element_by_accessibility_id(".").click()
        self.driver.find_element_by_accessibility_id('more, letters').click()
        self.driver.find_element_by_accessibility_id('q').click()
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(1)
        positions = []
        positions.append((170,380))
        self.driver.tap(positions)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_accessibility_id('q').click()
        self.driver.find_element_by_accessibility_id('p').click()
        self.driver.find_element_by_accessibility_id('q').click()
        self.driver.find_element_by_accessibility_id('p').click()
        self.driver.find_element_by_accessibility_id('q').click()
        self.driver.find_element_by_accessibility_id('p').click()
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(1)
        positions = []
        positions.append((90,450))
        self.driver.tap(positions)
        sleep(2)
        self.driver.switch_to.context(self.driver.contexts[4])
        # context = self.driver.contexts[4]
        # self.driver.switch_to.context(context)
        sleep(1)
        login = self.driver.find_elements_by_class_name("go-game-btn")
        sleep(1)
        login[0].click()
        # sleep(1)
        self.driver.switch_to.context('NATIVE_APP')

    def test_sg_chat(self):
        print '聊天'
        sleep(1)
        positions = []
        positions.append((180,540))
        self.driver.tap(positions)
        sleep(1)
        positions = []
        positions.append((170,80))
        self.driver.tap(positions)
        sleep(1)
        positions = []
        positions.append((170,510))
        self.driver.tap(positions)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_accessibility_id('Z').click()
        self.driver.find_element_by_accessibility_id('Send').click()
        sleep(1)
        positions = []
        positions.append((15,510))
        self.driver.tap(positions)
        sleep(1)
        self.driver.swipe(170,510,0,0,2500)

    def test_sg_mission(self):
        print '任务'
        sleep(1)
        positions = []
        positions.append((75,550))
        self.driver.tap(positions)

    def test_sg_fight(self):
        print '争夺'
        sleep(1)
        positions = []
        positions.append((130,550))
        self.driver.tap(positions)

    def test_sg_battle(self):
        print '抢银'
        sleep(1)
        positions = []
        positions.append((110,400))
        self.driver.tap(positions)

        sleep(1)
        positions = []
        positions.append((130,550))
        self.driver.tap(positions)

    def test_sg_rob(self):
        print '夺宝'
        sleep(1)
        positions = []
        positions.append((240,240))
        self.driver.tap(positions)

    def test_sg_army(self):
        print '阵容'
        sleep(2)
        positions = []
        positions.append((230,550))
        self.driver.tap(positions)
#        self.driver.implicitly_wait(2)
#        self.driver.find_element_by_class_name('changePackage-btn').click()

    def test_sg_mall(self):
        print '商城'
        sleep(1)
        positions = []
        positions.append((290,550))
        self.driver.tap(positions)
        sleep(2)
        self.driver.switch_to.context(self.driver.contexts[4])
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('payment-button').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('button-close').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('mall-type-1').click()

    def test_sg_home(self):
        print '导航栏首页按钮'
        sleep(2)
        self.driver.switch_to.context(self.driver.contexts[0])
        sleep(1)
        positions = []
        positions.append((25,540))
        self.driver.tap(positions)
        sleep(1)
        self.driver.switch_to.context(self.driver.contexts[4])

    def test_sg_force(self):
        print '势力'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-force').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('intro').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('button-close').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('n-header').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('force-back-btn').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-internal').click()
        sleep(1)
        self.driver.find_element_by_class_name('assistant-show-btn').click()
        sleep(1)
        force_assist = self.driver.find_elements_by_class_name('button-big-red')
        force_assist[10].click()
        sleep(1)
        force_assist[10].click()
        sleep(1)
        self.driver.find_element_by_class_name('button-close').click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[2].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-challenge').click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[3].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-foreign').click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[4].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-forcebg').click()
#        self.driver.find_element_by_id('btn-country').click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[5].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-member').click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[6].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-event').click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[7].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-city').click()
        sleep(1)
        city = self.driver.find_elements_by_tag_name('li')
        sleep(1)
        city[16].click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[8].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-exchange').click()
        sleep(1)
        force_back = self.driver.find_elements_by_class_name('force-back-btn')
        force_back[9].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-internal').click()
        sleep(1)
        self.driver.back()

    def test_sg_fuben(self):
        print '闯关'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-fuben').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('challenge-btn').click()
        sleep(1)
        self.driver.back()

    def test_sg_bg(self):
        print '战场'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-battleground').click()
        sleep(1)
        bg = self.driver.find_elements_by_tag_name('li')
        sleep(1)
        bg[1].click()
        sleep(1)
        bg[2].click()
        sleep(1)
        bg[0].click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('ranking').click()
        sleep(1)
        self.driver.back()

    def test_sg_teamFb(self):
        print '组队'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-teamfb').click()
        sleep(1)
        self.driver.back()

    def test_sg_rank(self):
        print '排行'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-ranking').click()
        sleep(1)
        rank = self.driver.find_elements_by_class_name('activityname')
        rank[0].click()
        sleep(1)
        rank_back = self.driver.find_elements_by_class_name('mojo-ui-button')
        rank_back[1].click()
        sleep(1)
        rank = self.driver.find_elements_by_class_name('activityname')
        rank[1].click()
        sleep(1)
        self.driver.back()

    def test_sg_entity(self):
        print '卡牌'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-entity-browse').click()
        sleep(1)
        self.driver.back()

    def test_sg_illustration(self):
        print '图鉴'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-illustration').click()
        sleep(1)
        preview = self.driver.find_elements_by_class_name('button-big-red')
        preview[1].click()
        sleep(1)
        self.driver.back()

    def test_sg_message(self):
        print '消息'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-messages').click()
        sleep(1)
        self.driver.back()

    def test_sg_intensify(self):
        print '强化'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-intensify').click()
        sleep(1)
        intensify = self.driver.find_elements_by_tag_name('li')
        sleep(2)
        intensify[1].click()
        sleep(1)
        intensify[2].click()
        sleep(1)
        self.driver.back()

    def test_sg_profile(self):
        print'玩家信息栏'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('mojo-com-profile-base').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('button-close').click()

    def test_sg_announcement(self):
        print'公告'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('announcement-center-img').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('button-close').click()

    def test_sg_activity(self):
        print'活动中心'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('activity-center-img').click()
        sleep(1)
        self.driver.back()

    def test_sg_demon(self):
        print'修炼'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-demon').click()
        demon = self.driver.find_elements_by_tag_name('li')
        sleep(1)
        demon[1].click()
        sleep(1)
        self.driver.back()
        sleep(1)
        self.driver.switch_to.context(self.driver.contexts[0])
        sleep(1)
        self.driver.swipe(275,500,-250,0,1000)
        sleep(1)
        self.driver.switch_to.context(self.driver.contexts[4])

    def test_sg_unrebirth(self):
        print'轮回'
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-unrebirth').click()
        sleep(1)
        self.driver.back()

    def test_sg_friend(self):
        print'好友'
        sleep(1)
        self.driver.switch_to.context(self.driver.contexts[0])
        sleep(1)
        self.driver.swipe(275,500,-250,0,1000)
        sleep(1)
        self.driver.switch_to.context(self.driver.contexts[4])
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('btn-friend').click()
        sleep(1)
        self.driver.back()