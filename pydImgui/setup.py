import os
import sys

from distutils.core import setup, Extension
from distutils import sysconfig

cpp_args = ['-std=c++11', '-stdlib=libc++']

sfc_module = Extension('pyd_imgui', sources = ['module.cpp', 'kiero/kiero.cpp', 'kiero/minhook/src/buffer.c',
                                               'kiero/minhook/src/hook.c', 'kiero/minhook/src/trampoline.c',
                                               'kiero/minhook/src/hde/hde32.c', 'kiero/minhook/src/hde/hde64.c',
                                               'imgui/imgui.cpp', 'imgui/imgui_demo.cpp', 'imgui/imgui_draw.cpp',
                                               'imgui/imgui_impl_dx9.cpp', 'imgui/imgui_impl_win32.cpp', 'imgui/imgui_tables.cpp', 'imgui/imgui_widgets.cpp'],
    include_dirs=['pybind11/include', 'kiero', 'kiero/minhook/include', 'Windows.h'],
    libraries=['user32'],
    language='c++',
    extra_compile_args = cpp_args,)

setup(name = 'pyd_imgui',
    version = '1.0',
    description = 'Python package with d3d9 hook and imgui.',
    ext_modules = [sfc_module],)
