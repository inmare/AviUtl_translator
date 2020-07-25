import pyperclip as copy
from Translator_main import eff_trans_gui
import webbrowser as web

#일본어 효과명 모음
eff_list_JP = ["色調補正", "クリッピング", "ぼかし", "境界ぼかし", "モザイク", "発光", "閃光", "拡散光", "グロー", "クロマキー", 
"カラーキー", "ルミナンスキー", "ライト", "シャドー", "縁取り", "凸エッジ", "エッジ抽出", "シャープ", "フェード", "ワイプ", 
"マスク", "斜めクリッピング", "放射ブラー", "方向ブラー", "レンズブラー", "モーションブラー", "座標", "拡大率", "透明度", "回転", 
"領域拡張", "リサイズ", "ローテーション", "反転", "振動", "ミラー", "ラスター", "波紋", "画像ループ", "極座標変換", 
"ディスプレイメントマップ", "ノイズ", "色ずれ", "単色化", "グラデーション", "特定色域変換", "動画ファイル合成", 
"インターレース解除", "カメラ制御オプション", "オフスクリーン描画", "オブジェクト分割", "合成モード", "円", "四角形", "三角形", 
"五角形", "六角形","背景", "星型"]

#영어 효과명 모음
eff_list_EN = ["Color compensation", "Clipping", "Blur", "Boundary blurring", "Mosaic", "Emission", "Flash", 
"Diffusion light", "Glow", "Chroma key", "Color key", "Luminance key", "Light", "Shadow", "Add border", "Bevel", 
"Edge extraction", "Sharpen","Fade", "Wipe", "Mask", "Diagonal clipping", "Radial Blur", "Direction blur", "Lens blur", 
"Motion blur", "Coordinate", "Zoom%", "Clearness", "Rotation", "Region expansion", "Resize", "Locked Rotation", "Reversal", 
"Vibration", "Mirror", "Raster", "Ripple", "Image tiling", "Polar coordinate conversion", "Displacement map", "Noise", 
"Color shift", "Monochromatic", "Gradient", "Specific color gamut conversion", "Video files synthesis", "De-interlacing", 
"Camera control options", "Off-screen drawing", "Object split", "Synthesis mode", "Circle", "Square", "Triangle", "Pentagon", 
"Hexagon", "Background", "Star"]

#효과당 세부항목 모음
detail_list = [
["明るさ", "Lightness", "コントラスト", "Contrast", "色相", "Hue", "輝度", "Luminance", "彩度", "Chroma", "飽和する", "Saturated"],
["上", "Top", "下", "Bottom", "左", "Left", "右", "Right"],
["範囲", "Range", "縦横比", "rAspect", "光の強さ", "Light Stre", "サイズ固定", "Fixed Size"], 
["範囲", "Range", "縦横比", "rAspect", "透明度の境界をぼかす", "Boundary blur of transparency"],
["サイズ", "Size", "タイル風", "Tile style"],
["強さ", "Strength", "拡散", "Diffusion", "しきい値", "Threshold", "拡散速度", "vDiffuse", "サイズ固定", "Fixed Size"],
["強さ", "Strength", "合成方法", "Fixed Size"],
["強さ", "Strength", "拡散", "Diffusion", "サイズ固定", "Fixed size"],
["強さ", "Strength", "拡散", "Diffusion", "しきい値", "Threshold", "ぼかし", "Blur", "光成分のみ", "Light only"],
["色相範囲", "~Hue", "彩度範囲", "~Chroma", "境界補正", "dEdge", "色彩補正", "Chromatic correction", "透過補正", "Transmission correction"],
["輝度範囲", "~Luminance", "色差範囲", "~DColor", "境界補正", "dEdge"],
["基準輝度", "RefLuminance", "ぼかし", "Blur"],
["強さ", "Strength", "拡散", "Diffusion", "比率", "Ratio", "逆光", "Backlight"],
["濃さ", "Thickness", "拡散", "Diffusion", "影を別オブジェクトとして表示", "Draw shadow as separate object"],
["サイズ", "Size", "ぼかし", "Blur"],
["幅", "Width", "高さ", "Height", "角度", "Angle"],
["強さ", "Strength", "しきい値", "Threshold", "輝度エッジを抽出", "Extract luminance edge", "透明度エッジを抽出", "Extract transparency edge"],
["強さ", "Strength", "範囲", "Range"],
["イン", "In", "アウト", "Out"],
["イン", "In", "アウト", "Out", "ぼかし", "Blur", "反転(イン)", "Flip (in)", "反転(アウト)", "Flip (out)"],
["回転", "Rotation", "サイズ", "Size", "縦横比", "rAspect", "ぼかし", "Blur", "マスクの反転", "Invert mask", "元のサイズに合わせる", "Match with original size"],
["中心X", "Center X", "中心Y", "Center Y", "角度", "Angle", "ぼかし", "Blur", "幅", "Width"],
["範囲", "Range", "サイズ固定", "Fixed Size"],
["範囲", "Range", "角度", "Angle", "サイズ固定", "Fixed Size"],
["範囲", "Range", "光の強さ", "Light Stre", "サイズ固定", "Fixed Size"],
["間隔", "Interval", "分解能", "Resolution", "残像", "Afterimage", "オフスクリーン描画", "Off-screen drawing", "出力時に分解能を上げる", "Increase resolution during export"],
[],
["拡大率", "Zoom%"],
["透明度", "Clearness"],
[],
["上", "Top", "下", "Bottom", "左", "Left", "右", "Right", "塗りつぶし", "Fill"],
["拡大率", "Zoom%", "補間なし", "No interpolation", "ドット数でサイズ指定", "Speicfied size by the number of dots"],
["90度回転", "90 degree rotation"],
["上下反転", "Flip vertical", "左右反転", "Flip horizontal", "輝度反転", "Invert luminance", "色相反転", "Hue inversion", "透明度反転", "Transparency inversion"],
["周期", "Period"],
["透明度", "Clearness", "減衰", "Attenuate", "境目調整", "dEdge", "中心の位置を変更", "Change the center position"],
["横幅", "Width", "高さ", "Height", "周期", "Period", "縦ラスター", "Vertical raster", "ランダム振幅", "Random amplitude"],
["中心X", "Center X", "中心Y", "Center Y", "幅", "Width", "高さ", "Height", "速度", "Speed"],
["横回数", "Hx#", "縦回数", "Vy#", "速度X", "Speed X", "速度Y", "Speed Y", "個別オブジェクト", "Individual objects"],
["中心幅", "Center width", "拡大率", "Zoom%", "回転", "Rotation", "渦巻", "Whirlpool"],
["変形X", "Deform X", "変形Y", "Deform Y", "回転", "Rotation", "サイズ", "Size", "縦横比", "rAspect", "ぼかし", "Blur", "元のサイズに合わせる", "Match with original size"],
["強さ", "Strength", "速度X", "Speed X", "速度Y", "Speed Y", "変化速度", "dy/dx", "周期X", "Cycle X", "周期Y", "Cycle Y", "しきい値", "Threshold"],
["ずれ幅", "Gap width", "角度", "Angle", "強さ", "Strength"],
["強さ", "Strength", "輝度を保持する", "Keep luminance"],
["強さ", "Strength", "中心X", "Center X", "中心Y", "Center Y", "角度", "Angle", "幅", "Width"],
[],
["色相範囲", "~Hue", "彩度範囲", "~Chroma", "境界補正", "dEdge"],
["再生範囲", "~Play", "再生速度", "vPlay", "拡大率", "Zoom%", "ループ再生", "Loop playback", "動画ファイルの同期", "Synchronize with video files", "ループ画像", "Loop image"],
[],
["カメラの方を向く", "Face the camera", "カメラの方を向く(縦横方向のみ)", "Face the camera (Hx and Vy only)", "カメラの方を向く(横方向のみ)", "Face the camera(Hx only)", "シャドーの対象から外す", "Exclude from shadow"],
[],
["横分割", "Hx div#", "縦分割", "Vy div#"],
["通常", "Normal", "加算", "Additive", "減算", "Subtractive", "乗算", "Multiply", "スクリーン", "Screen", "オーバーレイ", "Overlay", "比較(明)", "Brighter", "比較(暗)", "Darker", "輝度", "Luminance", "色差", "Color difference", "陰影", "Shadow", "明暗", "Contrast", "差分", "Difference"]
]

