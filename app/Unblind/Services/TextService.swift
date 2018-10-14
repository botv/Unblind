//
//  TextService.swift
//  Unblind
//
//  Created by Ben Botvinick on 10/13/18.
//  Copyright © 2018 Ben Botvinick. All rights reserved.
//

import Foundation
import Alamofire
import SwiftyJSON
import Firebase

struct TextService {
    static func summarizeText(blocks: [VisionTextBlock], completion: @escaping (String?) -> Void) {
        var blockInfoArray: [[String: Any]] = []
        
        for block in blocks {
            blockInfoArray.append([
                "text": block.text,
                "width": block.frame.size.width,
                "height": block.frame.size.height
            ])
        }
        
        let parameters: Parameters = [
            "blocks": blockInfoArray
        ]
        
        let headers: HTTPHeaders = [
            "Accept": "application/json"
        ]
        
        let url = "https://us-central1-unblind-9a7cd.cloudfunctions.net/summarize-text"
        
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
    }
}
