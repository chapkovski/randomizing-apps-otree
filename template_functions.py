import random
from . import models

def EGWTR_fun(page):
    page.player.eg_compute_temperature_payoffs()
    page.player.eg_compute_temperature_percentages()
    page.player.wtp_credits_temperature()
    return {'eg_temperature_round1_payoff': round(page.player.egtempq1payoff + page.player.egtempq2payoff + page.player.egtempq3payoff, 2),
    'eg_temperature_round2_payoff': round(page.player.egtempq4payoff + page.player.egtempq5payoff + page.player.egtempq6payoff,2),
    'eg_possible_temperature_credits': 7 * models.Constants.maxtemperaturerange,
    'eg_temperature_percentage1': round(page.player.eg_temperature_percentage1, 2),
    'eg_temperature_percentage2': round(page.player.eg_temperature_percentage2, 2)}

def EGSTR_fun(page):
    page.player.eg_compute_temperature_payoffs()
    page.player.eg_compute_temperature_percentages()
    page.player.wtp_credits_temperature()
    return {
            'eg_temperature_round1_payoff': round(page.player.egtempq1payoff + page.player.egtempq2payoff + page.player.egtempq3payoff, 2),
            'eg_temperature_round2_payoff': round(page.player.egtempq4payoff + page.player.egtempq5payoff + page.player.egtempq6payoff, 2),
            'eg_possible_temperature_credits': 7*models.Constants.maxtemperaturerange,
            'eg_temperature_percentage1': round(page.player.eg_temperature_percentage1,2),
            'eg_temperature_percentage2': round(page.player.eg_temperature_percentage2,2)}

def QSRWTR_fun(page):
    page.player.qsr_compute_temperature_payoffs()
    page.player.qsr_compute_temperature_percentages()
    page.player.wtp_credits_temperature()
    return {'qsr_temperature_round1_payoff': round(page.player.qsrtemp1payoff,2),
            'qsr_temperature_round2_payoff': round(page.player.qsrtemp2payoff,2),
            'qsr_temperature_percentage1':round(page.player.qsr_temperature_percentage1,2),
            'qsr_temperature_percentage2':round(page.player.qsr_temperature_percentage2,2)}


def QSRSTR_fun(page):
    page.player.qsr_compute_temperature_payoffs()
    page.player.qsr_compute_temperature_percentages()
    page.player.wtp_credits_temperature()
    return {'qsr_temperature_round1_payoff': round(page.player.qsrtemp1payoff,2),
            'qsr_temperature_round2_payoff': round(page.player.qsrtemp2payoff,2),
            'qsr_temperature_percentage1': round(page.player.qsr_temperature_percentage1,2),
            'qsr_temperature_percentage2': round(page.player.qsr_temperature_percentage2,2)}

def EGWCR_fun(page):
    page.player.eg_compute_cloud_payoffs()
    page.player.eg_compute_cloud_percentages()
    page.player.wtp_credits_cloud()
    return {'eg_cloud_round1_payoff': round(page.player.egcloudq1payoff + page.player.egcloudq2payoff + page.player.egcloudq3payoff,2),
            'eg_cloud_round2_payoff': round(page.player.egcloudq4payoff + page.player.egcloudq5payoff + page.player.egcloudq6payoff,2),
            'eg_possible_cloud_credits': 7 * models.Constants.maxcloudrange,
            'eg_cloud_percentage1': round(page.player.eg_cloud_percentage1, 2),
            'eg_cloud_percentage2': round(page.player.eg_cloud_percentage2, 2)}

def EGSCR_fun(page):
    page.player.eg_compute_cloud_payoffs()
    page.player.eg_compute_cloud_percentages()
    page.player.wtp_credits_cloud()
    return {'eg_cloud_round1_payoff': round(page.player.egcloudq1payoff + page.player.egcloudq2payoff + page.player.egcloudq3payoff,2),
            'eg_cloud_round2_payoff': round(page.player.egcloudq4payoff + page.player.egcloudq5payoff + page.player.egcloudq6payoff,2),
            'eg_possible_cloud_credits': 7 * models.Constants.maxcloudrange,
            'eg_cloud_percentage1': round(page.player.eg_cloud_percentage1, 2),
            'eg_cloud_percentage2': round(page.player.eg_cloud_percentage2, 2)}

