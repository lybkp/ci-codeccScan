#
# Contributed by Rodrigo Tobar <rtobar@icrar.org>
#
# ICRAR - International Centre for Radio Astronomy Research
# (c) UWA - The University of Western Australia, 2016
# Copyright by UWA (in the framework of the ICRAR)
#
'''
Wrapper for _yajl2 C extension module
'''

from ijson import common, compat, utils
from ijson.backends import _yajl2


_get_buf_size = lambda kwargs: kwargs.pop('buf_size', 64 * 1024)
_get_prefix = lambda prefix: [] if not prefix else prefix.split(".")

def _itemlike_pipeline(itemslike_coro, prefix, map_type, config):
    return (
        (itemslike_coro, (_get_prefix(prefix), map_type), {}),
        (_yajl2.parse_basecoro, (False,), {}),
        (_yajl2.basic_parse_basecoro, [], config)
    )

@utils.coroutine
def basic_parse_basecoro(target, **kwargs):
    return _yajl2.basic_parse_basecoro(target.send, **kwargs)

def basic_parse_gen(file, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = _get_buf_size(kwargs)
    return _yajl2.basic_parse(f, buf_size, **kwargs)

def basic_parse_async(file, **kwargs):
    buf_size = _get_buf_size(kwargs)
    return _yajl2.basic_parse_async(file, buf_size, **kwargs)

@utils.coroutine
def parse_basecoro(target, **kwargs):
    return _yajl2.parse_basecoro(target.send, **kwargs)

def parse_gen(file, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = _get_buf_size(kwargs)
    return _yajl2.parse(f, buf_size, **kwargs)

def parse_async(file, **kwargs):
    buf_size = _get_buf_size(kwargs)
    return _yajl2.parse_async(file, buf_size, **kwargs)


@utils.coroutine
def kvitems_basecoro(target, prefix, map_type=None, **kwargs):
    return _yajl2.kvitems_basecoro(target.send, prefix, map_type, **kwargs)

def kvitems_coro(target, prefix, map_type=None, **config):
    return utils.chain(target.send,
        *_itemlike_pipeline(_yajl2.kvitems_basecoro, prefix, map_type, config)
    )

def kvitems_gen(file, prefix, map_type=None, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = _get_buf_size(kwargs)
    prefix = _get_prefix(prefix)
    return _yajl2.kvitems(f, buf_size, prefix, map_type, **kwargs)

def kvitems_async(file, prefix, map_type=None, **kwargs):
    buf_size = _get_buf_size(kwargs)
    prefix = _get_prefix(prefix)
    return _yajl2.kvitems_async(file, buf_size, prefix, map_type, **kwargs)


@utils.coroutine
def items_basecoro(target, prefix, map_type=None, **kwargs):
    return _yajl2.items_basecoro(target.send, prefix, map_type, **kwargs)

def items_coro(target, prefix, map_type=None, **config):
    return utils.chain(target.send,
        *_itemlike_pipeline(_yajl2.items_basecoro, prefix, map_type, config)
    )

def items_gen(file, prefix, map_type=None, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = _get_buf_size(kwargs)
    prefix = _get_prefix(prefix)
    return _yajl2.items(f, buf_size, prefix, map_type, **kwargs)

def items_async(file, prefix, map_type=None, **kwargs):
    buf_size = _get_buf_size(kwargs)
    prefix = _get_prefix(prefix)
    return _yajl2.items_async(file, buf_size, prefix, map_type, **kwargs)

common.enrich_backend(globals())
