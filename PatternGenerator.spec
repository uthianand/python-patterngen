# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['PatternGenerator.py'],
             pathex=['C:\\Input'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('1.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\1.png', "DATA"),
			('2.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\2.png', "DATA"),
			('3.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\3.png', "DATA"),
			('4.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\4.png', "DATA"),
			('5.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\5.png', "DATA"),
			('6.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\6.png', "DATA"),
			('7.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\7.png', "DATA"),
			('8.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\8.png', "DATA"),
			('9.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\9.png', "DATA"),
			('blank.png','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\image\\blank.png', "DATA"),
			('calibrib.ttf','C:\\Users\\raghu2013\\Documents\\Anand\\PythonProj\\PatternGen\\font\\calibrib.ttf', "DATA"),
			]
			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='PatternGenerator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
