const PythonShell = require('python-shell').PythonShell;

module.exports = class ImageService {
	static describe(uri, callback) {
		let options = {
			mode: 'text',
			pythonOptions: ['-u'],
			scriptPath: 'lib',
			args: [uri]
		};

		PythonShell.run('describe_image.py', options, function (err, results) {
			if (err) callback(null);
			console.log('results: %j', results);
			callback(results);
		});
	}
};