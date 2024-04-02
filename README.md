# pyi-auto-decompile
decompiles the pyinstaller exe with auto magic hex patching.

Since its Korean, if you want english, open the issue.

# Todo & Current Issues
- **Current Issue**: unable to decrypt pyc from above 3.11 (fixing)

# Setup
You may need Visual C++.
You need Python 3.11+.

```
git clone https://github.com/cintagram/pyi-auto-decompile
git clone https://github.com/cintagram/pydumpck/

cd pydumpck
pip install -e .
```

# How 2 Use
0. Follow setup
1. Paste your exe in `target` folder.
2. Open main.py in cmd or terminal.
3. Enter your exe name. ex: test.exe
4. Wait 4 decompiler to finish.
5. Once finished, check `pyc_dec/<filename>.pyc.cdc.py`

# iSH Shell Environment (iOS No JB)
This tool also works in iphone iSH Shell app which is in the appstore.

1. Download ishenv.tar.gz on releases.
2. open ish shell, go to settings.
3. go to Filesystems, click import.
4. Select system_env.tar.gz which you downloaded.
5. Wait until finish.
6. When finished, click ishenv, click Boot from this filesystem.
7. The app will exit, you reopen.
8. I wrote instructions in env intro, follow them.

# Android Termux
install these libs and git clone this repo and do it yourself
I dont have android device (physical)
```
gcc
clang
clang++
rust
golang
python
python-pip
openssl
libxml2-dev
openjdk-17
binutils
cmake
automake
git
aapt
```
pip: tinyaes
(not all is listed here)


# Credits
- pyinstxtractor: extremecoders-re
- pydumpck original: serfend
- pycdc: zrax
- this tool: CintagramABP
