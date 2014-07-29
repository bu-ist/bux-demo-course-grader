# Grader settings module
#
# Course-specifc grader configuration goes here
# Loaded by ``bux_grader_framework`` at run time
#

XQUEUE_QUEUE = "test-pull"
XQUEUE_URL = "http://192.168.33.10:18040"
XQUEUE_USER = "lms"
XQUEUE_PASSWORD = "password"
XQUEUE_BASIC_USER = 'edx'
XQUEUE_BASIC_PASSWORD = 'edx'
XQUEUE_TIMEOUT = 10

RABBITMQ_USER = "guest"
RABBITMQ_PASSWORD = "guest"
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_VHOST = "/"

EVALUATOR_MODULES = {
    "dummy_grader"
}

DEFAULT_EVALUATOR = "dummy"