#!/usr/bin/python
import json
import os
import logging
import sys
from os.path import join
from pathlib import Path

from lib.util import Util, CONSOLE_LOGGING
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('codegen', 'templates'),
    autoescape=select_autoescape(['jinja2'])
)

import CppHeaderParser

from functools import reduce


_NAME = 'name'
_PARSED_NAME = '__name'
_SNAKE_NAME = '_name'
_VALUE = 'value'
_VALUES = 'values'
_PROPERTIES = 'properties'
_DEFAULT = 'default'
_TYPE = 'type'
_SIZE = 'size'
_PUBLIC = 'public'
_TYPE_MESSAGE_TYPES = 'MessageTypes'
_TYPE_STRING_LENGTHS = 'StringLengths'
_INIT_PY = "__init__.py"
_MESSAGE_TYPES_PY = "message_types.py"
_MESSAGE_UTIL_PY = "message_util.py"
_STRING_LENGTHS_PY = "string_lengths.py"
_ENUM_TEMPLATE = 'enum_template.jinja2'
_UTIL_TEMPLATE = 'util_template.jinja2'
_MESSAGE_TYPE_TEMPLATE = 'message_type_template.jinja2'
_ENUM_DIR = 'enums'
_UTIL_DIR = 'util'
_MESSAGE_TYPE_DIR = 'message_types'

DIR = os.getcwd()
GENERATED_DIR = join(DIR, "../dtc")


def camel_to_snake(str):
    res = reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, str).lower()
    res = res.replace('_i_d', '_id')  # hack to fix ID
    res = res.replace('_o_c_o', '_oco')  # hack to fix OCO
    return res


def write_init_py(directory):
    with open(join(directory, _INIT_PY), "w") as f:
        f.write("")


def parse_class_name(name):
    res = name.replace("s_", "").replace("_", "")
    return res


def new_package(directory):
    os.makedirs(directory)
    write_init_py(directory)


class DTCProtocolHeaderParser:
    def __init__(self, header_file):
        cppHeader = CppHeaderParser.CppHeader(header_file)
        self.enums = cppHeader.enums
        self.message_types = []
        self.message_types_only = []
        self.string_lengths = []
        for x in cppHeader.variables:
            if _DEFAULT in x:
                x[_VALUE] = x[_DEFAULT]
                if x[_TYPE] == 'const uint16_t':
                    self.message_types.append(x)
                    self.message_types_only.append(x[_NAME])
                else:
                    self.string_lengths.append(x)

        self.structs = []
        for _class in cppHeader.classes:
            class_name = parse_class_name(_class)
            snake_class_name = camel_to_snake(class_name).upper()
            if "::union" not in _class and snake_class_name in self.message_types_only:
                _class_obj = {
                    _NAME: class_name,
                    _SNAKE_NAME: camel_to_snake(class_name),
                    _PARSED_NAME: class_name,
                    _PROPERTIES: []
                }
                for x in cppHeader.classes[_class][_PROPERTIES][_PUBLIC]:
                    if _NAME in x and x[_NAME] and x[_NAME].lower() not in [_TYPE, _SIZE]:
                        x[_SNAKE_NAME] = camel_to_snake(x[_NAME])
                        _class_obj[_PROPERTIES].append(x)
                self.structs.append(_class_obj)
            else:
                logging.warning("Ignored struct %s" % _class)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def generate_enums(self, output_directory):
        enum_dir = join(output_directory, _ENUM_DIR)
        new_package(enum_dir)
        template = env.get_template(_ENUM_TEMPLATE)
        for enum in self.enums:
            with open(join(enum_dir, "%s.py" % camel_to_snake(enum[_NAME])), "w") as f:
                f.write(template.render(class_name=enum[_NAME], values=enum[_VALUES]))

        template = env.get_template(_ENUM_TEMPLATE)
        with open(join(enum_dir, _MESSAGE_TYPES_PY), "w") as f:
            f.write(template.render(class_name=_TYPE_MESSAGE_TYPES, values=self.message_types))

        template = env.get_template(_ENUM_TEMPLATE)
        with open(join(enum_dir, _STRING_LENGTHS_PY), "w") as f:
            f.write(template.render(class_name=_TYPE_STRING_LENGTHS, values=self.string_lengths))

    def generate_message_util(self, output_directory):
        util_dir = join(output_directory, _UTIL_DIR)
        new_package(util_dir)
        template = env.get_template(_UTIL_TEMPLATE)
        #logging.info(json.dumps(self.structs, indent=4))
        with open(join(util_dir, _MESSAGE_UTIL_PY), "w") as f:
            f.write(template.render(classes=self.structs))

    def generate_message_types(self, output_directory):
        message_type_dir = join(output_directory, _MESSAGE_TYPE_DIR)
        new_package(message_type_dir)
        template = env.get_template(_MESSAGE_TYPE_TEMPLATE)
        for struct in self.structs:
            name = struct[_PARSED_NAME]
            snake_name = camel_to_snake(name).upper()
            with open(join(message_type_dir, "%s.py" % camel_to_snake(name)), "w") as f:
                f.write(template.render(class_name=name, class_name_snake=snake_name, values=struct[_PROPERTIES]))

    def generate_python_code(self, output_directory):
        os.system("rm -rf %s" % output_directory)
        new_package(output_directory)
        self.generate_enums(output_directory)
        self.generate_message_types(output_directory)
        self.generate_message_util(output_directory)


if __name__ == '__main__':
    Util.setup_logging("CppHeaderParser", console=CONSOLE_LOGGING, log_to_file=False)
    parser = DTCProtocolHeaderParser("DTCProtocol.h")
    #logging.info(json.dumps(parser.structs, indent=4))
    parser.generate_python_code(output_directory=GENERATED_DIR)
