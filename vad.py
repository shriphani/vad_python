#!/usr/bin/env python

import webrtc_vad

def create_vad():
    vad_inst = webrtc_vad.WebRtcVad_Create()
    webrtc_vad.WebRtcVad_Init(vad_inst)
    return vad_inst

def free_vad(vad_inst):
    webrtc_vad.WebRtcVad_Free(vad_inst)

def process_frame(vad_inst, fs, frame):
    return webrtc_vad.processFrame(vad_inst, fs, frame) > 0

if __name__ == '__main__':

    vad_inst = create_vad()

    # Sampled at 8000hz, 160 frames of pure silence - should be 0
    print 'Speech in silence?', process_frame(vad_inst, 8000, [0 for _ in range(160)])
