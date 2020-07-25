module.exports = {
  purge: {
    enabled: true,
    content: [
      './**/*.html',
      './_site/**/*.html',
    ],
  },
  theme: {
    fontFamily: {
      body: ['"PT Serif"', 'Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif'],
      display: ['"PT Serif"', 'Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif'],
      mono: ['Menlo', 'Monaco', 'Consolas', '"Liberation Mono"', '"Courier New"', 'monospace'],
      sans: ['"PT Sans"', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', '"Helvetica Neue"', 'Arial', '"Noto Sans"', 'sans-serif', '"Apple Color Emoji"', '"Segoe UI Emoji"', '"Segoe UI Symbol"', '"Noto Color Emoji"'],
      serif: ['"PT Serif"', 'Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif']
    },
    extend: {}
  },
  variants: {},
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
