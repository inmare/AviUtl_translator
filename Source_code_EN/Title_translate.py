import pyperclip as copy
from Translator_main import helper_gui
import webbrowser as web

info_dict = {
    "track_list" : [],
    "check_list" : "",
    "dialog_string" : "",
    "dialog_break" : [],
    "dia_cut_end" : [],
    "track_num" : 0,
    "check_exist" : False,
    "dialog_exist" : False
}
#일단 받아서 분해한 정보들, 그리고 dialog를 어디에서부터 어디까지 바꿔야 할지 들어있는 사전

show_dict = {
    "track_list_JP" : [],
    "check_list_JP" : "",
    "dialog_list_JP" : [],
    "output_text" : "",
    "result_text_fin" : ""
}
#일차적으로 뽑아낸 일본어 결과들과 최종적으로 보여질 텍스트를 저장할 사전

local_fig_text = {
    "local_JP": ["\"円\"", "\"四角形\"", "\"三角形\"", "\"五角形\"", "\"六角形\"", "\"星型\""],
    "local_EN": ["\"Circle\"", "\"Square\"", "\"Triangle\"", "\"Pentagon\"", "\"Hexagon\"", "\"Star\""]
}

#구글 번역기 창을 열어주는 함수
def open_google():
    url = "https://translate.google.co.kr/?hl=ko"
    web.open_new(url)


#Title translate helper 추출된 글자 복사 버튼 함수   
def extract_copy():
    if show_dict["output_text"] != "":
        copy.copy(show_dict["output_text"])
        copy.paste()


#Title translate helper 결과 복사 버튼 함수
def result_copy():
    if show_dict["result_text_fin"] != "":
        copy.copy(show_dict["result_text_fin"])
        copy.paste()


#Title translate helper 전체 초기화 함수
def initialize_text(helper):
    init(info_dict)
    init(show_dict)
    helper["input1"].delete("1.0", "end")
    helper["input2"].delete("1.0", "end")
    helper["output1"].configure(state="normal")
    helper["output1"].delete("1.0", "end")
    helper["output1"].configure(state="disabled")
    helper["output2"].configure(state="normal")
    helper["output2"].delete("1.0", "end")
    helper["output2"].configure(state="disabled")
    helper["result"].set("")
    helper["check"].set("")


#모든 dict의 문자를 초기화 하는 함수.
def init(member_dict):
    for key, value in member_dict.items():
        if type(value) == list:
            member_dict[key] = []
        elif type(value) == str:
            member_dict[key] = ""
        elif type(value) == int:
            member_dict[key] = 0
        elif type(value) == bool:
            member_dict[key] = False


#입력받은 문자를 개행에 따라서 info_dict에 순서대로 저장해줌
def div_info(main_string_list):
    #각각 track, check, dialog 저장.
    for i in range(len(main_string_list)):
        if "--track" in main_string_list[i]:
            info_dict["track_list"].append(main_string_list[i])
            info_dict["track_num"] += 1
    for i in range(len(main_string_list)):
        if "--check" in main_string_list[i]:
            info_dict["check_list"] = main_string_list[i]
            info_dict["check_exist"] = True
            check_loc = i
            break
    for i in range(len(main_string_list)):
        if "--dialog" in main_string_list[i]:
            info_dict["dialog_string"] = main_string_list[i]
            info_dict["dialog_exist"] = True
            dialog_loc = i
            break
    #check와 dialog의 순서가 다르면 그에 대한 배열을 반환함.
    if info_dict["check_exist"] and info_dict["dialog_exist"] and check_loc < dialog_loc:
        list_order = [True, check_loc, dialog_loc]
    elif info_dict["check_exist"] or info_dict["dialog_exist"]:
        if info_dict["check_exist"]:
            list_order = [False, check_loc]
        else:
            list_order = [False, dialog_loc]
    else:
        list_order = [False, None]
    return list_order


