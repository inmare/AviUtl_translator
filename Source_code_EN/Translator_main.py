import tkinter as tk
from tkinter import font
from tkinter import ttk
#Title translate helper GUI
def helper_gui(root):
    widget_list = root.winfo_children()
    for item in widget_list:
        item.place_forget()

    import Title_translate as py_sec
    #스크립트 넣는 곳 라벨
    help_input_label = tk.Label(root, text="Script line", font=font_UI)
    help_input_label.place(x=10, y=2)
    #스크립트 넣는 곳 프레임
    input_1_frame=tk.Frame(root)
    input_1_frame.place(x=10, y=26, width=450, height=170)
    #스크립트 넣는 곳 스크롤바
    input_1_scroll=tk.Scrollbar(input_1_frame)
    input_1_scroll.pack(side="right", fill="y")
    #스크립트 넣는 곳
    help_input_1 = tk.Text(input_1_frame, font=font_Entry, yscrollcommand=input_1_scroll.set)
    help_input_1.pack(side="left", fill="y")
    input_1_scroll["command"]=help_input_1.yview

    #추출된 글자 표시하는 곳 라벨
    help_output_1_label = tk.Label(root, text="Extracted text", font=font_UI)
    help_output_1_label.place(x=470, y=83)
    #추출된 글자용 프레임
    output_1_frame=tk.Frame(root)
    output_1_frame.place(x=470, y=107, width=155, height=285)
    #추출된 글자용 스크롤바
    output_1_scroll = tk.Scrollbar(output_1_frame)
    output_1_scroll.pack(side="right", fill="y")
    #추출한 글자 표시하는 곳 프레임
    help_output_1 = tk.Text(output_1_frame, font=font_Entry, state="disabled", yscrollcommand=output_1_scroll.set)
    help_output_1.pack(side="left", fill="y")
    
    #바꿀 글자 넣을 곳 라벨
    help_input_2_label = tk.Label(root, text="Want to change", font=font_UI)
    help_input_2_label.place(x=633, y=83)
    #바꿀 글자 넣을 곳 프레임
    input_2_frame = tk.Frame(root)
    input_2_frame.place(x=633, y=107, width=155, height=285)
    #바꿀 글자 넣을 곳 스크롤바
    input_2_scroll = tk.Scrollbar(input_2_frame)
    input_2_scroll.pack(side="right", fill="y")
    #바꿀 글자 넣을 곳
    help_input_2 = tk.Text(input_2_frame, font=font_Entry, yscrollcommand=input_2_scroll.set)
    help_input_2.pack(side="left", fill="y")

    #결과 라벨 
    help_output_label = tk.Label(root, text="Result", font=font_UI)
    help_output_label.place(x=10, y=198)
    #결과 프레임
    output_2_frame=tk.Frame(root)
    output_2_frame.place(x=10, y=222, width=450, height=170)
    #결과 스크롤바
    output_2_scroll=tk.Scrollbar(output_2_frame)
    output_2_scroll.pack(side="right", fill="y")
    #결과
    help_output_2 = tk.Text(output_2_frame, font=font_Entry, state="disabled", yscrollcommand=output_2_scroll.set)
    help_output_2.pack(side="left", fill="y")
    output_2_scroll["command"]=help_output_2.yview

    #결과 상태 표시 라벨
    help_res_lab = tk.Label(root, text="Change result", font=font_UI)
    help_res_lab.place(x=10, y=400)
    #결과 상태 표시 항목 라벨
    change_res_text = tk.StringVar()
    help_res_lab_item = tk.Label(root, textvariable=change_res_text, font=font_Entry)
    help_res_lab_item.place(x=10, y=420)

    #검사 결과 라벨
    help_chk_lab = tk.Label(root, text="Check result", font=font_UI)
    help_chk_lab.place(x=10, y=440)
    #검사 결과 항목 라벨
    chk_lab_text = tk.StringVar()
    help_chk_lab_item = tk.Label(root, justify="left", textvariable=chk_lab_text, font=font_Entry)
    help_chk_lab_item.place(x=10, y=460)

    help_dict = {
        "input1": help_input_1,
        "input2": help_input_2,
        "output1": help_output_1,
        "output2": help_output_2,
        "result": change_res_text,
        "check": chk_lab_text
    }
    #추출 버튼
    help_extract_button = tk.Button(root, text="Extract", font=font_UI, command=lambda: py_sec.main_extract(help_dict))
    help_extract_button.place(x=470, y=7, width=73, height=40)
    #체크 버튼
    help_check_button = tk.Button(root, text="Check", font=font_UI, command=lambda: py_sec.main_check(help_dict))
    help_check_button.place(x=552, y=7, width=73, height=40)
    #변환 버튼
    help_change_button = tk.Button(root, text="Change", font=font_UI, command=lambda: py_sec.main_get_change(help_dict))
    help_change_button.place(x=633, y=7, width=73, height=40)
    #초기화 버튼
    help_init_button = tk.Button(root, text="Initialize", font=font_UI, command=lambda: py_sec.initialize_text(help_dict))
    help_init_button.place(x=714, y=7, width=73, height=40)
    #추출한 글자 복사 버튼
    help_copy_ext_button = tk.Button(root, text="Copy extracted text", font=font_UI, command=py_sec.extract_copy)
    help_copy_ext_button.place(x=470, y=50, width=155, height=30)
    #결과 복사 버튼
    help_copy_res_button = tk.Button(root, text="Copy result", font=font_UI, command=py_sec.result_copy)
    help_copy_res_button.place(x=633, y=50, width=155, height=30)
    #번역기 창 버튼
    help_init_button = tk.Button(root, text="Google\nTranaslate", font=font_UI, command=py_sec.open_google)
    help_init_button.place(x=694, y=530, width=93, height=60)


