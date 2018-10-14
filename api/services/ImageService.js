const PythonShell = require('python-shell').PythonShell;

module.exports = class ImageService {
    static describe(uri, callback) {
        let options = {
            mode: 'text',
            pythonOptions: ['-u'],
            scriptPath: 'pylib',
            args: [uri]
        };

        PythonShell.run('describe_image.pyc', options, function (err, results) {
        	console.log(err);
            if (err) callback(null);
            console.log('results: %j', results);
            callback(results);
        });
    }
};