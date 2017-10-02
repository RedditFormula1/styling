// Packages
const gulp = require('gulp')
const plumber = require('gulp-plumber')
const sass = require('gulp-sass')
const gutil = require('gulp-util')
const sasslint = require('gulp-sass-lint')
const autoprefixer = require('gulp-autoprefixer')
const del = require('del')

let project = {
	styles: 'src/**/*.scss',
	dist: 'dist/'
}

// Tasks
gulp.task('clean', function(cb) {
	del(project.dist, cb)
})

gulp.task('styles', function() {
	gulp.src(project.styles, {base: 'src'})
		.pipe(plumber())
		.pipe(sasslint())
		.pipe(sass({
			outputStyle: 'compressed'
		}))
		.pipe(autoprefixer({
			browsers: ['last 2 versions']
		}))
		.pipe(gulp.dest(project.dist))
})

gulp.task('build', function() {
	gulp.start('styles')
})

gulp.task('dev', function() {
	gulp.watch(project.styles, ['styles']);
})
