from jupyter_kernel import MagicKernel
from IPython.kernel.zmq import session as ss
import zmq
import logging

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def get_kernel():
    log = logging.getLogger('test')
    log.setLevel(logging.DEBUG)

    for hdlr in log.handlers:
        log.removeHandler(hdlr)

    hdlr = logging.StreamHandler(StringIO())
    hdlr.setLevel(logging.DEBUG)
    log.addHandler(hdlr)

    context = zmq.Context.instance()
    iopub_socket = context.socket(zmq.PUB)

    kernel = MagicKernel(session=ss.Session(), iopub_socket=iopub_socket,
                         log=log)
    return kernel


def get_log_text(kernel):
    return kernel.log.handlers[0].stream.getvalue()



k = get_kernel()
import ipdb; ipdb.set_trace()
pass