#track과 check에 있는 정보를 show_dict에 저장하도록 하게 해주는 함수.
def track_check_save():
    #track정보 추출 후 show_dict["track_list_JP에 저장"]
    for i in range(len(info_dict["track_list"])):
        track_num_1 = info_dict["track_list"][i].find(":")
        track_num_2 = info_dict["track_list"][i].find(",")
        show_dict["track_list_JP"].append(info_dict["track_list"][i][track_num_1 + 1:track_num_2])

    #track정보 추출 후 show_dict["check_list_JP에 저장"]
    if info_dict["check_exist"]:
        check_num_1 = info_dict["check_list"].index(":")
        check_num_2 = info_dict["check_list"].index(",")
        show_dict["check_list_JP"] = info_dict["check_list"][check_num_1 + 1:check_num_2]


#/와 ,의 위치에 따라서 어느 부분을 추출할지를 결정한 후 추출하는 함수.
def slash_n_comma(i, slash_exist, comma_exist, slash_index, comma_index):
    #둘 다 있는 경우와 어느 한쪽만 있는 경우로 나누어서 번역진행.
    #분류한 문자열은 후에 화면에 표시될 정보로 전달 되어야함.
    #/ ,의 존재 여부, 그리고 어느게 더 빠른 위치에 있느냐에 따라 if문을 사용해서 저장하는 배열이 다름.
    if slash_exist and comma_exist:
        if slash_index < comma_index:
            info_dict["dia_cut_end"].append(slash_index)
            return info_dict["dialog_break"][i][1:slash_index]
        else:
            info_dict["dia_cut_end"].append(comma_index)
            return info_dict["dialog_break"][i][1:slash_index]
    elif slash_exist or comma_exist:
        if slash_exist:
            info_dict["dia_cut_end"].append(slash_index) 
            return info_dict["dialog_break"][i][1:slash_index]
        else:
            info_dict["dia_cut_end"].append(comma_index)
            return info_dict["dialog_break"][i][1:comma_index]


#[]이 있을 때 dialog에 대해서 문자를 추출하는 함수
def bracket_exist_func(i, info_dict):
    #/와 ,의 위치를 찾은 다음 더 빠른 쪽의 위치와 존재 여부를 찾음.
    #bracket이 있을 때는 ]의 뒤쪽을 시작점으로 설정후 번역 진행.
    bracket_index = info_dict["dialog_break"][i].index("]")
    if "/" in info_dict["dialog_break"][i][bracket_index:]:
        slash_index = info_dict["dialog_break"][i].index("/")
        slash_exist = True
    else:
        slash_index = None
        slash_exist = False
    
    if "," in info_dict["dialog_break"][i][bracket_index:]:
        comma_index = info_dict["dialog_break"][i].index(",")
        comma_exist = True
    else:
        comma_index = None
        comma_exist = False

    #찾은 값에 따라 if문을 사용해서 다르게 번역진행
    break_result = slash_n_comma(i, slash_exist, comma_exist, slash_index, comma_index)
    return break_result


#[]이 없을 때 dialog에서 문자를 추출하는 함수
def bracket_nonexist_func(i, info_dict):
    #/와 ,의 위치를 찾은 다음 더 빠른 쪽의 위치와 존재 여부를 찾음.
    if "/" in info_dict["dialog_break"][i]:
        slash_index = info_dict["dialog_break"][i].index("/")
        slash_exist = True
    else:
        slash_index = None
        slash_exist = False
    
    if "," in info_dict["dialog_break"][i]:
        comma_index = info_dict["dialog_break"][i].index(",")
        comma_exist = True
    else:
        comma_index = None
        comma_exist = False
    
    #찾은 값에 따라 if문을 사용해서 다르게 번역진행
    break_result = slash_n_comma(i, slash_exist, comma_exist, slash_index, comma_index)
    return break_result


