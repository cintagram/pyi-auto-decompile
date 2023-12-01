import subprocess
import zipfile
from pathlib import Path
import os
import pyinstxtractor as pyix
import compile

def find_common_hex(hex_line1, hex_line2):
    set_line1 = set(hex_line1)
    set_line2 = set(hex_line2)
    return ''.join(set_line1.intersection(set_line2))

if __name__ == "__main__":
	print("""
	펄스의 짱짱 pyinstaller 디컴파일러
	
	리셀은 하던지 말던지 상관없는데 자기가 만든거라고만 하지 말아주면 딱좋노
	
	""")
	filename = input("target폴더 안에 exe 집어넣고 파일명 입력(확장자 포함): ")
	pyix.main("target/{}".format(filename))
	print("--------------------------\n언패킹 완료노 ㄱㄷ")
	print("매직헥스 패치중")
	p = Path(os.path.join(os.path.abspath(os.getcwd()), "base_library.zip"))
	extractpath = os.path.join(os.path.abspath(os.getcwd()), "base_library_ex")
	if not os.path.exists(extractpath):
		os.mkdir(extractpath)
		
	fantasy_zip = zipfile.ZipFile(p)
	fantasy_zip.extractall(extractpath)
	fantasy_zip.close()
	#input("@")
	with open(os.path.join(extractpath, "operator.pyc"), 'rb') as fle:
	    first_line_bytes = fle.readline()
	    hex1 = first_line_bytes.hex()
	with open(os.path.join(extractpath, "re.pyc"), "rb") as fe:
		fist = fe.readline()
		hex2 = fist.hex()
	common_hex = find_common_hex(hex1, hex2)
	print("매직헥스 발견: " + str(common_hex))
	common_hex_length = len(common_hex)
	with open("{}.pyc".format(filename.strip(".exe")), "rb") as file:
	    rest_of_file = file.read()
	    file.seek(0)
	    new_first_line = (common_hex + '00' * (common_hex_length - len(rest_of_file)))
	with open("{}.pyc".format(filename.strip(".exe")), "wb") as file:
	    file.write(bytes(new_first_line, "utf-8") + rest_of_file)
	print("메인파일 복호화 하는중")
	if os.path.exists("{}.pyc".format(filename.strip(".exe"))):
		compile.extractwh("{}.pyc".format(filename.strip(".exe")))
	elif os.path.exists("main.pyc"):
		compile.extractwh("main.pyc")
	else:
		print("타겟 pyc를 찾지 못했습니다")
	