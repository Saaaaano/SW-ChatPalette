import re
from bs4 import BeautifulSoup
import requests
import header as h


def get_chara_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # 能力値ボーナスの取得
    ability_score = {
        '器用': soup.find('input', {'id': 'NB1'})['value'],
        '敏捷': soup.find('input', {'id': 'NB2'})['value'],
        '筋力': soup.find('input', {'id': 'NB3'})['value'],
        '生命': soup.find('input', {'id': 'NB4'})['value'],
        '知力': soup.find('input', {'id': 'NB5'})['value'],
        '精神': soup.find('input', {'id': 'NB6'})['value'],
    }

    # 技能値レベルの取得
    list = []
    GLv = soup.find_all('input', id=re.compile('^V_GLv'))
    for i in range(len(GLv)-2):
        list.append(GLv[i]['value'])
    USED_SKILL = {
        '冒険者': soup.find('input', {'id': 'lv'})['value']
    }
    for v, names in zip(list, h.SKILL_NAME):
        if v == '':
            v = '0'
        if int(v) > 0:
            USED_SKILL[names] = v

    # 武器情報の取得
    arms = []
    arms_name = soup.find_all('input', {'id': 'arms_name[]'})
    arms_hit = soup.find_all('input', {'id': 'arms_hit[]'})
    arms_critical = soup.find_all('input', {'id': 'arms_critical[]'})
    arms_damage = soup.find_all('input', {'id': 'arms_damage[]'})
    arms_iryoku = soup.find_all('input', {'id': 'arms_iryoku[]'})
    for i in range(len(arms_name)):
        data = {
            '武器名': arms_name[i]['value'],
            '命中': arms_hit[i]['value'],
            'クリティカル': arms_critical[i]['value'],
            'ダメージ': arms_damage[i]['value'],
            '威力': arms_iryoku[i]['value']
        }
        arms.append(data)

    # 防具情報の取得
    protect = {
        '回避': soup.find('input', {'id': 'kaihi'})['value'],
        '防護点': soup.find('input', {'id': 'bougo'})['value']
    }

    return protect, arms, USED_SKILL, ability_score
