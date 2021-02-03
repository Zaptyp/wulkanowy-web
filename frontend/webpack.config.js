const path = require("path")

module.exports = {
    entry: {
        login : "./src/login.js",
        content : "./src/content.js"
     },
    output: {
      filename : "[name].js",
        path : path.resolve(__dirname, "./static/frontend")
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
};