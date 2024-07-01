# AIChatBot

## 1. 项目介绍

本项目标是实现基于语音识别的智能音箱功能，包括语音识别、语音合成等；实现基于聊天机器人的智能音箱功能，包括自然语言处理、情感分析、智能推荐等；提高智能音箱的智能化程度和用户体验，满足用户多样化的需求；为其他类似场景提供一种基于语音识别和聊天机器人的智能音箱解决方案。

## 2. 大模型导入

1. 下载并安装 **ollama**

   ```txt
    https://ollama.com/
   ```

2. 部署开源大模型 **Llama3**，参数8b，模型大小 4.7G，命令行输入：

   ```cmd
   ollama pull llama3:8b
   ```

3. 部署开源大模型 **Llava**(用于图像处理)，参数7b，模型大小 4G，命令行输入：

   ```cmd
   ollama pull llava:latest
   ```


4. 工具包

   ```cmd
   ./tools/text2voice # 文本转语音
   ./tools/voice2text # 语音转文本
   ```

## 3. 运行Flask框架

1. 导入相关包

   ```cmd
   pip install flask, flask_socketio
   ```

2. 启动项目

   ```cmd
   python -m flask run --port=5001
   ```
