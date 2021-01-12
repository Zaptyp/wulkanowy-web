const path = require("path");

module.exports = {
    entry: {
        attedance : "./files/js/attendance.js",
        exams : "./files/js/exams.js",
        grades : "./files/js/grades.js",
        homeworks : "./files/js/homeworks.js",
        login : "./files/js/login.js",
        messages : "./files/js/messages.js",
        mobile_access : "./files/js/mobile_access.js",
        notes : "./files/js/notes.js",
        start : "./files/js/start.js",
        timetable : "./files/js/timetable.js",
    },
    output: {
        filename: "out-[name].js",
        path: path.resolve(__dirname, "./files/js/dist")
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