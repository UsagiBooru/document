## openapi
OpenAPI(v3)で記述したAPIドキュメント一覧です

### ファイルの説明
- **main.v1.yaml**
  - サイト内全てのエンドポイントのドキュメントです
- **separated(フォルダ)**
  - サイト内のエンドポイントをサービス毎に分けたドキュメントです
  - **required-api(フォルダ)**
    - サイトを稼働させる上で必須となる全APIです
  - **optional-api(フォルダ)**
    - サイトを稼働させる上で追加することができる任意のAPIです
  - **scripts(フォルダ)**
    - main.v1.yaml をエンドポイント毎に分けて切り出すのに利用するスクリプト群です
      - **template.json**
        - extract-path.pyで出力する際のテンプレートです。
      - **extract-path.py**
        - 指定されたpath下にある全エンドポイントを可能な限り切り出してきます
        - (不完全な可能性があるので必ず出力を確認してください)
      - **extract-struct.py**
        - 指定された名称のstructを切り出して出力します
      - **update-struct.py**
        - 指定されたファイルをmain.v1.yamlのstructを用いて更新します