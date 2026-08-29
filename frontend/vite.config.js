import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  base: './',
  plugins: [
    react(),
    tailwindcss(),
  ],
  // Tailwind runs through @tailwindcss/vite here. Declare PostCSS inline so Vite does
  // not walk up and pick the repo-root postcss.config.mjs, which belongs to the Next.js
  // app and requires @tailwindcss/postcss - a package this workspace does not install.
  css: {
    postcss: {},
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      }
    }
  }
})