#결과로 내보낼 문장
main_string = ""

#초기화 하는 함수
def initialize(effTrans):
    global main_string
    effTrans["input"].delete("1.0", "end")
    effTrans["output"].configure(state="normal")
    effTrans["output"].delete("1.0", "end")
    effTrans["output"].configure(state="disabled")
    effTrans["alert"].set("")
    main_string = ""


#복사하는 함수
def copy_effect(effTrans):
    global main_string
    if main_string != "":
        copy.copy(main_string[:-1])
        copy.paste()


#효과사전을 열어주는 함수
def open_web():
    url = "https://yatsumehole.github.io/AUCompare/AUCompare.html"
    web.open_new(url)


#효과 세부사항을 변형시켜 주는 함수
def change_detail(shape_in_it):
    global main_string
    global detail_list
    if len(detail_list[shape_in_it]) == 0:
        return None
    for i in range(0, len(detail_list[shape_in_it])-1, 2):
        if detail_list[shape_in_it][i] in main_string:
            main_string_temp = main_string.replace(detail_list[shape_in_it][i], detail_list[shape_in_it][i+1])
            main_string = main_string_temp


#효과명을 영어로 바꾸어주는 함수
def change_title():
    global main_string
    for i in range(len(eff_list_JP)):
        if eff_list_JP[i] in main_string:
            main_string_temp = main_string.replace(eff_list_JP[i], eff_list_EN[i])
            main_string = main_string_temp
            return i
        elif not (eff_list_JP[i] in main_string) and i == len(eff_list_JP)-1:
            return -1


#효과 스크립트를 변형시키는 메인함수
def main_change(effTrans):
    global main_string
    main_string = effTrans["input"].get("1.0","end")
    #변수 main_string에 변화시킬 효과를 입력
    shape_in_it = change_title()
    #일단 change_title을 통해서 효과명을 바꿈. 반환하는 값은 해당하는 효과의 배열 인덱스 값
    if shape_in_it == -1: #효과를 잘못 입력했을 때
        main_string = ""
        effTrans["output"].configure(state="normal")
        effTrans["output"].delete("1.0", "end")
        effTrans["output"].configure(state="disabled")        
        return effTrans["alert"].set("No effect matches the list of effect names in the program, or whole script is in English. Please check the script.")
    elif shape_in_it != -1 and shape_in_it >= len(eff_list_JP)-7: #입력한 효과가 도형일 때
        effTrans["output"].configure(state="normal")
        effTrans["output"].delete("1.0", "end")
        effTrans["output"].insert("1.0", main_string)
        effTrans["output"].configure(state="disabled")
        return effTrans["alert"].set("Translation finished.")
    elif shape_in_it != -1 and shape_in_it < len(eff_list_JP)-7: #입력한 효과가 도형이 아닐 때
        change_detail(shape_in_it)
        effTrans["output"].configure(state="normal")
        effTrans["output"].delete("1.0", "end")
        effTrans["output"].insert("1.0", main_string)
        effTrans["output"].configure(state="disabled")
        return effTrans["alert"].set("Translation finished.")

