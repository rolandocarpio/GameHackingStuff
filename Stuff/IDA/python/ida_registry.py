# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: registry
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_registry', [dirname(__file__)])
        except ImportError:
            import _ida_registry
            return _ida_registry
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_registry', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_registry = swig_import_helper()
    del swig_import_helper
else:
    import _ida_registry
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


import ida_idaapi

import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        func.func_dict["bc695redef"] = True
        return func


def reg_read_string(*args):
  """
  reg_read_string(name, subkey=None, _def=None) -> PyObject *
  """
  return _ida_registry.reg_read_string(*args)

def reg_data_type(*args):
  """
  reg_data_type(name, subkey=None) -> regval_type_t
  """
  return _ida_registry.reg_data_type(*args)

def reg_read_binary(*args):
  """
  reg_read_binary(name, subkey=None) -> PyObject *
  """
  return _ida_registry.reg_read_binary(*args)

def reg_write_binary(*args):
  """
  reg_write_binary(name, py_bytes, subkey=None)
  """
  return _ida_registry.reg_write_binary(*args)

def reg_subkey_subkeys(*args):
  """
  reg_subkey_subkeys(name) -> PyObject *
  """
  return _ida_registry.reg_subkey_subkeys(*args)

def reg_subkey_values(*args):
  """
  reg_subkey_values(name) -> PyObject *
  """
  return _ida_registry.reg_subkey_values(*args)
ROOT_KEY_NAME = _ida_registry.ROOT_KEY_NAME
reg_unknown = _ida_registry.reg_unknown
reg_sz = _ida_registry.reg_sz
reg_binary = _ida_registry.reg_binary
reg_dword = _ida_registry.reg_dword

def reg_delete_subkey(*args):
  """
  reg_delete_subkey(name) -> bool
  """
  return _ida_registry.reg_delete_subkey(*args)

def reg_delete_tree(*args):
  """
  reg_delete_tree(name) -> bool
  """
  return _ida_registry.reg_delete_tree(*args)

def reg_delete(*args):
  """
  reg_delete(name, subkey=None) -> bool
  """
  return _ida_registry.reg_delete(*args)

def reg_subkey_exists(*args):
  """
  reg_subkey_exists(name) -> bool
  """
  return _ida_registry.reg_subkey_exists(*args)

def reg_exists(*args):
  """
  reg_exists(name, subkey=None) -> bool
  """
  return _ida_registry.reg_exists(*args)

def reg_read_strlist(*args):
  """
  reg_read_strlist(list, subkey)
  """
  return _ida_registry.reg_read_strlist(*args)

def reg_update_strlist(*args):
  """
  reg_update_strlist(subkey, add, maxrecs, rem=None, ignorecase=False)
  """
  return _ida_registry.reg_update_strlist(*args)

def reg_write_string(*args):
  """
  reg_write_string(name, utf8, subkey=None)
  """
  return _ida_registry.reg_write_string(*args)

def reg_read_int(*args):
  """
  reg_read_int(name, defval, subkey=None) -> int
  """
  return _ida_registry.reg_read_int(*args)

def reg_write_int(*args):
  """
  reg_write_int(name, value, subkey=None)
  """
  return _ida_registry.reg_write_int(*args)

def reg_read_bool(*args):
  """
  reg_read_bool(name, defval, subkey=None) -> bool
  """
  return _ida_registry.reg_read_bool(*args)

def reg_write_bool(*args):
  """
  reg_write_bool(name, value, subkey=None)
  """
  return _ida_registry.reg_write_bool(*args)

def reg_update_filestrlist(*args):
  """
  reg_update_filestrlist(subkey, add, maxrecs, rem=None)
  """
  return _ida_registry.reg_update_filestrlist(*args)

def reg_load(*args):
  """
  reg_load()
  """
  return _ida_registry.reg_load(*args)

def reg_flush(*args):
  """
  reg_flush()
  """
  return _ida_registry.reg_flush(*args)

