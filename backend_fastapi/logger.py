# Logger setup

import logging

logging.basicConfig(
    filename='employee_backend.log',
    level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger=logging.getLogger()