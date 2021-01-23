const path = require("path");

module.exports = {
    entry: {
        attedance : "./static/frontend/js/attendance.js",
        exams : "./static/frontend/js/exams.js",
        grades : "./static/frontend/js/grades.js",
        homeworks : "./static/frontend/js/homeworks.js",
        login : "./static/frontend/js/login.js",
        messages : "./static/frontend/js/messages.js",
        mobile_access : "./static/frontend/js/mobile_access.js",
        notes : "./static/frontend/js/notes.js",
        start : "./static/frontend/js/start.js",
        timetable : "./static/frontend/js/timetable.js",
    },
    output: {
        filename: "out-[name].js",
        path: path.resolve(__dirname, "./static/frontend/js/dist")
    },
    watch: false,
    mode: "development",
    devtool: "source-map",
    module: {
        rules: [
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ["@babel/preset-env"]
                    }
                }
            }
        ]
    }
}