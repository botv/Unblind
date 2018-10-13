module.exports = class ImageService {
	static describe(uri, callback) {
		console.log('downloading image');
		let imagePath = 'tmp/' + uniqid() + '.jpg';
		Jimp.read(uri, function (err, image) {
			try {
				image
					.resize(256, Jimp.AUTO)
					.write(imagePath, function () {
						try {
							console.log('analyzing image');
							callback('description');
							console.log('analysis complete');
						} catch (err) {
							callback(null);
							console.log('analysis failed');
						}
						fs.unlinkSync(imagePath);
					});
			} catch (err) {
				console.log('download failed');
				callback(null);
			}
		});
	}
};