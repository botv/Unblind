const express = require('express');

const router = express.Router();

router.get('*', function (req, res, next) {
	const token = req.query.token;
	if (token === 'temp') {
		next();
	} else {
		res.status(500);
		res.end()
	}
});

module.exports = router;
