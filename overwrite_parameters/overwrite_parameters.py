#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
原音設定値を手動入力し、すべての行に適用する。
"""

import utaupy as up


def define_parameters() -> object:
    """
    上書きしたいパラメーターを手動入力してもらう。
    """
    dummy_oto = up.otoini.Oto()
    dummy_oto.offset = int(input('左ブランク    : '))
    dummy_oto.overlap = int(input('オーバーラップ: '))
    dummy_oto.preutterance = int(input('先行発声      : '))
    dummy_oto.consonant = int(input('固定範囲      : '))
    dummy_oto.cutoff = int(input('右ブランク    : '))
    return dummy_oto


def overwrite_parameters(original_otoini: object, dummy_oto: object) -> object:
    """
    otoiniのパラメータを上書き
    """
    for oto in original_otoini:
        oto.offset = dummy_oto.offset
        oto.overlap = dummy_oto.overlap
        oto.preutterance = dummy_oto.preutterance
        oto.consonant = dummy_oto.consonant
        oto.cutoff = dummy_oto.cutoff
    return original_otoini


def main():
    """
    PATHを指定して全体の処理を実行
    """
    path_otoini_in = input('編集したい oto.ini ファイルを D&D して下さい。\n>>> ').strip('"')
    path_otoini_out = 'oto_result.ini'
    otoini = up.otoini.load(path_otoini_in)
    print('各種パラメータに上書きしたい数値を、半角数字で入力してください。')
    dummy_oto = define_parameters()
    input('上記の値で良い場合はEnterを押してください。')
    overwrite_parameters(otoini, dummy_oto)
    otoini.write(path_otoini_out)
    input('完了しました。Enterを押すと終了します。')


if __name__ == '__main__':
    main()
