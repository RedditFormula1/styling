const gulp = require('gulp')
const del = require('del')
const plumber = require('gulp-plumber')
const sass = require('gulp-sass')
const sasslint = require('gulp-sass-lint')
const autoprefixer = require('gulp-autoprefixer')

const project = {
  styles : './src/styles/**/*.scss',
  images: 'src/images/**/*',
  dist   : './dist/'
}

gulp.task('clean', function(cb) {
  del(project.dist, cb)
})

gulp.task('styles', function() {
  gulp.src(project.styles)
    .pipe(plumber())
    .pipe(sasslint())
    .pipe(sass({
      outputStyle: 'compressed'
    }))
    .pipe(gulp.dest(project.dist))
})

gulp.task('images', function() {
  return gulp.src(project.images, {base: 'src'})
    .pipe(plumber())
    .pipe(gulp.dest(project.dist))
})

gulp.task('build', function() {
  gulp.start('styles', 'images')
})

gulp.task('dev', function() {
  gulp.watch(project.styles, ['styles'])
})
