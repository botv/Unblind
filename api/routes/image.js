const express = require('express');
const ImageService = require('../services/ImageService');

const router = express.Router();

router.get('/describe', function (req, res, next) {
	const uri = req.query.uri;
	ImageService.describe(uri, function(description) {
		if (description != null) {
			res.send(description)
		} else {
			res.status(500);
			res.end()
		}
	});
});

module.exports = router;
