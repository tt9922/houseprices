import flet as ft
import pandas as pd
import os

# 1. 住宅価格データセット（Ames Housing）を読み込む
CACHE_FILE = "assets/house_prices.csv"

# Check if running in Flet
import sys
if os.path.exists(CACHE_FILE):
    print(f"Loading from asset: {CACHE_FILE}")
    df_house = pd.read_csv(CACHE_FILE)
else:
    # Fallback or error
    print(f"Asset not found: {CACHE_FILE}")
    base_path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(base_path, "assets", "house_prices.csv")
    if os.path.exists(abs_path):
         print(f"Loading from absolute path: {abs_path}")
         df_house = pd.read_csv(abs_path)
    else:
         # Try loading from relative path in web build structure if needed, or fail
         try:
             df_house = pd.read_csv("house_prices.csv")
         except:
             raise FileNotFoundError(f"Could not find {CACHE_FILE} or {abs_path}")

# 2. データの先頭5行を表示
print("--- 住宅データの先頭5行 ---")
print(df_house.head())

# 3. どんな項目があるか確認
print("\n--- データの項目（一部） ---")
print(df_house.columns.tolist()[:10]) # 数が多いので最初の10個だけ表示

COLUMN_TRANSLATIONS = {
    "Id": "ID",
    "MSSubClass": "建物クラス",
    "MSZoning": "用途地域",
    "LotFrontage": "間口距離",
    "LotArea": "敷地面積",
    "Street": "接面道路の種類",
    "Alley": "路地へのアクセス",
    "LotShape": "敷地の形状",
    "LandContour": "土地の平坦性",
    "Utilities": "公共設備",
    "LotConfig": "区画の配置",
    "LandSlope": "土地の傾斜",
    "Neighborhood": "近隣地域",
    "Condition1": "近接条件1",
    "Condition2": "近接条件2",
    "BldgType": "建物タイプ",
    "HouseStyle": "住宅スタイル",
    "OverallQual": "全体的な品質",
    "OverallCond": "全体的な状態",
    "YearBuilt": "建築年",
    "YearRemodAdd": "改築年",
    "RoofStyle": "屋根のスタイル",
    "RoofMatl": "屋根の素材",
    "Exterior1st": "外装材1",
    "Exterior2nd": "外装材2",
    "MasVnrType": "石積みタイプ",
    "MasVnrArea": "石積み面積",
    "ExterQual": "外装の品質",
    "ExterCond": "外装の状態",
    "Foundation": "基礎のタイプ",
    "BsmtQual": "地下室の高さ",
    "BsmtCond": "地下室の状態",
    "BsmtExposure": "地下室の露出",
    "BsmtFinType1": "地下室仕上がり1",
    "BsmtFinSF1": "地下室仕上がり面積1",
    "BsmtFinType2": "地下室仕上がり2",
    "BsmtFinSF2": "地下室仕上がり面積2",
    "BsmtUnfSF": "地下室未仕上がり面積",
    "TotalBsmtSF": "地下室合計面積",
    "Heating": "暖房の種類",
    "HeatingQC": "暖房の品質",
    "CentralAir": "中央空調",
    "Electrical": "電気システム",
    "1stFlrSF": "1階面積",
    "2ndFlrSF": "2階面積",
    "LowQualFinSF": "低品質仕上がり面積",
    "GrLivArea": "地上居住面積",
    "BsmtFullBath": "地下フルバス",
    "BsmtHalfBath": "地下ハーフバス",
    "FullBath": "フルバス",
    "HalfBath": "ハーフバス",
    "BedroomAbvGr": "ベッドルーム数",
    "KitchenAbvGr": "キッチン数",
    "KitchenQual": "キッチンの品質",
    "TotRmsAbvGrd": "総部屋数",
    "Functional": "機能性",
    "Fireplaces": "暖炉数",
    "FireplaceQu": "暖炉の品質",
    "GarageType": "ガレージタイプ",
    "GarageYrBlt": "ガレージ建築年",
    "GarageFinish": "ガレージ仕上がり",
    "GarageCars": "ガレージ駐車台数",
    "GarageArea": "ガレージ面積",
    "GarageQual": "ガレージ品質",
    "GarageCond": "ガレージ状態",
    "PavedDrive": "舗装された私道",
    "WoodDeckSF": "ウッドデッキ面積",
    "OpenPorchSF": "オープンポーチ面積",
    "EnclosedPorch": "囲いポーチ面積",
    "3SsnPorch": "3シーズンポーチ面積",
    "ScreenPorch": "スクリーンポーチ面積",
    "PoolArea": "プール面積",
    "PoolQC": "プール品質",
    "Fence": "フェンス",
    "MiscFeature": "その他機能",
    "MiscVal": "その他価値",
    "MoSold": "販売月",
    "YrSold": "販売年",
    "SaleType": "販売タイプ",
    "SaleCondition": "販売条件",
    "SalePrice": "販売価格"
}

