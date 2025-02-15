

# ROS2 星座確認Publisher
[![test](https://github.com/Satoru1210/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Satoru1210/mypkg/actions/workflows/test.yml)

このROS 2パッケージは、現在の日付以降の星座、曜日、および日付情報を表示する機能を持ちます。このパッケージはこれらの情報を定期的にパブリッシュする`zodiac_publisher`ノードで構成されています。

## 動作環境

このパッケージは以下の環境で動作が確認済み:
- **OS**: Ubuntu 22.04 LTS
- **ROS 2 バージョン名**: humble

## ノード概要

### `zodiac_publisher` ノード
- トピック名: `zodiac`
- 毎秒2回、以下の形式のデータをパブリッシュします:
  ```
  日付: YYYY-MM-DD, 曜日: Weekday, 星座: Zodiac Sign(星座)
  ```
- 現在の日付から1日ずつ増加させながら、該当する星座を表示します。

## ノードとトピックについて

###  ノードとファイルの概要
- **`zodiac_publisher.py`**: 日付と星座データを生成し、0.5秒間隔で`zodiac`トピックにパブリッシュするノード。
- **`listener.py`**:テスト用のノード。 `zodiac`トピックのデータを受信し、ログに出力するノード。
- **`launch/talk_listen.launch.py`**:テスト用のファイル。 `zodiac_publisher`と`listener`ノードを同時に起動するためのLaunchファイル。

###  トピックの概要

- **トピック名**: `zodiac`
  `zodiac_publisher` ノードが `zodiac` トピックに星座情報を含むメッセージをパブリッシュします。
テストでは`listener` ノードを用いて`zodiac`をサブスクライブします。

- **メッセージ型**: `String`
  各メッセージには、以下の情報が含まれます：
  - 日付
  - 曜日
  - 星座情報

- **例**:
  ```
  data: ' 日付: 2025-01-18, 曜日: Saturday, 星座: Capricorn(やぎ座)'
  ```

## 使用方法

### ノードの実行

端末を二つ用意します   
- 一つ目の端末で以下のコマンドを実行
```
 ros2 run mypkg zodiac_publisher
```  
- 二つ目の端末で以下のコマンドを実行
```
 ros2 topic echo /zodiac
```


## 実行例

以下はノードを実行した際の出力例です:


### 実行結果
```
data: ' 日付: 2025-01-14, 曜日: Tuesday, 星座: Capricorn(やぎ座)'
---
data: ' 日付: 2025-01-15, 曜日: Wednesday, 星座: Capricorn(やぎ座)'
---
data: ' 日付: 2025-01-16, 曜日: Thursday, 星座: Capricorn(やぎ座)'
---
data: ' 日付: 2025-01-17, 曜日: Friday, 星座: Capricorn(やぎ座)'
---
data: ' 日付: 2025-01-18, 曜日: Saturday, 星座: Capricorn(やぎ座)'
---
data: ' 日付: 2025-01-19, 曜日: Sunday, 星座: Capricorn(やぎ座)'
---
...
```




## ライセンス
- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
- このパッケージのコードの一部は，本人の許可を得て下記のスライドのもの（CC-BY-SA 4.0 by Ryuichi Ueda）を，自身の著作としたものです．
    - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
- ©2024 Satoru Homma

--- 

