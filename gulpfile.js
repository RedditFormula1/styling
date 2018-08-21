const gulp = require('gulp')
const del = require('del')
const spritesmith = require('gulp.spritesmith')
const plumber = require('gulp-plumber')
const sass = require('gulp-sass')
const sasslint = require('gulp-sass-lint')
const autoprefixer = require('gulp-autoprefixer')
const merge = require('merge-stream')

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
    .pipe(autoprefixer({
      browsers: ['last 2 versions']
    }))
    .pipe(gulp.dest(project.dist))
})

gulp.task('flairs', function() {
  const spriteData = gulp.src('./src/flairs/*.png').pipe(spritesmith({
    imgName: 'flairs.png',
    cssName: '_user-flairs.scss',
    cssTemplate: './src/flair-template.css.handlebars'
  }))

  const imageStream = spriteData.img.pipe(gulp.dest('./src/images/'))

  const cssStream = spriteData.css.pipe(gulp.dest('./src/styles/modules/'))

  return merge(imageStream, cssStream)
})

gulp.task('images', function() {
  return gulp.src(project.images, {base: 'src'})
    .pipe(plumber())
    .pipe(gulp.dest(project.dist))
})

gulp.task('build', ['flairs'], function() {
  gulp.start('styles', 'images')
})

gulp.task('dev', function() {
  gulp.watch(project.styles, ['styles'])
})
