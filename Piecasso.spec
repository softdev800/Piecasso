# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['paint.py'],
             pathex=['D:\\Portfolio\\Piecasso'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Piecasso',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='icons\\piecasso.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Piecasso')
app = BUNDLE(coll,
             name='Piecasso.app',
             icon='icons/piecasso.icns',
             bundle_identifier='com.ucoder.Piecasso',
             info_plist={
                 'NSHighResolutionCapable': 'True'
             },
)
