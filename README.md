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

## Notes

The default configuration in `settings.py` will look for a local XQueue install created using the `fullstack` provisioning instructions:
https://github.com/edx/configuration/wiki/edX-Production-Stack.

Here's an example problem you could add to your course to test the grader once it's up and running:

```xml
<problem>
  <text>
    <p>Say hello to the dummy external grader!</p>
  </text>
  <coderesponse queuename="test-pull">
    <textbox />
    <codeparam>
      <initial_display></initial_display>
      <answer_display>Hello, dummy grader!</answer_display>
      <grader_payload>
        {
          "answer": "Hello, dummy grader!"
        }
      </grader_payload>
    </codeparam>
  </coderesponse>
</problem>
```
