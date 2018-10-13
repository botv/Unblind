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
    static func getText(image: UIImage, completion: @escaping ([VisionTextBlock]) -> Void) {
        let vision = Vision.vision()
        let textRecognizer = vision.onDeviceTextRecognizer()
        let visionImage = VisionImage(image: image)
        
        textRecognizer.process(visionImage) { result, error in
            guard error == nil, let result = result else {
                return completion([])
            }

            completion(result.blocks)
        }
    }
}
