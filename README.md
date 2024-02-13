# pyi-auto-decompile
decompiles the pyinstaller exe with auto magic hex patching.

Since its Korean, if you want english, open the issue.

# Setup
You may need Visual C++.
You need Python 3.9+.

```
git clone https://github.com/cintagram/pyi-auto-decompile
git clone https://github.com/cintagram/pydumpck/

cd pydumpck
cd pydumpck-1.17.9
pip install -e .
```

# How 2 Use
0. Follow setup
1. Paste your exe in `target` folder.
2. Open main.py in cmd or terminal.
3. Enter your exe name. ex: test.exe
4. Wait 4 decompiler to finish.
5. Once finished, check `pyc_dec/<filename>.pyc.cdc.py`

# iSH Shell Environment
This tool also works in iphone iSH Shell app.

1. Download ishenv.tar.gz on releases.
2. open ish shell, go to settings.
3. go to Filesystems, click import.
4. Select ishenv.tar.gx which you downloaded.
5. Wait until finish.
6. When finished, click ishenv, click Boot from this filesystem.
7. The app will exit, you reopen.
8. I wrote instructions in env intro, follow them.

# ToDo
use other pyc pyz when os/re pyc nonexist

somehin else

# Credits
- pyinstxtractor: extremecoders-re
- pydumpck original: serfend
- pycdc: zrax
- this tool: CintagramABP