def QSRWCR_fun(page):
    page.player.qsr_compute_cloud_payoffs()
    page.player.qsr_compute_cloud_percentages()
    page.player.wtp_credits_cloud()
    return {'qsr_cloud_round1_payoff': round(page.player.qsrcloud1payoff,2),
            'qsr_cloud_round2_payoff': round(page.player.qsrcloud2payoff,2),
            'qsr_cloud_percentage1': round(page.player.qsr_cloud_percentage1,2),
            'qsr_cloud_percentage2': round(page.player.qsr_cloud_percentage2,2)}

def QSRSCR_fun(page):
   page.player.qsr_compute_cloud_payoffs()
   page.player.qsr_compute_cloud_percentages()
   page.player.wtp_credits_cloud()
   return {'qsr_cloud_round1_payoff': round(page.player.qsrcloud1payoff,2),
           'qsr_cloud_round2_payoff': round(page.player.qsrcloud2payoff,2),
           'qsr_cloud_percentage1': round(page.player.qsr_cloud_percentage1,2),
           'qsr_cloud_percentage2': round(page.player.qsr_cloud_percentage2,2)}
   
def EGWDR_fun(page):
    page.player.compute_dicerolls()
    page.player.eg_compute_dice_payoffs()
    page.player.eg_compute_dice_percentages()
    page.player.wtp_credits_dice()
    return {'eg_dice_round1_payoff': round(page.player.egdice1payoff + page.player.egdice2payoff + page.player.egdice3payoff,2),
            'eg_dice_round2_payoff': round(page.player.egdice4payoff + page.player.egdice5payoff + page.player.egdice6payoff,2),
            'eg_possible_dice_credits': 7 * models.Constants.maxdicerange,
            'eg_dice_percentage1': round(page.player.eg_dice_percentage1, 2),
            'eg_dice_percentage2': round(page.player.eg_dice_percentage2, 2)}


def EGSDR_fun(page):
    page.subsession.compute_dicerolls()
    page.player.eg_compute_dice_payoffs()
    page.player.eg_compute_dice_percentages()
    page.player.wtp_credits_dice()
    return {'eg_dice_round1_payoff': round(page.player.egdice1payoff + page.player.egdice2payoff + page.player.egdice3payoff,2),
            'eg_dice_round2_payoff': round(page.player.egdice4payoff + page.player.egdice5payoff + page.player.egdice6payoff,2),
            'eg_possible_dice_credits': 7 * models.Constants.maxdicerange,
            'eg_dice_percentage1': round(page.player.eg_dice_percentage1, 2),
            'eg_dice_percentage2': round(page.player.eg_dice_percentage2, 2)}

def QSRWDR_fun(page):
    page.player.compute_dicerolls()
    page.player.qsr_compute_dice_payoffs()
    page.player.qsr_compute_dice_percentages()
    page.player.wtp_credits_dice()
    return {'qsr_dice_round1_payoff': round(page.player.qsrdice1payoff,2),
            'qsr_dice_round2_payoff': round(page.player.qsrdice2payoff,2),
            'qsr_dice_percentage1': round(page.player.qsr_dice_percentage1,2),
            'qsr_dice_percentage2': round(page.player.qsr_dice_percentage2,2)}

def QSRSDR_fun(page):
    page.player.compute_dicerolls()
    page.player.qsr_compute_dice_payoffs()
    page.player.qsr_compute_dice_percentages()
    page.player.wtp_credits_dice()
    return {'qsr_dice_round1_payoff': round(page.player.qsrdice1payoff,2),
            'qsr_dice_round2_payoff': round(page.player.qsrdice2payoff,2),
            'qsr_dice_percentage1': round(page.player.qsr_dice_percentage1,2),
            'qsr_dice_percentage2': round(page.player.qsr_dice_percentage2,2)}

def EGWBR_fun(page):
    page.player.eg_compute_ball_payoffs()
    page.player.eg_compute_ball_percentages()
    page.player.wtp_credits_ball()
    return {'eg_ball_round1_payoff': round(page.player.egball1payoff + page.player.egball2payoff + page.player.egball3payoff,2),
            'eg_ball_round2_payoff': round(page.player.egball4payoff + page.player.egball5payoff + page.player.egball6payoff,2),
            'eg_possible_ball_credits': 7 * models.Constants.maxballrange,
            'eg_ball_percentage1': round(page.player.eg_ball_percentage1, 2),
            'eg_ball_percentage2': round(page.player.eg_ball_percentage2, 2)}

