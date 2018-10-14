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
    static let token = "temp"
    
    static func getText(image: UIImage, completion: @escaping (String?) -> Void) {
        let vision = Vision.vision()
        let textRecognizer = vision.onDeviceTextRecognizer()
        let visionImage = VisionImage(image: image)
        
        textRecognizer.process(visionImage) { result, error in
            guard error == nil, let result = result else {
                return completion(nil)
            }
            
            TextService.cleanupRemote(text: result.text) { text in
                completion(text)
            }
        }
    }
    
    static func getDescription(image: UIImage, completion: @escaping (String?) -> Void) {
        StorageService.uploadImage(image) { uri in
            if var uri = uri {
                uri = uri.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed)!
                print(uri)
                
                let parameters: Parameters = [
                    "token": token,
                    "uri": uri
                ]
                
                let url = "https://unblind-219302.appspot.com/image/describe"
                
                Alamofire.request(url, method: .get, parameters: parameters).responseJSON() { response in
                    switch response.result {
                    case .success:
                        if let data = response.data {
                            let json = try! JSON(data: data)
                            let result = json[0].string!
                            completion(result)
                        }
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
