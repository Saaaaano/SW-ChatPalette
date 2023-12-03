from gettext import npgettext
import streamlit as st
import function as fc
import header as h
from PIL import Image

image = Image.open('./static/fabicon.png')
st.set_page_config(
    page_title = "SW2.5 チャパレ生成",
    page_icon = image
)

st.title("SW2.5 チャパレ生成")

url = st.text_input('キャラシ保管所のURLを入力してください。')
#url = "https://charasheet.vampire-blood.net/m9a60ba04af5804b1342626db532d94ee"

if url:
    protect, arms, skills, ability_score = fc.get_chara_data(url)
    w_disp = 0
    txt = "2d6　平目"

    # txt = txt + "\n\n▽ 冒険者判定"
    for name, b in ability_score.items():
        txt = txt + "\n2d6+" + skills['冒険者'] + "+" + b + "  冒険者Lv+" + name + "B"
        if name == "生命" or name == "精神":
            txt = txt + "/" + name + "抵抗"


    if arms is not None:
        # txt = txt + "\n\n▽ 戦士系技能(パッシブ補正込み)"
        for i in range(len(arms)):
            if arms[i]['武器名'] != "":
                txt = txt + "\n2d6+" + arms[i]['命中'] + \
                    "　" + arms[i]['武器名'] + "の命中(パッシブ補正込み)"
                txt = txt + "\nk" + arms[i]['威力']  + "@" + \
                    arms[i]['クリティカル'] + "+" + arms[i]['ダメージ'] + \
                    "　" + arms[i]['武器名'] + "のダメージ(パッシブ補正込み)"
        txt = txt + "\n2d6+" + protect['回避'] + "  回避"
    
    # txt = txt + "\n\n▽ 魔法使い系技能"
    for skillname, lv in skills.items():
        if skillname in h.magic_skills:
            txt = txt + "\n2d6+" + lv + "+" + \
                ability_score['知力'] + "　" + \
                "行使判定(" + skillname + ")"
    
    # txt = txt + "\n\n▽ その他の戦闘技能"
    for skillname, lv in skills.items():
        if skillname == "バード":
            txt = txt + "\n2d6+" + lv + "+" + \
                ability_score['精神'] + "　" + "演奏判定"
        if skillname == "アルケミスト":
            txt = txt + "\n2d6+" + lv + "+" + \
                ability_score['知力'] + "　" + "賦術判定"      

    # txt = txt + "\n\n▽ その他の非戦闘技能"
    for skillname, lv in skills.items():
        if skillname in h.extra_skills:
            if skillname == "スカウト":
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['器用'] + "　" + \
                    skillname + "+器用\n\t(隠蔽,解除,スリ,変装,罠設置)"
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['敏捷'] + "　" + skillname + "+敏捷\n\t(受け身, 隠密, 軽業, 先制, 登攀, 尾行)"
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['知力'] + "　" + skillname + \
                    "+知力\n\t(足跡, 異常感知, 聞き耳, 危険感知, 探索, 地図作製, 天候予測, 宝物鑑定, 罠回避)"
            if skillname == "レンジャー":
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['器用'] + "　" + skillname + \
                    "+器用\n\t(隠蔽, 応急手当, 解除, 罠設置)"
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['敏捷'] + "　" + skillname + \
                    "+敏捷\n\t(受け身, 隠密, 軽業, 登攀, 尾行)"
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['知力'] + "　" + \
                    skillname + \
                    "+知力\n\t(足跡, 異常感知, 聞き耳, 危険感知, 探索, 地図作製, 天候予測, 病気知識, 薬品学, 罠回避)"
            if skillname == "セージ":
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['知力'] + "　" + \
                    skillname + \
                    "+知力\n\t(見識,地図作製,病気知識,文献,文明鑑定,宝物鑑定,魔物知識,薬品学)"
            if skillname == "ライダー":
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['敏捷'] + "　" + \
                    skillname + \
                    "+敏捷\n\t(受け身,騎乗)"
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['知力'] + "　" + \
                    skillname + \
                    "+知力\n\t(弱点隠蔽,地図作製,魔物知識)"
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['知力'] + "　" + \
                    "観察判定(ライダー+知力B)\n\t(足跡追跡，異常感知,危機感知,探索,罠回避)※要【探索指令】"
            if skillname == "アルケミスト":
                txt = txt + "\n2d6+" + lv + "+" + \
                    ability_score['知力'] + "　" + \
                    skillname + \
                    "+知力\n\t(見識,文献,薬品学)"
    
    # txt = txt + "\n\n=====能力値====="
    # for skillname, lv in skills.items():
    #     txt = txt + "\n//" + skillname + '=' + lv
    # for name, b in ability_score.items():
    #     txt = txt + "\n//" + name + '=' + b


    st.code(txt)