def EGSBR_fun(page):
    page.player.eg_compute_ball_payoffs()
    page.player.eg_compute_ball_percentages()
    page.player.wtp_credits_ball()
    return {'eg_ball_round1_payoff': round(page.player.egball1payoff + page.player.egball2payoff + page.player.egball3payoff,2),
            'eg_ball_round2_payoff': round(page.player.egball7payoff + page.player.egball8payoff + page.player.egball9payoff,2),
            'eg_possible_ball_credits': 7 * models.Constants.maxballrange,
            'eg_ball_percentage1': round(page.player.eg_ball_percentage1, 2),
            'eg_ball_percentage3': round(page.player.eg_ball_percentage3, 2)}

def QSRWBR_fun(page):
    page.player.qsr_compute_ball_payoffs()
    page.player.qsr_compute_ball_percentages()
    page.player.wtp_credits_ball()
    return {'qsr_ball_round1_payoff': round(page.player.qsrballpayoff1,2),
            'qsr_ball_round2_payoff': round(page.player.qsrballpayoff2,2),
            'qsr_ball_percentage1': round(page.player.qsr_ball_percentage1,2),
            'qsr_ball_percentage2': round(page.player.qsr_ball_percentage2,2)}

def QSRSBR_fun(page):
    page.player.qsr_compute_ball_payoffs()
    page.player.qsr_compute_ball_percentages()
    page.player.wtp_credits_ball()
    return {'qsr_ball_round1_payoff': page.player.qsrballpayoff1,
            'qsr_ball_round3_payoff': page.player.qsrballpayoff2,
            'qsr_ball_percentage1': round(page.player.qsr_ball_percentage1,2),
            'qsr_ball_percentage3': round(page.player.qsr_ball_percentage3,2)}

#error messages
def QSRT1_error(page, values):
    if values["qsrtemperaturequestion1"] + values["qsrtemperaturequestion2"] + values["qsrtemperaturequestion3"] + values['qsrtemperaturequestion4']!= 100:
        return "Die Antworten müssen zusammen 100 ergeben!"


def QSRT2_error(page, values):
    if values["qsrtemperaturequestion5"] + values["qsrtemperaturequestion6"] + values[
        "qsrtemperaturequestion7"] + values["qsrtemperaturequestion8"] != 100:
        return "Die Antworten müssen zusammen 100 ergeben!"


def QSRC1_error(page, values):
    if values["qsrcloudquestion1"] + values["qsrcloudquestion2"] + values["qsrcloudquestion3"] + values['qsrcloudquestion4']!= 100:
        return "Die Antworten müssen zusammen 100 ergeben!"


def QSRC2_error(page, values):
    if values["qsrcloudquestion5"] + values["qsrcloudquestion6"] + values[
        "qsrcloudquestion7"] + values["qsrcloudquestion8"] != 100:
        return "Die Antworten müssen zusammen 100 ergeben!"


def QSRD1_error(page, values):
    if values["qsrdicequestion1"] + values["qsrdicequestion2"] + values["qsrdicequestion3"] + values['qsrdicequestion4']!= 100:
        return "Die Antworten müssen zusammen 100 ergeben!"


def QSRD2_error(page, values):
    if values["qsrdicequestion5"] + values["qsrdicequestion6"] + values[
        "qsrdicequestion7"] + values["qsrdicequestion8"] != 100:
        return "Die Antworten müssen zusammen 100 ergeben!"


def QSRB1_error(page, values):
    if values["qsrballquestion1"] + values["qsrballquestion2"] + values["qsrballquestion3"] + values['qsrballquestion4']!= 100:
        return "Die Antworten müssen zusammen 100 ergeben!"


def QSRB2_error(page, values):
    if values["qsrballquestion5"] + values["qsrballquestion6"] + values[
        "qsrballquestion7"] + values["qsrballquestion8"] != 100:
        return "Die Antworten müssen zusammen 100 ergeben!"