def eff_trans_gui(root):
    widget_list = root.winfo_children()
    for item in widget_list:
        item.place_forget()

    import Effect_translate as py_fir
    #입력하는 곳 라벨
    eff_label_input = tk.Label(root, text="Script line", font=font_UI)
    eff_label_input.place(x=10, y=7)
    #결과 라벨
    eff_label_result = tk.Label(root, text="Result", font=font_UI)
    eff_label_result.place(x=10, y=257)

    #입력하는 곳
    eff_text_input = tk.Text(root, font=font_Entry)
    eff_text_input.place(x=10, y=30, width=670, height=217)
    #결과 출력하는 곳
    eff_text_output = tk.Text(root, font=font_Entry, state="disabled")
    eff_text_output.place(x=10, y=280, width=670, height=217)

    #번역 결과 라벨
    eff_alert_label = tk.Label(root, text="Translate result", font=font_UI)
    eff_alert_label.place(x=10, y=500)
    #번역 결과 알려주는 곳
    eff_res_alert_text = tk.StringVar()
    eff_result_alert = tk.Label(root, textvariable=eff_res_alert_text, font=font_Entry)
    eff_result_alert.place(x=10, y=520)

    #추가 설명
    eff_recommend = tk.Label(root, justify="left", text="Some of lines could not translate perfectly.\nThen please check effect dictionary or manual at program information.", font=font_UI)
    eff_recommend.place(x=10, y=550)

    eff_trans_dict = {
        "input": eff_text_input,
        "output": eff_text_output,
        "alert": eff_res_alert_text
    }
    #번역하는 버튼
    eff_button_input = tk.Button(root, text="Translate", font=font_UI, command=lambda: py_fir.main_change(eff_trans_dict))
    eff_button_input.place(x=690, y=30, width=100, height=40)
    #초기화하는 버튼
    eff_button_clear = tk.Button(root, text="Initialize", font=font_UI, command=lambda: py_fir.initialize(eff_trans_dict))
    eff_button_clear.place(x=690, y=75, width=100, height=40)
    #복사하는 버튼
    eff_button_copy = tk.Button(root, text="Copy result", font=font_UI, command=lambda: py_fir.copy_effect(eff_trans_dict))
    eff_button_copy.place(x=690, y=120, width=100, height=40)
    #효과 사전 버튼
    eff_dict_copy = tk.Button(root, text="Effect\nDictionary", font=font_UI, command=py_fir.open_web)
    eff_dict_copy.place(x=690, y=165, width=100, height=60)



if __name__ == '__main__':
    root = tk.Tk()
    root.title("AviUtl Translation")
    root.geometry("800x600+100+100")
    root.resizable(False, False)
    font_UI = tk.font.Font(family="Arial", size=11, weight="bold")
    font_Entry = tk.font.Font(family="Arial", size=11)
    menubar = tk.Menu(root)
    helper_gui(root)
    menubar.add_command(label="Title translate helper", command=lambda: helper_gui(root))
    menubar.add_command(label="Effect translator", command=lambda: eff_trans_gui(root))
    root.config(menu=menubar)
    root.mainloop()