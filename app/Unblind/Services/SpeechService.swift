//
//  SpeechService.swift
//  Unblind
//
//  Created by Ben Botvinick on 10/13/18.
//  Copyright © 2018 Ben Botvinick. All rights reserved.
//

import AVFoundation

struct SpeechService {
    static func say(string: String) {
        let utterance = AVSpeechUtterance(string: string)
        utterance.voice = AVSpeechSynthesisVoice(language: "en-US")
        
        let synth = AVSpeechSynthesizer()
        synth.speak(utterance)
    }
}
