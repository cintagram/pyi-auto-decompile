import subprocess
import os
import re
import json

code_template = '''
''.join(
    (lambda func: (str(chr(i ^ xor_table[i % len(xor_table)])) for i in range(
        {rangenum_1},
        {rangenum_2}
    ) if func(i)))
    (lambda i: (
        
{condition_sep}
        
    ))
)
'''

def extract_string_between(original_string, start_string, end_string):
    start_index = original_string.find(start_string) + len(start_string)
    end_index = original_string.find(end_string, start_index)
    
    if start_index != -1 and end_index != -1:
        extracted_string = original_string[start_index:end_index]
        return extracted_string
    else:
        return "Substring not found."
        
def process_script(pattern, xor_table):
    condition_pattern = re.compile('round\(abs\([^)]+\)\)\)')

    matches = condition_pattern.findall(pattern)

    passcontinuestring = matches[-4]
    rangeroundstring = matches[-3]
    condition_list = []

    for l in range(len(matches) - 5):
        new_data = {"condition_{}".format(l): matches[int(l)]}
        condition_list.append(new_data)
        l += 1

    condition_func = ""
    for k in range(len(matches) - 5):
        condition_key = condition_list[k]["condition_{}".format(k)]
        if k == len(matches) - 6:
            condition_func += f"""\t\t\tTrue if {condition_key} == i else False"""
        elif k == 0:
            condition_func += f"""\t\tTrue if {condition_key} == i else\n\t\t"""
            
        else:
            condition_func += f"""True if {condition_key} == i else\n\t\t"""

    condition_sep = condition_func.format(**{f"condition_{k}": data[f"condition_{k}"] for k, data in enumerate(condition_list)})

    condition_tel = {"rangenum_1": passcontinuestring, "rangenum_2": rangeroundstring, "condition_sep": condition_sep}

    return code_template.format(**condition_tel)

def extract_pattern(script):
    pattern_matches = re.findall(r"abs\(([+-]?\d+\.\d+)\)", script)
    pattern_floats = [float(match) for match in pattern_matches]
    return pattern_floats
    
def pair_floats(float_list):
    return [(float_list[i], float_list[i + 1]) for i in range(0, len(float_list) - 1, 2)]

def extractwh(path):
    subprocess.run(['pydumpck', '--tf', path, '-y', 'pyc', '-o', '../pyc_dec'])
    print("디컴파일 끝\npyc_dec 폴더에 <파일명>.pyc.cdc.py 확인 ㄱ")
    
    #이거는 엠피린 그래버 컨피그 문법오류 고치는건데 미완임
    """
    nerec = open("/home/Empyrean-Decryptor/config_dec/Client.pyc.cdc.py", "r", encoding = "utf-8").read()
	
	#Fixing Syntax Errors (Very Dirty, dont look these plz!! :(
    print("Detected Syntax Errors, Fixing...")
    newrec = nerec.replace("xor_table = []", "xor_table = [")
	
    second = newrec.replace("]\n__CONFIG__", "]]\n__CONFIG__")

    original_string = (second.replace('passif', 'if').replace('passelif', 'elif'))
    start_string = "xor_table = ["
    end_string = "]]\n__CONFIG"
    result = extract_string_between(original_string, start_string, end_string)
    pa = result.replace("))))][chr", "))))], [chr").strip("[").strip("]")
    fixedtable = original_string.replace("xor_table = [{}]".format(result), "xor_table = [{}]".format(pa))
    
    #Fix Code Structure
    print("Fixing Code Structure...")
    if not os.path.exists("temp"):
        os.mkdir("temp")
        
    open("temp/xortables.py", "w+", encoding="utf-8").write("global xor_table\nxor_table = [{}]".format(pa.replace("chr(round(abs((", "chr(round(abs(").replace("))))]", ")))]").replace("))))", ")))").replace(")))][", "))), ")))
    s2 = "__CONFIG__ = {"
    e2 = "}"
    exconfig2 = extract_string_between(original_string, s2, e2)
    structures = exconfig2.split(",")
    qyeh = "__CONFIG__ = {"
    for a in range(len(structures)):
        from grabberextracted.temp.xortables import xor_table as xor_tables
        structures[a] = process_script(structures[a], xor_tables)
        qyeh += (structures[a] + ",")
        a += 1
    open("temp/xortables.py", "a", encoding = "utf-8").write("\n\n{}".format(qyeh+"}\nprint(list(__CONFIG__))"))
    final_decoded = open("temp/xortables.py", "r", encoding = "utf-8").read()
    
    
	#Compile Fixed Source
    open("/home/Empyrean-Decryptor/config_dec/config_decfixed.py", "w+", encoding = "utf-8").write(final_decoded)
    compiled = compile(final_decoded, "<string>", "exec")
    exec(compiled)
    print("-----------------------------")
    print("DECRYPTION SUCCESSFUL")
    print("FOUND LINKED WEBHOOK: ")
    """