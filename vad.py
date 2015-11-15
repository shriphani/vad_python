#!/usr/bin/env python

import webrtc_vad

def create_vad():
    vad_inst = webrtc_vad.WebRtcVad_Create()
    webrtc_vad.WebRtcVad_Init(vad_inst)
    return vad_inst

def free_vad(vad_inst):
    webrtc_vad.WebRtcVad_Free(vad_inst)

def process_frame(vad_inst, fs, frame):
    return webrtc_vad.processFrame(vad_inst, fs, frame)