#dialog의 정보를 추출하는 함수
def dialog_save():
    dialog_to_list = list(info_dict["dialog_string"])
    #콜론, 세미콜론 사이의 내용만 분리하기 위해 콜론과 세미콜론들의 위치를 찾아줌
    dia_colon_loc = info_dict["dialog_string"].find(":") #콜론을 찾은 후 dia_colon_loc에 저장
    #세미콜론들의 위치들을 찾아준후 dia_semi_colon_loc에 저장해 줌.
    dia_semi_colon_loc = []
    semi_colon_num = info_dict["dialog_string"].count(";")
    semi_colon_loc_temp = 0
    for i in range(semi_colon_num):
        semi_colon_loc = info_dict["dialog_string"].find(";", semi_colon_loc_temp)
        dia_semi_colon_loc.append(int(semi_colon_loc))
        semi_colon_loc_temp = semi_colon_loc+1

    #그 후 str,list[int:int]를 통해 dialog_to_list의 원하는 부분을 가져옴.
    for i in range(semi_colon_num):
        if i == 0:
            #처음의 경우에는 콜론이기 때문에 0번째 세미콜론 위치와 콜론사이의 정보를 가져옴
            info_dict["dialog_break"].append(dialog_to_list[dia_colon_loc : dia_semi_colon_loc[0]])
        else:
            #그 후에는 i-1번째, i번째 사이의 세미콜론사이의 정보를 가져오게함.
            info_dict["dialog_break"].append(dialog_to_list[dia_semi_colon_loc[i-1] : dia_semi_colon_loc[i]])
    #[]유무 여부에 따라 추출에 이용하는 함수가 다름
    for i in range(semi_colon_num):
        if "[" in info_dict["dialog_break"][i]:
            dialog_temp = "".join(bracket_exist_func(i, info_dict))
            show_dict["dialog_list_JP"].append(dialog_temp)
        else:
            dialog_temp = "".join(bracket_nonexist_func(i, info_dict))
            show_dict["dialog_list_JP"].append(dialog_temp)  


#Extracted text에 내보낼 수 있도록 추출된 문자열들을 합쳐주는 함수
class combine_text:
    def check_comb(self, output_text, show_dict):
            return output_text + show_dict["check_list_JP"] + "\n"

    def track_comb(self, output_text, show_dict):
        for i in range(len(show_dict["track_list_JP"])):
            show_dict["output_text"] = show_dict["output_text"] + show_dict["track_list_JP"][i] + "\n"
        return show_dict["output_text"]

    def dialog_comb(self, output_text, show_dict):
        for i in range(len(show_dict["dialog_list_JP"])):
            if i != len(show_dict["dialog_list_JP"]) - 1:
                show_dict["output_text"] = show_dict["output_text"] + show_dict["dialog_list_JP"][i] + "\n"
            else:
                show_dict["output_text"] = show_dict["output_text"] + show_dict["dialog_list_JP"][i]
        return show_dict["output_text"]  


#track, check, dialog에서 추출한 글자들을 출력할 수 있게 전부 합쳐줌.
def combine_text_save(list_order_info):
    comb_text = combine_text()
    if info_dict["track_num"] != 0: #track의 존재여부 확인
        show_dict["output_text"] = comb_text.track_comb(show_dict["output_text"], show_dict)
    if list_order_info[0]: #check, dialog의 순서 및 존재여부 확인
        if list_order_info[1] < list_order_info[2]:
            show_dict["output_text"] = comb_text.check_comb(show_dict["output_text"], show_dict)
            show_dict["output_text"] = comb_text.dialog_comb(show_dict["output_text"], show_dict)
        else:
            show_dict["output_text"] = comb_text.dialog_comb(show_dict["output_text"], show_dict)
            show_dict["output_text"] = comb_text.check_comb(show_dict["output_text"], show_dict)
    else:
        if info_dict["check_exist"]:
            show_dict["output_text"] = comb_text.check_comb(show_dict["output_text"], show_dict)
        elif info_dict["dialog_exist"]:
            show_dict["output_text"] = comb_text.dialog_comb(show_dict["output_text"], show_dict)


