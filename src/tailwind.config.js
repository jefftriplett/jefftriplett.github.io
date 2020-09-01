// const ptSans = require("typeface-pt-sans");
// const ptSerif = require("typeface-pt-serif");
const defaultTheme = require("tailwindcss/defaultTheme");


module.exports = {
  purge: {
    enabled: true,
    mode: 'all',
    content: [
      './**/*.html',
      './_site/**/*.html',
    ],
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
    require('@tailwindcss/typography'),
  ],
}
