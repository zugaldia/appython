from appython.components.queue.base_manager import BaseManager
from shared.config import Config

import logging


class QueueManager(BaseManager):

    @classmethod
    def launch_user_registration(cls, user_id):
        data = {'user_id': user_id}
        cls.launch_task(
            queue_name='user-registration', data=data,
            dry_run=Config.IS_DEVELOPMENT)
