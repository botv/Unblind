//
//  ImageService.swift
//  Unblind
//
//  Created by Ben Botvinick on 10/12/18.
//  Copyright © 2018 Ben Botvinick. All rights reserved.
//

import UIKit
import Firebase

struct ImageService {
    static func getText(image: UIImage, completion: @escaping (String?) -> Void) {
        let vision = Vision.vision()
        let textRecognizer = vision.onDeviceTextRecognizer()
        let visionImage = VisionImage(image: image)
        
        textRecognizer.process(visionImage) { result, error in
            guard error == nil, let result = result else {
                return completion(nil)
            }

            let resultText = result.text
            completion(resultText)
//            for block in result.blocks {
//                let blockText = block.text
//                let blockConfidence = block.confidence
//                let blockLanguages = block.recognizedLanguages
//                let blockCornerPoints = block.cornerPoints
//                let blockFrame = block.frame
//                for line in block.lines {
//                    let lineText = line.text
//                    let lineConfidence = line.confidence
//                    let lineLanguages = line.recognizedLanguages
//                    let lineCornerPoints = line.cornerPoints
//                    let lineFrame = line.frame
//                    for element in line.elements {
//                        let elementText = element.text
//                        let elementConfidence = element.confidence
//                        let elementLanguages = element.recognizedLanguages
//                        let elementCornerPoints = element.cornerPoints
//                        let elementFrame = element.frame
//                    }
//                }
//            }
        }
    }
}