VALUE_TRANSLATIONS = {
    "RL": "低密度住宅地",
    "RM": "中密度住宅地",
    "C (all)": "商業地",
    "FV": "水上集落",
    "RH": "高密度住宅地",
    "Pave": "舗装",
    "Grvl": "砂利",
    "Reg": "正規形",
    "IR1": "やや不規則",
    "IR2": "不規則",
    "IR3": "かなり不規則",
    "Lvl": "平坦",
    "Bnk": "傾斜",
    "HLS": "丘陵",
    "Low": "低地",
    "AllPub": "全公共設備",
    "NoSewr": "下水なし",
    "NoSeWa": "下水・水なし",
    "Elo": "電気のみ",
    "Inside": "内側",
    "Corner": "コーナー",
    "CulDSac": "袋小路",
    "FR2": "2面接道",
    "FR3": "3面接道",
    "Gtl": "緩やか",
    "Mod": "中程度",
    "Sev": "急勾配",
    "1Fam": "一戸建て",
    "2fmCon": "2世帯",
    "Duplex": "2連棟",
    "TwnhsE": "タウンハウス（端）",
    "Twnhs": "タウンハウス（中）",
    "1Story": "1階建て",
    "1.5Fin": "1.5階建て（完了）",
    "1.5Unf": "1.5階建て（未完）",
    "2Story": "2階建て",
    "2.5Fin": "2.5階建て（完了）",
    "2.5Unf": "2.5階建て（未完）",
    "SFoyer": "スプリットホワイエ",
    "SLvl": "スプリットレベル",
    "Gable": "切妻",
    "Hip": "寄棟",
    "Gambrel": "腰折れ",
    "Mansard": "マンサード",
    "Flat": "平屋根",
    "Shed": "片流れ",
    "Ex": "優秀",
    "Gd": "良",
    "TA": "平均",
    "Fa": "可",
    "Po": "不可",
    "PConc": "打設コンクリート",
    "CBlock": "コンクリートブロック",
    "Y": "はい",
    "N": "いいえ",
    "SBrkr": "標準ブレーカー",
    "FuseA": "ヒューズA",
    "FuseF": "ヒューズF",
    "FuseP": "ヒューズP",
    "Mix": "混合",
    "WD": "保証証書",
    "CWD": "現金保証証書",
    "VWD": "バリデーション保証証書",
    "New": "新築",
    "COD": "着払い",
    "Con": "契約",
    "ConLw": "契約（低金利）",
    "ConLI": "契約（低頭金）",
    "ConLD": "契約（低頭金）",
    "Oth": "その他",
    "Normal": "通常",
    "Abnorml": "異常",
    "AdjLand": "隣接地",
    "Alloca": "割り当て",
    "Family": "家族間",
    "Partial": "一部完了",
    "nan": "欠損"
}

