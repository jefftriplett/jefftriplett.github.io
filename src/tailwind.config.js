const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  purge: {
    enabled: process.env.JEKYLL_ENV == "production",
    mode: "all",
    content: ["./**/*.html", "./_site/**/*.html"],
  },
  theme: {
    extend: {
      fontFamily: {
        body: ['"PT Serif"', ...defaultTheme.fontFamily.serif],
        display: ['"PT Serif"', ...defaultTheme.fontFamily.serif],
        // mono: ['Menlo', ...defaultTheme.fontFamily.mono],
        mono: ['"PT Mono"', ...defaultTheme.fontFamily.mono],
        sans: ['"PT Sans"', ...defaultTheme.fontFamily.sans],
        serif: ['"PT Serif"', ...defaultTheme.fontFamily.serif],
      },
    },
  },
  variants: {},
  plugins: [
    require("@tailwindcss/typography"),
    require("tailwindcss-debug-screens"),
  ],
  future: {
    removeDeprecatedGapUtilities: true,
  },
};
