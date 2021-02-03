const path = require("path")

module.exports = {
    entry: {
        login : "./src/login.js",
        content : "./src/content.js"
     },
     module: {
        rules: [
          {
            //"allowJs": true,
            test: /\.tsx?$/,
            use: 'ts-loader',
            exclude: /node_modules/,
          },
        ],
      },
      resolve: {
        extensions: [ '.tsx' ,'.jsx', '.ts', '.js' ],
      },
      output: {
        filename: '[name].js',
        path: path.resolve(__dirname, "./static/frontend"),
      },
    };