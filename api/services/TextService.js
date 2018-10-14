const PythonShell = require('python-shell').PythonShell;

module.exports = class TextService {
	static cleanup(text, callback) {
		let options = {
			mode: 'text',
			pythonOptions: ['-u'],
			pythonPath: 'env/bin/python',
			scriptPath: 'pylib'
		};

		PythonShell.run('cleanup_text.py', options, function (err, results) {
			if (err) callback(null);
			console.log('results: %j', results);
			callback(results);
		});
	}
};