# A VoiceWake-Detection Script
# 简单的语音唤醒检测脚本
## Author：kkl

---

这是一个简单的Python脚本项目，可以在你的项目中加入语音唤醒功能（热词检测）。

### 文件结构
```bash
├───voice_wake.py
├───models
├───recordings
```

本项目为单脚本项目，主要程序逻辑全部在`voice_wake.py`中。`models/`文件夹中存放模型文件。`recordings`存放唤醒后答复的录音，我已经在其中放入一个中文答复录音`voiceWake.wav`。

## 运行指南
本项目基于`Python`编程语言，使用的是`Windows`环境，程序运行使用的`Python`版本为`3.11.5`，建议使用[Anaconda](https://www.anaconda.com)配置`Python`环境。

### 环境配置
```
# 环境配置
conda create -n VoiceAI python=3.11.5
conda activate VoiceAI

# 安装热词检测工具
pip install pvporcupine

# 安装音频录制工具
pip install pyaudio

# 安装音频播放工具
pip install pygame
```

### PICOVOICE-AccessKey获取
需要前往[picovoice](https://console.picovoice.ai/)注册账号，注册完成即可获得AccessKey。


### 模型文件
模型文件存放于`models/`文件夹下，在脚本中通过变量`KEYWORD_PATHS`指定（应该可以指定多个，本项目中只使用了一个模型。

前往[picovoice/pnn](https://console.picovoice.ai/ppn)可以自定义语言，唤醒词，五分钟内就可以导出自定义的模型！亲测，使用英文的识别率高一些噢！

我在`voice_wake.py`中使用的模型可能因为版权原因不能分享，所以各位需要亲自去自定义属于你的模型。

## 鸣谢
本项目的唤醒词检测部分基于项目[porcupine](https://github.com/Picovoice/porcupine)，非常感谢！