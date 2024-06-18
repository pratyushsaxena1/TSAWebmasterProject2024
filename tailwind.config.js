/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./api/templates/**/*.html", "./api/static/src/**/*.js"],
  theme: {
    // put all hex code colors in here, formatted as darkGreen: "#12372A",
    colors: {
      beige: "#F6F4EA",
      lightGreen: "#C5D8BE",
      darkGreen: "#3B6348",
      blackGreen: "#006400",
      black: "#000000",
    },
    extend: {},
  },
  plugins: [require("tailwindcss-animated")],
};
