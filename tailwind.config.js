/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html"],
  theme: {
    screens: {
        'lg': {'max': '992px'},
        'md': {'max': '768px'},
        'sm': {'max': '480px'}
    },
    container: {
        padding: '20px',
        center: true
    },
    extend: {
    colors: {
        black: '#000',
        white: '#fff',
        gray: '#e2e2e2'
    }

    },
  },
  plugins: [],
}
