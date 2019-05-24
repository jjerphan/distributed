from __future__ import print_function, division, absolute_import

import subprocess
import logging

from . import config
from dask.config import config
from .actor import Actor, ActorFuture
from .core import connect, rpc
from .deploy import LocalCluster, Adaptive
from .diagnostics import progress
from .client import (
    Client,
    Executor,
    CompatibleExecutor,
    wait,
    as_completed,
    default_client,
    fire_and_forget,
    Future,
    futures_of,
    get_task_stream,
)
from .lock import Lock
from .nanny import Nanny
from .pubsub import Pub, Sub
from .queues import Queue
from .scheduler import Scheduler
from .threadpoolexecutor import rejoin
from .utils import sync
from .variable import Variable
from .worker import Worker, get_worker, get_client, secede, Reschedule
from .worker_client import local_client, worker_client

from tornado.gen import TimeoutError

from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]

logging.info("Distributed %s imported" % __version__)
logging.info("Git revision: %s" % __git_revision__)

git_branches = subprocess.check_output(["git", "branch"])
logging.info("git branches:\n%s" % git_branches)

del get_versions, versions
