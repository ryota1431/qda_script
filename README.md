# QDA Files Generator

このプロジェクトは、MOLファイル形式の分子構造データをOpenSCAD用のSCADファイルに変換するPythonスクリプトです。

## 機能

- 指定のディレクトリからテキストファイルを読込み、qdaファイルを生成します。

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

4. 以下のコマンドでスクリプトを実行します：
   ```
   python main.py
   ```



## ライセンス

このプロジェクトは [MITライセンス](LICENSE) の下で公開されています。

## 貢献

バグ報告や機能リクエストは、GitHubのIssueを通じてお願いします。プルリクエストも歓迎します。



