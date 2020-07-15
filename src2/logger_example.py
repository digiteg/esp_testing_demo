import sys
import traceback
from microtest.micrologger import MicroLogger
from microtest.basiclogger import LogLevels

log = MicroLogger()

log.basicConfig(vlevel=LogLevels.DEBUG)
log.log_debug("Test message: {}({})", 100, "foobar")
log.log_info("Test message2: {}({})", 200, "foobar")
log.log_warning("Test message3: {}({})",300,"foobar")
log.log_error("Test message4")
log.log_critical("Test message5")
log.log_info("Test message6")


def extract_function_name():
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        fname = stk[0][3]
        return fname

def log_exception(ex):
        log.log_error("Function {} raised {} ({}): {}",
                 extract_function_name(),  # this is optional
                 ex.__class__,
                 ex.__doc__,
                 ex
                 )

try:
    1/0
except Exception as e:
    log_exception(e)



try:
    assert 1==2
except Exception as e:
    log_exception(e)