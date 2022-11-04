project(
  'operato',
  'cpp',
  version: '0.0.1',
  default_options : ['cpp_std=c++20']
)

include_directories = include_directories(['/usr/include'])

sources = [
  'operato.cc'
]

cpp_args = [
  # Pre-processor defines
  '-DFMT_HEADER_ONLY',
  # Warnings
  '-Wall',
  '-Werror',
  '-Wpedantic'
]

executable(
  'operato',
  sources,
  include_directories : include_directories,
  cpp_args : cpp_args)

