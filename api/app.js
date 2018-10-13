const createError = require('http-errors');
const express = require('express');

process.on('uncaughtException', function (err) {
	console.error(err);
});

const indexRouter = require('./routes/index');

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.use('/', indexRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
	next(createError(404));
});

// error handler
app.use(function (err, req, res) {
	res.status(err.status || 500);
	res.end()
});

module.exports = app;
