# -*- coding: utf-8 -*-
import pvporcupine
import pyaudio
import struct

import pygame
import time

PICOVOICE_API_KEY = "Vj5ZuDFjV2LrbKDXEJrh/UfGKvuiOKizzne71Lnab4UsJBMQeuFMEA=="

FILE_PATH = "recordings/voiceWake.wav"

KEYWORD_PATHS = "models\Hey-Jarvis_en_windows_v3_0_0.ppn"


def VoiceWake():
    pygame.mixer.init()
    pygame.mixer.music.load(FILE_PATH)

    porcipine = pvporcupine.create(
        access_key=PICOVOICE_API_KEY,
        keyword_paths=[KEYWORD_PATHS],  # 自己去网站下载自己自定义的模型
    )

    myaudio = pyaudio.PyAudio()

    stream = myaudio.open(
        input_device_index=0,
        rate=porcipine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcipine.frame_length,
    )

    print("[Voice-Wake] Begin!")

    while True:
        # 开始监听关键词
        audio_obj = stream.read(porcipine.frame_length, exception_on_overflow=False)
        audio_obj_unpacked = struct.unpack("h" * porcipine.frame_length, audio_obj)

        keyword_idx = porcipine.process(audio_obj_unpacked)
        if keyword_idx >= 0:
            # 播放应答音频
            pygame.mixer.music.play()
            print("[Voice-Wake] Success!")

            # 等待音频播放完毕
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            # 音频播放结束后的处理逻辑
            print("[Voice-Wake] finish!")

            # 释放资源
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            stream.stop_stream()
            stream.close()
            myaudio.terminate()

            # 跳出循环，结束
            break


if __name__ == "__main__":
    VoiceWake()
