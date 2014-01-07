from __future__ import print_function, division
import sys
from os.path import expanduser, join, exists, split


def add_hotspotter_to_path():
    # Look for hotspotter in ~/code
    hotspotter_dir = join(expanduser('~'), 'code', 'hotspotter')
    if not exists(hotspotter_dir):
        print('[pyhesaff] hotspotter_dir=%r DOES NOT EXIST!' % (hotspotter_dir,))
    # Append hotspotter location (not dir) to PYTHON_PATH (i.e. sys.path)
    hotspotter_location = split(hotspotter_dir)[0]
    sys.path.append(hotspotter_location)

# Ensure hotspotter is in path before importing it
add_hotspotter_to_path()

from hotspotter import helpers

# Localize hessian affine code
code_dir   = join(expanduser('~'), 'code')
hsdir      = join(code_dir, 'hotspotter')
extern_dir = join(hsdir, '_tpl', 'extern_feat')
hesaffsrc_dir = join(code_dir, 'hesaff')

hesaffbuild_dir = join(hesaffsrc_dir, 'build')
filemap = {
    hesaffbuild_dir: ['hesaffexe.exe',
                      'libhesaff.so',
                      'libhesaff.dylib',
                      'hesaffexe.mac',
                      'hesaffexe.ln',
                      'libhesaff.dll'],
    hesaffsrc_dir: ['pyhesaff.py'],
}

for srcdir, fname_list in filemap.iteritems():
    for fname in fname_list:
        src  = join(srcdir, fname)
        dest = join(extern_dir, fname)
        try:
            helpers.copy(src, dest)
        except Exception as ex:
            print(ex)

#raw_input('[_tpl/localize] Press enter to continue')
