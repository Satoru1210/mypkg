

# ROS2 星座確認Publisher
[![test](https://github.com/Satoru1210/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Satoru1210/mypkg/actions/workflows/test.yml)

このROS 2パッケージは、現在の日付以降の星座、曜日、および日付情報を表示する機能を持ちます。このパッケージはこれらの情報を定期的にパブリッシュする`talker`ノードと、これを受信してログに出力する`listener`ノードで構成されています。

## 動作環境

このパッケージは以下の環境で動作が確認済み:
- **OS**: Ubuntu 22.04 LTS
- **ROS 2 バージョン名**: foxy

## ノード概要

### `talker` ノード
- トピック名: `zodiac_topic`
- 毎秒2回、以下の形式のデータをパブリッシュします:
  ```
  日付: YYYY-MM-DD, 曜日: Weekday, 星座: Zodiac Sign(星座)
  ```
- 現在の日付から1日ずつ増加させながら、該当する星座を表示します。

### `listener` ノード
- `zodiac_topic`トピックからデータをサブスクライブし、受信したメッセージをログとして出力します。

## 使用方法

### パッケージのセットアップ

1. ワークスペースにパッケージをクローンします:
   ```
   cd ~/ros2_ws/src
   git clone https://github.com/Satoru1210/mypkg.git
   ```

2. パッケージをビルドします:
   ```
   cd ~/ros2_ws
   colcon build
   ```

### ノードの実行
実行方法は以下の二つがあります。
### - 二つの端末で実行する方法
端末を二つ用意します
- talker
  一つ目の端末で以下のコマンドを実行
```
 ros2 run mypkg talker
```
- listener
  二つ目の端末で以下のコマンドを実行
```
 ros2 run mypkg listener
```


### - 一つの端末で実行する方法
以下のコマンドで`talker`と`listener`ノードを同時に実行します:
```
ros2 launch mypkg talk_listen.launch.py
```

## 実行例

以下はノードを実行した際の出力例です:


### - 二つの端末で実行した結果
```
[INFO] [1735494387.281452488] [listener]: listen:  日付: 2024-12-30, 曜日: Monday, 星座: Capricorn(やぎ座)
[INFO] [1735494387.772145678] [listener]: listen:  日付: 2024-12-31, 曜日: Tuesday, 星座: Capricorn(やぎ座)
[INFO] [1735494388.271891249] [listener]: listen:  日付: 2025-01-01, 曜日: Wednesday, 星座: Capricorn(やぎ座)
[INFO] [1735494388.771798809] [listener]: listen:  日付: 2025-01-02, 曜日: Thursday, 星座: Capricorn(やぎ座)
[INFO] [1735494389.271881959] [listener]: listen:  日付: 2025-01-03, 曜日: Friday, 星座: Capricorn(やぎ座)
[INFO] [1735494389.772985333] [listener]: listen:  日付: 2025-01-04, 曜日: Saturday, 星座: Capricorn(やぎ座)
...
```

### - 一つの端末で実行した結果

```
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [427]
[INFO] [listener-2]: process started with pid [429]
[listener-2] [INFO] [1735492775.613125159] [listener]: listen:  日付: 2024-12-30, 曜日: Monday, 星座: Capricorn(やぎ座)
[listener-2] [INFO] [1735492776.107207855] [listener]: listen:  日付: 2024-12-31, 曜日: Tuesday, 星座: Capricorn(やぎ座)
[listener-2] [INFO] [1735492776.607125524] [listener]: listen:  日付: 2025-01-01, 曜日: Wednesday, 星座: Capricorn(やぎ座)
...
```

## ノードとトピックについて

### - ノードとファイルの概要
- **`talker.py`**: 日付と星座データを生成し、0.5秒間隔で`zodiac_topic`トピックにパブリッシュするノード。
- **`listener.py`**: `zodiac_topic`トピックのデータを受信し、ログに出力するノード。
- **`launch/talk_listen.launch.py`**: `talker`と`listener`ノードを同時に起動するためのLaunchファイル。

### - トピックの概要

- **トピック名**: `zodiac_topic`  
  `talker` ノードが `zodiac_topic` トピックに星座情報を含むメッセージをパブリッシュし、`listener` ノードがそれをサブスクライブします。

- **メッセージ型**: `String`  
  各メッセージには、以下の情報が含まれます：
  - 日付
  - 曜日
  - 星座情報  

- **例**:  
  ```
  日付: 2024-12-30, 曜日: Monday, 星座: Capricorn(やぎ座)
  ```


## ライセンス
- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
- このパッケージのコードの一部は，本人の許可を得て下記のスライドのもの（CC-BY-SA 4.0 by Ryuichi Ueda）を，自身の著作としたものです．
    - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
- ©2024 Satoru Homma

--- 

