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
            guard let uri = uri else { return completion(nil) }
            
            let parameters: Parameters = [
                "token": token,
                "uri": "https%3A%2F%2Ffirebasestorage.googleapis.com%2Fv0%2Fb%2Funblind-9a7cd.appspot.com%2Fo%2F2018-10-13T21%3A23%3A32Z.jpg%3Falt%3Dmedia%26token%3D66c85b00-5c8a-44f8-82c7-a4f61a37e2c3"
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
        }
        
    }
}
