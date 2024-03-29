const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: [
    './*.html',
    './**/*.html',
    './_site/*.html',
    './_site/**/*.html'
  ],
  darkMode: 'media',
  theme: {
    extend: {
      fontFamily: {
        body: ['Inter', ...defaultTheme.fontFamily.serif],
        display: ['Inter', ...defaultTheme.fontFamily.serif],

        // body: ['"PT Serif"', ...defaultTheme.fontFamily.serif],
        // display: ['"PT Serif"', ...defaultTheme.fontFamily.serif],
        // // mono: ['Menlo', ...defaultTheme.fontFamily.mono],
        // mono: ['"PT Mono"', ...defaultTheme.fontFamily.mono],
        // sans: ['"PT Sans"', ...defaultTheme.fontFamily.sans],
        // serif: ['"PT Serif"', ...defaultTheme.fontFamily.serif],
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
