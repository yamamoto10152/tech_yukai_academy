# Plan: yamamoto フォルダ構成を naota パターンに揃える

## 現状

**naota の構成パターン:**
```
naota/
├── Day2_PM/
│   ├── 01_if/
│   │   ├── exercises/   ← 問題ファイル（TODO付き）
│   │   ├── extra/       ← 追加問題
│   │   └── solution/    ← 模範解答
│   ├── 02_while/
│   ...
├── Day3_AM/
│   ├── 05_ファイルの読み込み/
│   ...
└── test.py
```

**yamamoto の現状:**
```
yamamoto/
├── day1_pm/              ← 小文字
│   ├── __pycache__/
│   ├── lecture_editor_shortcuts.md
│   └── lecture_python_comments.py
├── day3_pm/              ← 小文字、番号なし
│   ├── __pycache__/
│   ├── exceptions/       ← example/extra/solution
│   ├── libraries/        ← example/extra/solution
│   ├── decorators/       ← example/extra/solution
│   ├── classes/          ← example/extra/solution
│   └── cooking_app/      ← example/extra/solution
├── Day3_numpy_pandas_ml.pdf
└── Day3_PM.pdf
```

## 変換計画

### ターゲット構造:
```
yamamoto/
├── Day1_PM/
│   └── solution/
│       ├── lecture_editor_shortcuts.md
│       └── lecture_python_comments.py
├── Day3_PM/
│   ├── 01_例外処理/
│   │   ├── exercises/    (元: example/)
│   │   ├── extra/
│   │   └── solution/
│   ├── 02_ライブラリ/
│   │   ├── exercises/    (元: example/)
│   │   ├── extra/
│   │   └── solution/
│   ├── 03_デコレーター/
│   │   ├── exercises/    (元: example/)
│   │   ├── extra/
│   │   └── solution/
│   ├── 04_クラス/
│   │   ├── exercises/    (元: example/)
│   │   ├── extra/
│   │   └── solution/
│   └── 05_クッキングアプリ/
│       ├── exercises/    (元: example/)
│       ├── extra/
│       └── solution/
├── Day3_numpy_pandas_ml.pdf
├── Day3_PM.pdf
└── test.py
```

### 変更点まとめ:
1. `day1_pm` → `Day1_PM`（大文字統一）、ファイルを `solution/` に配置
2. `day3_pm` → `Day3_PM`（大文字統一）
3. 各トピックに `番号_日本語名` を付与
4. `example/` → `exercises/` にリネーム（naota パターンに合わせる）
5. `__pycache__/` を削除
6. `test.py` を yamamoto 直下に作成（naota と同様）
7. PDF は現状維持（元々 yamamoto 直下にある）
