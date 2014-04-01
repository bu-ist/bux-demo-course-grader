# Demo External Grader

Defines package requirements and configuration for a demo course grader.

## Requirements

* BU External Grader Framework - https://github.com/bu-ist/bux-grader-framework
* A configured XQueue queue / credentials
* RabbitMQ

## Quick Start

```bash
git clone git@github.com:bu-ist/bux-demo-course-grader
cd bux-demo-course-grader
pip install -r requirements.txt
```

Modify the configuration in `settings.py` and start the grader:

```bash
grader --settings=settings
```

Type `Ctl-C` to stop the grader.

For provisioning of production and development VM environments use the configuration repository: https://github.com/bu-ist/bux-grader-configuration.
