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

struct TextService {
    static let token = "temp"
    
    static func cleanup(text: String, completion: @escaping (String) -> Void) {
        completion(text)
    }
    
    static func cleanupRemote(text: String, completion: @escaping (String) -> Void) {
        let parameters: Parameters = [
            "token": token,
            "text": "hi"
        ]
        
        let url = "https://unblind-219302.appspot.com/text/cleanup"
        
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
                completion(text)
            }
        }
    }
}
