//
//  ImageService.swift
//  Unblind
//
//  Created by Ben Botvinick on 10/12/18.
//  Copyright © 2018 Ben Botvinick. All rights reserved.
//

import UIKit
import Firebase
import Alamofire
import SwiftyJSON

struct ImageService {
    static func getText(image: UIImage, completion: @escaping (String?) -> Void) {
        let vision = Vision.vision()
        let textRecognizer = vision.onDeviceTextRecognizer()
        let visionImage = VisionImage(image: image)
        
        textRecognizer.process(visionImage) { result, error in
            guard error == nil, let result = result else {
                return completion(nil)
            }
            
            TextService.summarizeText(blocks: result.blocks) { text in
                completion(text)
            }
        }
    }
    
    static func getDescription(image: UIImage, completion: @escaping (String?) -> Void) {
        StorageService.uploadImage(image) { uri in
            if let uri = uri {
                let parameters: Parameters = [
                    "uri": uri
                ]
                
                let headers: HTTPHeaders = [
                    "Accept": "application/json"
                ]

                let url = "https://us-central1-unblind-9a7cd.cloudfunctions.net/describe-image"
                
                Alamofire.request(url, method: .post, parameters: parameters, encoding: JSONEncoding.default, headers: headers).responseString() { response in
                    switch response.result {
                    case .success:
                        print(response.value!)
                        completion(response.value)
                    case .failure(let error):
                        print(error)
                        completion(nil)
                    }
                }
            } else {
                return completion(nil)
            }
        }
    }
}
