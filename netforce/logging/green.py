# Copyright 2018 eBay Inc.
# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


from eventlet import corolocal
import logging
from logging.handlers import WatchedFileHandler


class GreenletIdAddingFilter(logging.Filter):
    def filter(self, record):
        record.greenlet = corolocal.get_ident()
        return True


class FilterAddingWatchedHandler(WatchedFileHandler):
    """
    Subclass of watched handler that can be used to add a filter that adds the
    greenlet id information to the log record. This can then be used by the
    logger formatter strings in logging conf
    e.g %(asctime)-15s %(name)-5s %(levelname)-8s  %(message)s %(greenlet)-12s
    """

    def __init__(self, *args, **kwargs):
        super(FilterAddingWatchedHandler, self).__init__(*args, **kwargs)
        self.addFilter(GreenletIdAddingFilter())