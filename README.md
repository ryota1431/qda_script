# QDA Files Generator

このプログラムは、指定されたディレクトリ内のテキストファイルを読み込み、QDAファイルを生成します。

## 機能

- 指定のディレクトリからテキストファイルを読込む
- テキストファイルからwavelengthとabsorbance or intensityを取得
- テキストファイルのファイル名から塩の滴下量を取得
- イオンの滴下量でソートされたqdaファイルを出力
- 現在は滴定試験のプロットのみ対応(今後、そのほかの機能追加予定)

## 必要条件

- Python 3.6以上
- qdafile


## Pythonのインストールと仮想環境の構築

### Pythonのインストール

1. [Python公式ウェブサイト](https://www.python.org/downloads/)から、最新版のPythonをダウンロードします。
2. ダウンロードしたインストーラーを実行し、指示に従ってインストールを完了します。
3. インストール時に「Add Python to PATH」オプションにチェックを入れてください。

### 仮想環境の構築

1. コマンドプロンプト（Windows）またはターミナル（macOS/Linux）を開きます。

2. プロジェクトのディレクトリに移動します：
   ```
   cd path/to/your/project
   ```

3. 仮想環境を作成します：
   ```
   python -m venv venv
   ```

4. 仮想環境を有効化します：
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

## インストール

1. このリポジトリをクローンまたはダウンロードします。

2. 仮想環境を有効化した状態で、必要なパッケージをインストールします：
   ```
   pip install qdafile
   ```


## 使用方法

1. コマンドプロンプトまたはターミナルを開きます。

2. プロジェクトのディレクトリに移動します：
   ```
   cd path/to/your/project
   ```

3. 仮想環境を有効化します（まだ有効化していない場合）：
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```


4. カレントディレクトリに"data"という名前のディレクトリを作成
    ```
    mkdir data
    ```

5. dataディレクトリに滴定試験の結果のテキストファイルをまとめたディレクトリを保存する

6. 以下のコマンドでスクリプトを実行します：
   ```
   python main.py
   ```

7. カレントディレクトリにqdaファイルが生成されていることを確認する


## 注意
### 滴定試験のファイルの命名規則について
以下の命名規則に従ってファイル名を付けてください。
- UVの場合
```
yyyymmdd_compoundname_salt_eq_solvent_nuL.txt
```
- PLの場合
```
yyyymmdd_compoundname_salt_eq_solvent_nnm_nuL.txt
```
| 項目         | 説明                                           |
|--------------|------------------------------------------------|
| yyyymmdd     | 20241121のような形式の日付                     |
| compoundname | 化合物名                                       |
| salt         | 滴下した塩                                     |
| solvent      | 溶媒                                           |
| nnm          | 励起波長 "300nm","400nm"のように単位をつける   |
| nuL          | 滴下した塩の量 "0uL","2uL"のように単位をつける (uL以外はつけないでください) |







## ライセンス

このプロジェクトは [MITライセンス](LICENSE) の下で公開されています。

## 貢献

バグ報告や機能リクエストは、GitHubのIssueを通じてお願いします。プルリクエストも歓迎します。