def main(page: ft.Page):
    """
    アプリケーションのメインエントリポイント。
    
    Fletページのレイアウトを定義し、データテーブル、相関分析チャート、
    価格予測フォーム、欠損値分析チャートを表示・制御します。

    Args:
        page (ft.Page): Fletのページオブジェクト。UIコンポーネントを追加するキャンバスとして機能します。
    """
    page.title = "Ames Housing Data"
    
    # Prediction UI
    # Existing Inputs
    area_input = ft.TextField(label="居住面積 (sq ft)", value="1500", width=200)
    year_input = ft.TextField(label="建築年 (西暦)", value="2000", width=200)
    # New Inputs
    bsmt_input = ft.TextField(label="地下室面積 (sq ft)", value="800", width=200)
    
    qual_slider = ft.Slider(min=1, max=10, divisions=9, value=5, label="{value}", width=300)
    qual_text = ft.Text(f"全体的な品質 (Overall Quality): 5", size=16)
    def on_qual_change(e):
        qual_text.value = f"全体的な品質 (Overall Quality): {int(e.control.value)}"
        qual_text.update()
    qual_slider.on_change = on_qual_change

    garage_slider = ft.Slider(min=0, max=4, divisions=4, value=2, label="{value}台", width=300)
    garage_text = ft.Text(f"ガレージ収容台数 (Garage Cars): 2台", size=16)
    def on_garage_change(e):
        garage_text.value = f"ガレージ収容台数 (Garage Cars): {int(e.control.value)}台"
        garage_text.update()
    garage_slider.on_change = on_garage_change

    predict_btn = ft.ElevatedButton(text="高精度で予想 (Predict)", icon="auto_awesome", height=50)
    result_text = ft.Text("条件を入力して予想ボタンを押してください", size=24, weight=ft.FontWeight.BOLD, color="green")
    calculation_text = ft.Markdown("", visible=False)

    def on_predict_click(e):
        try:
            # Get values
            area = float(area_input.value)
            year = float(year_input.value)
            bsmt = float(bsmt_input.value)
            qual = int(qual_slider.value)
            garage = int(garage_slider.value)
            
            # Predict
            input_val = [[area, year, qual, garage, bsmt]]
            # Warning: sklearn expects specific feature names or numpy array. 
            # We pass a list of list which is standard.
            pred_price = model.predict(input_val)[0]
            
            result_text.value = f"予想価格: ${pred_price:,.2f}"
            result_text.update()
            
            # Feature Importances
            importances = model.feature_importances_
            # Create a simple text bar chart for importance
            importance_desc = ""
            for name, imp in zip(['居住面積', '築年数', '全体の品質', 'ガレージ', '地下室'], importances):
                bar = "█" * int(imp * 20) # Scale mainly for visual
                importance_desc += f"- **{name}**: {bar} ({imp*100:.1f}%)\n"

            # Display explanation
            calculation_text.value = f"""
### AI決定の重要度 (Feature Importance)
ランダムフォレストモデルが、どの情報を重視して価格を決定したかの割合です：

{importance_desc}

*(注: これらは複雑に絡み合って価格を決定しています。「品質」と「広さ」が特に重要視される傾向があります)*
            """
            calculation_text.visible = True
            calculation_text.update()
            
        except ValueError:
            result_text.value = "数値を正しく入力してください"
            result_text.update()
            calculation_text.visible = False
            calculation_text.update()
    
    predict_btn.on_click = on_predict_click

    # --- Missing Value Analysis ---
    missing_data = df_house.isnull().sum()
    missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
    
    # Chart Data Preparation (Top 15)
    missing_chart_groups = []
    for i, (col, count) in enumerate(missing_data.head(15).items()):
        col_label = f"{col}\n({COLUMN_TRANSLATIONS.get(col, col)})"
        missing_chart_groups.append(
            ft.BarChartGroup(
                x=i,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=count,
                        width=30,
                        color="red",
                        tooltip=f"{col_label}: {count}件",
                        border_radius=0,
                    ),
                ],
            )
        )

    missing_chart = ft.BarChart(
        bar_groups=missing_chart_groups,
        border=ft.border.all(1, "grey400"),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Count"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=i, label=ft.Container(ft.Text(col[:6], size=10), padding=5)
                ) for i, (col, _) in enumerate(missing_data.head(15).items())
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color="grey300", width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor="grey900",
        expand=True,
    )

    missing_list = ft.ListView(
        [
            ft.Text("欠損値の多い項目一覧 (Top Missing Columns)", size=20, weight=ft.FontWeight.BOLD),
             *[
                 ft.Text(f"{i+1}. {col} ({COLUMN_TRANSLATIONS.get(col, col)}): {count}件 ({count/len(df_house)*100:.1f}%)", 
                         color="red" if count > 1000 else "orange" if count > 100 else "black") 
                 for i, (col, count) in enumerate(missing_data.items())
             ]
        ],
        expand=True
    )

    # --- Tabs Layout ---
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="データ一覧 (Data)",
                content=ft.Column(
                    [
                        ft.Row(
                            [table],
                            scroll=ft.ScrollMode.ALWAYS,
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True
                ),
            ),
            ft.Tab(
                text="分析 (Analysis)",
                content=ft.Column(
                    [
                        ft.Container(explanation_text, padding=10),
                        ft.Container(chart, height=400, padding=20),
                        ft.Container(analysis_text, padding=20, expand=True)
                    ],
                   expand=True
                )
            ),
            ft.Tab(
                text="AI予想 (Prediction)",
                content=ft.Container(
                    ft.Column(
                        [
                            ft.Text("高精度AIによる価格予想 (Random Forest)", size=20, weight=ft.FontWeight.BOLD),
                            ft.Text("以下の条件を入力してください:", size=16),
                            ft.Divider(),
                            ft.Row([area_input, bsmt_input, year_input], alignment="center"),
                            ft.Container(height=10),
                            qual_text,
                            qual_slider,
                            ft.Container(height=10),
                            garage_text,
                            garage_slider,
                            ft.Container(height=20),
                            ft.Container(predict_btn, padding=20),
                            ft.Divider(),
                            result_text,
                            ft.Container(calculation_text, padding=10)
                        ],
                        horizontal_alignment="center",
                        spacing=10,
                        scroll=ft.ScrollMode.AUTO
                    ),
                    padding=30,
                    alignment=ft.alignment.top_center
                )
            ),
            ft.Tab(
                text="欠損値 (Missing Values)",
                content=ft.Column(
                    [
                        ft.Text("データの「穴」を可視化します。赤い棒が長いほど、多くのデータが失われています。", size=16),
                        ft.Container(missing_chart, height=400, padding=20),
                        ft.Container(missing_list, padding=20, expand=True)
                    ],
                    expand=True
                )
            ),
        ],
        expand=True,
    )

    page.add(t)


if __name__ == "__main__":
    ft.app(main)
