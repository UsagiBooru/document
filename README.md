# document
UsagiBooruに関心を持ってくださりありがとうございます!

## UsagiBooruって何?
このプロジェクトは既存のBooruサービス、またはPixivを倒すことを目的としたものです。
つまり、多くの人に利用されるイラスト投稿サイトを目指します。
現状開発は1人ですが、開発者を募集しています。

### 特徴
#### 必要に応じた機能の取り付け取り外し
このプロジェクトではマイクロサービスアーキテクチャ採用です。
サイト内に掲示板が必要ならforumサービス、Wikiが必要ならwikiサービス
必要に応じてカスタマイズが可能です。

#### 連合システム
特定のアニメの二次創作だけを投稿できるサイトとかほしくないですか?
本プロジェクトでは非中央集権型なイラスト投稿サイトを目指します。
連合システムにより、個人的に描いたイラストだけ、特定のアニメだけ、雑多なんでもありなど
用途別の様々なインスタンスに自動的に伝播させることも可能となるでしょう。
あのMastodonで採用されているActivityPubをベースとして利用するため、
既存のMastodon、Misskeyなどのインスタンスとも連携可能です。

#### IPFSバックエンド
ファイルを永久に保管したり、サーバー負荷を軽減したくありませんか?
そのために分散ファイルシステムであるIPFSをサポートします。
もちろん従来の一般的な配信方式も利用可能です。

### 設計
#### マイクロサービスアーキテクチャ
スケール可能・持続的開発が可能なものとするため
関心事によってリポジトリを分けて設計します
フロントエンドとバックエンドは完璧に分けて開発し
裏方だけを利用することも可能とします。

#### OpenAPIv3採用
統一規格、最終形を具体的なものとするため
OpenAPIv3を使ったドキュメントを予め用意しました。
このドキュメント通りに動作するものを目指します。
OpenAPI採用により、APIクライアントの開発はスムーズに行えることでしょう。

#### Go言語採用
以前から私が利用しているPythonは簡単に書けましたが、非常に遅いものでした。
これからの時代に採用されていくのはGoであると確信していることからGo言語を採用しました。


### Q&A
#### なんか似たようなプロジェクト(NuxtImageBoard)があるけど?
NuxtImageBoardは以前作成していたものをOSS化したものであり、アクティブに開発する予定はありません。
これは同様のものを更に拡張し書き直すプロジェクトです。以前とデザインは近いですが互換性はありません。

#### プロジェクト名の由来は?
私のアイコン見てピンと来たらそれです。

#### なぜAGPL?
運営されているインスタンスの透明性を確保したいからです。
また、参考としているMastodon、MisskeyなどもAGPLでありそれらに追従したいと考えたからです。

#### いつ完成する?
2021年内に公開したいと考えています。