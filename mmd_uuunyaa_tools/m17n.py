# -*- coding: utf-8 -*-
# This file can be automatically generated by blender_addon_m17n_tools.
# See: https://github.com/UuuNyaa/blender_addon_m17n_tools
# It can (should) also be put in a different, specific py file.

import bpy

def _(msgid: str) -> str:
  return msgid

def iface_(msgid: str) -> str:
  return bpy.app.translations.pgettext_iface(msgid)

def register():
  bpy.app.translations.register(__name__, translation_dict)

def unregister():
  bpy.app.translations.unregister(__name__)

# ##### BEGIN AUTOGENERATED I18N SECTION #####
# NOTE: You can safely move around this auto-generated block (with the begin/end markers!),
#       and edit the translations by hand.
#       Just carefully respect the format of the tuple!

translation_dict = {
  "ja_JP": {
    #: mmd_uuunyaa_tools/__init__.py:39
    ("*", "Utility tools for MMD model & scene editing by Uuu(/>ω<)/Nyaa!."): "MMDモデル＆シーン編集のためのユーティリティーツールです。by Uuu(/>ω<)/Nyaa!",
    #: mmd_uuunyaa_tools/__init__.py:40
    ("*", "View3D > Tool Shelf > MMD Tools Panel"): "3Dビュー > サイドバー > MMD Toolsパネル",
    #: mmd_uuunyaa_tools/asset_search/actions.py:73
    ("*", "Failed to download assets from SmutBase. The response format may have changed."): "SmutBaseからのアセットダウンロードに失敗しました。レスポンスフォーマットが変わっている可能性があります。",
    #: mmd_uuunyaa_tools/asset_search/actions.py:100
    ("*", "Failed to download assets from BowlRoll. Incorrect download key."): "BowlRollからのアセットダウンロードに失敗しました。ダウンロードキーが正しくありません。",
    #: mmd_uuunyaa_tools/asset_search/actions.py:116
    ("*", "Failed to download assets from Google Drive. Incorrect download key."): "Google Driveからのアセットダウンロードに失敗しました。ダウンロードキーが正しくありません。",
    #: mmd_uuunyaa_tools/asset_search/actions.py:137
    ("*", "Failed to download assets from uploader.jp. The response format may have changed."): "uploader.jpからのアセットダウンロードに失敗しました。レスポンスフォーマットが変わっている可能性があります。",
    #: mmd_uuunyaa_tools/asset_search/actions.py:405
    ("*", "The file path is too long. This can be alleviated to some extent by shortening the Asset Extract Root Folder in the Add-on Preferences."): "ファイルパスが長すぎます。アドオンプリファレンスのアセット展開ルートフォルダーを短くすることで軽減できます。",
    #: mmd_uuunyaa_tools/asset_search/assets.py:33
    ("*", "All"): "全て",
    #: mmd_uuunyaa_tools/asset_search/assets.py:34
    ("*", "Model (.pmx)"): "モデル (.pmx)",
    #: mmd_uuunyaa_tools/asset_search/assets.py:35
    ("*", "Model (.blend)"): "モデル (.blend)",
    #: mmd_uuunyaa_tools/asset_search/assets.py:36
    ("*", "Motion (.vmd)"): "モーション (.vmd)",
    #: mmd_uuunyaa_tools/asset_search/assets.py:37
    ("*", "Pose (.vpd)"): "ポーズ (.vpd)",
    #: mmd_uuunyaa_tools/asset_search/assets.py:38
    ("*", "Lighting"): "照明",
    #: mmd_uuunyaa_tools/asset_search/assets.py:39
    ("*", "Material"): "マテリアル",
    #: mmd_uuunyaa_tools/asset_search/assets.py:40
    ("*", "World (.blend)"): "ワールド (.blend)",
    #: mmd_uuunyaa_tools/asset_search/operators.py:13
    ("Operator", "Reload Asset JSONs"): "アセットJSONをリロード",
    #: mmd_uuunyaa_tools/asset_search/operators.py:23
    ("Operator", "Update Assets JSON"): "アセットJSONを更新",
    #: mmd_uuunyaa_tools/asset_search/operators.py:40
    ("Operator", "Update Debug Asset JSON"): "デバッグアセットJSONを更新",
    #: mmd_uuunyaa_tools/asset_search/operators.py:57
    ("Operator", "Delete Debug Asset JSON"): "デバッグアセットJSONを削除",
    #: mmd_uuunyaa_tools/asset_search/operators.py:72
    ("Operator", "Delete Asset Cached Files"): "アセットキャッシュファイルを削除",
    #: mmd_uuunyaa_tools/asset_search/panels.py:267
    ("*", "Type:"): "タイプ:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:268
    ("*", "ID:"): "ID:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:270
    ("*", "Name:"): "名前:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:271
    ("*", "Aliases:"): "別名:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:272 mmd_uuunyaa_tools/asset_search/panels.py:349
    ("*", "Tags:"): "タグ:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:273
    ("*", "Updated at:"): "更新時刻",
    #: mmd_uuunyaa_tools/asset_search/panels.py:274
    ("*", "Note:"): "メモ",
    #: mmd_uuunyaa_tools/asset_search/panels.py:276
    ("*", "Source:"): "配信元:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:281
    ("Operator", "Download"): "ダウンロード",
    #: mmd_uuunyaa_tools/asset_search/panels.py:284
    ("*", "Downloading"): "ダウンロード中",
    #: mmd_uuunyaa_tools/asset_search/panels.py:284 mmd_uuunyaa_tools/asset_search/panels.py:288 mmd_uuunyaa_tools/converters/physics/cloth.py:177
    ("*", "Cache:"): "キャッシュ:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:285
    ("Operator", "Cancel"): "キャンセル",
    #: mmd_uuunyaa_tools/asset_search/panels.py:289 mmd_uuunyaa_tools/asset_search/panels.py:301
    ("*", "Path:"): "パス:",
    #: mmd_uuunyaa_tools/asset_search/panels.py:296 mmd_uuunyaa_tools/asset_search/panels.py:302
    ("Operator", "Import"): "インポート",
    #: mmd_uuunyaa_tools/asset_search/panels.py:305 mmd_uuunyaa_tools/asset_search/panels.py:308
    ("Operator", "Retry"): "リトライ",
    #: mmd_uuunyaa_tools/asset_search/panels.py:332
    ("*", "UuuNyaa Asset Search"): "UuuNyaaアセットサーチ",
    #: mmd_uuunyaa_tools/asset_search/panels.py:344
    ("*", "Asset type"): "アセットタイプ",
    #: mmd_uuunyaa_tools/asset_search/panels.py:345 mmd_uuunyaa_tools/asset_search/panels.py:486
    ("*", "Query"): "クエリ",
    #: mmd_uuunyaa_tools/asset_search/panels.py:352
    ("*", "Cached"): "キャッシュ済",
    #: mmd_uuunyaa_tools/asset_search/panels.py:365
    ("*", "{search_result_count} of {search_result_hit_count} results"): "{search_result_count} 件 / {search_result_hit_count} 件中",
    #: mmd_uuunyaa_tools/asset_search/panels.py:411
    ("*", "Invalid search result, Please search again."): "無効な検索結果です。再検索してください。",
    #: mmd_uuunyaa_tools/asset_search/panels.py:418
    ("*", "Loading {loading_count} item{plural_form_suffix}..."): "{loading_count} 件をロード中...",
    #: mmd_uuunyaa_tools/asset_search/panels.py:438
    ("*", "UuuNyaa Assets Operator"): "UuuNyaaアセットオペレーター",
    #: mmd_uuunyaa_tools/asset_search/panels.py:449
    ("*", "Reload local asset JSON files"): "ローカルアセットJSONファイルをリロード",
    #: mmd_uuunyaa_tools/asset_search/panels.py:455
    ("*", "Download and Update to the latest assets"): "最新アセットをダウンロードして更新",
    #: mmd_uuunyaa_tools/asset_search/panels.py:469
    ("*", "Debug"): "デバッグ",
    #: mmd_uuunyaa_tools/asset_search/panels.py:475
    ("*", "Fetch an asset for debug"): "デバッグ用にアセットを取得",
    #: mmd_uuunyaa_tools/asset_search/panels.py:476
    ("*", "issue #"): "issue番号",
    #: mmd_uuunyaa_tools/asset_search/panels.py:483
    ("*", "Download and Update to the latest filterd assets for debug"): "デバッグ用にフィルタ済み最新アセットをダウンロードして更新",
    #: mmd_uuunyaa_tools/asset_search/panels.py:485
    ("*", "Repository"): "リポジトリ",
    #: mmd_uuunyaa_tools/asset_search/panels.py:487
    ("*", "Write to"): "書込み先",
    #: mmd_uuunyaa_tools/asset_search/panels.py:489
    ("Operator", "Update Assets JSON by query"): "アセットJSONをクエリで更新",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:19
    ("Operator", "Add Human (metarig) from MMD Armature"): "MMDアーマチュアからHuman (metarig)を追加",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:22
    ("Operator", "Clean Armature"): "アーマチュアを掃除",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:23
    ("Operator", "Clean Koikatsu Armature"): "コイカツアーマチュアを掃除",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:224
    ("Operator", "Integrate Rigify and MMD Armatures"): "RigifyとMMDアーマチュアを統合",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:227 mmd_uuunyaa_tools/converters/armatures/operators.py:279
    ("Operator", "Join Armatures"): "アーマチュアを結合",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:227 mmd_uuunyaa_tools/converters/armatures/operators.py:279
    ("*", "Join MMD and Rigify armatures"): "RigifyとMMDアーマチュアを結合",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:228 mmd_uuunyaa_tools/converters/armatures/operators.py:280
    ("*", "MMD main bone layer"): "MMDメインボーンレイヤー",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:229 mmd_uuunyaa_tools/converters/armatures/operators.py:281
    ("*", "MMD others bone layer"): "MMDその他ボーンレイヤー",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:230 mmd_uuunyaa_tools/converters/armatures/operators.py:282
    ("*", "MMD shadow bone layer"): "MMDシャドウボーンレイヤー",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:231 mmd_uuunyaa_tools/converters/armatures/operators.py:283
    ("*", "MMD dummy bone layer"): "MMDダミーボーンレイヤー",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:276
    ("Operator", "Bind MMD to Rigify"): "MMDをRigifyに束縛",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:328
    ("Operator", "Convert Rigify Armature to MMD compatible"): "RigifyアーマチュアをMMD互換に変換",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:332
    ("*", "Upper Body2 as"): "上半身２として",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:342
    ("*", "Lower Body as"): "下半身として",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:378 mmd_uuunyaa_tools/converters/armatures/operators.py:447 mmd_uuunyaa_tools/panels.py:56 mmd_uuunyaa_tools/panels.py:61
    ("Operator", "Apply MMD Rest Pose"): "MMDレストポーズを適用",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:381 mmd_uuunyaa_tools/converters/armatures/operators.py:450
    ("*", "Iterations"): "反復",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:381 mmd_uuunyaa_tools/converters/armatures/operators.py:450
    ("*", "Number of solving iterations"): "反復解決回数",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:382 mmd_uuunyaa_tools/converters/armatures/operators.py:451
    ("*", "Pose arms"): "腕をポーズ",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:383 mmd_uuunyaa_tools/converters/armatures/operators.py:452
    ("*", "Pose legs"): "脚をポーズ",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:384 mmd_uuunyaa_tools/converters/armatures/operators.py:453
    ("*", "Pose fingers"): "指をポーズ",
    #: mmd_uuunyaa_tools/converters/armatures/operators.py:419
    ("Operator", "Convert AutoRig Armature to MMD compatible"): "AutoRigアーマチュアをMMD互換に変換",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:14
    ("*", "UuuNyaa MMD Rigify"): "UuuNyaa MMD Rigify",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:48
    ("*", "MMD-Rigify:"): "MMD-Rigify",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:49
    ("*", "Bind"): "束縛",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:50 mmd_uuunyaa_tools/converters/armatures/panels.py:113
    ("*", "Eyes"): "目",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:52 mmd_uuunyaa_tools/converters/armatures/panels.py:63 mmd_uuunyaa_tools/converters/armatures/panels.py:115 mmd_uuunyaa_tools/converters/armatures/panels.py:123
    ("*", "Leg.L"): "脚.L",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:53 mmd_uuunyaa_tools/converters/armatures/panels.py:64 mmd_uuunyaa_tools/converters/armatures/panels.py:116 mmd_uuunyaa_tools/converters/armatures/panels.py:124
    ("*", "Leg.R"): "脚.R",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:55
    ("*", "Toe.L"): "つま先.L",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:56
    ("*", "Toe.R"): "つま先.R",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:58 mmd_uuunyaa_tools/converters/armatures/panels.py:118
    ("*", "IK-FK:"): "IK-FK",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:60 mmd_uuunyaa_tools/converters/armatures/panels.py:120
    ("*", "Arm.L"): "腕.L",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:61 mmd_uuunyaa_tools/converters/armatures/panels.py:121
    ("*", "Arm.R"): "腕.R",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:69
    ("*", "MMD Layers:"): "MMDレイヤー",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:71 mmd_uuunyaa_tools/converters/armatures/panels.py:128
    ("*", "Main"): "メイン",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:74
    ("*", "Others"): "その他",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:77
    ("*", "Shadow"): "シャドウ",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:80
    ("*", "Dummy"): "ダミー",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:85
    ("*", "UuuNyaa MMD AutoRig"): "UuuNyaa MMD AutoRig",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:112
    ("*", "MMD-AutoRig:"): "MMD-AutoRig:",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:126
    ("*", "Layers:"): "レイヤー:",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:131
    ("*", "Sub"): "サブ",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:134
    ("*", "Spine"): "脊柱",
    #: mmd_uuunyaa_tools/converters/armatures/panels.py:137
    ("*", "Limbs"): "肢体",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:60 mmd_uuunyaa_tools/converters/physics/collision.py:25 mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:65
    ("*", "Nothing"): "なし",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:73
    ("*", "Cotton"): "綿",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:96
    ("*", "Silk"): "絹",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:119
    ("*", "Breast Pyramid"): "胸ピラミッド",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:145
    ("*", "UuuNyaa Cloth Adjuster"): "UuuNyaaクロス調整器",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:167
    ("*", "Collision:"): "コリジョン:",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:173 mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:968 mmd_uuunyaa_tools/converters/physics/collision.py:78 mmd_uuunyaa_tools/converters/physics/rigid_body.py:29
    ("*", "Batch Operation:"): "一括操作:",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:174 mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:969 mmd_uuunyaa_tools/converters/physics/collision.py:79 mmd_uuunyaa_tools/converters/physics/rigid_body.py:30
    ("Operator", "Copy to Selected"): "選択にコピー",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:179 mmd_uuunyaa_tools/converters/physics/cloth.py:469 mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:50
    ("*", "Simulation Start"): "シミュレーション開始",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:180 mmd_uuunyaa_tools/converters/physics/cloth.py:475 mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:51
    ("*", "Simulation End"): "シミュレーション終了",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:186
    ("*", "Subdivision:"): "細分化",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:187 mmd_uuunyaa_tools/converters/physics/cloth.py:326 mmd_uuunyaa_tools/converters/physics/cloth.py:505
    ("*", "Subdivision Levels"): "細分化レベル",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:192
    ("*", "Copy Cloth Adjuster Settings"): "クロス調整器をコピー",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:227 mmd_uuunyaa_tools/converters/physics/panels.py:45
    ("Operator", "Select Cloth Mesh"): "クロスメッシュを選択",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:230 mmd_uuunyaa_tools/converters/physics/collision.py:120
    ("*", "Same MMD Model"): "同じMMDモデル",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:231 mmd_uuunyaa_tools/converters/physics/collision.py:121
    ("*", "Same Physics Settings"): "同じ物理設定",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:232
    ("*", "Same Cache Settings"): "同じキャッシュ設定",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:286
    ("Operator", "Remove Mesh Cloth"): "クロスを除去",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:323
    ("Operator", "Convert Rigid Body to Cloth"): "リジッドボディをクロスに変換",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:328
    ("*", "Physics Mode"): "物理モード",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:333
    ("*", "Extend Ribbon Area"): "リボンエリア拡張",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:383
    ("*", "Multiple MMD models selected. Please select single model at a time."): "複数のMMDモデルが選択されています。ひとつずつモデルを選択してください。",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:412 mmd_uuunyaa_tools/converters/physics/collision.py:209 mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:180
    ("*", "Presets"): "プリセット",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:419
    ("*", "Vertex Mass"): "頂点の質量",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:432
    ("*", "Stiffness"): "剛性",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:445 mmd_uuunyaa_tools/converters/physics/collision.py:216
    ("*", "Damping"): "減衰",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:451
    ("*", "Collision Quality"): "コリジョンの品質",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:457
    ("*", "Minimum Distance"): "最小距離",
    #: mmd_uuunyaa_tools/converters/physics/cloth.py:463
    ("*", "Impulse Clamping"): "撃力を制限",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:159
    ("*", "Target bones not found."): "対象ボーンが見つからない",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:774
    ("*", "Add Pyramid Mesh by Breast Bone"): "胸ボーンからピラミッドメッシュを追加",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:777
    ("*", "Head/Tail"): "ヘッド/テール",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:778
    ("*", "String Length Ratio"): "弦長比",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:779
    ("*", "Base Area Factor"): "底面積係数",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:780
    ("*", "Project Base Vertices Vertically"): "底面頂点を垂直に投影",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:821
    ("Operator", "Convert Pyramid Mesh to Cloth"): "ピラミッドメッシュをクロスに変換",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:824 mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:889
    ("*", "Boundary Expansion Hop Count"): "境界拡張ホップ数",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:886
    ("Operator", "Assign Pyramid Weights"): "ピラミッドへウェイトを割当",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:941
    ("*", "UuuNyaa Pyramid Cloth Adjuster"): "UuuNyaaピラミッドクロス調整器",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:958
    ("*", "Weights:"): "ウエイト:",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:964
    ("*", "Cloth Physics:"): "クロス物理:",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:974
    ("*", "Copy Pyramid Cloth Adjuster Settings"): "ピラミッドクロス調整器をコピー",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:1003
    ("*", "String Pin Weight"): "弦固定ウェイト",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:1009
    ("*", "Apex Pin Weight"): "頂点固定ウェイト",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:1015
    ("*", "Base Pin Weight"): "底面固定ウェイト",
    #: mmd_uuunyaa_tools/converters/physics/cloth_pyramid.py:1021
    ("*", "Speed Multiplier"): "速度の乗数",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:38
    ("*", "Thin Smooth"): "薄くスムーズ",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:56
    ("*", "UuuNyaa Collision Adjuster"): "UuuNyaaコリジョン調整器",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:84
    ("Operator", "Copy Collision Adjuster Settings"): "コリジョン調整器をコピー",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:117 mmd_uuunyaa_tools/converters/physics/panels.py:41
    ("Operator", "Select Collision Mesh"): "コリジョンメッシュを選択",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:168
    ("Operator", "Remove Mesh Collision"): "コリジョンを除去",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:222
    ("*", "Thickness Outer"): "外側の厚さ",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:228
    ("*", "Thickness Inner"): "内側の厚さ",
    #: mmd_uuunyaa_tools/converters/physics/collision.py:234
    ("*", "Cloth Friction"): "摩擦",
    #: mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:15
    ("*", "UuuNyaa Dynamic Paint Adjuster"): "UuuNyaaダイナミックペイント調整器",
    #: mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:41
    ("*", "Cache"): "キャッシュ",
    #: mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:78
    ("*", "Canvas Skin Press"): "キャンバス 肌圧迫",
    #: mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:113
    ("*", "Brush Default"): "ブラシ デフォルト",
    #: mmd_uuunyaa_tools/converters/physics/dynamic_paint.py:187
    ("*", "Active Surface"): "アクティブサーフェス",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:21
    ("*", "UuuNyaa Physics"): "UuuNyaa物理演算",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:30
    ("*", "Relevant Selection:"): "関連選択",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:35
    ("Operator", "Select Rigid Body"): "リジッドボディを選択",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:51
    ("*", "MMD Model is not selected."): "MMDモデルが未選択",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:56
    ("*", "Visibility:"): "可視性:",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:58
    ("*", "Mesh"): "メッシュ",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:59
    ("*", "Armature"): "アーマチュア",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:60
    ("*", "Rigid Body"): "リジッドボディ",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:61
    ("*", "Cloth"): "クロス",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:64
    ("*", "Converter:"): "コンバーター:",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:68
    ("Operator", "Rigid Body to Cloth"): "リジッドボディをクロスに",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:73
    ("*", "Pyramid Cloth:"): "ピラミッドクロス:",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:74
    ("Operator", "Add Pyramid"): "ピラミッドを追加",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:75
    ("Operator", "Pyramid to Cloth"): "ピラミッドをクロスに",
    #: mmd_uuunyaa_tools/converters/physics/panels.py:76
    ("Operator", "Weight Repaint"): "ウェイト再ペイント",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body.py:15
    ("*", "UuuNyaa Rigid Body Adjuster"): "UuuNyaaリジッドボディ調整器",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body.py:35
    ("Operator", "Select Rigid Body Mesh"): "リジッドボディメッシュを選択",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body.py:38
    ("*", "Only in the MMD Model"): "MMDモデルのみ",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body.py:39
    ("*", "Only the same Settings"): "同じ設定のみ",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body_to_cloth.py:25
    ("*", "Auto"): "自動",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body_to_cloth.py:26
    ("*", "Bone Constraint"): "ボーンコンストレイント",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body_to_cloth.py:27
    ("*", "Surface Deform"): "サーフェス変形",
    #: mmd_uuunyaa_tools/converters/physics/rigid_body_to_cloth.py:75
    ("*", "No bones related with {rigid_body_name}, Please relate a bone to the Rigid Body."): "{rigid_body_name}に関連するボーンがありません。リジッドボディにボーンを関連付けてください。",
    #: mmd_uuunyaa_tools/editors/menus.py:14 mmd_uuunyaa_tools/editors/menus.py:34 mmd_uuunyaa_tools/editors/menus.py:54
    ("*", "MMD UuuNyaa"): "MMD UuuNyaa",
    #: mmd_uuunyaa_tools/editors/nodes.py:219
    ("*", "Skin Color Adjust"): "肌カラー調整",
    #: mmd_uuunyaa_tools/editors/nodes.py:222 mmd_uuunyaa_tools/tuners/material_tuners.py:261
    ("*", "Skin Bump"): "肌 凹凸",
    #: mmd_uuunyaa_tools/editors/nodes.py:225
    ("*", "Fabric Woven Texture"): "布地織物テクスチャ",
    #: mmd_uuunyaa_tools/editors/nodes.py:228 mmd_uuunyaa_tools/tuners/material_tuners.py:389
    ("*", "Fabric Bump"): "布地 凹凸",
    #: mmd_uuunyaa_tools/editors/nodes.py:231
    ("*", "Wave Bump"): "波形バンプ",
    #: mmd_uuunyaa_tools/editors/nodes.py:234
    ("*", "Magic Bump"): "マジックバンプ",
    #: mmd_uuunyaa_tools/editors/nodes.py:237
    ("*", "Shadowless BSDF"): "影なしBSDF",
    #: mmd_uuunyaa_tools/editors/nodes.py:240
    ("*", "Gem BSDF"): "宝石BSDF",
    #: mmd_uuunyaa_tools/editors/nodes.py:243
    ("*", "Liquid BSDF"): "液体BSDF",
    #: mmd_uuunyaa_tools/editors/nodes.py:246
    ("*", "Knit Texture"): "編み物Bテクスチャ",
    #: mmd_uuunyaa_tools/editors/nodes.py:249
    ("*", "Leather Texture"): "革テクスチャ",
    #: mmd_uuunyaa_tools/editors/nodes.py:252
    ("*", "Watercolor Texture"): "水彩画テクスチャ",
    #: mmd_uuunyaa_tools/editors/nodes.py:255
    ("*", "MMDTexUV"): "MMDTexUV",
    #: mmd_uuunyaa_tools/editors/nodes.py:258 mmd_uuunyaa_tools/tuners/material_adjusters.py:103
    ("*", "Subsurface Adjuster"): "サブサーフェス調節器",
    #: mmd_uuunyaa_tools/editors/nodes.py:261 mmd_uuunyaa_tools/tuners/material_adjusters.py:58
    ("*", "Wet Adjuster"): "ウエット調節器",
    #: mmd_uuunyaa_tools/editors/operators.py:18
    ("Operator", "Convert Materials for Eevee"): "マテリアルをEevee用に変換",
    #: mmd_uuunyaa_tools/editors/operators.py:19
    ("*", "Convert materials of selected objects for Eevee."): "選択中オブジェクトマテリアルをEevee用に変換",
    #: mmd_uuunyaa_tools/editors/operators.py:42
    ("Operator", "Setup Render Engine for Eevee"): "レンダーエンジンをEevee用に設定",
    #: mmd_uuunyaa_tools/editors/operators.py:43
    ("*", "Setup render engine properties for Eevee."): "レンダーエンジンプロパティをEevee用に設定",
    #: mmd_uuunyaa_tools/editors/operators.py:46
    ("*", "Use Bloom"): "ブルームを使用",
    #: mmd_uuunyaa_tools/editors/operators.py:47
    ("*", "Use Motion Blur"): "モーションブラーを使用",
    #: mmd_uuunyaa_tools/editors/operators.py:48
    ("*", "Use Film Transparent"): "フィルム透過を使用",
    #: mmd_uuunyaa_tools/editors/operators.py:108
    ("Operator", "Show Message Box"): "メッセージボックスを表示",
    #: mmd_uuunyaa_tools/editors/operators.py:129
    ("Operator", "Remove Unused Vertex Groups"): "未使用頂点グループをすべて削除",
    #: mmd_uuunyaa_tools/editors/operators.py:130
    ("*", "Remove unused vertex groups from the active meshes"): "アクティブメッシュから未使用頂点グループをすべて削除",
    #: mmd_uuunyaa_tools/editors/operators.py:133
    ("*", "Weight Threshold"): "ウエイトしきい値",
    #: mmd_uuunyaa_tools/editors/operators.py:197
    ("Operator", "Select Shape Key Target Vertices"): "シェイプキー対象の頂点を選択",
    #: mmd_uuunyaa_tools/editors/operators.py:198
    ("*", "Select shape key target vertices from the active meshes"): "アクティブメッシュのシェイプキー対象の頂点を選択",
    #: mmd_uuunyaa_tools/editors/operators.py:201 mmd_uuunyaa_tools/editors/operators.py:248
    ("*", "Distance Threshold"): "距離しきい値",
    #: mmd_uuunyaa_tools/editors/operators.py:244
    ("Operator", "Remove Unused Shape Keys"): "未使用シェイプキーをすべて削除",
    #: mmd_uuunyaa_tools/editors/operators.py:245
    ("*", "Remove unused shape keys from the active meshes"): "アクティブメッシュから未使用シェイプキーをすべて削除",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:117
    ("*", "Add Skin Hair Mesh"): "体毛メッシュを追加",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:118
    ("*", "Construct a skin hair mesh"): "体毛メッシュを構築",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:134
    ("*", "Align"): "整列",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:136
    ("*", "Align the new object to the world"): "新規オブジェクトをワールド空間で整列",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:136
    ("*", "World"): "ワールド",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:137
    ("*", "Align the new object to the view"): "新規オブジェクトを視点で整列",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:137
    ("*", "View"): "ビュー",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:138
    ("*", "3D Cursor"): "3Dカーソル",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:138
    ("*", "Use the 3D cursor orientation for the new object"): "新規オブジェクトに3Dカーソルの回転を使用",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:145
    ("*", "Location"): "位置",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:149
    ("*", "Rotation"): "回転",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:180
    ("*", "UuuNyaa"): "UuuNyaa",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:184
    ("Operator", "Skin Hair"): "体毛",
    #: mmd_uuunyaa_tools/generators/skin_hair.py:188
    ("*", "UuuNyaa Extras"): "UuuNyaaその他",
    #: mmd_uuunyaa_tools/panels.py:18
    ("*", "UuuNyaa Operator"): "UuuNyaaオペレーター",
    #: mmd_uuunyaa_tools/panels.py:28
    ("*", "Render:"): "レンダー:",
    #: mmd_uuunyaa_tools/panels.py:33
    ("*", "MMD to Rigify:"): "MMDからRigify:",
    #: mmd_uuunyaa_tools/panels.py:36
    ("Operator", "Add Metarig"): "メタリグを追加",
    #: mmd_uuunyaa_tools/panels.py:42
    ("Operator", "Integrate Armatures"): "アーマチュアを統合",
    #: mmd_uuunyaa_tools/panels.py:48
    ("*", "Bind Armatures"): "アーマチュアを束縛",
    #: mmd_uuunyaa_tools/panels.py:53
    ("*", "Rigify to MMD:"): "RigifyからMMD:",
    #: mmd_uuunyaa_tools/panels.py:54 mmd_uuunyaa_tools/panels.py:59
    ("Operator", "Convert to MMD compatible"): "MMD互換に変換",
    #: mmd_uuunyaa_tools/panels.py:58
    ("*", "(Experimental) Auto-Rig to MMD:"): "(実験的) Auto-RigからMMD:",
    #: mmd_uuunyaa_tools/preferences.py:21
    ("*", "Asset Search Results Max. Display Count"): "アセットサーチ結果の最大表示件数",
    #: mmd_uuunyaa_tools/preferences.py:22
    ("*", "Larger value is slower"): "大きい値ほど遅い",
    #: mmd_uuunyaa_tools/preferences.py:29
    ("*", "Asset JSONs Folder"): "アセットJSONフォルダー",
    #: mmd_uuunyaa_tools/preferences.py:30
    ("*", "Path to asset list JSON files"): "アセットJSONファイルのパス",
    #: mmd_uuunyaa_tools/preferences.py:36
    ("*", "Asset JSON Update Repository"): "アセットJSON更新リポジトリ",
    #: mmd_uuunyaa_tools/preferences.py:37
    ("*", "Specify the github repository which to retrieve the assets"): "アセットを取得するgithubリポジトリを指定",
    #: mmd_uuunyaa_tools/preferences.py:42
    ("*", "Asset JSON Update Query"): "アセットJSON更新クエリ",
    #: mmd_uuunyaa_tools/preferences.py:43
    ("*", "Specify the filter conditions for retrieving assets"): "アセットを取得するフィルタ条件を指定",
    #: mmd_uuunyaa_tools/preferences.py:48
    ("*", "Asset JSON Auto Update on Startup"): "起動時にアセットJSONを更新する",
    #: mmd_uuunyaa_tools/preferences.py:53
    ("*", "Asset Cache Folder"): "アセットキャッシュフォルダー",
    #: mmd_uuunyaa_tools/preferences.py:54
    ("*", "Path to asset cache folder"): "アセットキャッシュフォルダーのパス",
    #: mmd_uuunyaa_tools/preferences.py:60
    ("*", "Asset Max. Cache Size (MB)"): "アセット最大キャッシュサイズ(MB)",
    #: mmd_uuunyaa_tools/preferences.py:61
    ("*", "Maximum size (Mega bytes) of the asset cache folder"): "アセットキャッシュフォルダーの最大サイズ(メガバイト)",
    #: mmd_uuunyaa_tools/preferences.py:68
    ("*", "Asset Extract Root Folder"): "アセット展開ルートフォルダー",
    #: mmd_uuunyaa_tools/preferences.py:69
    ("*", "Path to extract the cached assets"): "キャッシュしたアセットの展開パス",
    #: mmd_uuunyaa_tools/preferences.py:75
    ("*", "Asset Extract Folder"): "アセット展開フォルダー",
    #: mmd_uuunyaa_tools/preferences.py:82
    ("*", "Asset Extract JSON"): "アセット展開JSON",
    #: mmd_uuunyaa_tools/preferences.py:91
    ("*", "Enable MMD Tools Translation"): "MMD Tools翻訳の有効化",
    #: mmd_uuunyaa_tools/preferences.py:107
    ("*", "Browse Assets"): "アセットを閲覧",
    #: mmd_uuunyaa_tools/preferences.py:111
    ("*", "Query Examples"): "クエリ例",
    #: mmd_uuunyaa_tools/preferences.py:119
    ("*", "Asset Cache Usage:"): "アセットキャッシュ利用量",
    #: mmd_uuunyaa_tools/preferences.py:140
    ("*", "Credits:"): "クレジット:",
    #: mmd_uuunyaa_tools/preferences.py:144
    ("*", "Rigid body Physics to Cloth Physics feature is the work of 小威廉伯爵."): "リジッドボディ物理からクロス物理機能は小威廉伯爵の作品です。",
    #: mmd_uuunyaa_tools/preferences.py:146
    ("*", "It was ported with his permission."): "この機能は本人の許可を得て移植したものです。",
    #: mmd_uuunyaa_tools/tuners/lighting_tuners.py:53 mmd_uuunyaa_tools/tuners/material_tuners.py:25
    ("*", "Reset"): "リセット",
    #: mmd_uuunyaa_tools/tuners/lighting_tuners.py:66
    ("*", "Left Accent"): "左アクセント",
    #: mmd_uuunyaa_tools/tuners/lighting_tuners.py:80
    ("*", "Double Side Accent"): "両側アクセント",
    #: mmd_uuunyaa_tools/tuners/lighting_tuners.py:94
    ("*", "God Ray"): "ゴッドレイ",
    #: mmd_uuunyaa_tools/tuners/lighting_tuners.py:108
    ("*", "Backlight"): "バックライト",
    #: mmd_uuunyaa_tools/tuners/lighting_tuners.py:122
    ("*", "Light Probe Grid"): "イラディアンスボリューム",
    #: mmd_uuunyaa_tools/tuners/lighting_tuners.py:136
    ("*", "Shadowless"): "シャドウレス",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:61
    ("*", "Specular"): "スペキュラー",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:62 mmd_uuunyaa_tools/tuners/material_tuners.py:645
    ("*", "Roughness"): "粗さ",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:63 mmd_uuunyaa_tools/tuners/panels.py:180
    ("*", "Wet"): "ウェット",
    ("Operator", "Wet"): "ウェット",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:106
    ("*", "Min"): "最小",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:107
    ("*", "Max"): "最大",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:108
    ("*", "Blood Color"): "血液カラー",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:109 mmd_uuunyaa_tools/tuners/panels.py:179
    ("*", "Subsurface"): "サブサーフェス",
    ("Operator", "Subsurface"): "サブサーフェス",
    #: mmd_uuunyaa_tools/tuners/material_adjusters.py:110
    ("*", "Subsurface Color"): "サブサーフェスカラー",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:48
    ("*", "Transparent"): "伝播",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:73
    ("*", "Eye Highlight"): "目ハイライト",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:98
    ("*", "Eye White"): "白目",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:123
    ("*", "Eye Iris"): "虹彩",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:153
    ("*", "Eye Lash"): "まつ毛",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:181
    ("*", "Hair Matte"): "髪 つや消し",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:209
    ("*", "Skin Mucosa"): "粘膜",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:303
    ("*", "Metal Noble"): "貴金属",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:331
    ("*", "Metal Base"): "卑金属",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:358
    ("*", "Stone Gem"): "石 宝石",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:420
    ("*", "Fabric Wave"): "布地 波形",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:453
    ("*", "Fabric Cotton"): "布地 綿",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:456 mmd_uuunyaa_tools/tuners/material_tuners.py:527 mmd_uuunyaa_tools/tuners/material_tuners.py:598 mmd_uuunyaa_tools/tuners/material_tuners.py:873
    ("*", "Color"): "カラー",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:457 mmd_uuunyaa_tools/tuners/material_tuners.py:528 mmd_uuunyaa_tools/tuners/material_tuners.py:599
    ("*", "Alpha"): "アルファ",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:458 mmd_uuunyaa_tools/tuners/material_tuners.py:529 mmd_uuunyaa_tools/tuners/material_tuners.py:601 mmd_uuunyaa_tools/tuners/material_tuners.py:650
    ("*", "Vector"): "ベクトル",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:459 mmd_uuunyaa_tools/tuners/material_tuners.py:530
    ("*", "Impurity"): "不純物",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:460 mmd_uuunyaa_tools/tuners/material_tuners.py:531 mmd_uuunyaa_tools/tuners/material_tuners.py:603 mmd_uuunyaa_tools/tuners/material_tuners.py:647 mmd_uuunyaa_tools/tuners/material_tuners.py:874
    ("*", "Scale"): "スケール",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:461 mmd_uuunyaa_tools/tuners/material_tuners.py:532
    ("*", "Angle"): "角度",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:462 mmd_uuunyaa_tools/tuners/material_tuners.py:533 mmd_uuunyaa_tools/tuners/material_tuners.py:648
    ("*", "Strength"): "強さ",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:463 mmd_uuunyaa_tools/tuners/material_tuners.py:534 mmd_uuunyaa_tools/tuners/material_tuners.py:600
    ("*", "Hole Alpha"): "穴アルファ",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:464 mmd_uuunyaa_tools/tuners/material_tuners.py:535
    ("*", "Gaps"): "すき間",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:465 mmd_uuunyaa_tools/tuners/material_tuners.py:536
    ("*", "Warp"): "縦糸",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:466 mmd_uuunyaa_tools/tuners/material_tuners.py:537
    ("*", "Woof"): "横糸",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:467 mmd_uuunyaa_tools/tuners/material_tuners.py:538
    ("*", "Distortion"): "歪み",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:468 mmd_uuunyaa_tools/tuners/material_tuners.py:539
    ("*", "Fibers"): "繊維",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:469 mmd_uuunyaa_tools/tuners/material_tuners.py:540
    ("*", "Fuzziness"): "曖昧さ",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:470 mmd_uuunyaa_tools/tuners/material_tuners.py:541
    ("*", "Errors"): "誤差",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:524
    ("*", "Fabric Silk"): "布地 絹",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:595
    ("*", "Fabric Knit"): "編物",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:602
    ("*", "Random Hue"): "ランダム色相",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:604
    ("*", "X Compression"): "X圧縮",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:640
    ("*", "Fabric Leather"): "革",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:643
    ("*", "Primary Color"): "プライマリーカラー",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:644
    ("*", "Secondary Color"): "セカンダリーカラー",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:646
    ("*", "Old/New"): "古い/新しい",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:649
    ("*", "Tartiary Detail"): "詳細さ",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:689
    ("*", "Plastic Gloss"): "プラスチック 光沢",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:717
    ("*", "Plastic Bump"): "プラスチック 凹凸",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:749
    ("*", "Plastic Matte"): "プラスチック つや消し",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:777
    ("*", "Plastic Emission"): "プラスチック 発光",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:806
    ("*", "Liquid Water"): "水",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:833
    ("*", "Liquid Cloudy"): "液体 白濁",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:870
    ("*", "Artistic Watercolor"): "表現手法 水彩画",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:875
    ("*", "Background Scale"): "背景スケール",
    #: mmd_uuunyaa_tools/tuners/material_tuners.py:876
    ("*", "Bleed Strength"): "滲み強度",
    #: mmd_uuunyaa_tools/tuners/operators.py:13
    ("Operator", "Tune Lighting"): "ライト調整",
    #: mmd_uuunyaa_tools/tuners/operators.py:31
    ("Operator", "Freeze Lighting"): "ライトを凍結",
    #: mmd_uuunyaa_tools/tuners/operators.py:48
    ("Operator", "Tune Material"): "マテリアル調整",
    #: mmd_uuunyaa_tools/tuners/operators.py:66
    ("Operator", "Attach Material Adjuster"): "マテリアル調整器を付加",
    #: mmd_uuunyaa_tools/tuners/operators.py:82
    ("Operator", "Detach Material Adjuster"): "マテリアル調整器を除去",
    #: mmd_uuunyaa_tools/tuners/panels.py:18
    ("*", "MMD UuuNyaa Sky"): "MMD UuuNyaa Sky",
    #: mmd_uuunyaa_tools/tuners/panels.py:28
    ("*", "Light Strength"): "照明強度",
    #: mmd_uuunyaa_tools/tuners/panels.py:29
    ("*", "Image Strength"): "表示強度",
    #: mmd_uuunyaa_tools/tuners/panels.py:41
    ("*", "UuuNyaa World not found."): "UuuNyaaワールドが見つからない",
    #: mmd_uuunyaa_tools/tuners/panels.py:46
    ("*", "IrradianceVolume not found. Please add it."): "イラディアンスボリュームが見つからないので追加してください",
    #: mmd_uuunyaa_tools/tuners/panels.py:51
    ("*", "for Eevee lighting, check Render Properties."): "Eevee照明用 レンダープロパティを確認",
    #: mmd_uuunyaa_tools/tuners/panels.py:56
    ("*", "Bake Indirect Lighting"): "間接照明をベイク",
    #: mmd_uuunyaa_tools/tuners/panels.py:74
    ("*", "MMD UuuNyaa Lighting"): "MMD UuuNyaa照明",
    #: mmd_uuunyaa_tools/tuners/panels.py:113
    ("*", "MMD UuuNyaa Material"): "MMD UuuNyaaマテリアル",
    #: mmd_uuunyaa_tools/tuners/panels.py:149
    ("*", "MMD UuuNyaa Material Adjuster"): "MMD UuuNyaaマテリアル調整器",
    #: mmd_uuunyaa_tools/tuners/panels.py:166
    ("*", "{material_name} is unsupported. Select other material to be output from Principled BSDF."): "{material_name} は未未対応です。プリンシプルBSDFから出力のある他のマテリアルを選択してください。",
    #: mmd_uuunyaa_tools/tuners/properties.py:17
    ("*", "Choose the lighting you want to use"): "照明を選択",
    #: mmd_uuunyaa_tools/tuners/properties.py:38
    ("*", "Choose the material you want to use"): "マテリアルを選択",
  },
}
# ##### END AUTOGENERATED I18N SECTION #####