#문자를 추출하는 메인함수
def main_extract(helper):
    init(info_dict)
    init(show_dict)
    info_dict["track_list"]
    main_string = helper["input1"].get("1.0","end")
    main_string_list = main_string.splitlines()
    #입력받은 문자를 개행에 따라서 사전에 순서대로 저장해줌
    #반환되는 값은 check와 dialog의 순서와 각각의 위치에 대한 배열값
    list_order_info = div_info(main_string_list)

    #전부 다 없으면 그냥 잘못된 스크립트를 입력했다고 하고 끝내버림.
    if info_dict["track_num"] == 0 and info_dict["check_exist"] == False and info_dict["dialog_exist"] == False:
        helper["output1"].configure(state="normal")
        helper["output1"].insert("1.0", "You typed\nwrong script.\nPlease type\nproper script.")
        return helper["output1"].configure(state="disabled")
    
    #track과 check는 정보를 분리하기 쉽기 때문에 바로 분리해서 track_JP와 check_JP에 저장.
    track_check_save()

    #dialog는 가장 일반적인 경우인 :~, :~/ ;~, ;~/ 부터 해결하기 시작함. 일단 문자열을 배열로 분해한다.
    if info_dict["dialog_exist"]:
        dialog_save()
    
    #track, check, dialog에서 추출한 글자들을 출력할 수 있게 전부 합쳐줌.
    combine_text_save(list_order_info)

    helper["check"].set("")
    helper["result"].set("")
    helper["output1"].configure(state="normal")
    helper["output1"].delete("1.0", "end")
    helper["output1"].insert("1.0", show_dict["output_text"])
    helper["output1"].configure(state="disabled")


###여기에서 부터 추출된 단어들을 번역 후 입력된 단어들을 검사해주는 함수###


#입력받은 단어들의 개수를 검사하는 함수.
def check_words_num(en_string_list):
    total_num = info_dict["track_num"]
    if info_dict["check_exist"]:
        total_num += 1
    if info_dict["dialog_exist"]:
        total_num += len(info_dict["dialog_break"])
    if total_num != len(en_string_list):
        return [True, total_num]
    else:
        return [False, total_num]


#부적절한 단어가 있는지 검사하는 함수
def check_improper_word(i, en_string_list):
    if "," in en_string_list[i]:
        return True
    elif "/" in en_string_list[i]:
        if "[" in en_string_list[i] and "]" in en_string_list[i]:
            index_first = en_string_list[i].find("/")
            index_last = en_string_list[i].rfind("/")
            index_br_first = en_string_list[i].find("[")
            index_br_last = en_string_list[i].find("]")
            if index_first < index_br_first or index_last > index_br_last:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#입력한 단어들을 검사하는 메인함수
def main_check(helper):
    if info_dict["track_num"] == 0 and info_dict["check_exist"] == False and info_dict["dialog_exist"] == False:
        return helper["check"].set("")
    #영단어 소환 후 분리 시켜놓음
    en_string = helper["input2"].get("1.0","end")
    en_string_list = en_string.splitlines()
    #영단어의 수가 많은가 적은가
    chk_num = check_words_num(en_string_list)
    if chk_num[0]:
        return helper["check"].set(f"Number of items does not match. Please type {chk_num[1]} items in \"Want to change\".")
    
    text_to_send = ""

    #영단어의 길이가 얼마나 긴가.
    for i in range(len(en_string_list)):
        if len(en_string_list[i]) > 16:
            text_to_send = text_to_send + "● Some of the items names may not be seen properly on AviUtl.\nIt is recommended that the length of the item be less than 16 characters. (No problem to \"Change\")\n"
            break
    
    #영단어에 부적절한 단어가 포함되어있는가.
    #,과 /는 바로 안 됨. 단 [/]는 됨.
    #└나 ↑나 ()괄호(일본어식)은 문자깨짐
    non_proper_word = ["└", "↑", "↓", "（", "）", "［", "］", "～"]
    for i in range(len(en_string_list)):
        if check_improper_word(i, en_string_list):
            return helper["check"].set("● Character \",\", \"/\" make script not working. Change them to alternative character.(\"/\"in \"[]\" is okay)\n")
        for j in (range(len(non_proper_word))):
            if non_proper_word[j] in en_string_list[i]:
                text_to_send = text_to_send + "● Character like \"└\", \"↑\" or double-byte character like \"（\", \"［\", \"～\" could show broken letter on script.\nChange them to alternave characeter. (Change \"└\" or \"↑\" to \">\" is recommended. Also no problem to \"Change\")\n"
                break
    
    if text_to_send == "":
        text_to_send = text_to_send + "It's okay to change."
    
    helper["result"].set("")
    helper["check"].set(text_to_send)
    

