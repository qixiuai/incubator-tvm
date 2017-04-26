"""Code generation related functions."""
from ._ffi.function import _init_api

def build_module(lowered_func, target):
    """Build lowered_func into Module.

    Parameters
    ----------
    lowered_func : LoweredFunc
        The lowered function

    target : str
        The target module type.

    Returns
    -------
    module : Module
        The corressponding module.
    """
    return _Build(lowered_func, target)


def enabled(target):
    """Whether target is enabled for codegen.

    Parameters
    ----------
    target : str
        The target module type.

    Returns
    -------
    enabled : boolean
        Whether the target module is enabled.
    """
    return _Enabled(target)


_init_api("tvm.codegen")
