var gulp = require('gulp'), 
    minifyCSS = require('gulp-minify-css'),
	webpack = require('gulp-webpack');

gulp.task('minify-css', function () {
    return gulp.src('css/*.css')
        .pipe(minifyCSS())
        .pipe(gulp.dest('build/css/'))
});

gulp.task('webpack', function() {
  return gulp.src('js/main.jsx')
    .pipe(webpack({
      output: { filename: '[name].js' },
      module: {
        loaders: [
          { test: /\.json$/, loader: 'json-loader' }, // required by mapbox.js
          { test: /\.jsx$/, loader: 'jsx-loader?insertPragma=React.createElement' },
        ],
      },
      resolve: { extensions: ['', '.jsx', '.js'] }
    }))
    .pipe(gulp.dest('build/js/'));
});

gulp.task('shrink', ['minify-css', 'webpack']);