###여기에서부터 결과화면에 단어의 출력과 관계된 함수###


#결과의 단어들을 전부 다 합하는 함수
def combine_result_text(en_string_list, en_str_list_num):
    result_text=""
    if info_dict["track_num"] != 0: #track
        for i in range(info_dict["track_num"]):
            trk_temp = info_dict["track_list"][i].replace(show_dict["track_list_JP"][i], en_string_list[en_str_list_num])
            result_text = result_text + trk_temp + "\n"
            en_str_list_num += 1
    if info_dict["check_exist"]: #check
        result_text = result_text + info_dict["check_list"].replace(show_dict["check_list_JP"], en_string_list[en_str_list_num]) + "\n"
        en_str_list_num += 1
    if info_dict["dialog_exist"]: #dialog
        for i in range(len(info_dict["dialog_break"])):
            break_temp = info_dict["dialog_break"][i]
            break_temp[1:info_dict["dia_cut_end"][i]] = en_string_list[en_str_list_num]
            if i == 0:
                result_text = result_text + "--dialog" + "".join(break_temp)
            else:
                result_text = result_text + "".join(break_temp)           
            en_str_list_num += 1
    show_dict["result_text_fin"] = result_text + ";"


#단어들을 Result에 내보내는 메인함수
def main_get_change(helper):
    en_string = helper["input2"].get("1.0","end")
    en_string_list = en_string.splitlines()
    en_str_list_num = 0

    #입력한 단어와 추출된 단어의 개수가 일치하지 않으면 바로 중지시킴
    chk_num = check_words_num(en_string_list)
    if chk_num[0]:
        helper["check"].set("")
        return helper["result"].set(f"Number of items does not match. Please type {chk_num[1]} items in \"Want to change\".")
    #가동을 아예시키지 못하는 함수가 있어도 중지시킴
    for i in range(len(en_string_list)):
        if check_improper_word(i, en_string_list):
            helper["check"].set("")
            return helper["result"].set("● Character \",\", \"/\" make script not working. Change them to alternative character.(\"/\"in \"[]\" is okay)\n")

    #기존의 입력한 정보와 Want to change에서 입력받은 단어들을 전부 다 합쳐주자!
    combine_result_text(en_string_list, en_str_list_num)

    #망할놈의 local fig가 있을 때는 자동으로 바꿔줌. 왜 작업이 다 끝나고 나서 이 문제가 있다는 걸 알았을까.
    if "local fig" in show_dict["result_text_fin"]:
        for i in range(len(local_fig_text["local_JP"])):
            if local_fig_text["local_JP"][i] in show_dict["result_text_fin"]:
                result_text_temp = show_dict["result_text_fin"].replace(local_fig_text["local_JP"][i], local_fig_text["local_EN"][i])
                show_dict["result_text_fin"] = result_text_temp
    #출력함
    helper["output2"].configure(state="normal")
    helper["output2"].insert("1.0", show_dict["result_text_fin"])
    helper["output2"].configure(state="disabled")
    helper["check"].set("")
    helper["result"].set("Change success!")