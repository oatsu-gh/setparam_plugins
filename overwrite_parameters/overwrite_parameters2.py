#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
元の原音設定を移植してから、BPMを変えたり開始拍数を変更したりする。
"""
import utaupy as up


def shift_offset(otoini: up.otoini.OtoIni, original_start_beat, new_start_beat, bpm):
    """
    開始拍数を変更する。
    """
    t = int((new_start_beat - original_start_beat) * 60000 / bpm)
    for oto in otoini:
        oto.offset += t


def change_bpm(otoini: up.otoini.OtoIni, original_bpm, new_bpm):
    """
    BPM変更に合わせてotoiniの数値を圧縮する。破壊的処理
    """
    ratio = original_bpm / new_bpm
    for oto in otoini:
        oto.offset = int(ratio * oto.offset)
        oto.overlap = int(ratio * oto.overlap)
        oto.preutterance = int(ratio * oto.preutterance)
        oto.consonant = int(ratio * oto.consonant)
        oto.cutoff = int(ratio * oto.cutoff)


def main():
    """
    PATHを指定して全体の処理を実行
    """
    # oto.iniファイル指定と読み取り
    path_otoini_in = input('編集したい oto.ini ファイルを D&D して下さい。\n>>> ').strip('"')
    path_otoini_out = 'oto_result.ini'
    otoini = up.otoini.load(path_otoini_in)
    # BPM入力
    original_bpm = int(input('変換まえのBPMを入力してください。\n>>> '))
    original_start_beat = float(input('変換まえの発声開始までの拍数を入力してください。\n>>> '))
    new_bpm = int(input('変換あとのBPMを入力してください。\n>>> '))
    new_start_beat = float(input('変換あとの発声開始までの拍数を入力してください。\n>>> '))
    # 確認
    input('上記の値で良い場合はEnterを押してください。')
    # 処理開始
    change_bpm(otoini, original_bpm, new_bpm)
    shift_offset(otoini, original_start_beat, new_start_beat)
    otoini.write(path_otoini_out)

    input('完了しました。Enterを押すと終了します。')
