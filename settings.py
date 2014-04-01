# Grader settings module
#
# Course-specifc grader configuration goes here
# Loaded by ``bux_grader_framework`` at run time
#

XQUEUE_QUEUE = ""
XQUEUE_URL = "http://localhost:18040"
XQUEUE_USER = "lms"
XQUEUE_PASSWORD = "password"
XQUEUE_TIMEOUT = 10

RABBITMQ_USER = "guest"
RABBITMQ_PASSWORD = "guest"
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_VHOST = "/"

EVALUATOR_MODULES = {
    "dummy_grader"
}
