//
//  StorageService.swift
//  Unblind
//
//  Created by Ben Botvinick on 10/13/18.
//  Copyright © 2018 Ben Botvinick. All rights reserved.
//

import Foundation
import FirebaseStorage

struct StorageService {
    static func uploadImage(_ image: UIImage, completion: @escaping (String?) -> Void) {
        let data = image.jpegData(compressionQuality: 0.1)!
        let timestamp = ISO8601DateFormatter().string(from: Date())
        let storageRef = Storage.storage().reference().child("\(timestamp).jpg")
        let uploadTask = storageRef.putData(data, metadata: nil)
        
        uploadTask.observe(.success) { snapshot in
            print("uploaded image")
            storageRef.downloadURL(completion: { (url, error) in
                guard let url = url?.absoluteString else { return completion(nil) }
                completion(url)
            })
        }
        
        uploadTask.observe(.failure) { err in
            print(err)
        }
    }
}
