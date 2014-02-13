#!/usr/env python
# Preprocesseror script to put cython annotation into pyx files
from __future__ import division, print_function
from os.path import splitext
import sys

START_TAG  = '#PYX START'
DEFINE_TAG = '#PYX DEFINE'
CDEF_TAG   = '#PYX CDEF'
ELSE_TAG   = '#PYX ELSE'
END_TAG    = '#PYX END'
MAP_TAG    = '#PYX MAP '


def pyx_preprocess(MODE, in_line, PYX_MAP):

    if in_line.find(START_TAG) != -1:
        in_line = in_line.replace(START_TAG, '')
        MODE = START_TAG
    elif in_line.find(DEFINE_TAG) != -1:
        in_line = in_line.replace(DEFINE_TAG, '')
        MODE = DEFINE_TAG
    elif in_line.find(CDEF_TAG) != -1:
        in_line = in_line.replace(CDEF_TAG, 'cdef').replace('\n', '')
        MODE = CDEF_TAG
    elif in_line.find(ELSE_TAG) != -1:
        in_line = in_line.replace(ELSE_TAG, '')
        MODE = ELSE_TAG
    elif in_line.find(END_TAG) != -1:
        in_line = in_line.replace(END_TAG, '')
        MODE = None
    # Check for map mode
    if in_line.find(MAP_TAG) != -1:
        map_cmd = in_line.replace(MAP_TAG, '')
        pos = map_cmd.find(' ')
        key = map_cmd[0:pos]
        val = map_cmd[pos + 1:].replace('\n', '')
        PYX_MAP[key] = val
        in_line = '#// MAPPING %s -> %s\n' % (key, val)
    # Perform mapping
    return MODE, in_line


def translate_cython_line(in_line, PYX_MAP):
    for key, val in PYX_MAP.iteritems():
        in_line = in_line.replace(key, val)
    in_line = in_line.replace('"""', '')
    in_line = in_line.replace('#', '')
    in_line = in_line.replace('//', '#')
    return in_line


def translate_python_to_cython(input_lines):
    try:
        from hscom import helpers
        timestamp = helpers.get_timestamp()
    except Exception:
        timestamp = '???'
        pass
    output_lines = ['# THIS FILE WAS AUTOGENERATED ON %s\n' % timestamp]
    MODE = None
    PYX_MAP = {}
    translate_nLines = 0
    for in_line in input_lines:
        MODE, in_line = pyx_preprocess(MODE, in_line, PYX_MAP)
        if MODE is None:
            # No cython annotations
            output_lines.append(in_line)
        elif MODE == START_TAG:
            # Start unannotating cython code;
            in_line = translate_cython_line(in_line, PYX_MAP)
            output_lines.append(in_line)
        elif MODE == ELSE_TAG:
            # Exclude from cython
            pass
        elif MODE == DEFINE_TAG:
            # Skip the python define
            if in_line.find('#') == -1 and in_line.find('):') != -1:
                MODE = None
                translate_nLines = 0
            # Translate the cython define
            elif in_line.find('#') == 0:
                translate_nLines = 1
        elif MODE == CDEF_TAG:
            translate_nLines = 1
            MODE = None
        # We are translating the next N lines
        if translate_nLines > 0:
            translate_nLines -= 1
            in_line = translate_cython_line(in_line, PYX_MAP)
            output_lines.append(in_line)
    return output_lines


def generate_pyx(py_fpath):
    # Read python file
    print('[pyx] reading: %r' % py_fpath)
    with open(py_fpath, 'r') as file_:
        input_lines = file_.readlines()
    # Translate python file
    print('[pyx] translating')
    output_lines = translate_python_to_cython(input_lines)
    # Write cython file
    pyx_fpath = splitext(py_fpath)[0] + '.pyx'
    print('[pyx] writing: %r' % pyx_fpath)
    cython_text = ''.join(output_lines)
    with open(pyx_fpath, 'w') as file_:
        file_.write(cython_text)
    return pyx_fpath

if __name__ == '__main__':
    import setup
    DEBUG = True
    py_fpath = sys.argv[-1]
    #py_fpath = 'hotspotter/spatial_verification2.py'
    pyx_fpath = generate_pyx(py_fpath)
    if pyx_fpath is not None:
        ret = setup.compile_cython(pyx_fpath)
        if ret == 0 and DEBUG:
            setup.inspect_cython_typness(pyx_fpath)
