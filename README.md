# dingtalk-python-sdk
A Python library for the DingTalk

# Installation

The latest stable version is [available on PyPI](https://pypi.org/project/dingtalk-python-sdk/)

```bash
pip install dingtalk-python-sdk
```

# Usage
```python
from dingtalk_python_sdk import robot

webhook = 'your-webhook-address'

dingtalk = robot.Robot(webhook)
dingtalk.send_text('Hello!')

```