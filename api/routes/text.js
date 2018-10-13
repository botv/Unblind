const express = require('express');
const TextService = require('../services/TextService');

const router = express.Router();

router.get('/cleanup', function (req, res, next) {
	const text = req.query.text;
	TextService.cleanup(text, function(text) {
		if (text != null) {
			res.send(text)
		} else {
			res.status(500);
			res.end()
		}
	});
});

module.exports = router;
